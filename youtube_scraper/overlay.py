import cv2
import numpy as np
import os
def add_img(dir):
    output = dir + '/' + dir +'_parsed_stitched.png'
    files = oslistdir(dir)
    prev = files[0]
    for i in range(1,len(files)):
        current_f = files[i]
        img1 = cv2.imread(prev)
        img2 = cv2.imread(current_f)
        vis = np.concatenate((img1,img2),axis = 0)
        cv2.imwrite(output,vis)
        prev = output

add_img("jaysunmah@gmail.com")


