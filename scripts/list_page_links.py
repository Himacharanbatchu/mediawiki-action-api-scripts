import requests

def list_page_links(page_title):
    url = 'YOUR_API_URL'
    params = {
        'action': 'query',
        'titles': page_title,
        'prop': 'links',
        'format': 'json'
    }
    response = requests.get(url, params=params)
    return response.json()

# Example usage
print(list_page_links('PAGE_TITLE'))
