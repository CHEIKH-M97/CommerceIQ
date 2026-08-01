import pytest

from commerceiq.validation.schema_validator import SchemaValidator


def test_valid_schema():

    validator = SchemaValidator(
        required_columns=[
            "order_id",
            "order_total",
        ]
    )

    result = validator.validate(
        [
            "order_id",
            "order_total",
            "extra_column",
        ]
    )

    assert result is True


def test_missing_required_column():

    validator = SchemaValidator(
        required_columns=[
            "order_id",
            "order_total",
        ]
    )

    with pytest.raises(ValueError):
        validator.validate(
            [
                "order_id",
            ]
        )