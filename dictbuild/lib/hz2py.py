# !/usr/bin/env python
# coding: utf-8

import sys

class hz2pyclass(object):
    u"""汉字转换成拼音 convert:无声调 convert_sd:有声调"""

    def __init__(self):
        super(hz2pyclass, self).__init__()
        self.wordlist = []
        with open("lib/word.txt") as f:
            for line in f:
                self.wordlist.append(line.split('    '))
            # print self.wordlist

    def convert(self, word):
        rlist = []
        for x in self.convert_sd(word):
            if x[0] not in rlist:
                rlist.append(x[0])
        return rlist

    def convert_sd(self, word):
        try:
            word = word.decode('gbk')
        except:
            word = word.decode('utf-8')
        if len(word) != 1:
            print u"请输入一个汉字"
            sys.exit()
        for x in self.wordlist:
            k = '\\u' + x[0]
            k = k.decode('unicode-escape')
            if word == k:
                rlist = []
                for i in x[1].strip().split():
                    rlist.append([i[:-1],i[-1:]])
                return rlist