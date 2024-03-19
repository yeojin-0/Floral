# 내 주변 꽃집 소개
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

        # 결과에서 카테고리가 '꽃집'에 해당하는 정보만 필터링하여 출력
        for item in result['items']:
            if '꽃집' in item['category']:
                title = item['title']  # 가게 이름
                link = item['link']  # 링크
                address = item['address']  # 주소
                roadAddress = item['roadAddress'] # 도로명 주소
                 
                st.markdown(f"""
                        **가게 이름:** {title}  

                        **링크:**  {link}

                        **주소:** {address} 
                        
                        **도로명 주소:** {roadAddress} 

                        """)
                st.markdown("---")  # 구분선 추가
    else:
        st.write("Error Code:", rescode)


if __name__ == "__main__":
    st.header('내 주변 꽃가게 검색하기')
    st.text("최대 5개까지 보여주며 리뷰순은 네이버 기준 입니다.")

    location = st.text_input("검색할 지역을 입력하세요(ㅇㅇ[시/군/구] ㅇㅇ[읍/면/동]): ")

    sort_type = st.radio("정렬 방식 선택:", ["정확도 순", "리뷰 순"])

    if st.button('검색'):
        search_shops(location, sort_type)