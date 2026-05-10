import pytest
from financial_indexes.api import get_sp500

def test_invalid_return_type():
    with pytest.raises(ValueError, match="Invalid return_type"):
        get_sp500(return_type='tuple')

def test_invalid_fields():
    with pytest.raises(ValueError, match="Unsupported field"):
        get_sp500(fields=['symbol', 'fake_field'])
