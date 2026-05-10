# Architecture Overview

**financial-indexes** is a lightweight Python library providing an easy programmatic interface to fetch constituents of financial indexes.

## Components
1. **API Layer (`__init__.py`, `api.py`)**: Exposes the user-facing functions like `get_sp500()`. Handles argument validation (`return_type`, `fields`) and formatting the output.
2. **Scraper Engine (`scraper.py`)**: Uses `requests` to fetch HTML from data sources (e.g., Wikipedia) and `beautifulsoup4` to extract data from tables.
3. **Cache Manager**: An in-memory, module-level dictionary that stores the parsed data upon the first successful fetch to prevent redundant network calls during the lifecycle of the Python process.

## Data Flow
User calls `get_sp500()` -> API layer checks cache -> If empty, Scraper Engine fetches Wikipedia and parses the HTML table -> Data is cached -> API layer filters fields and formats as list/dict -> Returns to User.
