# -*- coding: utf-8 -*-
import sys
import string

def ascstr(msg):
    res = ""
    b = msg[0].split(msg[1])
    for x in b:
        if 0 <= int(x) <= 127:
            res += chr(int(x))
        else:
            return x + u":格式错误"
    return res

def strasc(msg):
    res = []
    for x in msg[0]:
        if x in string.printable:
            res.append(str(ord(x)))
        else:
            return u'格式错误'
    return msg[1].join(res)

def zhalan(msg):
    res = ""
    for j in range(int(msg[1])):
        for i in range(j):
            res += msg[0][i::j]
        res += "\n"
    return res

def kaisa(msg):
    res0 = ""
    for i in range(int(msg[1])):
        res = ""
        for x in range(0,len(msg[0])):

            if ord(msg[0][x]) <= ord("z") and ord(msg[0][x]) >= ord("a"):

                if ord(msg[0][x]) >= ord("a") and ord(msg[0][x]) + i <= ord("z"):
                    res += chr(ord(msg[0][x]) + i)
                else:
                    res += chr(ord(msg[0][x]) + i - ord("z") + ord("a") - 1)

            elif ord(msg[0][x]) <= ord("Z") and ord(msg[0][x]) >= ord("A"):

                if ord(msg[0][x]) >= ord("A") and ord(msg[0][x]) + i <= ord("Z"):
                    res += chr(ord(msg[0][x]) + i)
                else:
                    res += chr(ord(msg[0][x]) + i - ord("Z") + ord("A") - 1)

            else:
                res += chr(ord(msg[0][x]))
        res0 += res + str(i).rjust(5) + "\n"
    return res0