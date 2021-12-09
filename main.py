from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import json
import vobject

app = FastAPI()


def search_results(query: str):
    response = requests.get(f"https://panoramafirm.pl/{query}")
    soup = BeautifulSoup(response.content, 'html.parser')
    found_results = soup.find_all('script', type='application/ld+json')[:-1]
    return [json.loads(result.string) for result in found_results]


def entries_to_vcards(entries: list[dict]):
    for entry in entries:
        card = vobject.vCard()
        card.add('fn').value = entry['name']
        card.add('email')
        card.email.value = entry['email']
        entry_telephone = entry.get('telephone', None)
        if entry_telephone:
            card.add('telephone').value = entry_telephone

        entry_address = entry.get('address', None)
        if entry_address:
            address = card.add('adr')
            address.value = vobject.vcard.Address(
                street=entry_address.get('streetAddress', ''), city=entry_address.get('addressLocality', ''), code=entry_address.get('postalCode', ''), country=entry_address.get('addressCountry', ''))
        print(card.serialize())
