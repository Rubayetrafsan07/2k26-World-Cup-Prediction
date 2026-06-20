import pandas as pd

df = pd.read_csv("data/processed/player_features_engineered.csv")

clusters = pd.read_csv("data/processed/player_clusters_labeled.csv")



# keep only important columns from clusters
clusters = clusters[["player_id", "cluster", "cluster_name"]]

# merge real + cluster
final_df = df.merge(clusters, on="player_id")


final_df.to_csv("data/processed/player_dashboard_dataset.csv", index=False)

print("Dashboard dataset created!")