import plotly.express as px
import pandas as pd


def average_metric_by_date_figure(df: pd.DataFrame, metric: str) -> str:
    """
    This function creates a figure that shows the average of a metric by date
    :param df: a dataframe with the data
    :param metric: the metric to be plotted
    :return: a figure
    """
    df = df.groupby(["date"]).mean(numeric_only=True).reset_index().sort_values("date")
    fig = px.line(
        df,
        x="date",
        y=metric,
        labels={"date": "Date", metric: f'Average {metric.replace("_", " ").title()}'},
        markers=True,
        title=f'Average {metric.replace("_", " ").title()} by Date',
        template="plotly_dark",
    )
    return fig.to_html(
        config={"displaylogo": False},
        include_plotlyjs=False,
        full_html=False,
        default_width="75%",
    )
