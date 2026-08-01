from pathlib import Path

import polars as pl

from commerceiq.ingestion.datasource import DataSource
from commerceiq.ingestion.exceptions import (
    FileNotFoundError,
    InvalidFileError,
)


class CSVDataSource(DataSource):
    """
    Reads data from CSV files.

    Purpose:
        Load CSV datasets into CommerceIQ.

    Responsibilities:
        - Validate file existence.
        - Load CSV content.
        - Return a Polars DataFrame.

    Inputs:
        Path to a CSV file.

    Outputs:
        Polars DataFrame.
    """

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def read(self) -> pl.DataFrame:
        if not self.file_path.exists():
            raise FileNotFoundError(
                f"CSV file not found: {self.file_path}"
            )

        if self.file_path.suffix.lower() != ".csv":
            raise InvalidFileError(
                f"Expected CSV file, got: {self.file_path.suffix}"
            )

        try:
            return pl.read_csv(self.file_path)

        except Exception as error:
            raise InvalidFileError(
                f"Could not read CSV file: {self.file_path}"
            ) from error