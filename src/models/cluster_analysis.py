import pandas as pd



df = pd.read_csv("data/processed/player_clusters.csv")

# CLUSTER STATISTICS

summary = df.groupby("cluster")[[
    "goals_per_90",
    "assists_per_90",
    "goal_contribution",
    "cards_per_90",
    "value_per_90"
]].mean()

print("\nCLUSTER SUMMARY:\n")
print(summary)


# POSITION DISTRIBUTION PER CLUSTER
print("\nPOSITION BREAKDOWN:\n")

for c in sorted(df["cluster"].unique()):
    print(f"\nCluster {c}:")
    print(df[df["cluster"] == c]["position"].value_counts())



# quick sanity check of players in each cluster
for cluster in sorted(df["cluster"].unique()):

    print("\n")
    print("=" * 50)
    print(f"CLUSTER {cluster}")
    print("=" * 50)

    print(
        df[df["cluster"] == cluster][
            ["name", "position"]
        ].head(20)
    )









































