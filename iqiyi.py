# -*- coding: utf-8 -*-

import requests
import os

jy_cookie = os.environ["jy_cookie"]


class aiqiyi:

    def user_information(self):
        url = 'https://bbs.125.la/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1'

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            # "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Cookie": jy_cookie,
            "Host": "bbs.125.la",
            "Referer": "https://bbs.125.la/",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
             # "sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
             # "sec-ch-ua-mobile": "?0",
             # "sec-ch-ua-platform": "\"Windows\""
        }
        data = {
            "formhash": "9c12567f",
            "submit": "1",
            "targerurl": "",
            "todaysay": "",
            "qdxq": "fd"
        }
        response = requests.post(url, headers=headers, data=data).text
        print(response)
        return response


