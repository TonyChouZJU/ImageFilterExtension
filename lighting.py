#!/usr/bin/env python
#coding=utf-8
'''
Created on 2011-6-27

@author: Chine
'''

import math
from PIL import Image
import cv2
import numpy as np

def lighting(img, power=20, center=None):
    height, width, _ = img.shape
    if center is None:
        center = width / 2, height / 2

    radius = int(math.sqrt(center[0] ** 2 + center[1] ** 2))  # 半径
    r_idx_array, c_idx_array = np.where(img[:, :, 0] < 256)
    r_idx_array = r_idx_array.reshape(height, width)
    c_idx_array = c_idx_array.reshape(height, width)
    distance = np.sqrt((r_idx_array-center[0]) ** 2 + (c_idx_array - center[1]) ** 2)
    r_ok, c_ok = np.where(distance < radius)

    brightness = power * (radius - distance) / radius

    brightness = brightness[:, :, np.newaxis]

    brightness = np.repeat(brightness, 3, axis=2)
    img[r_ok, c_ok, :] = np.minimum(img[r_ok, c_ok, :] + brightness[r_ok, c_ok, :], 255)
    return img

'''
def lighting(img, power, center=None):
    #@效果：灯光
    #@param img: instance of Image
    #@param power: 光照强度
    #@param center: 光源坐标(x, y)，默认在图片中心
    #@return: instance of Image
    if img.mode != "RGB":
        img = img.convert("RGB")

    width, height = img.size

    if center is None:
        center = width / 2, height / 2

    radius = int(math.sqrt(center[0] ** 2 + center[1] ** 2)) # 半径

    pix = img.load()

    for w in xrange(width):
        for h in xrange(height):
            # 当前像素点到光源中心距离
            distance = int(math.sqrt((w - center[0]) ** 2 + (h - center[1]) ** 2))

            if distance < radius:
                brightness = power * (radius - distance) / radius
                # 光亮值和到光源中心的距离成反比

                r, g, b = pix[w, h]
                r = min(r + brightness, 255)
                g = min(g + brightness, 255)
                b = min(b + brightness, 255)
                pix[w, h] = r, g, b

    return img
'''

if __name__ == "__main__":
    import sys, os, time

    path = os.path.dirname(__file__) + os.sep.join(['./', 'images', 'lam.jpg'])
    path = os.path.join(os.path.dirname(__file__), 'images', 'lam.jpg')

    power = 20
    center = None
    
    if len(sys.argv) == 2:
        try:
            power = int(sys.argv[1])
        except ValueError:
            path = sys.argv[1]
    elif len(sys.argv) >= 3:
        path = sys.argv[1]
        power = int(sys.argv[2])
    if len(sys.argv) == 4:
        center = tuple(sys.argv[3])

    start = time.time()
    
    #img = Image.open(path)
    img = cv2.imread(path)[:, :, (2, 1, 0)].astype(np.uint32)
    img = lighting(img, power, center)
    img = Image.fromarray(np.uint8(img))

    img.save(os.path.splitext(path)[0]+'.lighting_2.jpg', 'JPEG')

    end = time.time()
    print 'It all spends %f seconds time' % (end-start) 
