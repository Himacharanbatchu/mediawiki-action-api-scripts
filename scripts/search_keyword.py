import requests

params = {
    'action': 'query',
    'list': 'search',
    'srsearch': 'keyword',  # replace 'keyword' with your search term
    'format': 'json'
}

response = requests.get('https://en.wikipedia.org/w/api.php', params=params)
print(response.json())
