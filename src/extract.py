"""Extract: Excel de LinkedIn → CSVs limpios en data/processed/."""

from pathlib import Path

import pandas as pd


def extract_discovery(xl: pd.ExcelFile) -> pd.DataFrame:
    raw = xl.parse("DISCOVERY", header=None)
    data = {}
    for _, row in raw.iterrows():
        key = str(row.iloc[0]).strip()
        val = row.iloc[1]
        data[key] = val
    return pd.DataFrame([data])


def extract_engagement(xl: pd.ExcelFile) -> pd.DataFrame:
    df = xl.parse("ENGAGEMENT", header=0)
    df.columns = ["date", "impressions", "engagements"]
    df["date"] = pd.to_datetime(df["date"], format="%m/%d/%Y")
    df["impressions"] = pd.to_numeric(df["impressions"], errors="coerce").fillna(0).astype(int)
    df["engagements"] = pd.to_numeric(df["engagements"], errors="coerce").fillna(0).astype(int)
    return df


def extract_top_posts(xl: pd.ExcelFile) -> pd.DataFrame:
    raw = xl.parse("TOP POSTS", header=None)
    # ponytail: two tables side by side, cols 0-2 = by engagement, cols 4-6 = by impressions
    header_row = raw[raw.iloc[:, 0] == "Post URL"].index[0]
    data = raw.iloc[header_row + 1:]

    by_eng = data.iloc[:, :3].copy()
    by_eng.columns = ["post_url", "publish_date", "engagements"]
    by_eng = by_eng.dropna(subset=["post_url"])

    by_imp = data.iloc[:, 4:7].copy()
    by_imp.columns = ["post_url", "publish_date", "impressions"]
    by_imp = by_imp.dropna(subset=["post_url"])

    by_eng["engagements"] = pd.to_numeric(by_eng["engagements"], errors="coerce").fillna(0).astype(int)
    by_imp["impressions"] = pd.to_numeric(by_imp["impressions"], errors="coerce").fillna(0).astype(int)

    eng_map = by_eng.set_index("post_url")["engagements"].to_dict()
    imp_map = by_imp.set_index("post_url")["impressions"].to_dict()

    all_urls = set(eng_map.keys()) | set(imp_map.keys())
    rows = []
    for url in all_urls:
        eng_row = by_eng[by_eng["post_url"] == url]
        imp_row = by_imp[by_imp["post_url"] == url]
        date = eng_row["publish_date"].iloc[0] if len(eng_row) else imp_row["publish_date"].iloc[0]
        rows.append({
            "post_url": url,
            "publish_date": date,
            "engagements": eng_map.get(url, 0),
            "impressions": imp_map.get(url, 0),
        })

    df = pd.DataFrame(rows)
    df["publish_date"] = pd.to_datetime(df["publish_date"], format="%m/%d/%Y")
    df = df.sort_values("impressions", ascending=False).reset_index(drop=True)
    return df


def extract_followers(xl: pd.ExcelFile) -> pd.DataFrame:
    raw = xl.parse("FOLLOWERS", header=None)
    header_row = raw[raw.iloc[:, 0] == "Date"].index[0]
    total_followers = int(raw.iloc[0, 1])

    df = raw.iloc[header_row + 1:].copy()
    df.columns = ["date", "new_followers"]
    df["date"] = pd.to_datetime(df["date"], format="%m/%d/%Y")
    df["new_followers"] = pd.to_numeric(df["new_followers"], errors="coerce").fillna(0).astype(int)
    df = df.reset_index(drop=True)
    return df, total_followers


def extract_demographics(xl: pd.ExcelFile) -> pd.DataFrame:
    df = xl.parse("DEMOGRAPHICS", header=0)
    df.columns = ["category", "value", "percentage"]
    df["percentage"] = df["percentage"].apply(
        lambda x: 0.5 if str(x).strip() == "< 1%" else float(str(x).replace("%", ""))
    )
    return df


def run_extract(input_path: str | Path, output_dir: str | Path) -> dict:
    input_path = Path(input_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    xl = pd.ExcelFile(input_path, engine="openpyxl")

    discovery = extract_discovery(xl)
    discovery.to_csv(output_dir / "discovery.csv", index=False)

    engagement = extract_engagement(xl)
    engagement.to_csv(output_dir / "engagement.csv", index=False)

    top_posts = extract_top_posts(xl)
    top_posts.to_csv(output_dir / "top_posts.csv", index=False)

    followers, total_followers = extract_followers(xl)
    followers.to_csv(output_dir / "followers.csv", index=False)

    demographics = extract_demographics(xl)
    demographics.to_csv(output_dir / "demographics.csv", index=False)

    return {
        "total_followers": total_followers,
        "discovery": discovery,
    }
