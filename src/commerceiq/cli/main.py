import argparse

from commerceiq.app.commerceiq_app import CommerceIQApp


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

        report = app.analyze(args.csv_path)

        print(report)

    else:
        parser.print_help()