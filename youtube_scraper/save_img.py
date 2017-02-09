import requests
from PIL import Image
import os
import shutil

def saveFromFile(file):
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
                print(line)
                saveImage(dirName,count,line.strip())
                count += 1
def saveImage(dirName,name,url):
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
    newSize = (x/2,y/2)
    img = img.resize(newSize, Image.ANTIALIAS)
    img.save(imgName, optimize =True, quality=95)
    
fileName = "output.txt"
saveFromFile(fileName)
