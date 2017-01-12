#!/usr/bin/env python
#coding=utf-8
'''
Created on 2011-6-30

@author: Chine
'''

from PIL import Image
import numpy as np
import cv2

def subtense(img):
    r = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    b = img[:, :, 2].copy()
    img[:, :, 0] = np.minimum(g * b / 255, 255)
    img[:, :, 1] = np.minimum(b * r / 255, 255)
    img[:, :, 2] = np.minimum(r * g / 255, 255)
    return img

'''
def subtense(img):

    @效果：对调
    @param img: instance of Image
    @return: instance of Image
    
    if img.mode != "RGB":
        img.convert("RGB")
    
    width, height = img.size
    pix = img.load()
    
    for w in xrange(width):
        for h in xrange(height):
            r, g, b = pix[w, h]
            
            pix[w, h] = min(255, int(g * b / 255)), \
                        min(255, int(b * r / 255)), \
                        min(255, int(r * g / 255))
                  
    return img
'''

if __name__ == "__main__":
    import sys, os, time

    path = os.path.dirname(__file__) + os.sep.join(['./', 'images', 'lam.jpg'])
    path = os.path.join(os.path.dirname(__file__), 'images', 'lam.jpg')

    if len(sys.argv) == 2:
        path  = sys.argv[1]

    start = time.time()

    #img = Image.open(path)
    img = cv2.imread(path)[:, :, (2, 1, 0)].astype(np.int32)
    img = subtense(img)
    img_save = Image.fromarray(np.uint8(img))
    img_save.save(os.path.splitext(path)[0]+'.subtense_2.jpg', 'JPEG')

    end = time.time()
    print 'It all spends %f seconds time' % (end-start)
