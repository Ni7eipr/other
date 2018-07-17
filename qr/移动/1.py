from PIL import Image
import sys

W = 115
H = 115
try:
    img = Image.open("1.jpg")
    for i in range(H):
        for j in range(W):
            out = 'O' if sum(img.getpixel((j,i))) > 255 else ' '
            sys.stdout.write(str(out))
        print
except:
    pass
a = """
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OO                              OOOOOOOOOOOOO    OOOO     OOOOOOOOOOOO    OOO                               OOO
OO                              OOOOOOOOOOOOO    OOOO     OOOOOOOOOOOO    OOO                               OOO
OO                              OOOOOOOOOOOOO    OOOO     OOOOOOOOOOOO    OOO                               OOO
OO                              OOOOOOOOOOOOO    OOOO     OOOOOOOOOOOO    OOO                               OOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOO    OOOOO    OOOOOOOOOOOO         OOOOOOO     OOOOOOOOOOOOOOOOOOOOO     OOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOO    OOOOO    OOOOOOOOOOOO         OOOOOOO     OOOOOOOOOOOOOOOOOOOOO     OOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOO    OOOOO    OOOOOOOOOOOO         OOOOOOO     OOOOOOOOOOOOOOOOOOOOO     OOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOO    OOOOO    OOOOOOOOOOOO         OOOOOOO     OOOOOOOOOOOOOOOOOOOOO     OOO
OO    OOOO             OOOO     OOOOOOOOOOOOOOOOOOOOO     OOOOOOO     OOOOOOO     OOOO             OOOO     OOO
OO    OOOO             OOOO     OOOOOOOOOOOOOOOOOOOOO     OOOOOOO     OOOOOOO     OOOO             OOOO     OOO
OO    OOOO             OOOO     OOOOOOOOOOOOOOOOOOOOO     OOOOOOO     OOOOOOO     OOOO             OOOO     OOO
OO    OOOO             OOOO     OOOOOOOOOOOOOOOOOOOOO     OOOOOOO     OOOOOOO     OOOO             OOOO     OOO
OO    OOOO             OOOO     OOOO             OOOO        OOOOOOOOO    OOO     OOOO             OOOO     OOO
OO    OOOO             OOOO     OOOO             OOOO        OOOOOOOOO    OOO     OOOO             OOOO     OOO
OO    OOOO             OOOO     OOOO             OOOO        OOOOOOOOO    OOO     OOOO             OOOO     OOO
OO    OOOO             OOOO     OOOO             OOOO        OOOOOOOOO    OOO     OOOO             OOOO     OOO
OO    OOOO             OOOO     OOOO             OOOO        OOOOOOOOO    OOO     OOOO             OOOO     OOO
OO    OOOO             OOOO     OOOOOOOO     OOOOOOOOOOOOOOOO    OOOOOOOOOOOO     OOOO             OOOO     OOO
OO    OOOO             OOOO     OOOOOOOO     OOOOOOOOOOOOOOOO    OOOOOOOOOOOO     OOOO             OOOO     OOO
OO    OOOO             OOOO     OOOOOOOO     OOOOOOOOOOOOOOOO    OOOOOOOOOOOO     OOOO             OOOO     OOO
OO    OOOO             OOOO     OOOOOOOO     OOOOOOOOOOOOOOOO    OOOOOOOOOOOO     OOOO             OOOO     OOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOO         OOOO         OOOOOOO         OOO     OOOOOOOOOOOOOOOOOOOOO     OOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOO         OOOO         OOOOOOO         OOO     OOOOOOOOOOOOOOOOOOOOO     OOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOO         OOOO         OOOOOOO         OOO     OOOOOOOOOOOOOOOOOOOOO     OOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOO         OOOO         OOOOOOO         OOO     OOOOOOOOOOOOOOOOOOOOO     OOO
OO                              OOOO    OOOOO    OOOO     OOO    OOOOO    OOO                               OOO
OO                              OOOO    OOOOO    OOOO     OOO    OOOOO    OOO                               OOO
OO                              OOOO    OOOOO    OOOO     OOO    OOOOO    OOO                               OOO
OO                              OOOO    OOOOO    OOOO     OOO    OOOOO    OOO                               OOO
OO                              OOOO    OOOOO    OOOO     OOO    OOOOO    OOO                               OOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO             OOOOOOOO             OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO             OOOOOOOO             OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO             OOOOOOOO             OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO             OOOOOOOO             OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OO                     OOOO                  OOOO    OOOOO   OOOO     OOOO   OOOOO    OOOO     OOOO    OOOOOOOO
OO                     OOOO                  OOOO    OOOOO   OOOO     OOOO   OOOOO    OOOO     OOOO    OOOOOOOO
OO                     OOOO                  OOOO    OOOOO   OOOO     OOOO   OOOOO    OOOO     OOOO    OOOOOOOO
OO                     OOOO                  OOOO    OOOOO   OOOO     OOOO   OOOOO    OOOO     OOOO    OOOOOOOO
OOOOOOOOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO    OOOO     OOO    OOOOO       OOOOOOOOOOOOO             OOOOOOOO
OOOOOOOOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO    OOOO     OOO    OOOOO       OOOOOOOOOOOOO             OOOOOOOO
OOOOOOOOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO    OOOO     OOO    OOOOO       OOOOOOOOOOOOO             OOOOOOOO
OOOOOOOOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO    OOOO     OOO    OOOOO       OOOOOOOOOOOOO             OOOOOOOO
OOOOOOOOOO    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO    OOOO     OOO    OOOOO       OOOOOOOOOOOOO             OOOOOOOO
OOOOOOOOOO    OOOOO    OOOO         OOOOOOOOO    OOOOOOOOOOOOOOOO     OOOO            OOOOOOOOOOOOO         OOO
OOOOOOOOOO    OOOOO    OOOO         OOOOOOOOO    OOOOOOOOOOOOOOOO     OOOO            OOOOOOOOOOOOO         OOO
OOOOOOOOOO    OOOOO    OOOO         OOOOOOOOO    OOOOOOOOOOOOOOOO     OOOO            OOOOOOOOOOOOO         OOO
OOOOOOOOOO    OOOOO    OOOO         OOOOOOOOO    OOOOOOOOOOOOOOOO     OOOO            OOOOOOOOOOOOO         OOO
OOOOOOOOOOOOOO         OOOOOOOOO    OOOOOOOOOOOOOOOOO     OOOOOOO     OOOOOOOOOOOOOOOO    OOOOOOOOO         OOO
OOOOOOOOOOOOOO         OOOOOOOOO    OOOOOOOOOOOOOOOOO     OOOOOOO     OOOOOOOOOOOOOOOO    OOOOOOOOO         OOO
OOOOOOOOOOOOOO         OOOOOOOOO    OOOOOOOOOOOOOOOOO     OOOOOOO     OOOOOOOOOOOOOOOO    OOOOOOOOO         OOO
OOOOOOOOOOOOOO         OOOOOOOOO    OOOOOOOOOOOOOOOOO     OOOOOOO     OOOOOOOOOOOOOOOO    OOOOOOOOO         OOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOOOOOO         OOOO            OOOOO    OOO             OOOOO             OOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOOOOOO         OOOO            OOOOO    OOO             OOOOO             OOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOOOOOO         OOOO            OOOOO    OOO             OOOOO             OOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOOOOOO         OOOO            OOOOO    OOO             OOOOO             OOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOOOOOO         OOOO            OOOOO    OOO             OOOOO             OOO
OO            OOOOOOOOO    OOOOOOOOO    OOOOOOOOOOOOOOOOOO       OOOOOOOOO   OOOOOOOOOOOOO         OOOOOOOOOOOO
OO            OOOOOOOOO    OOOOOOOOO    OOOOOOOOOOOOOOOOOO       OOOOOOOOO   OOOOOOOOOOOOO         OOOOOOOOOOOO
OO            OOOOOOOOO    OOOOOOOOO    OOOOOOOOOOOOOOOOOO       OOOOOOOOO   OOOOOOOOOOOOO         OOOOOOOOOOOO
OO    OOOOOOOO     OOOOOOOO                               OOO             OOO     OOOO    OOOOO             OOO
OO    OOOOOOOO     OOOOOOOO                               OOO             OOO     OOOO    OOOOO             OOO
OO    OOOOOOOO     OOOOOOOO                               OOO             OOO     OOOO    OOOOO             OOO
OO    OOOOOOOO     OOOOOOOO                               OOO             OOO     OOOO    OOOOO             OOO
OO    OOOOOOOO             OOOOO                     OOOOOOOO         OOOO   OOOOOOOOOOOOOOOOOOOOOO    OOOOOOOO
OO    OOOOOOOO             OOOOO                     OOOOOOOO         OOOO   OOOOOOOOOOOOOOOOOOOOOO    OOOOOOOO
OO    OOOOOOOO             OOOOO                     OOOOOOOO         OOOO   OOOOOOOOOOOOOOOOOOOOOO    OOOOOOOO
OO    OOOOOOOO             OOOOO                     OOOOOOOO         OOOO   OOOOOOOOOOOOOOOOOOOOOO    OOOOOOOO
OO    OOOOOOOO             OOOOO                     OOOOOOOO         OOOO   OOOOOOOOOOOOOOOOOOOOOO    OOOOOOOO
OO    OOOO    OOOOOOOOO         OOOOOOOO     OOOO    OOOOOOOOOOOOOOOOO                             OOOOOOOOOOOO
OO    OOOO    OOOOOOOOO         OOOOOOOO     OOOO    OOOOOOOOOOOOOOOOO                             OOOOOOOOOOOO
OO    OOOO    OOOOOOOOO         OOOOOOOO     OOOO    OOOOOOOOOOOOOOOOO                             OOOOOOOOOOOO
OO    OOOO    OOOOOOOOO         OOOOOOOO     OOOO    OOOOOOOOOOOOOOOOO                             OOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO    OOOOO    OOOO        OOOOOOOOO    OOOOOOOOOOOO    OOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO    OOOOO    OOOO        OOOOOOOOO    OOOOOOOOOOOO    OOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO    OOOOO    OOOO        OOOOOOOOO    OOOOOOOOOOOO    OOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO    OOOOO    OOOO        OOOOOOOOO    OOOOOOOOOOOO    OOOOOOOOOOOOOOOOOOOOO
OO                              OOOO         OOOOOOOOOOOOOOOO    OOOOO    OOO     OOOO    OOOOOOOOO         OOO
OO                              OOOO         OOOOOOOOOOOOOOOO    OOOOO    OOO     OOOO    OOOOOOOOO         OOO
OO                              OOOO         OOOOOOOOOOOOOOOO    OOOOO    OOO     OOOO    OOOOOOOOO         OOO
OO                              OOOO         OOOOOOOOOOOOOOOO    OOOOO    OOO     OOOO    OOOOOOOOO         OOO
OO                              OOOO         OOOOOOOOOOOOOOOO    OOOOO    OOO     OOOO    OOOOOOOOO         OOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOOOOOOOOOOOOOOOOOOO     OOO             OOOOOOOOOOOO    OOOOOOOOO    OOOOOOOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOOOOOOOOOOOOOOOOOOO     OOO             OOOOOOOOOOOO    OOOOOOOOO    OOOOOOOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOOOOOOOOOOOOOOOOOOO     OOO             OOOOOOOOOOOO    OOOOOOOOO    OOOOOOOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOOOOOOOOOOOOOOOOOOO     OOO             OOOOOOOOOOOO    OOOOOOOOO    OOOOOOOO
OO    OOOO             OOOO     OOOO         OOOOOOOO     OOOOOOO                                           OOO
OO    OOOO             OOOO     OOOO         OOOOOOOO     OOOOOOO                                           OOO
OO    OOOO             OOOO     OOOO         OOOOOOOO     OOOOOOO                                           OOO
OO    OOOO             OOOO     OOOO         OOOOOOOO     OOOOOOO                                           OOO
OO    OOOO             OOOO     OOOO    OOOOO    OOOOOOOOO   OOOOOOOOOOOOOOOO     OOOO         OOOO         OOO
OO    OOOO             OOOO     OOOO    OOOOO    OOOOOOOOO   OOOOOOOOOOOOOOOO     OOOO         OOOO         OOO
OO    OOOO             OOOO     OOOO    OOOOO    OOOOOOOOO   OOOOOOOOOOOOOOOO     OOOO         OOOO         OOO
OO    OOOO             OOOO     OOOO    OOOOO    OOOOOOOOO   OOOOOOOOOOOOOOOO     OOOO         OOOO         OOO
OO    OOOO             OOOO     OOOO    OOOOO    OOOOOOOOO   OOOOOOOOOOOOOOOO     OOOO         OOOO         OOO
OO    OOOO             OOOO     OOOO                         OOOOOOOOOOOOO   OOOOO    OOOOOOOOOOOOOOOOO     OOO
OO    OOOO             OOOO     OOOO                         OOOOOOOOOOOOO   OOOOO    OOOOOOOOOOOOOOOOO     OOO
OO    OOOO             OOOO     OOOO                         OOOOOOOOOOOOO   OOOOO    OOOOOOOOOOOOOOOOO     OOO
OO    OOOO             OOOO     OOOO                         OOOOOOOOOOOOO   OOOOO    OOOOOOOOOOOOOOOOO     OOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOO                 OOOOOOOOOOOO                     OOOO     OOOOOOOO     OOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOO                 OOOOOOOOOOOO                     OOOO     OOOOOOOO     OOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOO                 OOOOOOOOOOOO                     OOOO     OOOOOOOO     OOO
OO    OOOOOOOOOOOOOOOOOOOOO     OOOO                 OOOOOOOOOOOO                     OOOO     OOOOOOOO     OOO
OO                              OOOO    OOOOOOOOO         OOOOOOOOOOOOOOOO            OOOOOOOOO             OOO
OO                              OOOO    OOOOOOOOO         OOOOOOOOOOOOOOOO            OOOOOOOOO             OOO
OO                              OOOO    OOOOOOOOO         OOOOOOOOOOOOOOOO            OOOOOOOOO             OOO
OO                              OOOO    OOOOOOOOO         OOOOOOOOOOOOOOOO            OOOOOOOOO             OOO
OO                              OOOO    OOOOOOOOO         OOOOOOOOOOOOOOOO            OOOOOOOOO             OOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
""".strip()

imgo = Image.new('RGB', (W, H), (255, 255, 255))
out = {}
for i, ii in enumerate(a.splitlines()):
    out[i] = {}
    for j, jj in enumerate(ii):
        out[i][j] = jj
        if jj == ' ':
            imgo.putpixel((j,i), (0, 0, 0))
        else:
            imgo.putpixel((j,i), (255, 255, 255))
imgo.save('out.jpg')
