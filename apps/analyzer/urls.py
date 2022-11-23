from django.urls import path
from .views import ChartView, IndexView
from .api import api


urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("subreddit/", ChartView.as_view(), name="subreddit"),
    path("api/", api.urls),
]
