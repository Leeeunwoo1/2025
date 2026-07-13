import streamlit as st

st.set_page_config(
    page_title="동신여자고등학교 식물도감",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 동신여자고등학교 식물도감")
st.write("학교에서 볼 수 있는 나무와 꽃을 소개하는 앱입니다.")

menu = st.sidebar.radio(
    "메뉴 선택",
    ["홈", "향나무", "철쭉", "목련", "벚나무", "은행나무"]
)

if menu == "홈":
    st.header("🌱 학교 식물 소개")
    st.write("""
    동신여자고등학교에는 다양한 나무와 꽃이 자라고 있습니다.
    
    대표적으로
    - 🌲 향나무(교목)
    - 🌸 철쭉(교화)
    - 🌸 목련
    - 🌸 벚나무
    - 🌳 은행나무
    
    를 볼 수 있습니다.
    """)

elif menu == "향나무":
    st.header("🌲 향나무")

    st.subheader("이름의 유래")
    st.write("향기로운 냄새가 나는 나무라서 향나무라는 이름이 붙었습니다.")

    st.subheader("특징")
    st.write("""
    - 사계절 푸른 상록수
    - 병충해에 강함
    - 오래 사는 나무
    """)

    st.subheader("쓰임새")
    st.write("""
    - 학교 조경수
    - 공원 조경
    - 목재와 공예품
    """)

elif menu == "철쭉":
    st.header("🌸 철쭉")

    st.subheader("이름의 유래")
    st.write("봄철에 피는 꽃이라 '철쭉'이라는 이름이 붙었습니다.")

    st.subheader("특징")
    st.write("""
    - 봄에 꽃이 핌
    - 분홍색, 붉은색 꽃
    - 우리나라에서 흔함
    """)

    st.subheader("쓰임새")
    st.write("""
    - 화단 조경
    - 학교 교화
    """)

elif menu == "목련":
    st.header("🌸 목련")

    st.subheader("이름의 유래")
    st.write("꽃봉오리가 붓을 닮았다고 하여 목련이라 불립니다.")

    st.subheader("특징")
    st.write("""
    - 잎보다 꽃이 먼저 핌
    - 흰 꽃
    - 향기가 좋음
    """)

    st.subheader("쓰임새")
    st.write("""
    - 관상수
    - 학교와 공원 조경
    """)

elif menu == "벚나무":
    st.header("🌸 벚나무")

    st.subheader("이름의 유래")
    st.write("벚꽃이 무리 지어 피는 모습에서 이름이 유래했다는 설이 있습니다.")

    st.subheader("특징")
    st.write("""
    - 봄에 꽃이 만개
    - 연분홍색 꽃
    """)

    st.subheader("쓰임새")
    st.write("""
    - 벚꽃길
    - 학교 조경
    """)

elif menu == "은행나무":
    st.header("🌳 은행나무")

    st.subheader("이름의 유래")
    st.write("은빛 살구처럼 생긴 열매에서 은행나무라는 이름이 붙었습니다.")

    st.subheader("특징")
    st.write("""
    - 살아있는 화석
    - 가을 노란 단풍
    - 오래 사는 나무
    """)

    st.subheader("쓰임새")
    st.write("""
    - 가로수
    - 학교 조경
    """)
