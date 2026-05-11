from .scraper import fetch_and_parse_sp500, fetch_and_parse_nasdaq100

SUPPORTED_FIELDS = {'symbol', 'name', 'sector', 'sub_industry', 'date_added', 'cik', 'founded'}
SUPPORTED_FIELDS_NASDAQ100 = {'symbol', 'name', 'industry', 'subsector'}
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

def get_nasdaq100(return_type='list', fields=None):
    if return_type not in ('list', 'dict'):
        raise ValueError("Invalid return_type. Must be 'list' or 'dict'.")
    if fields is None:
        fields = ['symbol']
    for field in fields:
        if field not in SUPPORTED_FIELDS_NASDAQ100:
            raise ValueError(f"Unsupported field: {field}")
            
    if 'nasdaq100' not in _CACHE:
        _CACHE['nasdaq100'] = fetch_and_parse_nasdaq100()
        
    data = _CACHE['nasdaq100']
    
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

