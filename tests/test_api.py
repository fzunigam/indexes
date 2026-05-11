import pytest
from indexes.api import get_sp500

def test_invalid_return_type():
    with pytest.raises(ValueError, match="Invalid return_type"):
        get_sp500(return_type='tuple')

def test_invalid_fields():
    with pytest.raises(ValueError, match="Unsupported field"):
        get_sp500(fields=['symbol', 'fake_field'])

def test_get_sp500_list():
    res = get_sp500(return_type='list', fields=['symbol'])
    assert len(res) > 400
    assert isinstance(res[0], str)

def test_get_sp500_dict():
    res = get_sp500(return_type='dict', fields=['name'])
    assert 'AAPL' in res
    assert 'name' in res['AAPL']
