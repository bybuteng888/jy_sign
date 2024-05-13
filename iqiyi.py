# -*- coding: utf-8 -*-



import requests
import os

jy_cookie = os.environ["jy_cookie"]

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

print(response.text)
msg = f"\n[+]签到获得{growth}成长值\n[+]连续签到：{continueSignDaysSum}天\n[+]签到周期：{rouund_day}天/{rewardDay}天"
return msg

