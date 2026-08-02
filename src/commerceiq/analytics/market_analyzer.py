import polars as pl

from commerceiq.analytics.result import (
    MarketAnalysisResult
)


class MarketAnalyzer:

    def analyze(
        self,
        data: pl.DataFrame
    ) -> MarketAnalysisResult:

        return MarketAnalysisResult(

            revenue_by_channel=
                self.revenue_by_channel(data),

            revenue_by_governorate=
                self.revenue_by_governorate(data),

            revenue_by_zone=
                self.revenue_by_zone(data),

            revenue_by_geography_type=
                self.revenue_by_geography_type(data),
        )