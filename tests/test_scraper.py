from indexes.scraper import fetch_and_parse_sp500, fetch_and_parse_nasdaq100, fetch_and_parse_sp100

def test_scraper_returns_data():
    # Note: in real implementation, mock requests.get, but for this basic setup we test structure
    data = fetch_and_parse_sp500()
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'symbol' in data[0]

def test_scraper_returns_nasdaq100_data():
    data = fetch_and_parse_nasdaq100()
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'symbol' in data[0]
    assert 'industry' in data[0]

def test_fetch_and_parse_sp100():
    data = fetch_and_parse_sp100()
    assert isinstance(data, list)
    assert len(data) >= 100
    assert 'symbol' in data[0]
    assert 'name' in data[0]
    assert 'sector' in data[0]