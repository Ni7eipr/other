# !/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image

filename = "ce.txt"

def create_img(x,y,ifname,ofname):
    image = Image.new("RGB",(x,y))
    file = open(ifname)

    for i in range(0,x):
        for j in range(0,y):
            line = file.readline()
            rgb = line.strip().split(",")
            image.putpixel((i,j),(int(rgb[0]),int(rgb[1]),int(rgb[2])))
    # im.show()
    image.save(ofname+'.jpg', 'jpeg');

r = []
rows = len(open(filename).readlines())
for i in range(2,rows):
    if rows%i == 0:
        r.append([i,rows/i])
for i in r:
    create_img(i[0],i[1],filename,str(i))