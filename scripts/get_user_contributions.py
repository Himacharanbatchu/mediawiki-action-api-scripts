import requests

def get_user_contributions(username):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "usercontribs",
        "ucuser": username,
        "uclimit": "max",
        "format": "json"
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    username = "YOUR_USERNAME"  # Replace with the desired username
    contributions = get_user_contributions(username)
    print(contributions)