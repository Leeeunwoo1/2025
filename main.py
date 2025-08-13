import streamlit as st

# 1. MBTI별 직업 데이터 정의 (데이터는 코드 상단에 모아서 관리하는 것이 깔끔해요!)
MBTI_JOB_DATA = {
    "ISTJ": ["공무원", "회계사", "데이터 분석가", "경찰관"],
    "ISFJ": ["간호사", "초등학교 교사", "사서", "사회 복지사"],
    "INFJ": ["상담사", "심리학자", "작가", "대학교수"],
    "INTJ": ["과학자", "IT 개발자", "전략 기획자", "건축가"],
    "ISTP": ["엔지니어", "정비사", "스포츠 선수", "기술자"],
    "ISFP": ["미술가", "음악가", "디자이너", "동물 조련사"],
    "INFP": ["시인", "예술가", "언어 치료사", "작가"],
    "INTP": ["연구원", "프로그래머", "철학자", "발명가"],
    "ESTP": ["영업원", "경영 컨설턴트", "파일럿", "경찰관"],
    "ESFP": ["연예인", "이벤트 플래너", "유치원 교사", "가이드"],
    "ENFP": ["크리에이터", "마케터", "강사", "상담사"],
    "ENTP": ["창업가", "변호사", "발명가", "칼럼니스트"],
    "ESTJ": ["경영자", "관리자", "회계사", "군인"],
    "ESFJ": ["영업 관리", "서비스업 종사자", "유치원 교사", "간호사"],
    "ENFJ": ["리더", "강사", "인사 담당자", "정치인"],
    "ENTJ": ["CEO", "변호사", "경영 컨설턴트", "대학교수"]
}

def main():
    # 페이지 기본 설정: 제목, 아이콘 등
    st.set_page_config(
        page_title="나에게 딱 맞는 MBTI별 직업 추천!",
        page_icon="✨",
        layout="centered" # 페이지 레이아웃을 중앙으로 설정하여 더욱 정돈된 느낌을 줍니다.
    )

    # 헤더 섹션
    st.title("🧐 MBTI별 직업 추천 서비스")
    st.write("나의 MBTI 유형에 딱 맞는 직업들을 알아보세요! 커리어 탐색에 도움이 될 거예요. 😊")

    # 간격을 두어 시각적인 분리
    st.markdown("---")

    # 이미지 추가 (사이즈를 줄여 더 깔끔하게)
    st.image(
        "https://images.unsplash.com/photo-1517457375823-379e491c4984?q=80&w=600&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        width=300, # 이미지 크기 조절
        caption="당신의 숨겨진 잠재력을 찾아보세요!" # 캡션 추가
    )
    st.markdown("---")


    # 사용자 입력 섹션
    # 첫 번째 선택지로는 빈 문자열을 넣어 사용자가 선택하기 전에는 아무것도 선택되지 않은 상태로 둡니다.
    # sorted() 함수로 MBTI 유형들을 정렬하여 시각적으로 정돈된 느낌을 줍니다.
    mbti_type = st.selectbox(
        "✨ **당신의 MBTI는 무엇인가요?**",
        options=[""] + sorted(list(MBTI_JOB_DATA.keys())),
        index=0 # 첫 번째 옵션(빈 문자열)이 기본으로 보이도록 설정
    )

    # 버튼 클릭 시 작동
    if st.button("🚀 내 직업 추천받기!"):
        if mbti_type: # MBTI 유형이 선택되었는지 확인
            # 선택된 MBTI 유형에 맞는 직업 리스트 가져오기
            # .get() 메서드를 사용하여 키가 없을 경우 기본값([])을 반환하도록 하여 오류를 방지합니다.
            recommended_jobs = MBTI_JOB_DATA.get(mbti_type, [])

            st.markdown("---") # 결과와 구분을 위한 선
            st.subheader(f"✅ **{mbti_type}** 유형에게 추천하는 직업이에요!")
            st.write("아래 직업들을 통해 당신의 재능을 꽃피울 수 있기를 응원합니다! 🌷")

            if recommended_jobs:
                # 추천 직업을 리스트 형식으로 깔끔하게 출력
                for job in recommended_jobs:
                    st.markdown(f"- **{job}**") # 마크다운을 이용해 볼드체와 리스트로 표현
            else:
                st.info("이런! 아직 **[{}](https://www.google.com/search?q={}%EB%B3%84+%EC%A7%81%EC%97%85)".format(mbti_type,mbti_type) + "** 유형에 대한 직업 추천 데이터가 부족하네요. 곧 업데이트 될 예정이니 조금만 기다려주세요! ㅠㅠ")

            st.markdown("---")
            st.info("💡 이 추천은 일반적인 경향성을 바탕으로 하며, 모든 사람에게 일률적으로 적용되는 것은 아니에요. 다양한 경험을 통해 자신에게 맞는 길을 찾아나가는 것이 중요하답니다!")
        else:
            # MBTI 유형이 선택되지 않았을 때 경고 메시지
            st.warning("앗! MBTI 유형을 먼저 선택해주세요! 😲")

# 앱 실행 시 main 함수 호출
if __name__ == "__main__":
    main()
