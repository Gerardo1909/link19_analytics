"""Transform: limpieza + feature engineering sobre CSVs procesados."""

import re
from pathlib import Path
from urllib.parse import unquote

import pandas as pd

SLUG_STOPWORDS = {
    "ugcpost", "share", "activity", "posts", "www", "linkedin", "com",
    "https", "http", "en", "de", "la", "el", "los", "las", "un", "una",
    "que", "por", "para", "con", "del", "al", "se", "es", "no", "su",
    "como", "pero", "más", "este", "esta", "estos", "estas", "fue",
    "son", "muy", "ya", "hay", "ser", "sobre", "todo", "entre", "cuando",
    "sin", "hasta", "desde", "donde", "durante", "cada", "puede",
    "dias", "tiempo", "esto", "esos", "estas", "algunos",
    "estuve", "dedicando", "bastante", "estos", "ideas",
}

DAY_NAMES_ES = {
    0: "Lunes", 1: "Martes", 2: "Miércoles", 3: "Jueves",
    4: "Viernes", 5: "Sábado", 6: "Domingo",
}

MONTH_NAMES_ES = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre",
}


def extract_topics_from_url(url: str) -> list[str]:
    decoded = unquote(str(url))
    # ponytail: format is username_TOPICS-share-ID or username_TOPICS-ugcPost-ID
    slug_match = re.search(r"_([a-zA-ZÀ-ÿ][\w\-À-ÿ]+?)(?:-(?:share|ugcPost|ugcpost)-)", decoded)
    if not slug_match:
        return []
    slug = slug_match.group(1).lower()
    tokens = re.split(r"[-_\s]+", slug)
    topics = [
        t for t in tokens
        if len(t) > 3 and t not in SLUG_STOPWORDS and not t.isdigit()
        and not re.fullmatch(r"[0-9a-f]{4,}", t)
    ]
    return topics


def transform_engagement(processed_dir: Path) -> pd.DataFrame:
    df = pd.read_csv(processed_dir / "engagement.csv", parse_dates=["date"])
    df["day_of_week"] = df["date"].dt.dayofweek.map(DAY_NAMES_ES)
    df["month"] = df["date"].dt.month.map(MONTH_NAMES_ES)
    df["engagement_rate"] = (df["engagements"] / df["impressions"].replace(0, float("nan"))).fillna(0)
    df.to_csv(processed_dir / "engagement.csv", index=False)
    return df


def transform_top_posts(processed_dir: Path) -> pd.DataFrame:
    df = pd.read_csv(processed_dir / "top_posts.csv", parse_dates=["publish_date"])
    df["topics"] = df["post_url"].apply(extract_topics_from_url).apply(", ".join)
    df["engagement_rate"] = (df["engagements"] / df["impressions"].replace(0, float("nan"))).fillna(0)
    df["day_of_week"] = df["publish_date"].dt.dayofweek.map(DAY_NAMES_ES)
    df["month"] = df["publish_date"].dt.month.map(MONTH_NAMES_ES)
    df.to_csv(processed_dir / "top_posts.csv", index=False)
    return df


def transform_followers(processed_dir: Path, total_followers: int) -> pd.DataFrame:
    df = pd.read_csv(processed_dir / "followers.csv", parse_dates=["date"])
    total_gained = df["new_followers"].sum()
    start_followers = total_followers - total_gained
    df["cumulative_followers"] = start_followers + df["new_followers"].cumsum()
    df["rolling_7d_avg"] = df["new_followers"].rolling(7, min_periods=1).mean().round(2)
    df.to_csv(processed_dir / "followers.csv", index=False)
    return df


def transform_demographics(processed_dir: Path) -> pd.DataFrame:
    df = pd.read_csv(processed_dir / "demographics.csv")
    df.to_csv(processed_dir / "demographics.csv", index=False)
    return df


def run_transform(processed_dir: str | Path, total_followers: int) -> None:
    processed_dir = Path(processed_dir)
    transform_engagement(processed_dir)
    transform_top_posts(processed_dir)
    transform_followers(processed_dir, total_followers)
    transform_demographics(processed_dir)
