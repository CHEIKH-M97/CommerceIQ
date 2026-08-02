from __future__ import annotations


import polars as pl


class TableFormatter:
    """
    Formats Polars DataFrames into clean ASCII tables.
    """
    def format(self, data: pl.DataFrame) -> str:
        COLUMN_NAMES = {
            "order_source": "Channel",
            "revenue": "Revenue (TND)",
            "orders": "Orders",
            "unique_customers": "Customers",
            "average_order": "Avg Order",
            "zone": "Zone",
            "geography_type": "Geography",
            "client_governorat": "Governorate",
        }

        if data.is_empty():
            return "(no data)"

        # Human-friendly header labels
        headers = [COLUMN_NAMES.get(column, column) for column in data.columns]

        # Build rows with per-column formatting
        rows: list[list[str]] = []
        for row in data.iter_rows():
            formatted_row: list[str] = []
            for i, value in enumerate(row):
                col = data.columns[i]
                if value is None:
                    formatted = ""
                elif col in ("revenue", "average_order"):
                    try:
                        formatted = f"{float(value):,.2f}"
                    except Exception:
                        formatted = str(value)
                elif col in ("orders", "unique_customers"):
                    try:
                        formatted = f"{int(value):,}"
                    except Exception:
                        formatted = str(value)
                else:
                    formatted = str(value)

                formatted_row.append(formatted)

            rows.append(formatted_row)
        # Determine the width of each column
        widths = []

        for i, header in enumerate(headers):
            longest = len(header)

            for row in rows:
                longest = max(longest, len(row[i]))

            widths.append(longest)

        # Header
        header_line = "  ".join(
            header.ljust(widths[i])
            for i, header in enumerate(headers)
        )

        separator = "-" * len(header_line)

        body = [
            "  ".join(
                row[i].ljust(widths[i])
                for i in range(len(headers))
            )
            for row in rows
        ]

        return "\n".join(
            [
                header_line,
                separator,
                *body,
            ]
        )