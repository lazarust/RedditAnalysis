from django.views.generic import TemplateView
from .utils import praw_utils, fig_utils
import pandas as pd


class IndexView(TemplateView):
    template_name = "index.html"


class ChartView(TemplateView):
    template_name = "charts.html"

    def create_charts(self, data: pd.DataFrame) -> list[str]:
        chart_list = []

        chart_list.append(
            fig_utils.average_metric_by_date_figure(data, metric="score").to_html()
        )

        chart_list.append(
            fig_utils.average_metric_by_date_figure(
                data, metric="upvote_ratio"
            ).to_html()
        )

        chart_list.append(
            fig_utils.average_metric_by_date_figure(
                data, metric="author_karma"
            ).to_html()
        )

        chart_list.append(
            fig_utils.average_metric_by_date_figure(
                data, metric="num_comments"
            ).to_html()
        )

        return chart_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = praw_utils.get_post_data(self.request.GET["subreddit-select"])
        context["charts"] = self.create_charts(data)
        return context
