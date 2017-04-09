import cv2
import numpy as np
import os
import sys
def add_img(dir):
    output = dir + '/' + dir +'_parsed_stitched.png'
    files = os.listdir(dir + "/parsed")
    prev = dir + "/parsed/" + files[0]
    for i in range(1,len(files)):
        current_f = dir + "/parsed/" + files[i]
        img1 = cv2.imread(prev)
        img2 = cv2.imread(current_f)
        vis = np.concatenate((img1,img2),axis = 0)
        cv2.imwrite(output,vis)
        prev = output

add_img(sys.argv[1])


