import requests

def list_page_images(title):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": title,
        "prop": "images",
        "format": "json"
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    title = "YOUR_PAGE_TITLE"  # Replace with the desired page title
    images = list_page_images(title)
    print(images)