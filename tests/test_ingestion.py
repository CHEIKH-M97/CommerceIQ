import pytest

from commerceiq.ingestion.csv_source import CSVDataSource
from commerceiq.ingestion.exceptions import FileNotFoundError


def test_csv_source_creation():
    source = CSVDataSource("test.csv")

    assert source.file_path.name == "test.csv"


def test_missing_file():
    source = CSVDataSource("missing.csv")

    with pytest.raises(FileNotFoundError):
        source.read()