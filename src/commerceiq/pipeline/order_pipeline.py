from commerceiq.ingestion.datasource import DataSource
from commerceiq.validation.schema_validator import SchemaValidator
from commerceiq.pipeline.result import PipelineResult

class OrderPipeline:
    """
    Pipeline responsible for loading and validating orders.
    """

    def __init__(
        self,
        data_source: DataSource,
        validator: SchemaValidator,
    ):
        self.data_source = data_source
        self.validator = validator


    def run(self):  
        data = self.data_source.read()

        self.validator.validate(
            data.columns
        )

        return PipelineResult(
    data=data,
    success=True,
    rows_count=data.shape[0],
    warnings=[]
)