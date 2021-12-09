from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import json
app = FastAPI()


def search_results(query: str):
    response = requests.get(f"https://panoramafirm.pl/{query}")
    soup = BeautifulSoup(response.content, 'html.parser')
    found_results = soup.find_all('script', type='application/ld+json')[:-1]
    entries = []
    for result in found_results:
        entries.append(json.loads(result.string))
