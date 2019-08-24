"""Download the facts to a file called 'facts'."""
import requests


url = 'https://cat-fact.herokuapp.com/facts'
req = requests.get(url)

if req.status_code == 200:
    facts = req.json()
    with open('facts', 'w') as f:
        for fact_object in facts['all']:
            f.write(fact_object['text'] + '\n')