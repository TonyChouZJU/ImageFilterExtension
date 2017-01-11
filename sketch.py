#!/usr/bin/env python
#coding=utf-8
'''
Created on 2011-6-23

@author: Chine
'''
from PIL import Image
import numpy as np
import cv2

def sketch(img, threshold):

    threshold = min(max(0, threshold), 100)
    height, width, _ = img.shape
    #注意不恩给你使用 uint
    img = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.int32)
    img_src = img[:height-1, :width-1, ].copy()
    img_rb = img[1:, 1:, ].copy()
    r_idx, c_idx = np.where(abs(img_src-img_rb) > threshold)
    dst_img = np.ones(img_src.shape) * 255
    dst_img[r_idx, c_idx] = 0
    return dst_img

'''
def sketch(img, threshold):

    @效果：素描
    @param img: instance of Image
    @param threshold: 阈值，阈值越小，绘制的像素点越多，大小范围[0, 100]
    @return: instance of Image

    if threshold < 0: threshold = 0
    if threshold > 100: threshold = 100
    
    width, height = img.size
    img = img.convert('L') # convert to grayscale mode
    pix = img.load() # get pixel matrix

    # 主计算方法
    # 根据经验，对当前像素点的灰度值与右下角比较
    # 差值大于阈值则绘制
    for w in xrange(width):
        for h in xrange(height):
            if w == width-1 or h == height-1:
                continue
            
            src = pix[w, h] # 当前像素点
            dst = pix[w+1, h+1] # 右下角像素点

            diff = abs(src - dst)

            if diff >= threshold:
                pix[w, h] = 0
            else:
                pix[w, h] = 255

    return img
'''


if __name__ == "__main__":
    import sys, os, time

    path = os.path.dirname(__file__) + os.sep.join(['./', 'images', 'lam.jpg'])
    path = os.path.join(os.path.dirname(__file__), 'images', 'lam.jpg')

    threshold = 15
    
    if len(sys.argv) == 2:
        try:
            threshold = int(sys.argv[1])
        except ValueError:
            path  = sys.argv[1]
    elif len(sys.argv) == 3:
        path = sys.argv[1]
        threshold = int(sys.argv[2])
        
    start = time.time()
    
    #img = Image.open(path)
    img = cv2.imread(path)[:, :, (2, 1, 0)].astype(np.uint32)
    img = sketch(img, threshold)
    img_save = Image.fromarray(np.uint8(img))
    img_save.save(os.path.splitext(path)[0]+'.sketch_2.jpg', 'JPEG')
    
    end = time.time()
    print 'It all spends %f seconds time' % (end-start)
