#!/usr/bin/env python
#coding=utf-8
'''
Created on 2011-7-3

@author: Chine
'''

import math
from PIL import Image
import numpy as np
import cv2

from inosculate import inosculate

def moire_fringe(img, degree):
    degree = min(max(degree, 1), 16)
    height, width, _ = img.shape
    center = width / 2, height / 2

    r_idx_array, c_idx_array = np.where(img[:, :, 0] < 256)
    r_idx_array = r_idx_array.reshape(height, width)
    c_idx_array = c_idx_array.reshape(height, width)

    offset_x = center[0] - r_idx_array
    offset_y = center[1] - c_idx_array
    radian = np.arctan2(offset_y, offset_x)
    radius = np.sqrt(offset_x ** 2 + offset_y ** 2)

    x = radius * np.cos(radian + degree * radius)
    y = radius * np.sin(radian + degree * radius)

    x = np.minimum(np.maximum(x.astype(np.uint32), 0), width - 1)
    y = np.minimum(np.maximum(y.astype(np.uint32), 0), height - 1)

    dst_img = img[y, x, :]

    return inosculate(img, dst_img, 128)  # 对生成的图像和源图像进行色彩混合

'''
def moire_fringe(img, degree):

    #@效果：摩尔纹，对图像进行摩尔纹特效处理
    #@param img: instance of Image
    #@param degree: 强度，大小范围[1, 16]
    #@return: instance of Image

    degree = min(max(degree, 1), 16)
    
    if img.mode != "RGBA":
        img = img.convert("RGBA")
        
    width, height = img.size
    center = width / 2, height / 2 # 中心点
    pix = img.load()
    
    dst_img = Image.new("RGBA", (width, height))
    dst_pix = dst_img.load()
    
    for w in xrange(width):
        for h in xrange(height):
            offset_x = w - center[0]
            offset_y = h - center[1]
            
            radian = math.atan2(offset_y, offset_x) # 角度
            radius = math.sqrt(offset_x ** 2 + offset_y ** 2) # 半径
            
            x = int(radius * math.cos(radian + degree * radius))
            y = int(radius * math.sin(radian + degree * radius))
            
            x = min(max(x, 0), width - 1)
            y = min(max(y, 0), height - 1)
            
            dst_pix[w, h] = pix[x, y]
            
    return inosculate(img, dst_img, 128) # 对生成的图像和源图像进行色彩混合
'''

if __name__ == "__main__":
    import sys, os, time

    #path = os.path.dirname(__file__) + os.sep.join(['./', 'images', 'lam.jpg'])
    path = os.path.join(os.path.dirname(__file__), 'images', 'lam.jpg')

    degree = 6
    
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
    img = moire_fringe(img, degree)
    img_save = Image.fromarray(np.uint8(img))
    img_save.save(os.path.splitext(path)[0]+'.moire_fringe_2.png', 'PNG')

    end = time.time()
    print 'It all spends %f seconds time' % (end-start)
