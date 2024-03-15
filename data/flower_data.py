# flower_data.py
import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os

# load .env
load_dotenv()
FLOWER_API_KEY = os.getenv("FLOWER_API")

def get_flower_data(month, day):  # 매개변수로 월과 일을 받도록 수정
    key = FLOWER_API_KEY

    url = 'http://apis.data.go.kr/1390804/NihhsTodayFlowerInfo01/selectTodayFlower01'
    params = {'serviceKey': key, 'fMonth': month, 'fDay': day}
    response = requests.get(url, params=params)
    contents = response.text
    root = ET.fromstring(contents)
    body = root.find('.//result')

    return {
        'result_code': root.findtext('resultCode'),
        'result_msg': root.findtext('resultMsg'),
        'repcategory': root.findtext('repcategory'),
        'data_no': body.findtext('dataNo'),
        'f_month': body.findtext('fMonth'),
        'f_day': body.findtext('fDay'),
        'flow_nm': body.findtext('flowNm'),
        'f_sct_nm': body.findtext('fSctNm'),
        'f_eng_nm': body.findtext('fEngNm'),
        'flow_lang': body.findtext('flowLang'),
        'f_content': body.findtext('fContent'),
        'f_use': body.findtext('fUse'),
        'f_grow': body.findtext('fGrow'),
        'f_type': body.findtext('fType'),
        'file_name1': body.findtext('fileName1'),
        'file_name2': body.findtext('fileName2'),
        'file_name3': body.findtext('fileName3'),
        'img_url1': body.findtext('imgUrl1'),
        'img_url2': body.findtext('imgUrl2'),
        'img_url3': body.findtext('imgUrl3'),
        'publish_org': body.findtext('publishOrg')
    }
