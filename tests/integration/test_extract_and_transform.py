"""
Integration test: runs extract → transform against the real xlsx in data/raw/.
Skipped automatically if no xlsx is found (CI environments without the file).
"""
from pathlib import Path

import pandas as pd
import pytest

from extract import run_extract
from transform import run_transform

RAW_DIR = Path(__file__).parent.parent.parent / "data" / "raw"


def _find_xlsx() -> Path | None:
    files = list(RAW_DIR.glob("*.xlsx"))
    return files[0] if files else None


@pytest.mark.integration
def test_extract_and_transform_should_produce_valid_engagement_csv_when_given_real_xlsx(tmp_path):
    # Arrange
    xlsx = _find_xlsx()
    if xlsx is None:
        pytest.skip("No xlsx in data/raw — skipping integration test")

    # Act
    meta = run_extract(xlsx, tmp_path)
    run_transform(tmp_path, meta["total_followers"])

    # Assert — structural invariants on the transformed engagement CSV
    engagement = pd.read_csv(tmp_path / "engagement.csv")
    assert {"date", "impressions", "engagements", "day_of_week", "month", "engagement_rate"}.issubset(
        engagement.columns
    )
    assert (engagement["impressions"] >= 0).all()
    assert (engagement["engagement_rate"] >= 0).all()
    assert engagement["day_of_week"].notna().all()


@pytest.mark.integration
def test_extract_and_transform_should_produce_valid_followers_csv_when_given_real_xlsx(tmp_path):
    # Arrange
    xlsx = _find_xlsx()
    if xlsx is None:
        pytest.skip("No xlsx in data/raw — skipping integration test")

    # Act
    meta = run_extract(xlsx, tmp_path)
    run_transform(tmp_path, meta["total_followers"])

    # Assert — cumulative_followers must end at total_followers
    followers = pd.read_csv(tmp_path / "followers.csv")
    assert {"date", "new_followers", "cumulative_followers", "rolling_7d_avg"}.issubset(
        followers.columns
    )
    assert followers["cumulative_followers"].iloc[-1] == meta["total_followers"]
    assert (followers["new_followers"] >= 0).all()
