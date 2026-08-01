from dataclasses import dataclass

import polars as pl


@dataclass
class PipelineResult:
    """
    Stores the output of a CommerceIQ pipeline run.
    """

    data: pl.DataFrame
    success: bool
    rows_count: int
    warnings: list[str]