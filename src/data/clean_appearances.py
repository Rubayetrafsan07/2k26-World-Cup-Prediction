import pandas as pd

df_app = pd.read_csv("data/raw/appearances.csv")

print(df_app.head())

print(df_app.info())

print(df_app.columns)

print(df_app.isnull().sum())

print(df_app.duplicated().sum())

columns_to_keep = [
    "player_id",
    "date",
    "player_name",
    "competition_id",
    "yellow_cards",
    "red_cards",
    "goals",
    "assists",
    "minutes_played"
]
df_app = df_app[columns_to_keep]

df_app = df_app.dropna(subset=["player_name"])
df_app["date"] = pd.to_datetime(df_app["date"])

df_app.to_csv("data/processed/appearances_clean.csv",index=False)
