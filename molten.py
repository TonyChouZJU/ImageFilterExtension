#!/usr/bin/env python
#coding=utf-8
'''
Created on 2011-6-30

@author: Chine
'''

from PIL import Image
import numpy as np
import cv2
import matplotlib.pylab as plt

def molten(img):
    r = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    b = img[:, :, 2].copy()

    img[:, :, 0] = np.minimum(255, np.abs(r * 128 / (g + b + 1)))
    img[:, :, 1] = np.minimum(255, np.abs(g * 128 / (b + r + 1)))
    img[:, :, 2] = np.minimum(255, np.abs(b * 128 / (r + g + 1)))

    return img

'''
def molten(img):

    # @效果：熔铸
    # @param img: instance of Image
    # @return: instance of Image

    if img.mode != "RGB":
        img.convert("RGB")
        
    width, height = img.size
    pix = img.load()
    
    for w in xrange(width):
        for h in xrange(height):
            r, g, b = pix[w, h]
            
            pix[w, h] = min(255, int(abs(r * 128 / (g + b + 1)))), \
                        min(255, int(abs(g * 128 / (b + r + 1)))), \
                        min(255, int(abs(b * 128 / (r + g + 1))))
            
    return img
'''

if __name__ == "__main__":
    import sys, os, time

    #path = os.path.dirname(__file__) + os.sep.join(['./', 'images', 'lam.jpg'])
    path = os.path.join(os.path.dirname(__file__), 'images', 'lam.jpg')

    
    if len(sys.argv) == 2:
        path  = sys.argv[1]

    start = time.time()
    
    #img = Image.open(path)
    img = cv2.imread(path)[:, :, (2, 1, 0)].astype(np.uint32)
    img = molten(img)
    img_save = Image.fromarray(np.uint8(img))
    img_save.save(os.path.splitext(path)[0]+'.molten_2.jpg', 'JPEG')

    end = time.time()
    print 'It all spends %f seconds time' % (end-start)
