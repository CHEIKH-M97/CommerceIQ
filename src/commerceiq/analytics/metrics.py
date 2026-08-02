import polars as pl


def total_revenue(data: pl.DataFrame) -> float:
    """
    Returns the total revenue.
    """
    return float(data["order_total"].sum())


def total_orders(data: pl.DataFrame) -> int:
    """
    Returns the total number of orders.
    """
    return data.height


def average_order_value(data: pl.DataFrame) -> float:
    """
    Returns the average order value.
    """
    return float(data["order_total"].mean())


def unique_customers(data: pl.DataFrame) -> int:
    """
    Returns the number of unique customers
    based on their primary phone number.
    """
    return data["client_gsm1"].n_unique()