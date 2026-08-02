from dataclasses import dataclass


@dataclass
class BusinessKPIs:
    total_revenue: float
    total_orders: int
    unique_customers: int
    average_order_value: float