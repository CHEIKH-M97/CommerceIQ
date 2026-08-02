from commerceiq.analytics.metrics import (
    average_order_value,
    total_orders,
    total_revenue,
    unique_customers,
)

from commerceiq.reporting.models import BusinessKPIs

import polars as pl


class KPIBuilder:
    """
    Builds the main business KPIs from a dataset.
    """

    def build(
        self,
        data: pl.DataFrame,
    ) -> BusinessKPIs:

        return BusinessKPIs(
            total_revenue=total_revenue(data),
            total_orders=total_orders(data),
            unique_customers=unique_customers(data),
            average_order_value=average_order_value(data),
        )