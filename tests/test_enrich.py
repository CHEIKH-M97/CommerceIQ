import polars as pl

from commerceiq.enrichment.geography_enricher import (
    GeographyEnricher
)


def test_geography_enrichment():

    data = pl.DataFrame(
        {
            "client_governorat": [
                "sousse",
                "kairouan",
                "tunis",
            ]
        }
    )

    enricher = GeographyEnricher()

    result = enricher.enrich(data)

    assert result["zone"].to_list() == [
        "Center",
        "Center",
        "North",
    ]

    assert result["geography_type"].to_list() == [
        "Coastal",
        "Interior",
        "Coastal",
    ]