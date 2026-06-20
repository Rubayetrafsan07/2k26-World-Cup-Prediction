import pandas as pd

matches = pd.read_csv("data/processed/result_with_labels.csv")
teams = pd.read_csv("data/processed/team_strength_v2.csv")


if "Unnamed: 0" in teams.columns:
    teams = teams.rename(columns={"Unnamed: 0": "country"})


teams = teams.set_index("country")

data = []


# BUILD MATCH FEATURES

for _, row in matches.iterrows():

    home = row["home_team"]
    away = row["away_team"]

    if home not in teams.index or away not in teams.index:
        continue

    home_team = teams.loc[home]
    away_team = teams.loc[away]

    data.append([
        # HISTORICAL
        home_team["win_rate"],
        away_team["win_rate"],
        home_team["goal_diff"],
        away_team["goal_diff"],

        # PLAYER STRENGTH
        home_team["attack_strength"],
        away_team["attack_strength"],

        home_team["midfield_strength"],
        away_team["midfield_strength"],

        home_team["defense_strength"],
        away_team["defense_strength"],

        home_team["squad_quality"],
        away_team["squad_quality"],

        home_team["world_class_players"],
        away_team["world_class_players"],

        # TARGET
        row["result"]
    ])

# CREATE DATAFRAME
ml_df = pd.DataFrame(data, columns=[
    "home_win_rate",
    "away_win_rate",
    "home_goal_diff",
    "away_goal_diff",

    "home_attack_strength",
    "away_attack_strength",

    "home_midfield_strength",
    "away_midfield_strength",

    "home_defense_strength",
    "away_defense_strength",

    "home_squad_quality",
    "away_squad_quality",

    "home_world_class_players",
    "away_world_class_players",

    "result"
])

ml_df.to_csv("data/processed/match_ml_dataset_v2.csv", index=False)

print(ml_df.head())
print(ml_df.shape)