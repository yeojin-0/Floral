import random
import streamlit as st
from data.flower_data import get_flower_data

st.header('무작위 날짜의 꽃')
#st.sidebar.title('무작위 날짜의 꽃 확인하기')

# 랜덤 날짜의 꽃 확인하기 - 30일 31일 처리하기
def random_flower():
    rand_month = random.randrange(1,13)
    rand_day = random.randrange(1,31)
    
    # flower_data.py 파일의 함수 호출
    flower_data = get_flower_data(rand_month, rand_day)

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

random_flower()

