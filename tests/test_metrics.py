import polars as pl

from commerceiq.analytics.metrics import (
    average_order_value,
    total_orders,
    total_revenue,
    unique_customers,
)


def test_metrics():

    data = pl.DataFrame(
        {
            "order_total": [100.0, 50.0, 150.0],
            "client_gsm1": [
                "11111111",
                "22222222",
                "11111111",
            ],
        }
    )

    assert total_revenue(data) == 300.0
    assert total_orders(data) == 3
    assert average_order_value(data) == 100.0
    assert unique_customers(data) == 2