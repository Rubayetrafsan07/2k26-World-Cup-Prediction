import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data/processed/player_features_engineered.csv")


# SELECT FEATURES FOR CLUSTERING
features = [
    "goals_per_90",
    "assists_per_90",
    "goal_contribution",
    "cards_per_90",
    "value_per_90",
    "market_value_in_eur_latest"
]

X = df[features]

scaler = StandardScaler()  
X_scaled = scaler.fit_transform(X)

X_scaled = pd.DataFrame(X_scaled , columns=features)

final_df = pd.concat( [df[["player_id",  "name",  "position"]],  X_scaled], axis=1)


final_df.to_csv("data/processed/player_features_scaled.csv", index=False)

print("Scaling complete!")
print(final_df.head())
print(final_df.shape)