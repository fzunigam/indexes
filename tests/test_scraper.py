from financial_indexes.scraper import fetch_and_parse_sp500

def test_scraper_returns_data():
    # Note: in real implementation, mock requests.get, but for this basic setup we test structure
    data = fetch_and_parse_sp500()
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'symbol' in data[0]