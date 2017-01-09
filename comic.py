#!/usr/bin/env python
#coding=utf-8
'''
Created on 2011-6-27

@author: Chine
'''

from PIL import Image
import numpy as np

def comic(img):

    img_array = np.array(img).astype(np.uint32)
    r = img_array[:, :, 0]
    g = img_array[:, :, 1]
    b = img_array[:, :, 2]
    img_array[:, :, 0] = abs(g - b + g + r) * r / 256
    img_array[:, :, 1] = abs(b - g + b + r) * r / 256
    img_array[:, :, 2] = abs(b - g + b + r) * r / 256
    for ind in range(3):
        r_idx, c_idx = np.where(img_array[:, :, ind] >= 255)
        img_array[r_idx, c_idx, ind] = 255
    img_new = cv2.cvtColor(np.uint8(img_array), cv2.COLOR_RGB2GRAY)
    #cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    #img_new = Image.fromarray(np.uint8(img_array))
    return img_new

'''


def comic(img):
    @效果：连环画
    @param img: instance of Image
    @return: instance of Image
    width, height = img.size

    if img.mode != 'RGB':
        img = img.convert('RGB')

    pix = img.load()

    img_array = np.array(img).astype(np.uint16)
    r = img_array[:, :, 0]
    g = img_array[:, :, 1]
    b = img_array[:, :, 2]
    img_array[:, :, 0] = abs(g - b + g + r) * r / 256
    img_array[:, :, 1] = abs(b - g + b + r) * r / 256
    img_array[:, :, 2] = abs(b - g + b + r) * r / 256
    for ind in range(3):
        r_idx, c_idx = np.where(img_array[:, :, ind] >= 255)
        img_array[r_idx, c_idx, ind] = 255

    for w in xrange(width):
        for h in xrange(height):
            r, g, b = pix[w, h]

            pix[w, h] = tuple(map(lambda i: min(255, i),
                                  [abs(g - b + g + r) * r / 256,
                                   abs(b - g + b + r) * r / 256,
                                   abs(b - g + b + r) * r / 256]))



    img_arr_pix = np.array(img)

    return img.convert('L')
'''

if __name__ == "__main__":
    import sys, os, time
    import matplotlib.pylab as plt
    import cv2

    path = os.path.dirname(__file__) + os.sep.join(['./', 'images', 'guanlangaoshou.jpg'])
    path = os.path.dirname(__file__) + os.sep.join(['./', 'images', 'lam.jpg'])
    path = '/home/zyb/cv/simultate_detection_examples/third_party/ImageFilterExtension/images/lam.jpg'
    
    if len(sys.argv) == 2:
        path  = sys.argv[1]

    start = time.time()
    
    #img = Image.open(path)
    img = cv2.imread(path)[:, :, (2, 1, 0)]
    img = comic(img)
    plt.rcParams['image.cmap'] = 'gray'
    plt.imshow(img)
    plt.show()
    img.save(os.path.splitext(path)[0]+'.comic2.jpg', 'JPEG')

    end = time.time()
    print 'It all spends %f seconds time' % (end-start)
