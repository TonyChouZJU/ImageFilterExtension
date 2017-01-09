#!/usr/bin/env python
#coding=utf-8
'''
Created on 2011-6-30

@author: Chine
'''

from PIL import Image
import numpy as np

'''
def darkness(img):

    #@效果：暗调
    #@param img: instance of Image
    #@return: instance of Image


    return img.point(lambda i: int(i ** 2 / 255))
'''

def darkness(img):
    img = img.astype(np.uint32)
    img_array = img**2 / 255
    for ind in range(3):
        r_idx, c_idx = np.where(img_array[:, :, ind] >= 255)
        img_array[r_idx, c_idx, ind] = 255
    return img_array

if __name__ == "__main__":
    import sys, os, time

    #path = os.path.dirname(__file__) + os.sep.join(['/', 'images', 'lam.jpg'])
    path = os.path.join( os.path.dirname(__file__), 'images', 'lam.jpg')
    
    if len(sys.argv) == 2:
        path = sys.argv[1]

    start = time.time()
    
    #img = Image.open(path)
    import cv2
    import matplotlib.pylab as plt
    img = cv2.imread(path)[:, :, (2, 1, 0)]
    img = darkness(img)

    #plt.imshow(img/255.0)
    #plt.show()
    img = Image.fromarray(np.uint8(img))
    img.save(os.path.splitext(path)[0]+'.darkness_2.jpg', 'JPEG')

    end = time.time()
    print 'It all spends %f seconds time' % (end-start)
