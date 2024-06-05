from django.urls import path
from . import views

urlpatterns = [
    path("", views.RedditAPIView.as_view(), name="red"),
]
