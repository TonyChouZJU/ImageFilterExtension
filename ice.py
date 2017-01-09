#!/usr/bin/env python
#coding=utf-8
'''
Created on 2011-6-30

@author: Chine
'''

from PIL import Image
import cv2
import numpy as np


def ice(img):
    r = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    b = img[:, :, 2].copy()
    img[:, :, 0] = np.minimum(255, np.abs(r - g - b) * 3 / 2)
    img[:, :, 1] = np.minimum(255, np.abs(g - b - r) * 3 / 2)
    img[:, :, 2] = np.minimum(255, np.abs(b - r - g) * 3 / 2)
    return img

'''
def ice(img):
    #@效果：冰冻
    #@param img: instance of Image
    #@return: instance of Image


    if img.mode != "RGB":
        img.convert("RGB")

    width, height = img.size
    pix = img.load()

    for w in xrange(width):
        for h in xrange(height):
            r, g, b = pix[w, h]

            pix[w, h] = min(255, int(abs(r - g - b) * 3 / 2)), \
                        min(255, int(abs(g - b - r) * 3 / 2)), \
                        min(255, int(abs(b - r - g) * 3 / 2))

    return img
'''

if __name__ == "__main__":
    import sys, os, time

    #path = os.path.dirname(__file__) + os.sep.join(['./', 'images', 'lam.jpg'])
    path = os.path.join(os.path.dirname(__file__), 'images', 'lam.jpg')

    
    if len(sys.argv) == 2:
        path  = sys.argv[1]

    start = time.time()
    abs
    #img = Image.open(path)
    # cannot use np.uint, as can be negative
    img = cv2.imread(path)[:, :, (2, 1, 0)].astype(np.int32)
    img = ice(img)
    img = Image.fromarray(np.uint8(img))
    img.save(os.path.splitext(path)[0]+'.ice_2.jpg', 'JPEG')

    end = time.time()
    print 'It all spends %f seconds time' % (end-start)
