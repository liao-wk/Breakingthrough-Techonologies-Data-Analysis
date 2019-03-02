# python
# -*- coding:utf-8 -*-
# author liao_wk time
import re
import urllib.parse
qid_pattern = r"qid=(\d+)&"
url = "http%3A%2F%2Fapps.webofknowledge.com%2Fsummary.do%3Fproduct%3DUA%26search_mode%3DGeneralSearch%26page%3D1%26qid%3D3%26SID%3D6AC7wb6Lv5WuvZZ9rPk"
url = urllib.parse.unquote(url)
print(url)
result = re.findall(qid_pattern, url)
print(result)

