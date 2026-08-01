from pathlib import Path

import polars as pl

from commerceiq.ingestion.datasource import DataSource


class CSVDataSource(DataSource):
    """
    Reads data from CSV files.

    Purpose:
        Provide CSV data loading functionality.

    Responsibilities:
        - Receive a CSV file path.
        - Load the file.
        - Return a Polars DataFrame.

    Inputs:
        A path pointing to a CSV file.

    Outputs:
        A Polars DataFrame.
    """

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def read(self) -> pl.DataFrame:
        return pl.read_csv(self.file_path)