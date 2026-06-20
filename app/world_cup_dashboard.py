import streamlit as st
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.models.world_cup_simulator import run_world_cup
from src.models.monte_carlo_world_cup import monte_carlo_simulation

st.set_page_config(page_title="World Cup 2026 Simulator", layout="centered")

st.title("🌍 World Cup 2026 Prediction Engine")

if st.button("⚽ Run World Cup Simulation"):
    winner = run_world_cup()
    st.success(f"🏆 Winner: {winner}")

if st.button("📊 Run 100 Simulations"):
    results = monte_carlo_simulation(100)
    st.write(results)