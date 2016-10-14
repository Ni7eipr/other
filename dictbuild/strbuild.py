#!/usr/bin/python
# encoding=utf-8

def iterall(num1,num2,str):

    for x in xrange(num1,num2):
        exec("""from itertools import product
for x in product({argv}):
    s = ""
    for xx in x:
        s += xx
    print s""".format(argv=",".join([str] * x)))

# iterall(num1, num2, str)
# 从num1到num2-1位的所有str中的字符
alla = "'ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxyz0123456789'"
alll = "'abcdefghijklmnopqrstuvwxyz0123456789'"
allu = "'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'"
iterall(1,6,hexl)