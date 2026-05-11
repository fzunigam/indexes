# Indexes: A Lightweight S&P 500 Scraper & Financial Data API

`indexes` is a professional Python utility designed to **scrape and retrieve financial index constituents**, providing developers with a clean, programmatic interface to access real-time market data. Starting with the **S&P 500**, it simplifies the process of extracting stock market components for financial analysis and algorithmic trading.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/indexes.svg)](https://pypi.org/project/indexes/)
[![Python versions](https://img.shields.io/pypi/pyversions/indexes.svg)](https://pypi.org/project/indexes/)
[![Financial Data Extraction](https://img.shields.io/badge/Financial-Data-green.svg)](#)

## Why use Indexes?

For financial analysts and Python developers, keeping an up-to-date list of **S&P 500 constituents** can be tedious. `indexes` provides a simple, cached interface to fetch this data from reliable public sources (like Wikipedia), returning essential metadata such as **Sector, Sub-Industry, CIK, and Founded Date**.

## Key Features

- **Efficient S&P 500 Scraper**: Get up-to-date SPX constituents in seconds.
- **Flexible Data Formats**: Retrieve results as a Python `list` or a `dict` keyed by symbol.
- **Granular Field Selection**: Extract only what you need (symbol, name, sector, sub-industry, CIK, etc.).
- **Smart Caching**: Minimizes network requests by caching data within the same execution session.
- **Minimalist Design**: Zero-config, lightweight, and easy to integrate into larger financial pipelines.

## Installation

Install the package via pip:

```bash
pip install indexes
```

### Requirements

- Python >= 3.8
- `requests`
- `beautifulsoup4`

## Quick Start & Usage

```python
from indexes import get_sp500

# Get a simple list of all S&P 500 ticker symbols
symbols = get_sp500()
print(f"Total S&P 500 companies: {len(symbols)}")

# Get detailed company data as a dictionary keyed by ticker symbol
# Perfect for financial modeling and mapping
sp500_details = get_sp500(
    return_type='dict', 
    fields=['name', 'sector', 'sub_industry']
)

# Example: Accessing Apple Inc. metadata
print(sp500_details['AAPL'])
# Output: {'name': 'Apple Inc.', 'sector': 'Information Technology', 'sub_industry': 'Technology Hardware, Storage & Peripherals'}

# Get a list of dictionaries with custom fields
data = get_sp500(return_type='list', fields=['name', 'sector', 'cik'])
```

## API Documentation

### `get_sp500(return_type='list', fields=None)`

The primary entry point for fetching the S&P 500 index components.

- **`return_type`** (str): `'list'` (default) or `'dict'`.
- **`fields`** (list, optional): List of metadata fields to include. Defaults to `['symbol']`.
    - **Supported fields**: `symbol`, `name`, `sector`, `sub_industry`, `date_added`, `cik`, `founded`.

## Development and Contributions

We welcome contributions from the community! Whether it's adding new indexes (Nasdaq 100, Dow Jones) or improving the scraper's robustness, feel free to submit a Pull Request.

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/fzunigam/indexes.git
   cd indexes
   ```
2. Install in editable mode:
   ```bash
   pip install -e .
   ```

### Running Tests

Ensure stability by running the test suite:

```bash
pytest
```

---

## Disclaimer

This project was built with the **help of AI coding tools**. 

## License

`indexes` is licensed under the **MIT License**. See the [`LICENSE`](LICENSE) file for more information.
