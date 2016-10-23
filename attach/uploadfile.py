# !/usr/bin/env python
#-*- coding: UTF-8 -*-

import requests

def uploadfile(url,filepath,filename,filetype,formname,data,headers,proxies):
    files = {formname: (filename, open(filepath, 'rb'), filetype)}
    r = requests.post(url, files=files, headers=headers, data=data, proxies=proxies)
    return r.content

url = "http://web2.08067.me/upload.php"
filepath = "baidu.png"
filename = "baidu.png"
filetype = "image/png"
formname = "file"
proxies = {}#{"http": "http://127.0.0.1:8080",}

data = {
    'submit': 'submit'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'
}

print uploadfile(url,filepath,filename,filetype,formname,headers,data,proxies)