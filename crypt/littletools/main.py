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
cmd = "kaisa"
# 参数
msg = [
    """EW S4W WFU5LWV L1 T41SVW0 1M4 2S4L0W4KZ52 E5LZ LZW 9505KL4G 1X WVMUSL510 L1 9S7W S 810Y-8SKL50Y 592SUL 10 LZW 85NWK 1X UZ50WKW KLMVW0LK LZ41MYZ S 6150L8G-VWK5Y0WV TSK7WLTS88 UM445UM8M9 S0V S E5VW 4S0YW 1X KUZ118 TSK7WLTS88 241Y4S9K," KS5V KZ1W9S7W4. "LZ5K U1995L9W0L 9S47K S01LZW4 958WKL10W 50 LZW 0TS'K G1MLZ S0V TSK7WLTS88 VWNW8129W0L WXX14LK 50 UZ50S." X8SY { YK182V9ZUL9STU5V}""",
    "26"
]
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