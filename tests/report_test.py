
from commerceiq.reporting.models import BusinessKPIs
from commerceiq.reporting.report_generator import ReportGenerator


kpis = BusinessKPIs(
    total_revenue=123456.5,
    total_orders=1000,
    unique_customers=850,
    average_order_value=123.46,
)

report = ReportGenerator().generate(kpis)
assert "COMMERCEIQ REPORT" in report
assert "123,456.50 TND" in report
assert "1,000" in report