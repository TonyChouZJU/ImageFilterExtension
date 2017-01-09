#!/usr/bin/env python
#coding=utf-8
'''
Created on 2011-6-29

@author: Chine
'''

from PIL import Image
import numpy as np
import cv2

def colorize(img, red=250, green=88, blue=244):
    '''
    @效果：颜色渲染
    @param img: instance of Image
    @return: instance of Image
    '''

    red = min(max(0, red), 255)
    green = min(max(0, green), 255)
    blue = min(max(0, blue), 255)

    img_array = np.array(img).astype(np.int32)

    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray_img_array = np.tile(gray_img[:, :, np.newaxis], (1, 1, 3))
    img_array_new = img_array * gray_img_array / 255
    return img_array_new

if __name__ == "__main__":
    import sys, os, time
    import matplotlib.pylab as plt

    path = os.path.join(os.path.dirname(__file__), 'images', 'lam.jpg')
    red, green, blue = 250, 88, 244

    if len(sys.argv) == 2:
        path = sys.argv[1]
    elif len(sys.argv) == 5:
        path = sys.argv[1]
        red = int(sys.argv[2])
        green = int(sys.argv[3])
        blue = int(sys.argv[4])
    elif len(sys.argv) == 4:
        red = int(sys.argv[1])
        green = int(sys.argv[2])
        blue = int(sys.argv[3])

    start = time.time()

    print path
    img = cv2.imread(path)[:, :, (2, 1, 0)]
    img = colorize(img, red, green, blue)
    plt.imshow(img/255.)
    plt.show()
    img_save = Image.fromarray(np.uint8(img))
    img_save.save(os.path.splitext(path)[0]+'.colorize2.jpg', 'JPEG')

    end = time.time()
    print 'It all spends %f seconds time' % (end-start)
