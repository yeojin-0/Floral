import streamlit as st
from datetime import datetime
import streamlit as st
from data.flower_data import get_flower_data

st.header('오늘의 꽃')
#add_page_title(layout="wide")
st.sidebar.title('오늘의 꽃 확인하기')

col1, col2  = st.columns(2)

# 사용자로부터 원하는 날짜를 입력받음
with col2:
    selected_date = st.date_input("보고 싶은 날짜를 선택하세요", value=None)

# 사용자가 날짜를 선택하지 않았을 때의 예외 처리
if selected_date is not None:
    
    # 선택한 날짜를 월(month)과 일(day)로 나누기
    month = selected_date.month
    day = selected_date.day

    # flower_data.py 파일의 함수 호출
    flower_data = get_flower_data(month, day)

    # 변수명 지정
    result_code = flower_data['result_code']
    result_msg = flower_data['result_msg']
    repcategory = flower_data['repcategory']
    data_no = flower_data['data_no']
    f_month = flower_data['f_month']
    f_day = flower_data['f_day']
    flow_nm = flower_data['flow_nm']
    f_sct_nm = flower_data['f_sct_nm']
    f_eng_nm = flower_data['f_eng_nm']
    flow_lang = flower_data['flow_lang']
    f_content = flower_data['f_content']
    f_use = flower_data['f_use']
    f_grow = flower_data['f_grow']
    f_type = flower_data['f_type']
    publish_org = flower_data['publish_org']

    # col1 컬럼에 변수 적용
    with col1:
        st.subheader("{0}월 {1}일".format(f_month, f_day))
        st.markdown(f"""
        :blossom:**꽃 이름(국문):**:blossom: {flow_nm}  
        :blossom:**꽃 이름(학명):**:blossom: {f_sct_nm}  
        :blossom:**꽃 이름(영문):**:blossom: {f_eng_nm}
        """)
    
    st.divider()
    st.markdown(f"""
    **꽃말:** {flow_lang}  

    **내용:** {f_content}  

    **이용:** {f_use}  

    **기르기:** {f_grow}  

    **자생지:** {f_type}
    """)

    # 탭 생성
    tabs = st.tabs(["꽃 이미지 1", "꽃 이미지 2", "꽃 이미지 3"])

    # 각 탭에 이미지 및 정보 출력
    with tabs[0]:
        if flower_data['img_url1']:
            st.image(flower_data['img_url1'], use_column_width=True)
        else:
            st.write("이미지를 찾을 수 없습니다.")

    with tabs[1]:
        if flower_data['img_url2']:
            st.image(flower_data['img_url2'], use_column_width=True)
        else:
            st.write("이미지를 찾을 수 없습니다.")

    with tabs[2]:
        if flower_data['img_url3']:
            st.image(flower_data['img_url3'],use_column_width=True)
        else:
            st.write("이미지를 찾을 수 없습니다.")

    st.caption(f"{publish_org}")

else:
    st.warning("날짜를 선택해주세요.")

