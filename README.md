# Indexes

A lightweight, professional Python utility to scrape and retrieve financial index constituents, starting with the S&P 500.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/indexes.svg)](https://pypi.org/project/indexes/)
[![Python versions](https://img.shields.io/pypi/pyversions/indexes.svg)](https://pypi.org/project/indexes/)

## About

`indexes` provides a simple, cached interface to access up-to-date data for major financial indexes. It currently supports fetching S&P 500 constituents directly from reliable public sources, providing essential metadata like sector, sub-industry, and CIK.

## Features

- **Simple API**: Get index data in one function call.
- **Flexible Output**: Choose between list or dictionary formats.
- **Selective Fields**: Retrieve only the data you need (symbol, name, sector, etc.).
- **Automatic Caching**: Minimizes network requests during the same session.
- **Lightweight**: Minimal dependencies (`requests`, `beautifulsoup4`).

## Installation

```bash
pip install indexes
```

### Requirements

- Python >= 3.8
- `requests`
- `beautifulsoup4`

## Usage

```python
from financial_indexes import get_sp500

# Get all S&P 500 symbols as a list
symbols = get_sp500()
print(f"Total symbols: {len(symbols)}")

# Get detailed info for all companies as a dictionary keyed by symbol
sp500_details = get_sp500(
    return_type='dict', 
    fields=['name', 'sector', 'sub_industry']
)
print(sp500_details['AAPL'])
# Output: {'name': 'Apple Inc.', 'sector': 'Information Technology', 'sub_industry': 'Technology Hardware, Storage & Peripherals'}

# Get specific fields as a list of dictionaries
data = get_sp500(return_type='list', fields=['name', 'sector'])
```

## Documentation

### `get_sp500(return_type='list', fields=None)`

Returns constituents of the S&P 500 index.

- **`return_type`** (str): `'list'` (default) or `'dict'`.
- **`fields`** (list, optional): List of fields to include. Defaults to `['symbol']`.
    - Supported fields: `symbol`, `name`, `sector`, `sub_industry`, `date_added`, `cik`, `founded`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/financial-indexes.git
   cd financial-indexes
   ```
2. Create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -e .
   ```

### Running Tests

```bash
pytest
```

## License

`financial-indexes` is licensed under the MIT license. See the [`LICENSE`](LICENSE) file for more information.
