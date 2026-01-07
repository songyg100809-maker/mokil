your_project/
├── main.py                # 메인 페이지 (Home)
├── pages/                 # 다른 페이지들을 담는 폴더
│   ├── 1_About.py
│   ├── 2_Schedule.py
│   └── 3_Board.py
└── requirements.txt       # 설치가 필요한 라이브러리 목록
  streamlit
pandas
  import streamlit as st

# 페이지 설정
st.set_page_config(page_title="우리 학교 공식 홈페이지", page_icon="🏫")

st.title("🏫 우리 학교에 오신 것을 환영합니다!")
st.subheader("오늘의 주요 소식을 확인하세요.")

# 학교 홍보 이미지 (구글에서 가져온 샘플 이미지나 본인 학교 사진 URL로 교체하세요)
st.image("https://images.unsplash.com/photo-1541339907198-e08756ebafe3?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", caption="우리 학교 전경")

col1, col2 = st.columns(2)

with col1:
    st.info("### 📢 공지사항")
    st.write("- 1학기 기말고사 안내")
    st.write("- 축제 준비 위원회 모집")
    st.write("- 체육대회 대진표 공개")

with col2:
    st.success("### 🍱 오늘의 급식")
    st.write("- 현미밥")
    st.write("- 소고기 미역국")
    st.write("- 제육볶음 & 쌈채소")
    st.write("- 배추김치")
  import streamlit as st

st.title("🏫 학교 소개")

st.header("교훈")
st.markdown("> **"스스로 서고 함께 배우며 미래를 여는 학생"**")

st.header("우리 학교의 역사")
st.write("1990년 개교 이래 수많은 인재를 배출해 온 우리 학교는...")

# 지도 대신 위치 정보 표시
st.header("📍 찾아오시는 길")
st.write("서울특별시 OO구 OO로 123 (행복동)")
import streamlit as st
import pandas as pd

st.title("📅 학사 일정")

# 일정 데이터 예시
schedule_data = {
    "날짜": ["2024-03-02", "2024-05-05", "2024-07-20", "2024-08-16"],
    "행사명": ["입학식", "어린이날 휴교", "여름방학 식", "개학식"]
}
df = pd.DataFrame(schedule_data)

st.table(df) # 깔끔한 표로 출력
