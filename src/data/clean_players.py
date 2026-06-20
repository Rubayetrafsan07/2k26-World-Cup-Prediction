import pandas as pd

df_players = pd.read_csv("data/raw/players.csv")

print(df_players.head())

print(df_players.info())

print(df_players.columns)

print(df_players.isnull().sum())

print(df_players.duplicated().sum())

columns_to_keep = [
    "player_id",
    "name",
    "country_of_citizenship",
    "date_of_birth",
    "position",
    "sub_position",
    "height_in_cm",
    "foot",
    "market_value_in_eur",
    "highest_market_value_in_eur",
    "international_caps",
    "international_goals",
    "current_club_name"
]

df_players = df_players[columns_to_keep]

print(df_players.info())

df_players["date_of_birth"] = pd.to_datetime( df_players["date_of_birth"], errors="coerce")   

df_players= df_players.dropna(subset=["date_of_birth"])
df_players = df_players.dropna(subset=["country_of_citizenship"])  

df_players["international_caps"] = (df_players["international_caps"].fillna(0))   
df_players["international_goals"] = (df_players["international_goals"].fillna(0))

print(df_players.shape)
df_players.to_csv("data/processed/players_clean.csv", index=False )
