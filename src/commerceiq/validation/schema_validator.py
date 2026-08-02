REQUIRED_COLUMNS = [
    "order_id",
    "order_total",
    "order_source",
    "client_nom",
    "client_adresse",
    "client_governorat",
    "client_gsm1",
    "client_gsm2",
]
OPTIONAL_COLUMNS = [
    "client_gsm2",
]
class SchemaValidator:
    """
    Validates dataset columns.
    """

    def __init__(self
    ):
        self.required_columns = REQUIRED_COLUMNS
        self.optional_columns = OPTIONAL_COLUMNS

    def validate(self, columns: list[str]) -> bool:
        missing_columns = (
            set(self.required_columns)
            - set(columns)
        )

        if missing_columns:
            raise ValueError(
                f"Missing required columns: {missing_columns}"
            )

        return True