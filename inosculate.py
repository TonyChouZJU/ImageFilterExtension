#!/usr/bin/env python
#coding=utf-8
'''
Created on 2011-7-3

@author: Chine
'''

from PIL import Image
import numpy as np
import cv2

import matplotlib.pylab as plt
def inosculate(bg_img, fg_img, transparency):
    if fg_img.shape[-1] == 3:
        fg_img_png = cv2.cvtColor(fg_img.astype(np.uint8), cv2.COLOR_RGB2RGBA).astype(np.uint32)
    else:
        fg_img_png = fg_img

    if bg_img.shape[-1] == 3:
        bg_img_png = cv2.cvtColor(bg_img.astype(np.uint8), cv2.COLOR_RGB2RGBA).astype(np.uint32)
    else:
        bg_img_png = bg_img


    #plt.imshow(fg_img/255.)
    #plt.show()
    bg_height, bg_width, _ = bg_img.shape
    fg_height, fg_width, _ = fg_img.shape
    height = min(bg_height, fg_height)
    width = min(bg_width, fg_width)

    #bg_img_png = np.ones((bg_height, bg_width, 4)) * 255
    #fg_img_png = np.ones((fg_height, fg_width, 4)) * 255
    #bg_img_png[:, :, 0:3] = bg_img
    #fg_img_png[:, :, 0:3] = fg_img
    #bg_img_png = cv2.cvtColor(bg_img.astype(np.uint8), cv2.COLOR_RGB2RGBA).astype(np.uint32)
    #fg_img_png = cv2.cvtColor(fg_img.astype(np.uint8), cv2.COLOR_RGB2RGBA).astype(np.uint32)

    #dst_img = fg_img_png[:height, :width, :] * transparency / 255 + \
    #          bg_img_png[:height, :width, :] * (255 - transparency) / 255
    dst_img = (fg_img_png[:height, :width, :] - bg_img_png[:height, :width, :]) * transparency / 255 + \
              bg_img_png[:height, :width, :]

    return dst_img

'''
def inosculate(bg_img, fg_img, transparency):

    #@效果：图像融合
    #@param bg_img: 背景图像
    #@param fg_img: 前景图像
    #@param transparency: 前景透明度
    #@return: instance of Image

    
    # 宽和高取两个图像宽和高的最小值
    width, height = tuple(map(min, zip(bg_img.size, fg_img.size)))
    
    if fg_img.mode != "RGBA":
        fg_img = fg_img.convert("RGBA")
    
    dst_img = Image.new("RGBA", (width, height))
    
    bg_pix = bg_img.load()
    fg_pix = fg_img.load()
    
    dst_pix = dst_img.load()
    
    for w in xrange(width):
        for h in xrange(height):
            if fg_pix[w, h][3] != 0:
                # 如果前景像素点不透明
                
                # pixel = FG * transparency / 255 + BG * (255 - transparency) / 255
                dst_pix[w, h] = tuple(
                                      [int((f - b) * transparency / 255 + b) 
                                       for (b, f) in zip(bg_pix[w, h], fg_pix[w, h])]
                                      )
            
    return dst_img
'''

if __name__ == "__main__":
    import sys, os, time

    #bg_img_path = os.path.dirname(__file__) + os.sep.join(['./', 'images', 'guanlangaoshou.jpg'])
    #fg_img_path = os.path.dirname(__file__) + os.sep.join(['./', 'images', 'lam.jpg'])
    bg_img_path = os.path.join(os.path.dirname(__file__), 'images', 'guanlangaoshou.jpg')
    fg_img_path = os.path.join(os.path.dirname(__file__), 'images', 'lam.jpg')
    #bg_img_path = os.path.join(os.path.dirname(__file__), 'images', 'rgb.jpg')


    transparency = 128
    
    if len(sys.argv) == 2:
        transparency = int(sys.argv[1])
    elif len(sys.argv) == 3:
        bg_img_path = sys.argv[1]
        fg_img_path = sys.argv[2]
    elif len(sys.argv) == 4:
        bg_img_path = sys.argv[1]
        fg_img_path = sys.argv[2]
        transparency = int(sys.argv[3])

    start = time.time()
    
    #bg_img = Image.open(bg_img_path)
    #fg_img = Image.open(fg_img_path)
    bg_img = cv2.imread(bg_img_path)[:, :, (2, 1, 0)].astype(np.uint32)
    fg_img = cv2.imread(fg_img_path)[:, :, (2, 1, 0)].astype(np.uint32)
    img = inosculate(bg_img, fg_img, transparency)
    #img = inosculate(bg_img, bg_img, transparency)

    img_save = Image.fromarray(np.uint8(img))
    img_save.save(os.path.splitext(fg_img_path)[0]+'.inosculate_3.png', 'PNG')

    end = time.time()
    print 'It all spends %f seconds time' % (end-start)
