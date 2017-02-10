import requests
from PIL import Image
import os
import shutil
import threading

def saveFromFile(file):
    thread_list = []
    with open(file,'r') as f:
        count = 0
        lines = f.readlines()
        dirName = lines[0].strip()
        try:
            shutil.rmtree(dirName)
            os.mkdir(dirName)
        except:
            os.mkdir(dirName)

        for i in range(1,len(lines)):
            line = lines[i]
            if "i.ytimg.com" in line and line.startswith("http"):
                t = threading.Thread(target=saveImage, args=(dirName,count,line.strip()))
                t.daemon = True
                thread_list.append(t)
                count += 1
        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()
        print("done")

def saveImage(dirName,name,url):
    print(url)
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
    newSize = (2 * x,2 * y)
    img = img.resize(newSize, Image.ANTIALIAS)
    img.save(imgName, optimize =True, quality=95)
    
fileName = "output.txt"
saveFromFile(fileName)
