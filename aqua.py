#!/usr/bin/env python
#coding=utf-8
'''
Created on 2011-6-29

@author: Chine
'''

from PIL import Image
import numpy as np
import cv2


def aqua(img):

    r = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    b = img[:, :, 2].copy()

    img[:, :, 0] = np.minimum(np.maximum((g - b) ** 2 / 128, 0), 255)
    img[:, :, 1] = np.minimum(np.maximum((r - b) ** 2 / 128, 0), 255)
    img[:, :, 2] = np.minimum(np.maximum((r - g) ** 2 / 128, 0), 255)

    img = np.minimum(np.maximum(img, 0), 255)
    return img


'''
def aqua(img):

    @效果：碧绿
    @param img: instance of Image
    @return: instance of Image

    
    if img.mode != "RGB":
        img.convert("RGB")
    
    width, height = img.size
    pix = img.load()
    
    for w in xrange(width):
        for h in xrange(height):
            r, g, b = pix[w, h]
            
            pix[w, h] = min(255, int((g - b) ** 2 / 128)), \
                        min(255, int((r - b) ** 2 / 128)), \
                        min(255, int((r - g) ** 2 / 128))
            
    return img
'''

if __name__ == "__main__":
    import sys, os, time

    path = os.path.dirname(__file__) + os.sep.join(['./', 'images', 'lam.jpg'])
    path = os.path.join(os.path.dirname(__file__), 'images', 'lam.jpg')

    
    if len(sys.argv) == 2:
        path  = sys.argv[1]

    start = time.time()

    img = cv2.imread(path)[:, :, (2, 1, 0)].astype(np.uint32)
    #img = Image.open(path)
    img = aqua(img)
    img_save = Image.fromarray(np.uint8(img))
    img_save.save(os.path.splitext(path)[0]+'.aqua_2.jpg', 'JPEG')

    end = time.time()
    print 'It all spends %f seconds time' % (end-start)
