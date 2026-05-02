import streamlit as st

st.title("EC2 테스트 앱")

st.write("이 앱은 이름을 입력하면 인사해주는 간단한 테스트 앱입니다.")
st.caption("현재 페이지는 실습4에서 FastAPI를 활용하여 더 복잡한 기능의 백엔드 처리를 구현할 예정입니다.")

name = st.text_input("이름을 입력하세요")

if st.button("확인"):
    st.write(f"안녕하세요 {name}님!")