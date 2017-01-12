#!/usr/bin/env python
#coding=utf-8
'''
Created on 2011-7-2

@author: Chine
'''

import math
from PIL import Image
import numpy as np
import cv2


def wave(img, degree=4):

    img = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_RGB2RGBA).astype(np.int32)
    height, width, _ = img.shape

    r_idx, c_idx = np.where(img[:, :, 0] < 256)
    #r_idx = r_idx.reshape(height, width)
    #c_idx = c_idx.reshape(height, width)

    x = degree * np.sin(np.pi * 2 * r_idx / 128.0) + c_idx
    y = degree * np.cos(np.pi * 2 * c_idx / 128.0) + r_idx

    x = x.astype(np.int32)
    y = y.astype(np.int32)

    x = np.minimum(np.maximum(x, 0), width - 1)
    y = np.minimum(np.maximum(y, 0), height - 1)

    #x = x.reshape(height, width)
    #y = y.reshape(height, width)

    #dst_img = np.zeros(img.shape)
    dst_img = img[y, x].reshape(height, width, 4)
    return dst_img

'''
def wave(img, degree):

    @效果：波浪，对图像进行波浪特效处理
    @param img: instance of Image
    @param degree: 表示波浪的大小[0, 32] 
    @return: instance of Image

    
    degree = min(max(0, degree), 32)
    
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    
    width, height = img.size    
    pix = img.load()
    
    dst_img = Image.new("RGBA", (width, height))
    dst_pix = dst_img.load()
    
    pi2 = math.pi * 2
    
    for w in xrange(width):
        for h in xrange(height):
            x = int(degree * math.sin(pi2 * h / 128.0)) + w
            y = int(degree * math.cos(pi2 * w / 128.0)) + h
            
            x = min(max(x, 0), width - 1)
            y = min(max(y, 0), height - 1)
            
            dst_pix[w, h] = pix[x, y]
    
    return dst_img
'''

if __name__ == "__main__":
    import sys, os, time

    path = os.path.dirname(__file__) + os.sep.join(['./', 'images', 'lam.jpg'])
    path = os.path.join(os.path.dirname(__file__), 'images', 'lam.jpg')

    degree = 4
    
    if len(sys.argv) == 2:
        try:
            degree = int(sys.argv[1])
        except ValueError:
            path  = sys.argv[1]
    elif len(sys.argv) == 3:
        path = sys.argv[1]
        degree = sys.argv[2]

    start = time.time()
    
    #img = Image.open(path)
    img = cv2.imread(path)[:, :, (2, 1, 0)].astype(np.uint32)
    img = wave(img, degree)
    img_save = Image.fromarray(np.uint8(img))
    img_save.save(os.path.splitext(path)[0]+'.wave_2.png', 'PNG')

    end = time.time()
    print 'It all spends %f seconds time' % (end-start)
