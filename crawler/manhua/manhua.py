# coding: utf-8
import re
import requests
import os


class downloadcomic(object):
    """docstring for downloadcomic"""
    def __init__(self, url):
        super(downloadcomic, self).__init__()
        self.url = url
        self.path = ""

    def run(self):
        for x in self.getchapters(self.url)[-1::-1]:
            self.getimgs(self.url + "/" + x)

    def downloadimg(self, path, imgbin):
        path = self.path + "/" + path
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        if not os.path.exists(path):
            f = open(path, "wb")
            f.write(imgbin)

    def getnextpage(self, content):
        try:
            nurl = re.search("<a href='index_(\d*).html' id=\"mhona\">下一页</a></div>", content).group(1)
        except:
            return
        return nurl

    def getimgs(self, url):
        res = requests.get(url)
        path = re.match("http://manhua.fzdm.com/39/(.*)", url).group(1)
        nextpage = self.getnextpage(res.content)
        while nextpage:
            print "Downloading chapt:%s picture:%s" % (path,nextpage)
            picurl = re.search("<img src=\"(.*)\" id=\"mhpic\"", res.content).group(1)
            respic = requests.get(picurl)
            self.downloadimg(path + "/" + nextpage + ".jpg",respic.content)
            res = requests.get(url + "/index_%s.html" % nextpage)
            nextpage = self.getnextpage(res.content)

    def getchapters(self, url):
        res = requests.get(url)
        self.path = re.search("<h2>.*alt=\"(.*)\" />", res.content).group(1).decode("utf-8")
        chapters = re.findall("<li class=\"pure-u-1-2 pure-u-lg-1-4\"><a href=\"(\d*)/\"", res.content)
        return chapters

a = downloadcomic("http://manhua.fzdm.com/39")
a.run()











# rindex = requests.get(url)
# rre = re.findall("<li class=\"pure-u-1-2 pure-u-lg-1-4\"><a href=\"(\d*)/\" title=\"(.*)\">", rindex.content)

# for x in rre:
#     pass
#     # print x[0],x[1]

# print 1,x[1]
# if not os.path.exists(x[1].decode("utf-8")):
#     os.mkdir(x[1].decode("utf-8"))