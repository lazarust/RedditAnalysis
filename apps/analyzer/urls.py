from django.urls import path
from .views import IndexView, index

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("subreddit/", index, name="subreddit"),
]
