import os
import requests


def authorize_reddit():
    auth = requests.auth.HTTPBasicAuth(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET")
    )
    login_data = {
        "grant_type": "password",
        "username": os.getenv("REDDIT_USERNAME"),
        "password": os.getenv("REDDIT_PASSWORD"),
    }
    headers = {"User-Agent": "MyAPI/0.0.1"}
    response = requests.post(
        "https://www.reddit.com/api/v1/access_token",
        auth=auth,
        data=login_data,
        headers=headers,
    )
    token = response.json()["access_token"]
    headers = {**headers, **{"Authorization": f"bearer {token}"}}
    return headers
