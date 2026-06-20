import pandas as pd
from sklearn.cluster import KMeans


df = pd.read_csv("data/processed/player_features_scaled.csv")

# FEATURES FOR CLUSTERING
features = [
    "goals_per_90",
    "assists_per_90",
    "goal_contribution",
    "cards_per_90",
    "value_per_90",
    "market_value_in_eur_latest"
]

X = df[features]

# Replace NaN with 0 
X = X.fillna(0)

# APPLY KMEANS
kmeans = KMeans(n_clusters=5 , random_state=42 , n_init=10)

df["cluster"] = kmeans.fit_predict(X)

df.to_csv("data/processed/player_clusters.csv", index=False)

print("Clustering complete!")
print(df[["player_id", "name", "position", "cluster"]].head())