import cv2
import numpy as np
i1 = "../youtube_scraper/jaysunmah@gmail.com/0.jpg"
i2 = "../youtube_scraper/jaysunmah@gmail.com/1.jpg"
def add_img(i1,i2):
    img1 = cv2.imread(i1)
    img2 = cv2.imread(i2)
    # axis = 1 -> horizontal 0 -> vertical
    vis = np.concatenate((img1,img2),axis = 1)
    cv2.imwrite('out.png',vis)


def findImage((r,g,b)):

