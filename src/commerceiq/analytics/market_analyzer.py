import polars as pl

from commerceiq.analytics.result import MarketAnalysisResult


class MarketAnalyzer:

    def analyze(self, data: pl.DataFrame) -> MarketAnalysisResult:
        return MarketAnalysisResult(
            revenue_by_channel=self.revenue_by_channel(data),
            revenue_by_governorate=pl.DataFrame(),
            revenue_by_zone=pl.DataFrame(),
            revenue_by_geography_type=pl.DataFrame(),
        )

    def revenue_by_channel(
        self,
        data: pl.DataFrame,
    ) -> pl.DataFrame:
        """
        Analyze sales performance by marketing channel.
        """

        return (
            data
            .group_by("order_source")
            .agg(
                pl.col("order_total").sum().alias("revenue"),
                pl.len().alias("orders"),
                pl.col("client_gsm1").n_unique().alias("unique_customers"),
                pl.col("order_total").mean().round(2).alias("average_order"),
            )
            .sort("revenue", descending=True)
        )