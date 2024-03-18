import urllib.parse
import urllib.request
import json
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os

# load .env
load_dotenv()

query = '꽃집'
naver_client_id = os.getenv("NAVER_CLIENT_ID")
naver_client_secret = os.getenv("NAVER_CLIENT_SECRET")

st.header('내 주변 꽃가게 검색하기')

col1, col2 = st.columns(2)

def search_shops(location, sort):

    sort_criteria = "random" if sort == "정확도 순" else "comment"

    encText = urllib.parse.quote(query + ' ' + location)
    url = f"https://openapi.naver.com/v1/search/local.json?query={encText}&display=5&start=1&sort={sort_criteria}"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", naver_client_id)
    request.add_header("X-Naver-Client-Secret", naver_client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        result = json.loads(response_body)

        shop_data = []
        for item in result['items']:
            if '꽃집' in item['category']:
                title = item['title']
                link = item['link']
                address = item['address']
                roadAddress = item.get('roadAddress', '도로명 주소 정보 없음')

                shop_data.append({'가게 이름': title, '링크': link, '주소': address, '도로명 주소': roadAddress})

        if shop_data:
            df = pd.DataFrame(shop_data)
            st.dataframe(df, hide_index=True)
        else:
            st.info("해당 지역에 꽃가게가 없습니다.")
    else:
        st.error("데이터를 불러오는 중 오류가 발생했습니다.")

with col1:
    location = st.text_input("검색할 지역을 입력하세요(5개까지 출력됩니다): ")

sort_type = st.radio("정렬 방식 선택:", ["정확도 순", "리뷰 순"])

if st.button('검색'):
    search_shops(location, sort_type)
