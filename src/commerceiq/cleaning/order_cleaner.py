import polars as pl

from commerceiq.cleaning.result import CleaningResult


class OrderCleaner:
    """
    Cleans order datasets.

    Responsibilities:
        - Remove duplicate orders.
        - Normalize text fields.
    """

    def clean(self, data: pl.DataFrame) -> CleaningResult:

        original_rows = data.shape[0]

        data = self.remove_duplicates(data)

        data = self.normalize_text(data)

        final_rows = data.shape[0]

        return CleaningResult(
            data=data,
            original_rows=original_rows,
            final_rows=final_rows,
            duplicates_removed=(
                original_rows - final_rows
            ),
            warnings=[]
        )


    def remove_duplicates(
        self,
        data: pl.DataFrame
    ) -> pl.DataFrame:

        return data.unique(
            subset=["order_id"],
            keep="first"
        )


    def normalize_text(
        self,
        data: pl.DataFrame
    ) -> pl.DataFrame:

        text_columns = [
            "client_nom",
            "client_adresse",
            "client_governorat",
            "order_source",
        ]

        for column in text_columns:
            data = data.with_columns(
                pl.col(column)
                .str.strip_chars()
                .str.to_lowercase()
            )

        return data