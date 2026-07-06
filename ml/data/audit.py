"""
Dataset Audit Script

This module performs an initial audit of the raw groundwater dataset
without modifying it.

Outputs:
---------
reports/
    ├── column_summary.csv
    ├── missing_values.csv
    └── dataset_report.md
"""

from datetime import datetime

import pandas as pd

from ml.data.config import (
    COLUMN_SUMMARY_FILE,
    DATASET_REPORT_FILE,
    MISSING_VALUES_FILE,
    RAW_DATA_FILE,
    REPORTS_DIR,
)
from ml.data.load_data import load_dataset


def audit_dataset() -> None:
    """Run a complete audit on the raw dataset."""

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    df = load_dataset(RAW_DATA_FILE)

    rows, cols = df.shape

    # ------------------------------------------------------------------
    # Column Summary
    # ------------------------------------------------------------------

    column_summary = pd.DataFrame(
        {
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str),
            "Missing Values": df.isna().sum().values,
            "Unique Values": df.nunique().values,
        }
    )

    column_summary.to_csv(COLUMN_SUMMARY_FILE, index=False)

    # ------------------------------------------------------------------
    # Missing Values Report
    # ------------------------------------------------------------------

    missing_report = pd.DataFrame(
        {
            "Column": df.columns,
            "Missing Count": df.isna().sum().values,
            "Missing Percentage": (
                df.isna().mean().values * 100
            ).round(2),
        }
    )

    missing_report.to_csv(MISSING_VALUES_FILE, index=False)

    # ------------------------------------------------------------------
    # Dataset Statistics
    # ------------------------------------------------------------------

    duplicate_rows = int(df.duplicated().sum())

    memory_usage = round(
        df.memory_usage(deep=True).sum() / 1024**2,
        2,
    )

    report = f"""# Groundwater Dataset Audit Report

Generated on: {datetime.now()}

---

## Dataset Overview

| Metric | Value |
|--------|-------|
| Rows | {rows} |
| Columns | {cols} |
| Duplicate Rows | {duplicate_rows} |
| Memory Usage (MB) | {memory_usage} |

---

## Column Names

{chr(10).join(f"- {col}" for col in df.columns)}

---

## Missing Values

{missing_report.to_markdown(index=False)}

---

## Data Types

{column_summary[['Column','Data Type']].to_markdown(index=False)}

---

## Numeric Statistics

{df.describe(include='all').to_markdown()}
"""

    with open(DATASET_REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report)

    print("=" * 60)
    print("GROUNDWATER DATASET AUDIT")
    print("=" * 60)
    print(f"Rows              : {rows}")
    print(f"Columns           : {cols}")
    print(f"Duplicate Rows    : {duplicate_rows}")
    print(f"Memory Usage (MB) : {memory_usage}")
    print("=" * 60)

    print("\nReports Generated Successfully")
    print(f"• {COLUMN_SUMMARY_FILE}")
    print(f"• {MISSING_VALUES_FILE}")
    print(f"• {DATASET_REPORT_FILE}")


if __name__ == "__main__":
    audit_dataset()