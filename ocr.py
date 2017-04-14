# -*- coding: utf-8 -*-

"""

Spyder Editor
This is a temporary script file.

"""

import requests

import time

import PIL.Image
import PIL.ImageFilter
import PIL.ImageEnhance

def download_pic(pic_name):

    url = "http://www.jsds.gov.cn/index/fujia2.jsp"

    res = requests.get(url, stream=True)

    with open(pic_name,"wb") as f:

        for chunk in res.iter_content(chunk_size=1024):

            if chunk:

                f.write(chunk)

                f.flush()

        f.close()

def TransferImg(f_name):
    im = PIL.Image.open(f_name)
    im = im.convert('1')
    im = im.filter(PIL.ImageFilter.MedianFilter(1))
   # enhancer = PIL.ImageEnhance.Contrast(im)
   # im = enhancer.enhance(1)
    #im = im.convert('L')
    #im = im.convert('1')
    return im

def Segment(im):
    w = 9
    h = 16
    im_new = []
    for i in range(4):
        #im1 = im.crop((0,0,44,16))
        im1 = im.crop((2,0,44,16))
        im2 = im1.crop((w*i,0,w*(i+1),h))
        im_new.append(im2)
        #im_new.append(im1)
    return im_new

def CutPic(img):
    im = TransferImg(img)
    pics = Segment(im)
    i = 1;
    for pic in pics:
        pic.save('D:\\pic\\cut\%s.jpg'%str(i),'jpeg')
        i = i + 1
        
    
    
    
    



#for i in range(100):

# pic_name = "D:\\pic\\" + str(i) + ".png"

# download_pic(pic_name)

#print res.text

#im = PIL.Image.open("D:\\pic\\0.png")
#im.save('D:\\pic\\cut\%s.jpg'%'333','jpeg')
CutPic("D:\\pic\\0.png")
#new_im = im.convert('L')
#new_im = im.crop((0,0,100,100))
#new_im.show()