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
