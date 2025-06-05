import requests
from bs4 import BeautifulSoup

def fetch(url):
    try:
        print(f"Fetching: {url}")
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        return BeautifulSoup(res.text, "html.parser")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None
