from dataclasses import dataclass

import polars as pl


@dataclass
class CleaningResult:
    """
    Stores the result of a cleaning operation.
    """

    data: pl.DataFrame
    original_rows: int
    final_rows: int
    duplicates_removed: int
    warnings: list[str]