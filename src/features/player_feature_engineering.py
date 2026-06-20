import pandas as pd


df = pd.read_csv("data/processed/player_features.csv")

df["minutes_played"] = df["minutes_played"].replace(0,1) 

df = df[df["minutes_played"] >= 300]

# Feature Engineering

df["goals_per_90"] = (df["goals"] / df["minutes_played"]) * 90


df["assists_per_90"] = (df["assists"] / df["minutes_played"]) * 90

df["goal_contribution"] = df["goals"] + df["assists"]


df["cards_per_90"] = ((df["yellow_cards"] + 2 * df["red_cards"]) / df["minutes_played"]) * 90


df["value_per_90"] = df["market_value_in_eur_latest"] / df["minutes_played"]


df.to_csv("data/processed/player_features_engineered.csv",index=False)

print("Feature engineering complete!")
print(df.head())
print(df.shape)