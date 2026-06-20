import pandas as pd

df_matches = pd.read_csv("data/processed/result_with_labels.csv")

team_stats = pd.read_csv("data/processed/team_stats.csv", index_col=0)

data = []  # for ML table

for _, row in df_matches.iterrows():

    home = row["home_team"]
    away = row["away_team"]

    if home in team_stats.index and away in team_stats.index:

        data.append([
            team_stats.loc[home, "win_rate"],
            team_stats.loc[away, "win_rate"],
            team_stats.loc[home, "goal_diff"],
            team_stats.loc[away, "goal_diff"],
            row["result"]
        ])
    
#  cretae a DataFarme
ml_df = pd.DataFrame(data, columns=
    [
    "home_win_rate",
    "away_win_rate",
    "home_goal_diff",
    "away_goal_diff",
    "result"]
    )

ml_df.to_csv("data/processed/match_ml_dataset.csv", index=False)


