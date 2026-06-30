from unittest.mock import MagicMock

import numpy as np
import pandas as pd
import pytest

from extract import extract_demographics, extract_engagement, extract_followers, extract_top_posts


def _xl(df: pd.DataFrame) -> MagicMock:
    xl = MagicMock()
    xl.parse.return_value = df
    return xl


# ── extract_engagement ────────────────────────────────────────────────────────

def test_extract_engagement_should_parse_date_when_format_is_mm_dd_yyyy():
    # Arrange
    raw = pd.DataFrame({"A": ["07/01/2025"], "B": [100], "C": [5]})

    # Act
    result = extract_engagement(_xl(raw))

    # Assert
    assert result["date"].iloc[0] == pd.Timestamp("2025-07-01")


def test_extract_engagement_should_fill_nan_with_zero_when_impressions_is_missing():
    # Arrange
    raw = pd.DataFrame({"A": ["07/01/2025"], "B": [float("nan")], "C": [float("nan")]})

    # Act
    result = extract_engagement(_xl(raw))

    # Assert
    assert result["impressions"].iloc[0] == 0
    assert result["engagements"].iloc[0] == 0


def test_extract_engagement_should_return_int_dtype_when_values_are_numeric():
    # Arrange
    raw = pd.DataFrame({"A": ["07/01/2025"], "B": [42], "C": [3]})

    # Act
    result = extract_engagement(_xl(raw))

    # Assert
    assert result["impressions"].dtype == int
    assert result["engagements"].dtype == int


# ── extract_demographics ──────────────────────────────────────────────────────

def test_extract_demographics_should_return_0_5_when_percentage_is_less_than_1_percent():
    # Arrange
    raw = pd.DataFrame({"A": ["Company"], "B": ["Mercado Libre"], "C": ["< 1%"]})

    # Act
    result = extract_demographics(_xl(raw))

    # Assert
    assert result["percentage"].iloc[0] == 0.5


def test_extract_demographics_should_return_float_when_percentage_is_normal_string():
    # Arrange
    raw = pd.DataFrame({"A": ["Industry"], "B": ["Tech"], "C": ["12%"]})

    # Act
    result = extract_demographics(_xl(raw))

    # Assert
    assert result["percentage"].iloc[0] == 12.0


# ── extract_followers ─────────────────────────────────────────────────────────

def _followers_raw(total: int, rows: list[tuple]) -> pd.DataFrame:
    """Builds the raw sheet layout: total in row 0 col 1, 'Date' header, then data rows."""
    header = [("Total followers", total), (None, None), ("Date", None)]
    all_rows = header + rows
    return pd.DataFrame({0: [r[0] for r in all_rows], 1: [r[1] for r in all_rows]})


def test_extract_followers_should_return_total_followers_as_int_when_sheet_has_header():
    # Arrange
    raw = _followers_raw(700, [("07/01/2025", 2), ("07/02/2025", 3)])

    # Act
    _, total = extract_followers(_xl(raw))

    # Assert
    assert total == 700


def test_extract_followers_should_return_only_data_rows_after_date_header_when_parsing():
    # Arrange
    raw = _followers_raw(700, [("07/01/2025", 2), ("07/02/2025", 3)])

    # Act
    df, _ = extract_followers(_xl(raw))

    # Assert
    assert len(df) == 2
    assert list(df.columns) == ["date", "new_followers"]
    assert df["new_followers"].iloc[0] == 2


# ── extract_top_posts ─────────────────────────────────────────────────────────

def _top_posts_raw() -> pd.DataFrame:
    """Two tables side by side: cols 0-2 = by engagement, cols 4-6 = by impressions."""
    return pd.DataFrame({
        0: ["Post URL", "https://url_a", "https://url_b"],
        1: ["Publish Date", "03/16/2026", "03/02/2026"],
        2: ["Engagements", 38, 42],
        3: [np.nan, np.nan, np.nan],
        4: ["Post URL", "https://url_a", "https://url_c"],
        5: ["Publish Date", "03/16/2026", "03/18/2026"],
        6: ["Impressions", 11274, 4021],
    })


def test_extract_top_posts_should_merge_url_that_appears_in_both_tables_when_parsing():
    # Arrange — url_a is in both engagement and impressions tables
    raw = _top_posts_raw()

    # Act
    result = extract_top_posts(_xl(raw))

    # Assert
    url_a = result[result["post_url"] == "https://url_a"].iloc[0]
    assert url_a["engagements"] == 38
    assert url_a["impressions"] == 11274


def test_extract_top_posts_should_fill_zero_impressions_when_url_only_in_engagement_table():
    # Arrange — url_b is only in engagement table, not in impressions
    raw = _top_posts_raw()

    # Act
    result = extract_top_posts(_xl(raw))

    # Assert
    url_b = result[result["post_url"] == "https://url_b"].iloc[0]
    assert url_b["impressions"] == 0
    assert url_b["engagements"] == 42
