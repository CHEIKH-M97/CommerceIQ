class SchemaValidator:
    """
    Validates dataset columns.
    """

    def __init__(
        self,
        required_columns: list[str],
        optional_columns: list[str] | None = None,
    ):
        self.required_columns = required_columns
        self.optional_columns = optional_columns or []

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