import streamlit as st
import pandas as pd
import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)


from src.visuals.player_dashboard_charts import(
    create_cluster_chart,
    create_scatter_chart,
    create_position_chart,
    create_market_value_chart
)

st.set_page_config(
    page_title="Player Performance Dashboard",
    page_icon="⚽",
    layout="wide"
)

df = pd.read_csv("data/processed/player_dashboard_dataset.csv")

# title
st.title("⚽ World Cup Player Performance Dashboard")
st.markdown("Explore player clusters, positions and performance metrics.")


# Position Filter
positions = sorted( df["position"].dropna().unique())
selected_position = st.selectbox("Select Position", ["All"] + list(positions))


# cluster Filter
clusters = sorted(df["cluster_name"].unique())
selected_cluster = st.selectbox("Select Cluster",["All"] + list(clusters))


# applying filters

filtered_df = df.copy()

if selected_position != "All":
    filtered_df = filtered_df[
        filtered_df["position"] == selected_position
    ]

if selected_cluster != "All":
    filtered_df = filtered_df[
        filtered_df["cluster_name"] == selected_cluster
    ]


filtered_df = filtered_df.dropna()

# KPI SECTION
# =========================
st.subheader("📊 Key Performance Indicators")

avg_goals = filtered_df["goals_per_90"].mean()
avg_assists = filtered_df["assists_per_90"].mean()
avg_value = filtered_df["market_value_in_eur_latest"].mean()
total_players = filtered_df.shape[0]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Players", total_players)
col2.metric("Avg Goals/90", round(avg_goals, 2))
col3.metric("Avg Assists/90", round(avg_assists, 2))
col4.metric("Avg Market Value", round(avg_value, 2))




# PLAYER SEARCH
# =========================
st.subheader("🔍 Search Player")
search_name = st.text_input("Type player name (e.g. Ronaldo)")

if search_name:
    search_result = filtered_df[
        filtered_df["name"].str.contains(search_name, case=False, na=False)
    ]
    st.dataframe(search_result)



# show player table
st.subheader("Players")
st.dataframe(filtered_df[["name", "position", "cluster_name"]])


# show charts 
st.subheader("Cluster Distribution")

st.plotly_chart( create_cluster_chart(filtered_df) , use_container_width=True)

st.subheader("Goals vs Assists")

st.plotly_chart(create_scatter_chart(filtered_df) , use_container_width=True)

st.subheader("Position Distribution")

st.plotly_chart(create_position_chart(filtered_df) , use_container_width=True)

st.subheader("Market Value by Cluster")

st.plotly_chart(create_market_value_chart(filtered_df) , use_container_width=True)

