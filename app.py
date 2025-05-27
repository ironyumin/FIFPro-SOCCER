import streamlit as st

# 선수 데이터에 국가(nationality) 포함
players_db = [
    {
        "name": "Erling Haaland",
        "league": "Premier League",
        "age": 24,
        "position": "FW",
        "nationality": "Norway",
        "club": "Manchester City",
        "achievements": [
            "프리미어리그 우승 (2022–23)",
            "챔피언스리그 우승 (2022–23)",
            "프리미어리그 득점왕 (2022–23)"
        ]
    },
    {
        "name": "Jude Bellingham",
        "league": "La Liga",
        "age": 21,
        "position": "MF",
        "nationality": "England",
        "club": "Real Madrid",
        "achievements": [
            "라리가 올해의 선수 (2023–24)",
            "챔피언스리그 결승 진출 (2023–24)"
        ]
    },
    {
        "name": "Gianluigi Donnarumma",
        "league": "Ligue 1",
        "age": 25,
        "position": "GK",
        "nationality": "Italy",
        "club": "Paris Saint-Germain",
        "achievements": [
            "유로 2020 우승 (MVP)",
            "리그 1 우승 (2021–23)"
        ]
    },
    {
        "name": "Olivier Giroud",
        "league": "Serie A",
        "age": 37,
        "position": "FW",
        "nationality": "France",
        "club": "AC Milan",
        "achievements": [
            "2018 FIFA 월드컵 우승",
            "세리에 A 우승 (2021–22)"
        ]
    },
    {
        "name": "Jamal Musiala",
        "league": "Bundesliga",
        "age": 21,
        "position": "MF",
        "nationality": "Germany",
        "club": "Bayern Munich",
        "achievements": [
            "분데스리가 우승 (다수)"
        ]
    },
    {
        "name": "Manuel Neuer",
        "league": "Bundesliga",
        "age": 38,
        "position": "GK",
        "nationality": "Germany",
        "club": "Bayern Munich",
        "achievements": [
            "2014 FIFA 월드컵 우승",
            "FIFA 최우수 GK 수상"
        ]
    }
]

# 나이대 분류
def get_age_group(age):
    if age <= 20:
        return "20세 이하"
    elif 20 < age < 30:
        return "20세 이상 30세 미만"
    elif 30 <= age < 35:
        return "30세 이상 35세 미만"
    else:
        return "35세 이상"

# 타이틀
st.title("🌍 리그별, 국가별 유명 현역 선수 탐색기")

# 1. 리그 선택
league = st.selectbox("1️⃣ 리그를 선택하세요:", sorted(set(p["league"] for p in players_db)))

# 2. 리그에 해당하는 국가 목록
available_nations = sorted(set(p["nationality"] for p in players_db if p["league"] == league))
nationality = st.selectbox("2️⃣ 국가를 선택하세요:", available_nations)

# 3. 나이대 선택
age_group = st.selectbox("3️⃣ 나이대를 선택하세요:", ["20세 이하", "20세 이상 30세 미만", "30세 이상 35세 미만", "35세 이상"])

# 4. 포지션 선택
position = st.selectbox("4️⃣ 포지션을 선택하세요:", ["GK", "DF", "MF", "FW"])

# 5. 조건 필터링
filtered_players = [
    p for p in players_db
    if p["league"] == league and
       p["nationality"] == nationality and
       get_age_group(p["age"]) == age_group and
       p["position"] == position
]

# 선수 선택 및 정보 출력
if filtered_players:
    player_names = [p["name"] for p in filtered_players]
    selected_name = st.selectbox("5️⃣ 선수를 선택하세요:", player_names)
    selected_player = next(p for p in filtered_players if p["name"] == selected_name)

    st.subheader(f"👤 {selected_player['name']}")
    st.markdown(f"**국가:** {selected_player['nationality']}")
    st.markdown(f"**소속팀:** {selected_player['club']}")
    st.markdown(f"**나이:** {selected_player['age']}세")
    st.markdown(f"**포지션:** {selected_player['position']}")
    st.markdown("**🏆 주요 업적:**")
    for ach in selected_player["achievements"]:
        st.markdown(f"- {ach}")
else:
    st.warning("조건에 맞는 선수가 없습니다. 다른 조건을 선택해보세요.")

