"""Analyze: genera hallazgos y recomendaciones desde los datos transformados."""

from pathlib import Path

import pandas as pd


def analyze_engagement_by_day(engagement: pd.DataFrame) -> pd.DataFrame:
    active = engagement[engagement["impressions"] > 0]
    return (
        active.groupby("day_of_week")[["impressions", "engagements", "engagement_rate"]]
        .mean()
        .round(2)
        .sort_values("impressions", ascending=False)
    )


def analyze_engagement_by_month(engagement: pd.DataFrame) -> pd.DataFrame:
    active = engagement[engagement["impressions"] > 0]
    return (
        active.groupby("month")[["impressions", "engagements", "engagement_rate"]]
        .mean()
        .round(2)
        .sort_values("impressions", ascending=False)
    )


def analyze_topic_performance(top_posts: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for _, post in top_posts.iterrows():
        topics = [t.strip() for t in str(post["topics"]).split(",") if t.strip()]
        for topic in topics:
            rows.append({
                "topic": topic,
                "impressions": post["impressions"],
                "engagements": post["engagements"],
                "engagement_rate": post["engagement_rate"],
            })
    if not rows:
        return pd.DataFrame(columns=["topic", "avg_impressions", "avg_engagements", "avg_engagement_rate", "post_count"])

    topic_df = pd.DataFrame(rows)
    return (
        topic_df.groupby("topic")
        .agg(
            avg_impressions=("impressions", "mean"),
            avg_engagements=("engagements", "mean"),
            avg_engagement_rate=("engagement_rate", "mean"),
            post_count=("topic", "size"),
        )
        .round(2)
        .sort_values("avg_impressions", ascending=False)
    )


def analyze_posting_frequency(top_posts: pd.DataFrame) -> pd.DataFrame:
    return (
        top_posts.groupby("month")
        .size()
        .reset_index(name="post_count")
        .sort_values("post_count", ascending=False)
    )


def analyze_follower_growth(followers: pd.DataFrame) -> dict:
    total_gained = followers["new_followers"].sum()
    avg_daily = followers["new_followers"].mean()
    best_day = followers.loc[followers["new_followers"].idxmax()]
    worst_streak = 0
    current_streak = 0
    for val in followers["new_followers"]:
        if val == 0:
            current_streak += 1
            worst_streak = max(worst_streak, current_streak)
        else:
            current_streak = 0

    return {
        "total_gained": int(total_gained),
        "avg_daily": round(avg_daily, 2),
        "best_day_date": str(best_day["date"].date()),
        "best_day_count": int(best_day["new_followers"]),
        "longest_zero_streak": worst_streak,
    }


def analyze_demographics(demographics: pd.DataFrame) -> dict[str, pd.DataFrame]:
    result = {}
    for category in demographics["category"].unique():
        subset = demographics[demographics["category"] == category].sort_values("percentage", ascending=False)
        result[category] = subset.head(5)[["value", "percentage"]]
    return result


def generate_recommendations(
    by_day: pd.DataFrame,
    by_month: pd.DataFrame,
    topics: pd.DataFrame,
    demographics: dict[str, pd.DataFrame],
    follower_growth: dict,
) -> list[str]:
    recs = []

    if not by_day.empty:
        best_day = by_day.index[0]
        worst_day = by_day.index[-1]
        ratio = by_day.iloc[0]["impressions"] / max(by_day.iloc[-1]["impressions"], 1)
        recs.append(
            f"Posteá los **{best_day}** — {ratio:.1f}x más impressions que los {worst_day}."
        )

    if not by_month.empty:
        best_month = by_month.index[0]
        recs.append(f"Tu mejor mes fue **{best_month}** en promedio de impressions.")

    # ponytail: only recommend topics with 2+ posts to avoid noise
    frequent_topics = topics[topics["post_count"] >= 2] if not topics.empty else topics
    if not frequent_topics.empty:
        top_topic = frequent_topics.index[0]
        recs.append(
            f"El tema **{top_topic}** es tu mejor performer con {int(frequent_topics.iloc[0]['avg_impressions'])} impressions promedio ({int(frequent_topics.iloc[0]['post_count'])} posts)."
        )

    if "Job title" in demographics:
        top_title = demographics["Job title"].iloc[0]["value"]
        recs.append(f"Tu audiencia principal son **{top_title}s** — alineá tu contenido a sus intereses.")

    if "Industry" in demographics:
        top_industry = demographics["Industry"].iloc[0]["value"]
        recs.append(f"La industria dominante es **{top_industry}** ({demographics['Industry'].iloc[0]['percentage']}%).")

    if "Seniority" in demographics:
        top_seniority = demographics["Seniority"].iloc[0]["value"]
        pct = demographics["Seniority"].iloc[0]["percentage"]
        recs.append(f"El **{pct}%** de tu audiencia es nivel **{top_seniority}**.")

    recs.append(
        f"Ganaste **{follower_growth['total_gained']}** followers en el periodo "
        f"(promedio {follower_growth['avg_daily']}/día). "
        f"Mejor día: {follower_growth['best_day_date']} con {follower_growth['best_day_count']} nuevos."
    )

    return recs


def run_analyze(processed_dir: str | Path, discovery: pd.DataFrame, total_followers: int) -> dict:
    processed_dir = Path(processed_dir)

    engagement = pd.read_csv(processed_dir / "engagement.csv", parse_dates=["date"])
    top_posts = pd.read_csv(processed_dir / "top_posts.csv", parse_dates=["publish_date"])
    followers = pd.read_csv(processed_dir / "followers.csv", parse_dates=["date"])
    demographics_df = pd.read_csv(processed_dir / "demographics.csv")

    by_day = analyze_engagement_by_day(engagement)
    by_month = analyze_engagement_by_month(engagement)
    topics = analyze_topic_performance(top_posts)
    frequency = analyze_posting_frequency(top_posts)
    follower_growth = analyze_follower_growth(followers)
    demographics = analyze_demographics(demographics_df)

    recs = generate_recommendations(by_day, by_month, topics, demographics, follower_growth)

    return {
        "discovery": discovery,
        "total_followers": total_followers,
        "by_day": by_day,
        "by_month": by_month,
        "topics": topics,
        "frequency": frequency,
        "follower_growth": follower_growth,
        "demographics": demographics,
        "top_posts": top_posts,
        "recommendations": recs,
    }
