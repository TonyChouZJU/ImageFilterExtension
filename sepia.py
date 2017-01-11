#!/usr/bin/env python
#coding=utf-8
'''
Created on 2011-6-24

@author: Chine
'''
from PIL import Image
import numpy as np
import cv2


def sepia(img):
    r = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    b = img[:, :, 2].copy()
    bit_num = 16
    img[:, :, 0] = (25756 * r + 50397 * g + 12386 * b) >> bit_num
    img[:, :, 1] = (22872 * r + 44958 * g + 11010 * b) >> bit_num
    img[:, :, 2] = (17826 * r + 34996 * g + 8585 * b) >> bit_num
    img = np.minimum(np.maximum(img, 0), 255)
    return img
'''
def sepia(img):

    # @效果：老照片（深褐色）
    # @param img: instance of Image
    # @return: instance of Image

    
    # 获得图片的宽、高
    width, height = img.size

    pix = img.load()

    for w in xrange(width):
        for h in xrange(height):
            cr_p = pix[w, h] # 当前像素点

            R = (25756 * cr_p[0] + 50397 * cr_p[1] + 12386 * cr_p[2]) >> 16
            G = (22872 * cr_p[0] + 44958 * cr_p[1] + 11010 * cr_p[2]) >> 16;
            B = (17826 * cr_p[0] + 34996 * cr_p[1] + 8585 * cr_p[2]) >> 16;

            if R < 0: R = 0
            if R > 255: R = 255

            if G < 0: G = 0
            if G > 255: G = 255

            if B < 0: B = 0
            if B > 255: B = 255

            pix[w, h] = R, G, B

    return img
'''

if __name__ == "__main__":
    import sys, os, time
    
    path = os.path.dirname(__file__) + os.sep.join(['./', 'images', 'lam.jpg'])
    path = os.path.join(os.path.dirname(__file__), 'images', 'lam.jpg')

    if len(sys.argv) > 1:
        path = sys.argv[1]

    start = time.time()
    
    #img = Image.open(path)
    img = cv2.imread(path)[:, :, (2, 1, 0)].astype(np.int32)
    img = sepia(img)
    img_save = Image.fromarray(np.uint8(img))
    img_save.save(os.path.splitext(path)[0]+'.sepia_2.jpg', 'JPEG')

    end = time.time()
    print 'It all spends %f seconds time' % (end-start)
