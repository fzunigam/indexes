# S&P 500 Scraper Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a Python package to fetch S&P 500 constituents from Wikipedia with a simple, cached API.

**Architecture:** A procedural API layer handles argument validation and returns formatted data, while a scraper engine fetches HTML via `requests` and parses it with `BeautifulSoup`. A module-level cache prevents redundant requests.

**Tech Stack:** Python, setuptools, requests, beautifulsoup4, pytest.

---

### Task 1: Project Setup

**Files:**
- Create: `pyproject.toml`
- Create: `tests/test_setup.py`

**Step 1: Write the failing test**

```python
# tests/test_setup.py
import financial_indexes

def test_package_imports():
    assert financial_indexes.__version__ == "0.1.0"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_setup.py -v`
Expected: FAIL with "ModuleNotFoundError: No module named 'financial_indexes'"

**Step 3: Write minimal implementation**

```toml
# pyproject.toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "financial-indexes"
version = "0.1.0"
dependencies = [
    "requests",
    "beautifulsoup4"
]
```

```python
# src/financial_indexes/__init__.py
__version__ = "0.1.0"
```

**Step 4: Run test to verify it passes**

Run: `pip install -e .` then `pytest tests/test_setup.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add pyproject.toml tests/test_setup.py src/financial_indexes/__init__.py
git commit -m "chore: setup project and tests"
```

---

### Task 2: API Validation Logic

**Files:**
- Create: `tests/test_api.py`
- Create: `src/financial_indexes/api.py`

**Step 1: Write the failing test**

```python
# tests/test_api.py
import pytest
from financial_indexes.api import get_sp500

def test_invalid_return_type():
    with pytest.raises(ValueError, match="Invalid return_type"):
        get_sp500(return_type='tuple')

def test_invalid_fields():
    with pytest.raises(ValueError, match="Unsupported field"):
        get_sp500(fields=['symbol', 'fake_field'])
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_api.py -v`
Expected: FAIL

**Step 3: Write minimal implementation**

```python
# src/financial_indexes/api.py
SUPPORTED_FIELDS = {'symbol', 'name', 'sector', 'sub_industry', 'date_added', 'cik', 'founded'}

def get_sp500(return_type='list', fields=None):
    if return_type not in ('list', 'dict'):
        raise ValueError("Invalid return_type. Must be 'list' or 'dict'.")
    
    if fields is None:
        fields = ['symbol']
        
    for field in fields:
        if field not in SUPPORTED_FIELDS:
            raise ValueError(f"Unsupported field: {field}")
            
    return []
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_api.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add tests/test_api.py src/financial_indexes/api.py
git commit -m "feat: add api validation logic"
```

---

### Task 3: Scraper Engine

**Files:**
- Create: `tests/test_scraper.py`
- Create: `src/financial_indexes/scraper.py`

**Step 1: Write the failing test**

```python
# tests/test_scraper.py
from financial_indexes.scraper import fetch_and_parse_sp500

def test_scraper_returns_data(mocker):
    # Note: in real implementation, mock requests.get, but for this basic setup we test structure
    data = fetch_and_parse_sp500()
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'symbol' in data[0]
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_scraper.py -v`
Expected: FAIL

**Step 3: Write minimal implementation**

```python
# src/financial_indexes/scraper.py
import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

def fetch_and_parse_sp500():
    response = requests.get(URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'id': 'constituents'})
    
    results = []
    for row in table.find_all('tr')[1:]:
        cols = row.find_all(['td', 'th'])
        if len(cols) >= 8:
            results.append({
                'symbol': cols[0].text.strip(),
                'name': cols[1].text.strip(),
                'sector': cols[3].text.strip(),
                'sub_industry': cols[4].text.strip(),
                'date_added': cols[6].text.strip(),
                'cik': cols[7].text.strip(),
                'founded': cols[8].text.strip() if len(cols) > 8 else ''
            })
    return results
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_scraper.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add tests/test_scraper.py src/financial_indexes/scraper.py
git commit -m "feat: implement wikipedia scraper"
```

---

### Task 4: Integration and Caching

**Files:**
- Modify: `src/financial_indexes/api.py`
- Modify: `src/financial_indexes/__init__.py`
- Modify: `tests/test_api.py`

**Step 1: Write the failing test**

```python
# tests/test_api.py (append)
def test_get_sp500_list():
    res = get_sp500(return_type='list', fields=['symbol'])
    assert len(res) > 400
    assert isinstance(res[0], str)

def test_get_sp500_dict():
    res = get_sp500(return_type='dict', fields=['name'])
    assert 'AAPL' in res
    assert 'name' in res['AAPL']
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_api.py -v`
Expected: FAIL

**Step 3: Write minimal implementation**

```python
# src/financial_indexes/api.py (update)
from .scraper import fetch_and_parse_sp500

SUPPORTED_FIELDS = {'symbol', 'name', 'sector', 'sub_industry', 'date_added', 'cik', 'founded'}
_CACHE = {}

def get_sp500(return_type='list', fields=None):
    if return_type not in ('list', 'dict'):
        raise ValueError("Invalid return_type. Must be 'list' or 'dict'.")
    if fields is None:
        fields = ['symbol']
    for field in fields:
        if field not in SUPPORTED_FIELDS:
            raise ValueError(f"Unsupported field: {field}")
            
    if 'sp500' not in _CACHE:
        _CACHE['sp500'] = fetch_and_parse_sp500()
        
    data = _CACHE['sp500']
    
    if return_type == 'dict':
        return {
            row['symbol']: {k: v for k, v in row.items() if k in fields}
            for row in data
        }
    
    if return_type == 'list':
        if len(fields) == 1 and fields[0] == 'symbol':
            return [row['symbol'] for row in data]
        return [
            {k: v for k, v in row.items() if k in fields or k == 'symbol'}
            for row in data
        ]
```

```python
# src/financial_indexes/__init__.py (update)
from .api import get_sp500

__version__ = "0.1.0"
__all__ = ["get_sp500"]
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_api.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/financial_indexes tests/test_api.py
git commit -m "feat: integrate scraper with api and caching"
```
