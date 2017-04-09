import os
import sys
from PIL import Image

def resize(folder, fileName, factor):
    filePath = os.path.join(folder, fileName)
    im = Image.open(filePath)
    # w, h  = im.size
    newIm = im.resize((int(factor), int(factor)))
    # i am saving a copy, you can overrider orginal, or save to other folder
    newIm.save(filePath)

def bulkResize(imageFolder, factor):
    imgExts = ["png", "bmp", "jpg"]
    for path, dirs, files in os.walk(imageFolder):
        for fileName in files:
            ext = fileName[-3:].lower()
            if ext not in imgExts:
                continue

            resize(path, fileName, factor)

if __name__ == "__main__":
    imageFolder=sys.argv[1] # first arg is path to image folder
    resizeFactor=int(sys.argv[2])# 2nd is resize in %
    bulkResize(imageFolder, resizeFactor)
