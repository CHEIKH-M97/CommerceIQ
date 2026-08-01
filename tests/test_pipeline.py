from commerceiq.ingestion.csv_source import CSVDataSource
from commerceiq.pipeline.order_pipeline import OrderPipeline
from commerceiq.validation.schema_validator import SchemaValidator


def test_order_pipeline():

    source = CSVDataSource(
        "tests/test_data/sample_orders.csv"
    )

    validator = SchemaValidator(
        [
            "order_id",
            "order_total",
            "order_source",
            "client_nom",
            "client_adresse",
            "client_governorat",
            "client_gsm1",
        ]
    )

    pipeline = OrderPipeline(
        source,
        validator
    )

    result = pipeline.run()

    assert result.success is True
    assert result.rows_count == 3
    assert result.data.shape[0] == 3