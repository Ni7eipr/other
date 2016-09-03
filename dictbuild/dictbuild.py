# !/usr/bin/env python
# coding: utf-8

from lib.argparsem import argparseclass
from lib.hz2py import hz2pyclass
import platform

class dictbuild(object):
    """docstring for dict"""
    def __init__(self):
        super(dictbuild, self).__init__()
        self.name = []
        self.birth = []

        self.hz2py = hz2pyclass()
        self.ARGV = argparseclass()

        self.getname()
        self.getbirth()
        self.build()

    def getname(self):
        if self.ARGV["name"].isalpha():
            self.name.append(self.ARGV["name"].upper())
            self.name.append(self.ARGV["name"].lower())
            if self.ARGV["name"] not in self.name:
                self.name.append(self.ARGV["name"])
        else:
            if platform.system() == "Windows":
                num = 2
            else:
                num = 3
            r = []
            for x in range(len(self.ARGV["name"]))[::num]:
                 r.append(self.hz2py.convert(self.ARGV["name"][x:x+num]))

            tmp = ["",""]
            for x in r:
                for xx in x:
                    tmp[0] += xx
                    tmp[1] += xx[0]
            tmp.append(tmp[1][:-1])
            # tmp.append(tmp[1][1:])
            for x in tmp:
                self.name.append(x.upper())
                self.name.append(x.lower())

    def getbirth(self):
        self.birth.append(self.ARGV["birth"])
        self.birth.append(self.ARGV["birth"][2:])

    def build(self):
        for x in self.name:
            for xx in self.birth:
                print x + xx


word = dictbuild()
print word.name
print word.birth
dictlist = """
123456789
a123456
123456
a123456789
1234567890
woaini1314
qq123456
abc123456
123456a
123456789a
147258369
zxcvbnm
987654321
12345678910
abc123
qq123456789
123456789.
7708801314520
woaini
5201314520
q123456
123456abc
1233211234567
123123123
123456.
0123456789
asd123456
aa123456
135792468
q123456789
abcd123456
12345678900
woaini520
woaini123
zxcvbnm123
1111111111111111
w123456
aini1314
abc123456789
111111
woaini521
qwertyuiop
1314520520
1234567891
qwe123456
asd123
000000
1472583690
1357924680
789456123
123456789abc
z123456
1234567899
aaa123456
abcd1234
www123456
123456789q
123abc
qwe123
w123456789
7894561230
123456qq
zxc123456
123456789qq
1111111111
111111111
0000000000000000
1234567891234567
qazwsxedc
qwerty
123456..
zxc123
asdfghjkl
0000000000
1234554321
123456q
123456aa
9876543210
110120119
qaz123456
qq5201314
123698745
5201314
000000000
as123456
123123
5841314520
z123456789
52013145201314
a123123
caonima
a5201314
wang123456
abcd123
123456789..
woaini1314520
123456asd
aa123456789
741852963
a12345678
"""