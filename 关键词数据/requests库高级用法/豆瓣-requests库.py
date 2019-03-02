# python
# -*- coding:utf-8 -*-
# author liao_wk time
#  模拟登录豆瓣成功

import requests
requests2 = requests.Session()

data = {
    "ck": "",
    "name": "15343213097",
    "password": "2957694523",
    "remember":	"false",
    "ticket": ""
}
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/64.0",
#     "Accept": "application/json",
#     'Accept-Encoding':  'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#     'Connection': 'keep-alive',
#     'Content-Length': '59',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Host': 'accounts.douban.com',
#     'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
#     'X-Requested-With': 'XMLHttpRequest'
# }
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"
}

url_base = "https://accounts.douban.com/j/mobile/login/basic"
response = requests2.post(url_base, data, headers=headers)
print(response.json())

# 用豆瓣发布感想
data2 = {
            "ck": "??",  # 根据cookie内容来获取ck的值（参考值）
            "comment": "我想说："  # 输入评论的内容

}
response_2 = requests2.post("https://www.douban.com/", data2, headers=headers)
print(response_2.json())




