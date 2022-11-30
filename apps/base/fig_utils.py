import plotly.express as px
import pandas as pd


def average_metric_by_date(df: pd.DataFrame, metric: str):
    df = df.groupby(["date"]).mean().reset_index().sort_values("date")
    fig = px.line(df, x="date", y=metric)
    return fig
