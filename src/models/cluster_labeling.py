import pandas as pd


df = pd.read_csv("data/processed/player_clusters.csv")

# CLUSTER LABELS
cluster_names = {
    0: "Creative Players",
    1: "Defensive Players",
    2: "Aggressive Players",
    3: "Elite Attackers",
    4: "World-Class Players"
}

# Create new column
df["cluster_name"] = df["cluster"].map(
    cluster_names
)

df.to_csv("data/processed/player_clusters_labeled.csv",index=False)

print("Cluster labeling complete!")

print(df[
        ["name", "position", "cluster", "cluster_name"]
    ].head()
)