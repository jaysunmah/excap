import requests
from PIL import Image



def saveFromFile(file):
    with open(file,'r') as f:
        count = 0
        for line in f:
            print(line)
            if "i.ytimg.com" in line and line.startswith("http"):
                saveImage(count,line.strip())
                count += 1
def saveImage(name,url):
    imgName = "newsave/" + str(name) + ".jpg"
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
    newSize = (x/4,y/4)
    img = img.resize(newSize, Image.ANTIALIAS)
    img.save(imgName, optimize =True, quality=95)
    
fileName = "output.txt"
saveFromFile(fileName)
