import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

def fetch_and_parse_sp500():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(URL, headers=headers)
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

SP100_URL = "https://en.wikipedia.org/wiki/S%26P_100"

def fetch_and_parse_sp100():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(SP100_URL, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'id': 'constituents'})
    
    results = []
    for row in table.find_all('tr')[1:]:
        cols = row.find_all(['td', 'th'])
        if len(cols) >= 3:
            results.append({
                'symbol': cols[0].text.strip(),
                'name': cols[1].text.strip(),
                'sector': cols[2].text.strip(),
            })
    return results

NASDAQ100_URL = "https://en.wikipedia.org/wiki/Nasdaq-100"

def fetch_and_parse_nasdaq100():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(NASDAQ100_URL, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'id': 'constituents'})
    
    results = []
    for row in table.find_all('tr')[1:]:
        cols = row.find_all(['td', 'th'])
        if len(cols) >= 4:
            results.append({
                'symbol': cols[0].text.strip(),
                'name': cols[1].text.strip(),
                'industry': cols[2].text.strip(),
                'subsector': cols[3].text.strip(),
            })
    return results