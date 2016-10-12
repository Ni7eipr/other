#!/usr/bin/python
# encoding=utf-8

a = "wcrx{rju_456_RJU}"

def caesar(data):
    res = ""
    for x in range(26):
        for i in data:
            if ord(i) >= 65 and ord(i) <= 90 :
                if ord(i)+x > 90:
                    res += chr(ord(i)-26+x)
                else:
                    res += chr(ord(i)+x)
            elif ord(i) >= 97 and ord(i) <= 122:
                if ord(i)+x > 122:
                    res += chr(ord(i)-26+x)
                else:
                    res += chr(ord(i)+x)
            else:
                res += i
        res += "\n"
    return res

if __name__ == '__main__':
    print caesar(a)