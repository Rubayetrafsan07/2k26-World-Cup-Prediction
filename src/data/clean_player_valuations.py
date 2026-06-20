import pandas as pd

df_val = pd.read_csv("data/raw/player_valuations.csv")

print(df_val.head())

print(df_val.info())

print(df_val.columns)

print(df_val.isnull().sum())
print(df_val.duplicated().sum())

df_val = df_val[["player_id", "date", "market_value_in_eur", "current_club_name"]]

df_val["date"] = pd.to_datetime(df_val["date"])
print(df_val.info())
print(df_val.isnull().sum())

df_val.to_csv("data/processed/player_valuations_clean.csv",index=False)