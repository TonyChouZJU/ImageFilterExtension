#!/usr/bin/env python
#coding=utf-8
'''
Created on 2011-7-8

@author: Chine
'''

import math
from PIL import Image
import numpy as np
import cv2

def glowing_edge(img):
    width, height, _ = img.shape
    bottom = img[1:, :-1, :]  # 下方像素点
    right = img[:-1, 1:, :]   # 右方像素点
    current = img[:-1, :-1, :] #当前像素点

    img_array = np.sqrt((current-bottom)**2 + (current-right)**2) * 2
    img_array = np.minimum(np.maximum(img_array, 0), 255).astype(np.uint8)
    #img_png = np.ones((width-1, height-1, 4)) * 255
    if img_array.shape[-1] == 3:
        img_png = cv2.cvtColor(img_array, cv2.COLOR_RGB2RGBA)
    else:
        img_png = img_array
    #img_png[:, :, 0:3] = img_array
    return img_png

'''
def glowing_edge(img):
    # @效果：照亮边缘
    #@param img: instance of Image
    # @return: instance of Image

    if img.mode != "RGBA":
        img = img.convert("RGBA")

    width, height = img.size
    pix = img.load()

    for w in xrange(width-1):
        for h in xrange(height-1):
            bottom = pix[w, h+1] # 下方像素点
            right = pix[w+1, h] # 右方像素点
            current = pix[w, h] # 当前像素点

            # 对r, g, b三个分量进行如下计算
            # 以r分量为例：int(2 * math.sqrt((r[current]-r[bottom])^2 + r[current]-r[right])^2))
            pixel = [int(math.sqrt((item[0] - item[1]) ** 2 + (item[0] - item[2]) ** 2) * 2)
                     for item in zip(current, bottom, right)[:3]]
            pixel.append(current[3])

            pix[w, h] = tuple([min(max(0, i), 255) for i in pixel]) # 限制各分量值介于[0, 255]

    return img
'''


if __name__ == "__main__":
    import sys, os, time

    # path = os.path.dirname(__file__) + os.sep.join(['./', 'images', 'lam.jpg'])
    path = os.path.join(os.path.dirname(__file__), 'images', 'lam.jpg')
    
    if len(sys.argv) == 2:
        path = sys.argv[1]

    start = time.time()

    #img = Image.open(path)
    img = cv2.imread(path)[:, :, (2, 1, 0)].astype(np.uint32)
    img = glowing_edge(img)
    img_save = Image.fromarray(np.uint8(img))
    img_save.save(os.path.splitext(path)[0]+'.glowing_edge_2.jpg', 'JPEG')

    end = time.time()
    print 'It all spends %f seconds time' % (end-start)
            
