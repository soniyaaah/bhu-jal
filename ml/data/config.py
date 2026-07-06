"""
Global configuration for the Groundwater Intelligence Platform.

This module centralizes project paths and configuration constants
to avoid hardcoding file locations across the project.
"""

from pathlib import Path

# -----------------------------------------------------------------------------
# Project Root
# -----------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# -----------------------------------------------------------------------------
# Data Directories
# -----------------------------------------------------------------------------

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

# -----------------------------------------------------------------------------
# Reports
# -----------------------------------------------------------------------------

REPORTS_DIR = PROJECT_ROOT / "reports"

# -----------------------------------------------------------------------------
# Input Dataset
# -----------------------------------------------------------------------------

RAW_DATA_FILE = RAW_DATA_DIR / "dwlr_hyderabad.xlsx"

# -----------------------------------------------------------------------------
# Output Files
# -----------------------------------------------------------------------------

CLEAN_DATA_FILE = PROCESSED_DATA_DIR / "groundwater_cleaned.csv"

COLUMN_SUMMARY_FILE = REPORTS_DIR / "column_summary.csv"

MISSING_VALUES_FILE = REPORTS_DIR / "missing_values.csv"

DATASET_REPORT_FILE = REPORTS_DIR / "dataset_report.md"