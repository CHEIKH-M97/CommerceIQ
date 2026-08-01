import polars as pl

from commerceiq.cleaning.order_cleaner import OrderCleaner


def test_order_cleaner():

    data = pl.read_csv(
        "tests/test_data/dirty_orders.csv"
    )

    cleaner = OrderCleaner()

    result = cleaner.clean(data)

    result = cleaner.clean(data)

    assert result.original_rows == 3
    assert result.final_rows == 2
    assert result.duplicates_removed == 1