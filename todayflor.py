#streamlit run todayflor.py --server.port=5000
import streamlit as st

class FlowerApp:
    def __init__(self):
        self.page_names_to_funcs = {
            "Main Page": self.main_page,
            "today_flower": self.page2,
            "rand_flower": self.page3,
            "FlorPick": self.page4,
            "list": self.page5,
        }
        self.run_app()

    def run_app(self):
        # selected_page = st.sidebar.selectbox("Select a page", self.page_names_to_funcs.keys())
        selected_page = 'Main Page'  # 기본적으로 'Main Page' 페이지를 선택하도록 설정합니다.
        self.page_names_to_funcs[selected_page]()

    def main_page(self):
        st.markdown("# Floride")
        #st.sidebar.markdown("# 오늘의 꽃 메인 페이지")
        st.markdown("""
            어서오세요. 여기는 플로라이드입니다! 
            우리는 매일 다른 꽃을 소개하고, 꽃에 대한 정보와 이야기를 전달하여 여러분의 일상에 자연의 아름다움을 느낄 수 있게 하는 것이 목표입니다.

            ### 주요 기능

            - **오늘의 꽃 확인하기**: 매일 업데이트되는 오늘의 꽃을 확인하고, 각 꽃의 이름, 꽃말, 특징 등을 알아보세요.
            - **무작위 날짜의 꽃 확인하기**: 특정 날짜에 해당하는 무작위 꽃을 살펴보고, 그 꽃들의 특징에 대해 설명해 줍니다.
            - **플로픽 챗봇**: 플로픽 챗봇을 통해 각종 상황에 어울리는 꽃다발을 추천 받을 수 있어요! 
            고백 하는 날인데 어떤 꽃을 선물하는 게 좋을까요? 항상 장미만 생각했다면, 플로픽에게 추천 받아서 조금 더 본인의 마음을 간접적으로 표현하는 게 어떨까요? 어떤 꽃을 선물 해야할지 모르겠다면 플로픽에게 추천받아봐도 좋아요!
            - **꽃집 확인하기**: 주소를 입력하면 가까운 위치의 꽃집을 알려줘요. 원한다면 리뷰순으로 볼 수 있어요(네이버 기준) 

            ### 소개글

            - 매일매일 새롭게 업데이트되는 오늘의 꽃은 자연의 다채로운 아름다움을 만나보실 수 있습니다.
            - 꽃말, 특징, 유래 등 다양한 정보를 통해 꽃에 대한 정보를 얻을 수 있어요.
            - 플로픽 챗봇은 사용자의 감정과 상황에 맞는 꽃다발을 추천하여 소중한 사람에게 감동을 전해보세요.

        """)

        st.image("nsplash.jpg",use_column_width=True)

    def page2(self):
        st.markdown("# 오늘의 꽃 ")
        #st.sidebar.markdown("# 오늘의 꽃을 보여줘요 ")

    def page3(self):
        st.markdown("# 무작위 날짜로 보기 ")
        #st.sidebar.markdown("# 무작위 날짜의 꽃을 볼 수 있어요 ")

    def page4(self):
        st.markdown("# 플로픽 챗봇 ")
        #st.sidebar.markdown("# 꽃다발 추천해주는 챗봇 플로픽!")

    def page5(self):
        st.markdown("# 내 주변 꽃가게 ")
        #st.sidebar.markdown("# 내 주변 꽃가게를 확인 할 수 있어요!")

if __name__ == "__main__":
    app = FlowerApp()