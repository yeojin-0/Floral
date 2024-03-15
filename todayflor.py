# Contents of ~/my_app/streamlit_app.py / streamlit run streamlit_app.py
import streamlit as st

class FlowerApp:
    def __init__(self):
        self.page_names_to_funcs = {
            "Main Page": self.main_page,
            "오늘의 꽃": self.page2,
            "무작위 꽃": self.page3,
            "FlorPick": self.page4,
        }
        self.run_app()

    def run_app(self):
        # selected_page = st.sidebar.selectbox("Select a page", self.page_names_to_funcs.keys())
        selected_page = 'Main Page'  # 기본적으로 'Main Page' 페이지를 선택하도록 설정합니다.
        self.page_names_to_funcs[selected_page]()

    def main_page(self):
        st.markdown("# 오늘의 꽃")
        #st.sidebar.markdown("# 오늘의 꽃 메인 페이지")
        st.markdown("""
        ### 어서오세요! 오늘의 꽃에 오신 것을 환영합니다.

        우리는 매일 다른 꽃을 소개하고, 꽃에 대한 흥미로운 정보와 이야기를 전달하여 여러분의 일상에 자연의 아름다움을 더해드리고자 합니다.

        ### 주요 기능

        - **오늘의 꽃 확인하기**: 매일 업데이트되는 오늘의 꽃을 확인하고, 각 꽃의 이름, 꽃말, 특징 등을 알아보세요.
        - **무작위 날짜의 꽃 확인하기**: 특정 날짜에 해당하는 무작위 꽃을 살펴보고, 다양한 꽃들의 다양한 이야기를 만나보세요.
        - **플로픽 챗봇**: 플로픽 챗봇을 통해 각종 상황에 어울리는 꽃다발을 추천받아 보세요. 사랑의 고백, 감사의 마음 전달, 새로운 시작 축하 등 다양한 상황에 맞는 꽃다발을 만나보실 수 있습니다.

        ### 어떤 꽃을 기대할 수 있나요?

        - 매일매일 새롭게 업데이트되는 오늘의 꽃은 자연의 다채로운 아름다움을 만나보실 수 있습니다.
        - 꽃말, 특징, 유래 등 다양한 정보를 통해 꽃에 대한 새로운 관심을 불러일으킬 것입니다.
        - 플로픽 챗봇은 여러분의 감정과 상황에 맞는 특별한 꽃다발을 추천하여 소중한 사람에게 감동을 전해보세요.

        ### 지금 바로 시작해보세요!

        오늘의 꽃을 통해 자연의 아름다움을 만끽하고, 특별한 순간을 더욱 특별하게 만들어보세요. 아래 버튼을 클릭하여 주요 기능을 시작해보세요.
        """)

        st.image("red_rose.jpg",use_column_width=True)

    def page2(self):
        st.markdown("# 오늘의 꽃 ")
        #st.sidebar.markdown("# 오늘의 꽃을 보여줘요 ")

    def page3(self):
        st.markdown("# 무작위 날짜로 보기 ")
        #st.sidebar.markdown("# 무작위 날짜의 꽃을 볼 수 있어요 ")

    def page4(self):
        st.markdown("# 플로픽 챗봇 ")
        #st.sidebar.markdown("# 꽃다발 추천해주는 챗봇 플로픽!")

if __name__ == "__main__":
    app = FlowerApp()