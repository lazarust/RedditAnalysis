from django.views.generic import TemplateView
from .utils import praw_utils, fig_utils


class IndexView(TemplateView):
    template_name = "index.html"


class ChartView(TemplateView):
    template_name = "charts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chart_list = []
        data = praw_utils.get_post_data(self.request.GET["subreddit-select"])
        chart_list.append(
            fig_utils.average_metric_by_date_figure(data, metric="ups").to_html()
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

        # chart_list.append(fig_utils.create_wordcloud(data).to_html())

        context["charts"] = chart_list
        return context
