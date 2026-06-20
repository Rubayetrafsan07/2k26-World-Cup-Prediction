import pandas as pd

df = pd.read_csv("data/processed/player_clusters_labeled.csv")

print(df.columns.tolist())

print(df[["cluster","cluster_name"]]
      .drop_duplicates()
      .sort_values("cluster"))



df = pd.read_csv("data/processed/players_clean.csv")

print(df.columns.tolist())
print(df.head())


df = pd.read_csv("data/processed/team_stats.csv")

print(df.head())
print(df.columns.tolist())

df = pd.read_csv("data/processed/player_dashboard_dataset.csv")

print(
    df["country_of_citizenship"]
    .value_counts()
    .head(30)
)