import requests

def list_recent_changes():
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "recentchanges",
        "rclimit": "max",
        "format": "json"
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    changes = list_recent_changes()
    print(changes)