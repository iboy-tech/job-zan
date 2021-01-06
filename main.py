# -*- coding:UTF-8 -*-
# !/usr/bin/python

import os
import requests
import requests.packages.urllib3.util.ssl_
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

qq = os.environ['QQ']


def main(*args):
    api = "https://api.xmdpay.cn/API/mpz/api.php?qq="+qq
    data = requests.get(api, timeout=600).json()
    if data.get('msg') == "success":
        print("刷赞成功")
    print(data)


if __name__ == '__main__':
    main()
