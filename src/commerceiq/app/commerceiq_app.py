from pathlib import Path

from commerceiq.analytics.kpi_builder import KPIBuilder
from commerceiq.analytics.market_analyzer import MarketAnalyzer
from commerceiq.app.result import CommerceIQResult
from commerceiq.cleaning.order_cleaner import OrderCleaner
from commerceiq.enrichment.geography_enricher import GeographyEnricher
from commerceiq.ingestion.csv_source import CSVDataSource
from commerceiq.pipeline.order_pipeline import OrderPipeline
from commerceiq.reporting.report_generator import ReportGenerator
from commerceiq.validation.schema_validator import SchemaValidator


class CommerceIQApp:

    def run(
        self,
        csv_path: str | Path,
    ) -> CommerceIQResult:

        source = CSVDataSource(csv_path)

        pipeline = OrderPipeline(
            data_source=source,
            validator=SchemaValidator(),
            cleaner=OrderCleaner(),
        )

        pipeline_result = pipeline.run()

        data = GeographyEnricher().enrich(
            pipeline_result.data
        )

        analysis = MarketAnalyzer().analyze(data)

        kpis = KPIBuilder().build(data)

        report = ReportGenerator().generate(
            kpis=kpis,
            analysis=analysis,
        )

        return CommerceIQResult(
        kpis=kpis,
        analysis=analysis,
        data=data,
)