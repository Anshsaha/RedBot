from rest_framework.views import APIView
import requests
from .reddit_auth import authorize_reddit
from django.http import JsonResponse


class RedditAPIView(APIView):

    def get(self, request):
        headers = authorize_reddit()
        res_hot = requests.get(
            "https://oauth.reddit.com/r/india/hot",
            headers=headers,
            params={"limit": "50"},
        )
        data = res_hot.json()
        return JsonResponse({"data": data["data"]["children"]})
