from django.views.generic import TemplateView
from apps.base.praw_utils import get_post_data
from apps.base.fig_utils import average_metric_by_date


class IndexView(TemplateView):
    template_name = "index.html"


class ChartView(TemplateView):
    template_name = "charts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = get_post_data(self.request.GET["subreddit-select"])
        context["chart"] = average_metric_by_date(data, metric="ups").to_html()
        return context
