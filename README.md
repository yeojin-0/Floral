# Floral
Floral은 농촌진흥청에서 소개하는 오늘의 꽃을 알려주고 상황에 따라 꽃다발을 추천해주는 프로그램입니다.

## 만든 이유?
일상에서 길을 걷다 보면 종종 꽃들을 보게 됩니다. 그때마다 어떤 꽃인지 궁금한 마음이 들었습니다. 하나씩 찾아보는 것도 재미있었지만, 매일 하나씩 알아가는 과정이 더 재밌지 않을까 하고 오늘의 꽃에 대해 소개하고자 합니다.
또한, 이 프로그램을 통해 꽃에 대한 흥미를 높이고, 꽃의 아름다움과 의미를 함께 고민해보고자 했습니다. 특히 코로나 이후 화훼농가들이 어려움을 겪고 있어, 그들에게 조금이나마 도움이 되고자 꽃에 대한 관심을 높이고자 했습니다.

우리는 꽃을 선물할 때 어떤 꽃을 골라야 할지 고민합니다. 단순히 예쁘다고 선택하는 것이 아니라, 상황에 맞는 꽃말을 가진 꽃을 선택하여 더욱 좋은 인상을 남길 수 있을 것으로 생각했습니다. 
따라서 해당 상황에 어울리는 꽃다발을 추천하는 챗봇을 개발해보았습니다.

## 기능
- 오늘의 꽃: 농촌진흥청에서 소개하는 오늘의 꽃을 확인할 수 있습니다.
- 무작위 날짜의 오늘의 꽃 : 무작위 날짜를 선발하여 그 날짜에 해당되는 '오늘의 꽃'을 확인합니다.
- 상황별 꽃다발 추천하는 챗봇: 사랑 고백, 감사의 마음 전달, 위로가 필요한 상황 등 다양한 상황에 맞는 꽃다발을 추천해줍니다.
- 꽃집 확인하기: ㅇㅇ[시/군/구] ㅇㅇ[읍/면/동] 입력하면 그 주소를 기준으로 꽃집 5개를 소개시켜줍니다. 가까운순과 리뷰순 두 기준으로 볼 수있으며 리뷰순은 네이버 기준으로 확인할 수 있습니다. 

## 개발 환경
- python 3.10
```bash
pip install mysql-connector-python #MySQL 데이터베이스와 연결하기 위한 라이브러리
pip install streamlit # Streamlit 라이브러리
pip install langchain # 자연어 처리 모델을 쉽게 구축하고 훈련시킬 수 있는 라이브러리
pip install openai #  기계학습 모델을 쉽게 활용할 수 있는 도구
pip install python-dotenv # 환경 변수 파일을 로드
```
#### 시작 하기전 API 발급
- 오늘의 꽃 : https://www.data.go.kr/data/15084605/openapi.do  
- OpenAI: https://platform.openai.com/api-keys 
- Naver : https://developers.naver.com/docs/common/openapiguide/appregister.md


## 프로젝트 구조
```bash
├─ .gitignore
├─ LICENSE
├─ pink_rose.jpg
├─ README.md
├─ todayflor.py
│ 
│  
├─data
│  │  .env
│  │  flower_data.py
│  └─__init__.py
│          
└─pages
    │  .env
    │  FlorPick.py
    │  flower_list.py
    │  rand_flower.py
    └─ today_flower.py
```




