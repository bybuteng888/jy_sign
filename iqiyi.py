# -*- coding: utf-8 -*-

import json
import os
import re
import time
import requests
import requests
import os


jy_cookie = os.environ["jy_cookie"]
class aiqiyi:
def user_information(self):
        URL="https://bbs.125.la/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'cookie': jy_cookie,
        'Referer': 'https://bbs.125.la/'
    }
data = {
        "formhash": "9c12567f",
        "submit": "1",
        "targerurl": "",
        "todaysay": "",
        "qdxq": "fd"
    }
response = requests.post(URL, headers=headers, data=data)

if response.json()["credit"]!= None
    try:
                msg = "签到成功"
    except:
                msg = response.json()
    else:
        # print("（iqy）签到错误", res.content.decode())
                msg = response.json()
print(msg)
return msg

    return msg



