import pandas as pd

df = pd.read_csv("data/processed/player_dashboard_dataset.csv")

df["position"] = df["position"].fillna("Missing")

# SORT BY QUALITY
df = df.sort_values(by="market_value_in_eur_latest", ascending=False)


team_data = []

countries = df["country_of_citizenship"].unique()

for country in countries:

    squad = df[df["country_of_citizenship"] == country]

    
    # SELECT REALISTIC WORLD CUP SQUAD
    gk = squad[squad["position"] == "Goalkeeper"].head(3)
    dfb = squad[squad["position"] == "Defender"].head(8)
    mid = squad[squad["position"] == "Midfield"].head(8)
    att = squad[squad["position"] == "Attack"].head(7)

    team_squad = pd.concat([gk, dfb, mid, att])

    if len(team_squad) == 0:
        continue

    # TEAM FEATURES

    attack_strength = team_squad[team_squad["position"] == "Attack"]["goal_contribution"].mean()

    midfield_strength = team_squad[team_squad["position"] == "Midfield"]["goal_contribution"].mean()

    defense_strength = team_squad[team_squad["position"] == "Defender"]["value_per_90"].mean()

    goalkeeper_strength = team_squad[team_squad["position"] == "Goalkeeper"]["market_value_in_eur_latest"].mean()

    

    squad_quality = team_squad["market_value_in_eur_latest"].sum()

    world_class_players = (team_squad["cluster_name"] == "World-Class Players").sum()

    elite_attackers = (team_squad["cluster_name"] == "Elite Attackers").sum()

    creative_players = (team_squad["cluster_name"] == "Creative Players").sum()

    aggressive_players = (team_squad["cluster_name"] == "Aggressive Players").sum()

    defensive_players = (team_squad["cluster_name"] == "Defensive Players").sum()

    team_data.append([
        country,
        attack_strength,
        midfield_strength,
        defense_strength,
        goalkeeper_strength,
        squad_quality,
        world_class_players,
        elite_attackers,
        creative_players,
        aggressive_players,
        defensive_players
    ])


# CREATE FINAL DATASET

team_strength = pd.DataFrame(
    team_data,
    columns=[
        "country",
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
)

team_strength = team_strength.fillna(0)

team_strength.to_csv( "data/processed/team_player_strength.csv",index=False)

print(team_strength.head())
print(team_strength.shape)