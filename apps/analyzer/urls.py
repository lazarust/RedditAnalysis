from django.urls import path
from .views import ChartView, IndexView, subbreddit_search

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("subreddit/", ChartView.as_view(), name="subreddit"),
    path("search-subs/", subbreddit_search, name="search_subs"),
]
