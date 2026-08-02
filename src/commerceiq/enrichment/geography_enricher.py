import polars as pl

from commerceiq.enrichment.geography import (
    get_geography
)


class GeographyEnricher:
    """
    Adds geographic business information
    to order data.
    """

    def enrich(  
        self,
        data: pl.DataFrame
    ) -> pl.DataFrame:

        return data.with_columns(
            pl.col("client_governorat")
            .map_elements(
                lambda x: get_geography(x)["zone"],
                return_dtype=pl.String
            )
            .alias("zone"),

            pl.col("client_governorat")
            .map_elements(
                lambda x: get_geography(x)["type"],
                return_dtype=pl.String
            )
            .alias("geography_type"),
        )