import pandas as pd
import pytest

from analyze import (
    analyze_engagement_by_day,
    analyze_follower_growth,
    analyze_topic_performance,
)


# ── analyze_engagement_by_day ─────────────────────────────────────────────────

def test_analyze_engagement_by_day_should_exclude_zero_impression_rows_when_day_is_inactive():
    # Arrange — Miércoles has 0 impressions
    engagement = pd.DataFrame({
        "date": pd.date_range("2026-03-16", periods=3),
        "impressions": [100, 0, 200],
        "engagements": [5, 0, 10],
        "engagement_rate": [0.05, 0.0, 0.05],
        "day_of_week": ["Lunes", "Martes", "Miércoles"],
        "month": ["Marzo", "Marzo", "Marzo"],
    })

    # Act
    result = analyze_engagement_by_day(engagement)

    # Assert
    assert "Martes" not in result.index
    assert len(result) == 2


def test_analyze_engagement_by_day_should_sort_descending_by_impressions_when_multiple_days():
    # Arrange
    engagement = pd.DataFrame({
        "date": pd.date_range("2026-03-16", periods=2),
        "impressions": [100, 300],
        "engagements": [5, 15],
        "engagement_rate": [0.05, 0.05],
        "day_of_week": ["Lunes", "Martes"],
        "month": ["Marzo", "Marzo"],
    })

    # Act
    result = analyze_engagement_by_day(engagement)

    # Assert — Martes (300) should be first
    assert result.index[0] == "Martes"
    assert result.index[1] == "Lunes"


# ── analyze_follower_growth ───────────────────────────────────────────────────

def test_analyze_follower_growth_should_return_correct_total_when_summing_new_followers():
    # Arrange
    followers = pd.DataFrame({
        "date": pd.to_datetime(["2025-07-01", "2025-07-02", "2025-07-03"]),
        "new_followers": [2, 3, 5],
        "cumulative_followers": [665, 668, 673],
        "rolling_7d_avg": [2.0, 2.5, 3.33],
    })

    # Act
    result = analyze_follower_growth(followers)

    # Assert
    assert result["total_gained"] == 10
    assert result["avg_daily"] == pytest.approx(10 / 3, rel=1e-2)


def test_analyze_follower_growth_should_detect_longest_zero_streak_when_multiple_runs():
    # Arrange — streaks of 1, 3, and 2 zeros; longest = 3
    followers = pd.DataFrame({
        "date": pd.date_range("2025-07-01", periods=10),
        "new_followers": [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        "cumulative_followers": range(10),
        "rolling_7d_avg": [1.0] * 10,
    })

    # Act
    result = analyze_follower_growth(followers)

    # Assert
    assert result["longest_zero_streak"] == 3


def test_analyze_follower_growth_should_identify_best_day_when_one_day_has_peak():
    # Arrange
    followers = pd.DataFrame({
        "date": pd.to_datetime(["2025-07-01", "2025-07-02", "2025-07-03"]),
        "new_followers": [1, 8, 2],
        "cumulative_followers": [663, 671, 673],
        "rolling_7d_avg": [1.0, 4.5, 3.67],
    })

    # Act
    result = analyze_follower_growth(followers)

    # Assert
    assert result["best_day_date"] == "2025-07-02"
    assert result["best_day_count"] == 8


# ── analyze_topic_performance ─────────────────────────────────────────────────

def test_analyze_topic_performance_should_return_empty_dataframe_when_no_topics():
    # Arrange — topics column is empty strings
    top_posts = pd.DataFrame({
        "post_url": ["https://url_a"],
        "impressions": [100],
        "engagements": [5],
        "engagement_rate": [0.05],
        "topics": [""],
    })

    # Act
    result = analyze_topic_performance(top_posts)

    # Assert
    assert result.empty
    assert "avg_impressions" in result.columns


def test_analyze_topic_performance_should_aggregate_stats_when_multiple_posts_share_topic():
    # Arrange — both posts have "python" → avg_impressions = (100+200)/2 = 150
    top_posts = pd.DataFrame({
        "post_url": ["https://url_a", "https://url_b"],
        "impressions": [100, 200],
        "engagements": [5, 10],
        "engagement_rate": [0.05, 0.05],
        "topics": ["python, data", "python"],
    })

    # Act
    result = analyze_topic_performance(top_posts)

    # Assert
    assert "python" in result.index
    assert result.loc["python", "post_count"] == 2
    assert result.loc["python", "avg_impressions"] == pytest.approx(150.0)
