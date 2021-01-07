# -*- coding:UTF-8 -*-
# !/usr/bin/python

import os
import requests
import requests.packages.urllib3.util.ssl_
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

qq = os.environ['QQ']


def main(*args):
    api = "https://api.xmdpay.cn/API/mpz/api.php?qq="+qq
    for i in range(0, 21):
        data = requests.get(api, timeout=600)
        if "success" in data.text:
            print("第 {} 次刷赞成功".format(i))


if __name__ == '__main__':
    main()
