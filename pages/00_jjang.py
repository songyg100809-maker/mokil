import streamlit as st

st.title("🎸 동아리 활동")
st.write("목일중학교의 활기찬 동아리를 소개합니다.")

clubs = {
    "학술": ["방송부(MIBS)", "도서부", "수학탐구부"],
    "예체능": ["밴드부", "농구부", "미술부"],
    "자율": ["코딩부", "요리부", "환경보호부"]
}

for category, names in clubs.items():
    with st.expander(f"✨ {category} 동아리"):
        for name in names:
            st.write(f"- {name}")

st.info("💡 동아리 개설 신청은 매년 3월 학생회에 문의하세요.")
