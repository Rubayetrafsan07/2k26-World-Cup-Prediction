import pandas as pd

df = pd.read_csv("data/processed/result_clean.csv")


#  only national team matches (World Cup relevant teams)
df = df[df["tournament"].isin(
    [
    "FIFA World Cup",
    "UEFA Euro",
    "Copa América",
    "AFC Asian Cup",
    "African Cup of Nations",
    "CONCACAF Championship",
    "FIFA World Cup qualification"]
    )]

def get_result(row):

    if row["home_score"] > row["away_score"]:
        return "HomeWin"
    elif row["home_score"] < row["away_score"]:
        return "AwayWin"
    else:
        return "Draw"


df["result"] = df.apply(get_result,axis=1)   

df.to_csv("data/processed/result_with_labels.csv",index=False)

teams = pd.concat([df["home_team"], df["away_team"]]).unique()   


team_stats = pd.DataFrame(index=teams)   

team_stats["wins"] = 0 
team_stats["losses"] = 0
team_stats["draws"] = 0
team_stats["goals_scored"] = 0
team_stats["goals_conceded"] = 0
team_stats["matches"] = 0

# count wins :
for _, row in df.iterrows():

    home = row["home_team"]
    away = row["away_team"]

    home_goals = row["home_score"]
    away_goals = row["away_score"]

    # update matches played
    team_stats.loc[home, "matches"] += 1
    team_stats.loc[away, "matches"] += 1

    # goals
    team_stats.loc[home, "goals_scored"] += home_goals
    team_stats.loc[home, "goals_conceded"] += away_goals

    team_stats.loc[away, "goals_scored"] += away_goals
    team_stats.loc[away, "goals_conceded"] += home_goals

    # result logic
    if home_goals > away_goals:
        team_stats.loc[home, "wins"] += 1
        team_stats.loc[away, "losses"] += 1  

    elif home_goals < away_goals:
        team_stats.loc[away, "wins"] += 1
        team_stats.loc[home, "losses"] += 1

    else:
        team_stats.loc[home, "draws"] += 1
        team_stats.loc[away, "draws"] += 1


team_stats["win_rate"] = team_stats["wins"] / team_stats["matches"]
team_stats["goal_diff"] = team_stats["goals_scored"] - team_stats["goals_conceded"]

print(team_stats.sort_values(by="win_rate", ascending=False).head(10))

team_stats.to_csv("data/processed/team_stats.csv")








