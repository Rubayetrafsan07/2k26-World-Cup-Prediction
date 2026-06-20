import pandas as pd
import joblib


model = joblib.load("models/match_predictor.pkl")
team_stats = pd.read_csv("data/processed/team_stats.csv",index_col=0)


home_team = input("Home team: ").strip().title()  
away_team = input("Away team: ").strip().title()  

features = pd.DataFrame({
    "home_win_rate": [team_stats.loc[home_team, "win_rate"]],
    "away_win_rate": [team_stats.loc[away_team, "win_rate"]],
    "home_goal_diff": [team_stats.loc[home_team, "goal_diff"]],
    "away_goal_diff": [team_stats.loc[away_team, "goal_diff"]]
})

prediction = model.predict(features)
print()
print("Prediction:", prediction[0])
