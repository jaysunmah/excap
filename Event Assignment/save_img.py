import requests
from PIL import Image
import os
import shutil
import threading
import sys

def saveFromFile(dirName):
    thread_list = []
    with open("output.txt",'r') as f:
        count = 0
        lines = f.readlines()
        try:
            shutil.rmtree(dirName)
            os.mkdir(dirName)
        except:
            os.mkdir(dirName)

        for i in range(1,len(lines)):
            line = lines[i]
            print(line.strip())
            saveImage(dirName, count, line.strip())
            count += 1

            # if True:
                # t = threading.Thread(target=saveImage, args=(dirName,count,line.strip()))
                # t.daemon = True
                # thread_list.append(t)
                # count += 1
        # for thread in thread_list:
            # thread.start()
        # for thread in thread_list:
            # thread.join()
        print("done")

def saveImage(dirName,name,url):
    try:
        imgName = dirName + "/" + str(name) + ".jpg"
        with open(imgName,'wb') as handle:
            response = requests.get(url,stream = True)
            if not response.ok:
                print response
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
        img = Image.open(imgName)
        imgSize = img.size
        (x,y) = imgSize
        newSize = (x,y)
        img = img.resize(newSize, Image.ANTIALIAS)
        img.save(imgName, optimize =True, quality=95)
    except:
        print("unable to save %s" %(imgName))
        command = "rm %s" % (imgName)
        os.system(command)


name = sys.argv[1]

saveFromFile(name)
