import streamlit as st
from data.flower_data import get_flower_data
from datetime import datetime

# 꽃 정보
def display_flower_data(flower_data):
    st.subheader(f"{flower_data['f_month']}월 {flower_data['f_day']}일")
    st.markdown(f"""
        :blossom:**꽃 이름(국문):**:blossom: {flower_data['flow_nm']}  
        :blossom:**꽃 이름(학명):**:blossom: {flower_data['f_sct_nm']}  
        :blossom:**꽃 이름(영문):**:blossom: {flower_data['f_eng_nm']}
        """)
    st.divider()
    st.markdown(f"""
        **꽃말:** {flower_data['flow_lang']}  

        **내용:** {flower_data['f_content']}  

        **이용:** {flower_data['f_use']}  

        **기르기:** {flower_data['f_grow']}  
        
        **자생지:** {flower_data['f_type']}
        """)
    
    #탭 생성
    tabs = st.tabs(["꽃 이미지 1", "꽃 이미지 2", "꽃 이미지 3"])
    
    for i, img_url in enumerate([flower_data['img_url1'], flower_data['img_url2'], flower_data['img_url3']]):
        with tabs[i]:
            if img_url:
                st.image(img_url, use_column_width=True)
                st.caption(f"{flower_data['publish_org']}")

            else:
                st.write("이미지를 찾을 수 없습니다.")

if __name__ == "__main__":
    st.header('오늘의 꽃')
    col1, col2 = st.columns(2)

    selected_date = st.date_input("보고 싶은 날짜를 선택하세요", value=None)

    # 날짜 선택 시
    if selected_date:
        month = selected_date.month
        day = selected_date.day

    # 날짜 선택 하지 않으면 오늘 날짜
    else:
        now = datetime.now()
        month, day = now.month, now.day

    flower_data = get_flower_data(month, day)
    display_flower_data(flower_data)


