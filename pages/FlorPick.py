import mysql.connector
import streamlit as st
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import ChatMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# load .env
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-3.5-turbo-1106"

class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)


# MySQL 서버에 연결
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000",
    database="FlowerData"
)

# 커서 생성
cursor = connection.cursor()

st.header('플로픽이 꽃다발을 추천해줘요!')

# 꽃다발 상황에 따라 추천 - 챗봇 
def bouquet_chatbot():
    query = "SELECT * FROM flowerdata.flower_data WHERE flower_bouquet = 'TRUE';"
    cursor.execute(query)
    # 결과 가져오기
    rows = cursor.fetchall()
    for row in rows:
        data_no, f_month, f_day, f_name, f_sct_nm, f_eng_nm, \
        flow_lang, f_content, f_use, f_grow, f_type, f_img = row[3:15]

    if "messages" not in st.session_state:
        st.session_state["messages"] = [ChatMessage(role="assistant", 
        content="안녕하세요! 저는 플로픽이에요. 어떤 분께 꽃다발을 선물하고 싶으신가요?")]

    # 이전 대화 내용 출력
    for msg in st.session_state.messages:
        st.chat_message(msg.role).write(msg.content)

    if prompt := st.chat_input():
        st.session_state.messages.append(ChatMessage(role="user", content=prompt))
        st.chat_message("user").write(prompt)

        if not API_KEY:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()

        with st.chat_message("assistant"):
            want_to = f"""
                너는 아래 내용을 기반으로 질의응답을 하는 로봇이야.
                content
                너의 이름은 플로픽, 꽃다발을 추천해주는 챗봇으로 만들어졌어.
                {data_no}, {f_month}월 {f_day}일
                이름: {f_name}
                학명: {f_sct_nm}
                영문명: {f_eng_nm}
                꽃말: {flow_lang}
                내용: {f_content}
                용도: {f_use}
                유형: {f_type}
                이미지: {f_img}
                사랑을 고백하고 싶을 때: 장미, 히아신스  물망초, 스타티스, 수선화, 스토크, 솜다리, 작약
                친구나 가족에게 감사의 마음을 전하고 싶을 때: 잉글리쉬데이지, 프리지아, 카네이션, 루드베키아, 다알리아, 스위트피
                위로가 필요한 이에게 전하고 싶을 때: 수국, 안개초, 물망초, 프리지아, 잉글리쉬데이지, 안개초
                신선하고 긍정적인 에너지를 전하고 싶을 때: 해바라기, 수선화, 거베라, 칼라디움, 아네모네
                사과의 마음을 전하고 싶을 때: 아이리스, 카네이션,  델피니움, 스토크, 스위트피
                새로운 시작을 축하하고 싶을 때: 국화, 루드베키아, 아이리스, 수국, 천일홍, 라넌큘러스
                졸업식, 졸업작품발표회 등 본인이 하고 있는 일을 마무리해서 축하하고 싶을 때: 델피니움, 스타티스, 수선화, 해바라기
                새로운 관계의 시작, 기념일(사랑과 애정의 감정 표현) : 종꽃, 작약

                꽃 추천을 해주고 마지막 줄에는 꼭 꽃집청년들 사이트를 소개시켜서 그 꽃에 관련 상품을 보여줘
                사이트 주소 'https://www.f-mans.com/' 을 소개시켜서 꽃 관련 상품을 검색할 수 있게 유도해줘
            """
            
            stream_handler = StreamHandler(st.empty())
            llm = ChatOpenAI(openai_api_key=API_KEY, streaming=True, callbacks=[stream_handler], model_name=MODEL)
            response = llm([ChatMessage(role="system", content=want_to)] + st.session_state.messages)
            st.session_state.messages.append(ChatMessage(role="assistant", content=response.content))


bouquet_chatbot()

# 연결 종료
connection.close()