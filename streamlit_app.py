
import streamlit as st

# 타이틀과 귀여운 설명
st.title("🍿 CGV 부럽지 않은 팝콘 세트 메뉴")
st.subheader("모든 조합을 한눈에 확인해보세요!")

popcorn_options = ['기본', '카라멜', '어니언']
drink_options = ['생수', '탄산음료']

# 구분을 위한 얇은 선
st.divider()

# 중첩 루프로 스트림릿 화면에 출력
for popcorn in popcorn_options:
    for drink in drink_options:
        # f-string을 쓰면 문자열을 더 깔끔하고 예쁘게 출력할 수 있어요!
        st.write(f"🍔 **세트메뉴**: {popcorn} 팝콘 + {drink}")