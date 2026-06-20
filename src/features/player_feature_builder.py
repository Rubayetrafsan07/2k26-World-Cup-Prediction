import pandas as pd

players = pd.read_csv("data/processed/players_clean.csv")
appearances = pd.read_csv("data/processed/appearances_clean.csv")
valuations = pd.read_csv("data/processed/player_valuations_clean.csv")



appearance_stats = appearances.groupby("player_id").agg({
    "goals": "sum",
    "assists": "sum",
    "minutes_played": "sum",
    "yellow_cards": "sum",
    "red_cards": "sum"
}).reset_index()


# GET LATEST MARKET VALUE
valuations["date"] = pd.to_datetime(valuations["date"])

valuations = valuations.sort_values("date")

latest_values = valuations.groupby("player_id").tail(1)  

latest_values =  latest_values[["player_id", "market_value_in_eur"]]


# merge Datasets
player_features = players.merge(
    appearance_stats,
    on = "player_id",
    how="left"
)

player_features = player_features.merge(
    latest_values,
    on = "player_id",
    how = "left",
    suffixes=("","_latest")
) 


# HANDLE MISSING VALUES
stat_columns = [
    "goals",
    "assists",
    "minutes_played",
    "yellow_cards",
    "red_cards"
]

player_features[stat_columns]=(player_features[stat_columns].fillna(0))


player_features.to_csv("data/processed/player_features.csv",index=False)
print("player_features.csv created!")

print(player_features.head())
print(player_features.shape)





