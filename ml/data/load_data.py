"""
Dataset Loader.

Loads groundwater datasets from Excel or CSV.
"""

from pathlib import Path

import pandas as pd


def load_dataset(file_path: Path) -> pd.DataFrame:
    """
    Load groundwater dataset.

    Parameters
    ----------
    file_path : Path
        Path to dataset.

    Returns
    -------
    pd.DataFrame
    """

    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} not found.")

    suffix = file_path.suffix.lower()

    if suffix == ".xlsx":
        return pd.read_excel(file_path)

    if suffix == ".csv":
        return pd.read_csv(file_path)

    raise ValueError(
        "Unsupported file format. Expected CSV or Excel."
    )