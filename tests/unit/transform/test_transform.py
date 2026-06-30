import pandas as pd
import pytest

from transform import extract_topics_from_url, transform_engagement, transform_followers


# ── extract_topics_from_url ───────────────────────────────────────────────────

def test_extract_topics_from_url_should_return_topics_when_url_has_standard_linkedin_format():
    # Arrange
    url = "https://www.linkedin.com/posts/gerardo-toboso-512a48290_dataengineering-python-bigdata-share-7439307252412334080-puIN"

    # Act
    result = extract_topics_from_url(url)

    # Assert
    assert result == ["dataengineering", "python", "bigdata"]


def test_extract_topics_from_url_should_return_empty_when_url_has_no_slug_match():
    # Arrange
    url = "https://www.linkedin.com/in/gerardo-toboso-512a48290/"

    # Act
    result = extract_topics_from_url(url)

    # Assert
    assert result == []


def test_extract_topics_from_url_should_filter_stopwords_when_slug_contains_them():
    # Arrange — "share" and "python" → "share" is a stopword, "python" should pass
    url = "https://www.linkedin.com/posts/user_python-share-share-7439307252412334080-abc"

    # Act
    result = extract_topics_from_url(url)

    # Assert
    assert "share" not in result
    assert "python" in result


def test_extract_topics_from_url_should_filter_short_tokens_when_token_is_3_chars_or_less():
    # Arrange — "ai" (2 chars) should be filtered by the len > 3 guard
    url = "https://www.linkedin.com/posts/user_ai-machinelearning-share-1234567890-abc"

    # Act
    result = extract_topics_from_url(url)

    # Assert
    assert "ai" not in result
    assert "machinelearning" in result


# ── transform_engagement ──────────────────────────────────────────────────────

def test_transform_engagement_should_add_lunes_when_date_is_monday(tmp_path):
    # Arrange — 2026-03-16 is Monday
    pd.DataFrame({"date": ["2026-03-16"], "impressions": [100], "engagements": [5]}).to_csv(
        tmp_path / "engagement.csv", index=False
    )

    # Act
    result = transform_engagement(tmp_path)

    # Assert
    assert result.iloc[0]["day_of_week"] == "Lunes"
    assert result.iloc[0]["month"] == "Marzo"


def test_transform_engagement_should_compute_engagement_rate_when_impressions_are_nonzero(tmp_path):
    # Arrange
    pd.DataFrame({"date": ["2026-03-16"], "impressions": [100], "engagements": [5]}).to_csv(
        tmp_path / "engagement.csv", index=False
    )

    # Act
    result = transform_engagement(tmp_path)

    # Assert
    assert result.iloc[0]["engagement_rate"] == pytest.approx(0.05)


def test_transform_engagement_should_set_rate_to_zero_when_impressions_are_zero(tmp_path):
    # Arrange
    pd.DataFrame({"date": ["2026-03-16"], "impressions": [0], "engagements": [0]}).to_csv(
        tmp_path / "engagement.csv", index=False
    )

    # Act
    result = transform_engagement(tmp_path)

    # Assert
    assert result.iloc[0]["engagement_rate"] == 0.0


# ── transform_followers ───────────────────────────────────────────────────────

def test_transform_followers_should_compute_cumulative_from_base_when_total_given(tmp_path):
    # Arrange — total=700, period gains=5 (2+3), start=695
    pd.DataFrame({"date": ["2025-07-01", "2025-07-02"], "new_followers": [2, 3]}).to_csv(
        tmp_path / "followers.csv", index=False
    )

    # Act
    result = transform_followers(tmp_path, total_followers=700)

    # Assert: 695+2=697, 695+5=700
    assert result.iloc[0]["cumulative_followers"] == 697
    assert result.iloc[1]["cumulative_followers"] == 700


def test_transform_followers_should_compute_rolling_7d_avg_with_min_periods_1(tmp_path):
    # Arrange
    pd.DataFrame({
        "date": ["2025-07-01", "2025-07-02", "2025-07-03"],
        "new_followers": [2, 4, 0],
    }).to_csv(tmp_path / "followers.csv", index=False)

    # Act
    result = transform_followers(tmp_path, total_followers=100)

    # Assert: mean([2])=2.0, mean([2,4])=3.0, mean([2,4,0])=2.0
    assert result.iloc[0]["rolling_7d_avg"] == 2.0
    assert result.iloc[1]["rolling_7d_avg"] == 3.0
    assert result.iloc[2]["rolling_7d_avg"] == 2.0
