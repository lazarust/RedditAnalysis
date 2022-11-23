from django.views.generic import TemplateView
from apps.base.praw_utils import get_all_subs


class IndexView(TemplateView):
    template_name = "index.html"


class ChartView(TemplateView):
    template_name = "charts.html"
