#!/usr/bin/env python
#coding=utf-8
'''
Created on 2011-7-6

@author: Chine
'''

import random
from PIL import Image
import numpy as np
import cv2

'''
def diffuse(img, degree):
    #@效果：扩散
    #@param img: instance of Image
    #@param degree: 扩散范围，大小[1, 32]
    #@return: instance of Image

    degree = min(max(1, degree), 32)

    width, height = img.size

    dst_img = Image.new(img.mode, (width, height))

    pix = img.load()
    dst_pix = dst_img.load()

    for w in xrange(width):
        for h in xrange(height):
            # 随机获取当前像素周围一随机点
            x = w + random.randint(-degree, degree)
            y = h + random.randint(-degree, degree)

            # 限制范围
            x = min(max(x, 0), width - 1)
            y = min(max(y, 0), height - 1)

            dst_pix[w, h] = pix[x, y]

    return dst_img
'''

def diffuse(img, degree):
    height, width = img.shape[0:2]
    r_idx_array, c_idx_array = np.where(img[:, :, 0] < 256)
    r_idx_array = r_idx_array.reshape(height, width)
    c_idx_array = c_idx_array.reshape(height, width)
    rdm_array = np.random.randint(-degree, degree, size=(2, height, width))
    r_idx_array += rdm_array[0]
    c_idx_array += rdm_array[1]
    new_r_idx_array = np.minimum(np.maximum(r_idx_array, 0), height - 1)
    new_c_idx_array = np.minimum(np.maximum(c_idx_array, 0), width - 1)
    new_r_idx_array = new_r_idx_array.flatten()
    new_c_idx_array = new_c_idx_array.flatten()
    img = img[new_r_idx_array, new_c_idx_array].reshape(height, width, 3)
    return img


if __name__ == "__main__":
    import sys, os, time

    #path = os.path.dirname(__file__) + os.sep.join(['./', 'images', 'lam.jpg'])
    path = os.path.join( os.path.dirname(__file__), 'images', 'lam.jpg')
    #degree = 16
    degree = 2 
    
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
    import matplotlib.pylab as plt

    img = cv2.imread(path)[:, :, (2, 1, 0)].astype(np.uint32)
    img = diffuse(img, degree)
    img = Image.fromarray(np.uint8(img))
    img.save(os.path.splitext(path)[0]+'.diffuse_3.jpg', 'JPEG')

    end = time.time()
    print 'It all spends %f seconds time' % (end-start)
