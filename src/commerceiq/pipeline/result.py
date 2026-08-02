from dataclasses import dataclass

import polars as pl

from commerceiq.cleaning.result import CleaningResult


@dataclass
class PipelineResult:
    """
    Final result of an order processing pipeline.
    """

    data: pl.DataFrame
    success: bool
    rows_loaded: int
    cleaning_result: CleaningResult
    warnings: list[str]