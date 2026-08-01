class IngestionError(Exception):
    """
    Base exception for ingestion-related errors.
    """
    pass


class FileNotFoundError(IngestionError):
    """
    Raised when the input file does not exist.
    """
    pass


class InvalidFileError(IngestionError):
    """
    Raised when the input file cannot be processed.
    """
    pass