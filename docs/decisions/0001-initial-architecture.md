# ADR 0001: Initial Architecture and Tooling

## Status
Accepted

## Context
We need to build a lightweight Python package to fetch the components of financial indexes like the S&P 500 from Wikipedia. The solution needs to be fast, easy to install, and provide flexible output formats (list or dict).

## Decision
- **Web Scraping:** Use `requests` and `beautifulsoup4` instead of `pandas` to keep the dependency footprint small.
- **Interface:** Provide a simple procedural API (`get_sp500()`) rather than requiring users to instantiate classes.
- **Caching:** Implement a simple module-level in-memory cache to ensure repeated calls within the same script do not trigger unnecessary web requests.
- **Build System:** Standard `setuptools` with `pyproject.toml`.

## Consequences
- Requires manual parsing of HTML tables, which might need updates if Wikipedia changes its page structure.
- The package remains extremely lightweight, making it easy to embed in other projects without bringing in heavy data science libraries.
- The procedural API is straightforward for beginners but robust enough for programmatic use.
