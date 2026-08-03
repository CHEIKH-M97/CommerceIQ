# CommerceIQ
An end-to-end Business Intelligence platform that transforms Tunisian raw e-commerce order data into business insights for management team and decision-makers.

> 🚧 Currently under active development.

## Features

- CSV ingestion for large datasets
- Data validation pipeline
- Data cleaning pipeline
- Geographic enrichment (Zone & Coastal/Interior)
- Business KPI generation
- Channel performance analysis
- Regional performance analysis
- CLI reporting
- Modular architecture

## Dataset

The original dataset contains over **3 million Tunisian e-commerce orders** and is private.
A small anonymized sample (`data/sample_orders.csv`) is included for testing and demonstration purposes.

## Project Structure

```text
src/
├── analytics/
├── app/
├── cleaning/
├── cli/
├── config/
├── ingestion/
├── pipeline/
├── reporting/
├── validation/
```
## Example Output

```text
============================================================
                COMMERCEIQ REPORT
============================================================

BUSINESS KPIs

Revenue: 118,655,992.53 TND

Orders: 1,560,668

Customers: 624,909

Average Order: 76.03 TND
```

## Installation

```bash
git clone https://github.com/CHEIKH-M97/CommerceIQ.git

cd CommerceIQ

uv sync
```
## Usage

```bash
uv run commerceiq analyze data/sample_orders.csv
```

## Technologies

- Python 3.13
- Polars
- UV
- Pytest
- Git

## Why CommerceIQ?

Most analytics projects rely on small public datasets.

CommerceIQ is built around a real-world Tunisian e-commerce dataset containing more than one million orders.

The goal is to transform raw operational data into business intelligence that helps companies understand revenue distribution, customer behavior, marketing channel performance, and regional trends.