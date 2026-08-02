from commerceiq.cleaning.order_cleaner import OrderCleaner
from commerceiq.ingestion.datasource import DataSource
from commerceiq.validation.schema_validator import SchemaValidator
from commerceiq.pipeline.result import PipelineResult


class OrderPipeline:
    """
    Runs the complete order processing workflow.
    """

    def __init__(
        self,
        data_source: DataSource,
        validator: SchemaValidator,
        cleaner: OrderCleaner,
    ):
        self.data_source = data_source
        self.validator = validator
        self.cleaner = cleaner


    def run(self) -> PipelineResult:

        # Step 1: Load data
        data = self.data_source.read()

        # Step 2: Validate schema
        self.validator.validate(
            data.columns
        )

        # Step 3: Clean data
        cleaning_result = self.cleaner.clean(
            data
        )

        return PipelineResult(
    data=cleaning_result.data,
    success=True,
    rows_loaded=data.shape[0],
    cleaning_result=cleaning_result,
    warnings=cleaning_result.warnings,
)