import requests
import re
from  urllib.parse import unquote
#  过程挺复杂的
#  模块1：检索模块 def  search()
#  模块2：相关性click模块  def relate_click()
#  模块3：每页50个click模块 def page_count50_click()
#  模块4：添加入标记列表   def add_marklist()
#   模块5：......
requests2 = requests.Session()
sid_pattern = r"SID=(\w+)&"
qid_pattern = r"qid=(\d+)&"


def search(SID, query_item):
    url_base = "http://apps.webofknowledge.com/UA_GeneralSearch.do"
    qid_pattern = r"qid=(\d+)&"
##  表单参数
    data = {
        'search_mode': 'GeneralSearch',
        'max_field_notice':  '注意:+无法添加另一字段。',
        'page': '1',
        'input_invalid_notice':    '检索错误:+请输入检索词。',
        'exp_notice': '检索错误:+专利检索词可以在多个家族中找到 + (',
        'input_invalid_notice_limits': '+ < br / > 注意: +滚动框中显示的字段必须至少与一个其他检索字段相组配。',
        'pageSize': '50',
        'fieldCount': '1',
        'action': "search",
        'product': 'UA',
        'SID': SID,
        'max_field_count': '25',
        'sa_params': "	UA||"+SID+"|http://apps.webofknowledge.com|'",
        'formUpdated': 'true',
        'value(select1)': 'TS',
        'value(hidInput1)': '',
        'limitStatus': 'collapsed',
        'range': 'CUSTOM',
        'ss_lemmatization': 'On',
        'ss_spellchecking': 'Suggest',
        'SinceLastVisit_UTC': "",
        'SinceLastVisit_DATE': "",
         'value(input1)': query_item,
        'period': 'Year Range',
        'startYear': '1990',
        'endYear': '2018',
        'update_back2search_link_param': 'yes',
        'ssStatus': 'display:none',
        'ss_showsuggestions':  'ON',
        'ss_query_language': 'auto',
        'ss_numDefaultGeneralSearchFields': '',
        'rs_sort_by': 'RS.D;PY.D;AU.A;SO.A;VL.D;PG.A',
        # 'editions': ['WOS.ESCI', 'WOS.SSCI', 'WOS.SCI', 'WOS.IC', 'WOS.AHCI', 'WOS.ISTP', 'WOS.CCR', 'BCI.BCI', 'BCI.BCI',
        #              'MEDLINE.MEDLINE', 'RSCI.RSCI', 'SCIELO.SCIELO'],
        'ssStatus': 'display:none',
        'ss_showsuggestions': 'ON',
        'ss_numDefaultGeneralSearchFields': '1',
    }
	# 头部信息
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
    }
    try:
        response_1 = requests2.post(url_base, data=data, headers=headers)
        with open('result11.html', 'w', encoding='utf-8') as file:
            file.write(response_1.text)
        print(response_1.headers)
        print("status_code:", response_1.status_code)
        print(">>>>>>>>>>>>>>>>>>>")
        # print(response_1.text)
        # print(response_1.url)
        if "Topic" in response_1.text:
            print("爬取成功")
        else:
            print("》》》》爬取内容失败《《《《《《")
        #  输出qid

        # qid = re.findall(qid_pattern, )
        # print("qid=", qid)

    except:
        print("》》》》》》》检索失败《《《《《《《《")


def add_marklist(SID, qid):
    data = {
        'selectedIds': ['1;2;3;4;5;6;7;8;9;10'],
        'colName': '',
        'mark_from': '',
        'mark_to': '',
        'viewType': '',
        'summary': ''
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
    }
    url_base = "http://apps.webofknowledge.com/MarkRecords.do?product=UA&mark_id=UDB&SID="+SID+"&qid="+qid+"&search_mode=GeneralSearch"
    response_2 = requests2.post(url_base, data, headers=headers)
    with open('result2.html', 'w', encoding='utf-8') as file:
        file.write(response_2.text)
    print("url2:", response_2.url)
    print("status_code2:", response_2.status_code)


SID = "7DnoYRAkfRq732BmPxE"
query_item = "Agile Robots"
qid = '1'
search(SID, query_item)
add_marklist(SID, qid)
