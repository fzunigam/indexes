# Design: Financial Indexes Package (v0.1.0)

## Overview
A lightweight Python package to easily fetch the stocks composing financial indexes, starting with the S&P 500. Designed for developers who want a quick programmatic way to get index members without heavy dependencies or manual web scraping.

## 1. Project Structure & Tools
- **Package Name:** `financial-indexes`
- **Build System:** `setuptools` with `pyproject.toml`
- **Dependencies:** `requests`, `beautifulsoup4`

## 2. API Design
- **Core Function:** `get_sp500(return_type='list', fields=None)`
- **Parameters:**
  - `return_type` (str): Either `'list'` or `'dict'`.
  - `fields` (list[str]): The data fields to return. Defaults to `['symbol']`.
    - Available fields: `'symbol'`, `'name'`, `'sector'`, `'sub_industry'`, `'date_added'`, `'cik'`, `'founded'`.
- **Return Behavior:**
  - `return_type='list'`, `fields=['symbol']` -> `['AAPL', 'MSFT', ...]`
  - `return_type='list'`, multiple fields -> `[{'symbol': 'AAPL', 'name': 'Apple Inc.', 'sector': '...'}, ...]`
  - `return_type='dict'` -> Keys are always symbols. Values are dicts with the requested fields: `{'AAPL': {'name': 'Apple Inc.', 'sector': '...'}, ...}`

## 3. Data Flow & Caching
- **Source:** Wikipedia List of S&P 500 companies table.
- **Fetching:** Uses `requests` and parses HTML with `beautifulsoup4`.
- **Caching:** A module-level in-memory cache stores the parsed data upon the first call. Subsequent calls reuse this cached data to ensure fast execution and avoid rate-limiting or abusing Wikipedia's servers.

## 4. Error Handling
- Raises `ValueError` for invalid `return_type` or unsupported `fields`.
- Raises custom exceptions (e.g., `FetchError`, `ParseError`) if network requests fail or Wikipedia alters the table structure.
