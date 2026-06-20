import streamlit as st
import pandas as pd
import joblib
import base64


# PAGE CONFIG

st.set_page_config(
    page_title="World Cup Match Center",
    page_icon="⚽",
    layout="centered"
)

# BACKGROUND IMAGE

def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-image:
                linear-gradient(
                    rgba(0,0,0,0.45),
                    rgba(0,0,0,0.70)
                ),
                url("data:image/jpg;base64,{encoded}");

            background-size: cover;
            background-position: center 80px;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        .block-container {{
            padding-top: 8rem;
        }}

        .main-card {{
            background: rgba(0,0,0,0.60);
            backdrop-filter: blur(10px);
            border-radius: 25px;
            padding: 35px;
            border: 1px solid rgba(255,215,0,0.25);
            box-shadow: 0px 0px 25px rgba(0,0,0,0.4);
        }}

        .section-title {{
            text-align: center;
            color: #FFD700;
            font-size: 18px;
            letter-spacing: 5px;
            font-weight: 700;
            margin-bottom: 5px;
        }}

        .section-subtitle {{
            text-align: center;
            color: white;
            font-size: 18px;
            margin-bottom: 25px;
        }}

        .vs-box {{
            background: rgba(255,255,255,0.08);
            border-radius: 18px;
            padding: 20px;
            text-align: center;
            margin-top: 10px;
            margin-bottom: 25px;
        }}

        .vs-team {{
            color: white;
            font-size: 28px;
            font-weight: bold;
        }}

        .vs-text {{
            color: #FFD700;
            font-size: 34px;
            font-weight: 800;
            padding-left: 15px;
            padding-right: 15px;
        }}

        .stButton > button {{
            width: 100%;
            height: 60px;

            background: linear-gradient(
                135deg,
                #FFD700,
                #F5B800
            );

            color: black;
            font-size: 20px;
            font-weight: 800;

            border: none;
            border-radius: 50px;

            box-shadow:
                0px 0px 15px rgba(255,215,0,0.4);

            transition: 0.3s;
        }}

        .stButton > button:hover {{
            transform: scale(1.03);
            box-shadow:
                0px 0px 25px rgba(255,215,0,0.8);
        }}

        .stSelectbox div[data-baseweb="select"] {{
            background: rgba(255,255,255,0.95);
            border-radius: 10px;
        }}

        footer {{
            visibility: hidden;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("assets/WorldCup_2k26.jpg")



model = joblib.load("models/match_predictor.pkl")

team_stats = pd.read_csv("data/processed/team_stats.csv",index_col=0)

teams = sorted(team_stats.index)

st.markdown(
    """
    <div class="section-title">
        MATCH CENTER
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-subtitle">
        Predict the outcome of a World Cup showdown
    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# TEAM SELECTION

col1, col2 = st.columns(2)

with col1:
    home_team = st.selectbox(
        "🏠 Home Team",
        teams
    )

with col2:
    away_team = st.selectbox(
        "✈️ Away Team",
        teams
    )

# MATCH DISPLAY

st.markdown(
    f"""
    <div class="vs-box">
        <span class="vs-team">{home_team}</span>
        <span class="vs-text">VS</span>
        <span class="vs-team">{away_team}</span>
    </div>
    """,
    unsafe_allow_html=True
)


predict_btn = st.button(
    "🔮 Predict Match Outcome"
)

# PREDICTION

if predict_btn:

    features = pd.DataFrame({
        "home_win_rate": [team_stats.loc[home_team, "win_rate"]],
        "away_win_rate": [team_stats.loc[away_team, "win_rate"]],
        "home_goal_diff": [team_stats.loc[home_team, "goal_diff"]],
        "away_goal_diff": [team_stats.loc[away_team, "goal_diff"]],
    })

    prediction = str(model.predict(features)[0]).strip()

    st.markdown("<br>", unsafe_allow_html=True)

    # COMMON STYLE FUNCTION (reduces repetition visually)
    def result_box(title_color, border_color, content):
        return f"""
        <div style="
            background:rgba(0,0,0,0.55);
            border-left:6px solid {border_color};
            border-radius:15px;
            padding:20px;
            text-align:center;
        ">
            <h3 style="color:{title_color};">
                Predicted Winner
            </h3>

            <div style="color:white; font-size:32px; font-weight:700;">
                {content}
            </div>
        </div>
        """

    if prediction == "HomeWin":
        st.markdown(
            f"""
        <div style="
            text-align:center;
            font-size:34px;
            font-weight:700;
            color:#d19009;
            margin-top:10px;
        ">
            🏆 Congrats {home_team} 
        </div>
        """,
        unsafe_allow_html=True
    )   
    elif prediction == "AwayWin":
        st.markdown(
            f"""
            <div style="
                text-align:center;
                font-size:34px;
                font-weight:700;
                color:#d19009;
                margin-top:10px;
            ">
                 🏆 Congrats {away_team} 
            </div>
            """,
        unsafe_allow_html=True
    )
    else:
        st.markdown(
            f"""
            <div style="
                text-align:center;
                font-size:34px;
                font-weight:700;
                color:white;
                margin-top:10px;
            ">  
                🤝 DRAW
            </div>
            """,
        unsafe_allow_html=True
        )
    
    st.markdown("<br>", unsafe_allow_html=True)

    st.caption(
        "Random Forest Classifier • Historical FIFA Data • Educational Project"
    )


