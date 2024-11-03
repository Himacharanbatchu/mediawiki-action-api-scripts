import requests

def get_page_views(title):
    url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article"
    params = {
        "project": "en.wikipedia",
        "page": title,
        "granularity": "daily",
        "start": "20230101",  # Replace with your desired start date
        "end": "20230131"     # Replace with your desired end date
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    title = "YOUR_PAGE_TITLE"  # Replace with the desired page title
    views = get_page_views(title)
    print(views)