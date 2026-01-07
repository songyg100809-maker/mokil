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
