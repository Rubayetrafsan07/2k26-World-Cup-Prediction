import pandas as pd
from sklearn.preprocessing import StandardScaler

team = pd.read_csv("data/processed/team_player_strength.csv")
stats = pd.read_csv("data/processed/team_stats.csv")



if "Unnamed: 0" in stats.columns:
    stats = stats.rename(columns={"Unnamed: 0": "country"})


# NORMALIZE PLAYER-BASED FEATURES

features_to_scale = [
    "attack_strength",
    "midfield_strength",
    "defense_strength",
    "goalkeeper_strength",
    "squad_quality",
    "world_class_players",
    "elite_attackers",
    "creative_players",
    "aggressive_players",
    "defensive_players"
]

scaler = StandardScaler()

team_scaled = team.copy()
team_scaled[features_to_scale] = scaler.fit_transform(team_scaled[features_to_scale])


# MERGE WITH HISTORICAL STATS

final_df = stats.merge(
    team_scaled,
    on="country",
    how="inner"
)

final_df.to_csv("data/processed/team_strength_v2.csv",index=False)

print(final_df.head())
print(final_df.shape)