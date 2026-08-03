import argparse

from commerceiq.app.commerceiq_app import CommerceIQApp
from commerceiq.reporting.report_generator import ReportGenerator


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="commerceiq",
        description="Business Intelligence for Tunisian E-commerce",
    )

    subparsers = parser.add_subparsers(dest="command")

    analyze = subparsers.add_parser(
        "analyze",
        help="Analyze an orders CSV file",
    )

    analyze.add_argument(
        "csv_path",
        help="Path to the CSV file",
    )

    args = parser.parse_args()

    if args.command == "analyze":
        app = CommerceIQApp()

        result = app.run(args.csv_path)

        report = ReportGenerator().generate(
            result.kpis,
            result.analysis,
        )

        print(report)

    else:
        parser.print_help()