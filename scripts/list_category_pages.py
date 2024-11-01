import requests

params = {
    'action': 'query',
    'titles': 'Page_Title',  # replace 'Page_Title' with your page title
    'prop': 'categories',
    'format': 'json'
}

response = requests.get('https://en.wikipedia.org/w/api.php', params=params)
print(response.json())
