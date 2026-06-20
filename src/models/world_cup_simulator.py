import pandas as pd
import numpy as np
import joblib
import random


model = joblib.load("models/xgb_match_predictor.pkl")
le = joblib.load("models/label_encoder.pkl")

teams = pd.read_csv("data/processed/team_strength_v2.csv")


if "Unnamed: 0" in teams.columns:
    teams = teams.rename(columns={"Unnamed: 0": "country"})

teams = teams.set_index("country")


# FEATURE COLUMNS (IMPORTANT)

FEATURE_COLUMNS = [
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
    "away_world_class_players"
]

# MATCH SIMULATION

def simulate_match(home, away):

    home_row = teams.loc[home]
    away_row = teams.loc[away]

    match = pd.DataFrame([[
        home_row["win_rate"],
        away_row["win_rate"],
        home_row["goal_diff"],
        away_row["goal_diff"],

        home_row["attack_strength"],
        away_row["attack_strength"],

        home_row["midfield_strength"],
        away_row["midfield_strength"],

        home_row["defense_strength"],
        away_row["defense_strength"],

        home_row["squad_quality"],
        away_row["squad_quality"],

        home_row["world_class_players"],
        away_row["world_class_players"]
    ]], columns=FEATURE_COLUMNS)

    probs = model.predict_proba(match)[0]

    home_win_prob = probs[2]
    draw_prob = probs[1]
    away_win_prob = probs[0]

   
    home_strength = home_row["squad_quality"]
    away_strength = away_row["squad_quality"]

    home_win_prob *= (1 + home_strength * 0.1)
    away_win_prob *= (1 + away_strength * 0.1)

    total = home_win_prob + draw_prob + away_win_prob

    home_win_prob /= total
    draw_prob /= total
    away_win_prob /= total

    # Final decision
    result = random.choices(
        [home, "Draw", away],
        weights=[home_win_prob, draw_prob, away_win_prob]
    )[0]

    return result


# GROUP STAGE
def simulate_group(group_teams):

    points = {team: 0 for team in group_teams}

    for i in range(len(group_teams)):
        for j in range(i + 1, len(group_teams)):

            home = group_teams[i]
            away = group_teams[j]

            result = simulate_match(home, away)

            if result == home:
                points[home] += 3
            elif result == away:
                points[away] += 3
            else:
                points[home] += 1
                points[away] += 1

    return sorted(points.items(), key=lambda x: x[1], reverse=True)


# WORLD CUP SIMULATION

def run_world_cup():

    all_teams = [
        "Argentina", "Brazil", "France", "England",
        "Germany", "Spain", "Portugal", "Netherlands",
        "Belgium", "Croatia", "Uruguay", "United States",
        "Mexico", "Canada", "Japan", "Haiti",
        "Morocco", "Iran", "Nigeria", "Switzerland",
        "Denmark", "DR Congo", "Scotland", "Sweden",
        "Saudi Arabia", "Colombia", "Ecuador", "Qatar",
        "Australia", "Turkey", "Tunisia", "Austria"
    ]

  
    all_teams = [t for t in all_teams if t in teams.index]

    random.shuffle(all_teams)

    groups = [all_teams[i:i+4] for i in range(0, len(all_teams), 4)]

    qualified = []

    print("\n=== GROUP STAGE ===\n")

    for i, group in enumerate(groups):

        print(f"Group {chr(65+i)}:", group)

        standings = simulate_group(group)

        top2 = standings[:2]

        qualified.extend([team[0] for team in top2])

        print("Top 2:", top2)
        print()

    print("\n=== KNOCKOUT STAGE ===\n")

    round_teams = qualified

    while len(round_teams) > 1:

        next_round = []

        random.shuffle(round_teams)

        print(f"\n--- Round of {len(round_teams)} ---")

        for i in range(0, len(round_teams), 2):

            home = round_teams[i]
            away = round_teams[i + 1]

            winner = simulate_match(home, away)

            if winner == home:
                next_round.append(home)
            elif winner == away:
                next_round.append(away)
            else:
                next_round.append(random.choice([home, away]))

            print(f"{home} vs {away} → {winner}")

        round_teams = next_round

    print("\n🏆 WORLD CUP WINNER:", round_teams[0])
    return round_teams[0]

run_world_cup()