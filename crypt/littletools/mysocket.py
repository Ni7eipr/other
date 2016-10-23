#-*- coding: UTF-8 -*-
import socket
import json

from functions.Code import *
from functions.Burst import *
from functions.Crypto import *
from lib.argparse import Argparse

cmddict={
#       函数名                    函数功能                    参数(传入一个列表)
        'hexdec':hexdec,            # 十六进制 转 十进制        ["数据"]
        'bindec':bindec,            # 二进制   转 十进制        ["数据"]
        'octdec':octdec,            # 八进制   转 十进制        ["数据"]
        'dechex':dechex,            # 十进制   转 十六进制      ["数据"]
        'binhex':binhex,            # 二进制   转 十六进制      ["数据"]
        'octhex':octhex,            # 八进制   转 十六进制      ["数据"]
        'decbin':decbin,            # 十进制   转 二进制        ["数据"]
        'hexbin':hexbin,            # 十六进制 转 二进制        ["数据"]
        'octbin':octbin,            # 八进制   转 二进制        ["数据"]
        'decoct':decoct,            # 十进制   转 八进制        ["数据"]
        'hexoct':hexoct,            # 十六进制 转 八进制        ["数据"]
        'binoct':binoct,            # 二进制   转 八进制        ["数据"]

        'ascstr':ascstr,            # ascii码  转 字符串        ["ascii码","分隔符"]
        'strasc':strasc,            # 字符串   转 ascii码       ["字符串","分隔符"]

        'enbase64':enbase64,          # base64   加密             ["数据"]
        'debase64':debase64,          # base64   解密             ["数据"]
        'enurl':enurl,             # url      编码             ["数据"]
        'deurl':deurl,             # url      解码             ["数据"]
        'md5md5':md5md5,            # md5      加密             ["数据"]
        'zhalan':zhalan,            # 栅栏     加密解密         ["数据"]
        'kaisa':kaisa,             # 凯撒     加密解密         ["数据"]

        'backdict':backdict,          #
        'burstback':burstback
        }

# 函数名
cmd = "debase64"
# 参数
msg = ["UUyFTj8PCzF6geFn6xgBOYSvVTrbpNU4OF9db9wMcPD1yDbaJw==","20"]
# 调用
print cmddict[cmd](msg)

# bind_ip   = "127.0.0.1"
# bind_port = 51122
# while True:
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server.bind((bind_ip,bind_port))
#     server.listen(5)
#     client,addr = server.accept()
#     request = client.recv(1024)

#     jsondata = json.loads(request)
#     cmd = jsondata['cmd']
#     msg = jsondata['msg']
#     if jsondata['token'] != '7654123':
#         server.close()
#         client.close()
#     try:
#         data = cmddict[cmd](msg)
#     except Exception, e:
#         pass
#     else:
#         client.send(data)
#         f = open('log.txt','a')
#         f.writelines(strftime('%Y-%m-%d %H:%M:%S')+'    '+request+'    '+data+'  \n')
#         f.close()
#     finally:
#         server.close()
#         client.close()