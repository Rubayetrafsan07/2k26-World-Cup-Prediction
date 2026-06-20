from collections import Counter
from src.models.world_cup_simulator import run_world_cup

def monte_carlo_simulation(n_simulations=100):

    winners = []

    for i in range(n_simulations):

        winner = run_world_cup()
        winners.append(winner)

        print(f"Simulation {i+1}/{n_simulations} → {winner}")

    counts = Counter(winners)

    print("\n🏆 WORLD CUP WINNER PROBABILITIES:\n")

    for team, count in counts.most_common():
        print(f"{team}: {count / n_simulations * 100:.2f}%")

    return counts

# RUN IT
monte_carlo_simulation(100)