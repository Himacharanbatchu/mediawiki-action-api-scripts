import requests

def list_page_templates(title):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": title,
        "prop": "templates",
        "format": "json"
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    title = "YOUR_PAGE_TITLE"  # Replace with the desired page title
    templates = list_page_templates(title)
    print(templates)