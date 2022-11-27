from django.views.generic import TemplateView
from apps.base.praw_utils import get_post_data


class IndexView(TemplateView):
    template_name = "index.html"


class ChartView(TemplateView):
    template_name = "charts.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = get_post_data(self.request.GET["subreddit-select"])
        fig = data.plot.line(x="created_utc", y="score")
        return context
