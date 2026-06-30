"""Pipeline: orquesta extract → transform → analyze → report."""

from pathlib import Path

from extract import run_extract
from transform import run_transform
from analyze import run_analyze
from report import generate_report

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
OUTPUT_DIR = DATA_DIR / "output"


def find_excel_file() -> Path:
    xlsx_files = list(RAW_DIR.glob("*.xlsx"))
    if not xlsx_files:
        raise FileNotFoundError(f"No .xlsx files found in {RAW_DIR}")
    if len(xlsx_files) > 1:
        print(f"Multiple Excel files found, using: {xlsx_files[0].name}")
    return xlsx_files[0]


def main():
    input_path = find_excel_file()
    print(f"1/4 Extracting from {input_path.name}...")
    extract_meta = run_extract(input_path, PROCESSED_DIR)

    print("2/4 Transforming...")
    run_transform(PROCESSED_DIR, extract_meta["total_followers"])

    print("3/4 Analyzing...")
    findings = run_analyze(PROCESSED_DIR, extract_meta["discovery"], extract_meta["total_followers"])

    print("4/4 Generating report...")
    report_path = generate_report(findings, OUTPUT_DIR)

    print(f"\nDone. Check {report_path}")


if __name__ == "__main__":
    main()
