from commerceiq.reporting.models import BusinessKPIs
from commerceiq.reporting.formatter import format_currency
from commerceiq.reporting.table_formatter import TableFormatter


class ReportGenerator:

    def generate(
        self,
        kpis: BusinessKPIs,
        analysis: dict,
    ) -> str:

        lines = []

        lines.append("=" * 60)
        lines.append("                COMMERCEIQ REPORT")
        lines.append("=" * 60)

        lines.append("")
        lines.append("BUSINESS KPIs")
        lines.append("-" * 60)

        lines.append(
            f"Total Revenue      : {format_currency(kpis.total_revenue)}"
        )

        lines.append(
            f"Orders             : {kpis.total_orders:,}"
        )

        lines.append(
            f"Unique Customers   : {kpis.unique_customers:,}"
        )

        lines.append(
            f"Average Order      : {format_currency(kpis.average_order_value)}"
        )
        lines.append("")
        lines.append("=" * 60)
        lines.append("CHANNEL INTELLIGENCE")
        lines.append("=" * 60)

        lines.append(
            TableFormatter().format(
                analysis.revenue_by_channel
            )
        )
        lines.append("")
        lines.append("=" * 60)
        lines.append("Costal vs Internal INTELLIGENCE")
        lines.append("=" * 60)

        lines.append(
            TableFormatter().format(
                analysis.revenue_by_geography_type
            )
        )
        lines.append("")
        lines.append("=" * 60)
        lines.append("Zone INTELLIGENCE")
        lines.append("=" * 60)

        lines.append(
            TableFormatter().format(
                analysis.revenue_by_zone
            )
        )
        return "\n".join(lines)