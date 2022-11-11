from django.shortcuts import render
from django.views.generic import TemplateView
from apps.base.praw_utils import get_all_subs


def index(request, *args, **kwargs):
    return render(request, "index.html")


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subs"] = get_all_subs()
        print(context)
        return context
