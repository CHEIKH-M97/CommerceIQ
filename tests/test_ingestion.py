from commerceiq.ingestion.csv_source import CSVDataSource


def test_csv_source_creation():
    source = CSVDataSource("test.csv")

    assert source.file_path.name == "test.csv"