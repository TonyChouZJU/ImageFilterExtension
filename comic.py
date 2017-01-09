#coding=utf-8
'''
Created on 2011-6-27

@author: Chine
'''

from PIL import Image
import numpy as np

def comic(img):

    img_array = np.array(img).astype(np.uint32)
    r = img_array[:, :, 0].copy()
    g = img_array[:, :, 1].copy()
    b = img_array[:, :, 2].copy()
    img_array[:, :, 0] = abs(g - b + g + r) * r / 256
    img_array[:, :, 1] = abs(b - g + b + r) * r / 256
    img_array[:, :, 2] = abs(b - g + b + r) * r / 256
    #for ind in range(3):
    #    r_idx, c_idx = np.where(img_array[:, :, ind] >= 255)
    #   img_array[r_idx, c_idx, ind] = 255
    img_array = np.minimum(img_array, 255)
    return img_array
'''
def comic_1(img):
    #@卡通
    #@param img: instance of Image
    #@return: instance of Image
    width, height = img.size

    if img.mode != 'RGB':
        img = img.convert('RGB')

    pix = img.load()

    for w in xrange(width):
        for h in xrange(height):
            r, g, b = pix[w, h]

            pix[w, h] = tuple(map(lambda i: min(255, i),
                                  [abs(g - b + g + r) * r / 256,
                                   abs(b - g + b + r) * r / 256,
                                   abs(b - g + b + r) * r / 256]))



    #img_arr_pix = np.array(img)

    #return img.convert('L')
    return np.array(img)
'''

if __name__ == "__main__":
    import sys, os, time
    import matplotlib.pylab as plt
    import cv2

    path = os.path.join(os.path.dirname(__file__), 'images', 'lam.jpg')
    print path
    if len(sys.argv) == 2:
        path = sys.argv[1]

    start = time.time()
    
    img = cv2.imread(path)[:, :, (2, 1, 0)]
    img = comic(img)

    plt.rcParams['image.cmap'] = 'gray'
    plt.imshow(img/255.)
    plt.show()
    img_save = Image.fromarray(np.uint8(img)).convert('L')
    img_save.save(os.path.splitext(path)[0]+'.comic3.jpg', 'JPEG')

    end = time.time()
    print 'It all spends %f seconds time' % (end-start)
