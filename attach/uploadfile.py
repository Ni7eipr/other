# !/usr/bin/env python
#-*- coding: UTF-8 -*-

import requests


def uploadfile():
    url = "http://web2.08067.me/upload.php"
    formname = "file"
    filename = "baidu.png"
    filetype = "image/png"
    filepath = ""
    proxies = {"http": "http://127.0.0.1:8080"}
    proxies = {}
    content = "123456 test"
    data = {'submit': 'submit'}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'}
    if filepath:
        content = open(filepath, 'rb')
    files = {formname: (filename, content, filetype)}
    r = requests.post(url, files=files, headers=headers, data=data, proxies=proxies)
    return r.content
