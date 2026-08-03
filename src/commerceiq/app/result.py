from dataclasses import dataclass

import polars as pl

from commerceiq.analytics.result import MarketAnalysisResult
from commerceiq.reporting.models import BusinessKPIs


@dataclass
class CommerceIQResult:
    kpis: BusinessKPIs
    analysis: MarketAnalysisResult
    data: pl.DataFrame