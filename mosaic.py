#!/usr/bin/env python
#coding=utf-8
'''
Created on 2011-7-8

@author: Chine
'''

from PIL import Image
import numpy as np
import cv2
import matplotlib.pylab as plt
from PIL import ImageFilter


def mosaic(img, block_size):
    block_size = min(max(block_size, 1), 32)
    if img.shape[-1] == 3:
        img = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_RGB2RGBA).astype(np.uint32)

    block_size = min(max(block_size, 1), 32)
    size = block_size ** 2

    dst_img = np.ones(img.shape) * 255

    height, width, _ = img.shape
    #for w in xrange(0, width, block_size):
    for h in xrange(0, height, block_size):
        #for h in xrange(0, height, block_size):
        for w in xrange(0, width, block_size):
            #print w, h
            #print img[h:min(h+block_size, height), w:min(w+block_size, width), ].shape
            #print np.mean(img[h:min(h+block_size, height), w:min(w+block_size, width), ])
            r_ave, g_ave, b_ave, _ = \
                np.mean(img[h:min(h+block_size, height), w:min(w+block_size, width), ], axis=(0, 1))
            #for i in xrange(w, min(w + block_size, width)):
            for i in xrange(h, min(h + block_size, height)):
                #for j in xrange(h, min(h + block_size, height)):
                for j in xrange(w, min(w + block_size, width)):
                    dst_img[i, j, :] = r_ave, g_ave, b_ave, img[h, w, 3]
    return dst_img

'''
def mosaic(img, block_size):

    # @效果：马赛克
    # @param img: instance of Image
    # @param block_size: 方块大小，范围[1, 32]
    # @return: instance of Image

    
    block_size = min(max(block_size, 1), 32)
    
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    
    width, height = img.size
    pix = img.load()
    
    dst_img = Image.new("RGBA", (width, height))
    dst_pix = dst_img.load()
    
    for w in xrange(0, width, block_size):
        for h in xrange(0, height, block_size):
            r_sum, g_sum, b_sum = 0, 0, 0
            size = block_size ** 2
            
            for i in xrange(w, min(w+block_size, width)):
                for j in xrange(h, min(h+block_size, height)):
                    r_sum += pix[i, j][0]
                    g_sum += pix[i, j][1]
                    b_sum += pix[i, j][2]
                    
            r_ave = int(r_sum / size)
            g_ave = int(g_sum / size)
            b_ave = int(b_sum / size)
            
            for i in xrange(w, min(w+block_size, width)):
                for j in xrange(h, min(h+block_size, height)):
                    dst_pix[i, j] = r_ave, g_ave, b_ave, pix[w, h][3]
                    
    return dst_img
'''

if __name__ == "__main__":
    import sys, os, time

    #path = os.path.dirname(__file__) + os.sep.join(['./', 'images', 'lam.jpg'])
    path = os.path.join(os.path.dirname(__file__), 'images', 'lam.jpg')

    block_size = 5
    
    if len(sys.argv) == 2:
        try:
            block_size = int(sys.argv[1])
        except ValueError:
            path  = sys.argv[1]
    elif len(sys.argv) == 3:
        path = sys.argv[1]
        block_size = int(sys.argv[2])

    start = time.time()
    
    #img = Image.open(path)
    img = cv2.imread(path)[:, :, (2, 1, 0)].astype(np.uint32)
    img = mosaic(img, block_size)
    img_save = Image.fromarray(np.uint8(img))
    img_save.save(os.path.splitext(path)[0]+'.mosaic_2.png', 'PNG')

    end = time.time()
    print 'It all spends %f seconds time' % (end-start)
