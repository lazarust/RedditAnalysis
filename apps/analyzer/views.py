from django.shortcuts import render
from django.views.generic import TemplateView
from apps.base.praw_utils import get_all_subs


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subs"] = get_all_subs()
        return context


class ChartView(TemplateView):
    template_name = "charts.html"


def subbreddit_search(request, *args, **kwargs):
    return render(request, "index.html")
