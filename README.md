# Indexes: A Lightweight S&P 500, Nasdaq-100 & S&P 100 Scraper

`indexes` is a professional Python utility designed to **scrape and retrieve financial index constituents**, providing developers with a clean, programmatic interface to access real-time market data. It simplifies the process of extracting stock market components from the **S&P 500**, **Nasdaq-100**, and **S&P 100** for financial analysis and algorithmic trading.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/indexes.svg)](https://pypi.org/project/indexes/)
[![Python versions](https://img.shields.io/pypi/pyversions/indexes.svg)](https://pypi.org/project/indexes/)
[![Financial Data Extraction](https://img.shields.io/badge/Financial-Data-green.svg)](#)

## Why use Indexes?

For financial analysts and Python developers, keeping up-to-date lists of **S&P 500, Nasdaq-100 and S&P 100 constituents** can be tedious. `indexes` provides a simple, cached interface to fetch this data from reliable public sources (like Wikipedia), returning essential metadata such as **Sector, Industry, CIK, and more**.

## Key Features

- **Efficient Scrapers**: Get up-to-date S&P 500, Nasdaq-100 and S&P 100 constituents in seconds.
- **Flexible Data Formats**: Retrieve results as a Python `list` or a `dict` keyed by symbol.
- **Granular Field Selection**: Extract only what you need.
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
from indexes import get_sp500, get_nasdaq100, get_sp100

# Get a simple list of all S&P 500 ticker symbols
sp500_symbols = get_sp500()

# Get S&P 100 symbols
sp100_symbols = get_sp100()

# Get Nasdaq-100 details
nasdaq_details = get_nasdaq100(
    return_type='dict', 
    fields=['name', 'industry']
)

# Example: Accessing Apple Inc. metadata (present in both)
print(nasdaq_details['AAPL'])
# Output: {'name': 'Apple Inc.', 'industry': 'Technology'}

# Get a list of dictionaries with custom fields
data = get_sp500(return_type='list', fields=['name', 'sector', 'cik'])
```

## API Documentation

### `get_sp500(return_type='list', fields=None)`
The entry point for fetching the S&P 500 index components.
- **`return_type`** (str): `'list'` (default) or `'dict'`.
- **`fields`** (list, optional): Defaults to `['symbol']`.
    - **Supported fields**: `symbol`, `name`, `sector`, `sub_industry`, `date_added`, `cik`, `founded`.

### `get_nasdaq100(return_type='list', fields=None)`
The entry point for fetching the Nasdaq-100 index components.
- **`return_type`** (str): `'list'` (default) or `'dict'`.
- **`fields`** (list, optional): Defaults to `['symbol']`.
    - **Supported fields**: `symbol`, `name`, `industry`, `subsector`.

### `get_sp100(return_type='list', fields=None)`
The entry point for fetching the S&P 100 index components.
- **`return_type`** (str): `'list'` (default) or `'dict'`.
- **`fields`** (list, optional): Defaults to `['symbol']`.
    - **Supported fields**: `symbol`, `name`, `sector`.

## Development and Contributions

We welcome contributions from the community! Whether it's adding new indexes, new features or improving the scraper's robustness, feel free to submit a Pull Request.

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
