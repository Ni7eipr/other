from PIL import Image

# imgs = Image.open("s.gif")
# for i in range(4):
#     imgs.seek(i)
#     imgs.save(str(i) + ".gif")

imgo = Image.new('RGB', (450, 450), (255, 255, 255))

p1 = (0,0,225,225)
img1 = Image.open("0.gif")
imgo1 = img1.crop(p1)

p2 = (225,0,450,450)
img2 = Image.open("1.gif")
imgo2 = img2.crop(p2)

p3 = (0,225,450,450)
img3 = Image.open("2.gif")
imgo3 = img3.crop(p3)

p4 = (225,225,450,450)
img4 = Image.open("3.gif")
imgo4 = img4.crop(p4)

imgo.paste(imgo1, p1)
imgo.paste(imgo2, p2)
imgo.paste(imgo3, p3)
imgo.paste(imgo4, p4)

imgo.save('o.jpg')