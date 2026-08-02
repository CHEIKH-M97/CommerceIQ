from dataclasses import dataclass

import polars as pl


@dataclass
class MarketAnalysisResult:

    revenue_by_channel: pl.DataFrame

    revenue_by_governorate: pl.DataFrame

    revenue_by_zone: pl.DataFrame

    revenue_by_geography_type: pl.DataFrame