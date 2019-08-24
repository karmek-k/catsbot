"""Download the facts and return them in a list."""
import requests


def get_facts():
    url = 'https://cat-fact.herokuapp.com/facts'
    req = requests.get(url)

    if req.status_code == 200:
        facts = req.json()
        result = []
        for fact_object in facts['all']:
            result.append(fact_object['text'])
        return result
