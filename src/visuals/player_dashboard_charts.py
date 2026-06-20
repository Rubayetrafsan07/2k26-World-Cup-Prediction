import pandas as pd
import plotly.express as px

df = pd.read_csv( "data/processed/player_clusters_labeled.csv")


# CHART 1
# CLUSTER DISTRIBUTION

def create_cluster_chart(df):

    fig = px.histogram(
        df,
        x="cluster_name",
        title="Player Cluster Distribution"
    )
    return fig


# CHART 2
# GOALS VS ASSISTS

def create_scatter_chart(df):

    fig = px.scatter(
        df,
        x="goals_per_90",
        y="assists_per_90",
        color="cluster_name",
        hover_name="name",
        title="Goals vs Assists by Cluster"
    )
    return fig


# CHART 3
#player position 
def create_position_chart(df):

    fig = px.histogram(
        df,
        x="position",
        title="Player Position Distribution"
    )
    return fig


# CHART 4
#Market Value by Cluster
def create_market_value_chart(df):

    fig = px.box(
        df,
        x="cluster_name",
        y="market_value_in_eur_latest",
        title="Market Value by Cluster"
    )
    return fig

