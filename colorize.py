#!/usr/bin/env python
#coding=utf-8
'''
Created on 2011-6-29

@author: Chine
'''

from PIL import Image
import numpy as np

def colorize(img, red=250, green=88, blue=244):
    '''
    @效果：颜色渲染
    @param img: instance of Image
    @return: instance of Image
    '''
    
    red = max(0, red)
    red = min(255, red) 
    green = max(0, green)
    green = min(255, green)
    blue = max(0, blue)
    blue = min(255, blue)
    
    gray_img = img.convert("L")

    gray_img_array = np.array(gray_img, dtype=np.int32)
    img_array = np.array(img, dtype=np.int32)
    img_array_new = np.zeros(img_array.shape)
    img_array_new[:, :, 0] = img_array[:, :, 0] * gray_img_array / 255
    img_array_new[:, :, 1] = img_array[:, :, 1] * gray_img_array / 255
    img_array_new[:, :, 2] = img_array[:, :, 2] * gray_img_array / 255
    img_new = Image.fromarray(np.uint8(img_array_new))
    return img_new

    '''
        width, height = img.size
    pix = img.load()
    gray_pix = gray_img.load()

    for w in xrange(width):
        for h in xrange(height):
            gray = gray_pix[w, h]
            r, g, b = pix[w, h]

            r = int(red * gray / 255)
            g = int(green * gray /255)
            b = int(blue * gray /255)

            pix[w, h] = r, g, b

    '''


if __name__ == "__main__":
    import sys, os, time
    import matplotlib.pylab as plt

    path = os.path.dirname(__file__) + os.sep.join(['./', 'images', 'lam.jpg'])
    red, green, blue = 250, 88, 244

    if len(sys.argv) == 2:
        path = sys.argv[1]
    elif len(sys.argv) == 5:
        path  = sys.argv[1]
        red = int(sys.argv[2])
        green = int(sys.argv[3])
        blue = int(sys.argv[4])
    elif len(sys.argv) == 4:
        red = int(sys.argv[1])
        green = int(sys.argv[2])
        blue = int(sys.argv[3])

    start = time.time()
    
    img = Image.open(path)
    img = colorize(img, red, green, blue)
    plt.imshow(img)
    plt.show()
    img.save(os.path.splitext(path)[0]+'.colorize2.jpg', 'JPEG')

    end = time.time()
    print 'It all spends %f seconds time' % (end-start)
