# -*- coding: utf-8 -*-

"""

Spyder Editor
This is a temporary script file.

"""

import requests

import time

import PIL.Image

def download_pic(pic_name):

    url = "http://www.jsds.gov.cn/index/fujia2.jsp"

    res = requests.get(url, stream=True)

    with open(pic_name,"wb") as f:

        for chunk in res.iter_content(chunk_size=1024):

            if chunk:

                f.write(chunk)

                f.flush()

        f.close()


#for i in range(100):

# pic_name = "D:\\pic\\" + str(i) + ".png"

# download_pic(pic_name)

#print res.text

#im = PIL.Image.open("‪D:\\动漫\\漫画\\东京食尸鬼\\Re1-99\\GhoulRe02\\TG_RE_2\\01.png")

#new_im = im.convert('L')

#new_im.show()