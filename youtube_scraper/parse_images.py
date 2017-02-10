import os
import shutil
import cv2
import sys


def openImagesFromFolder(refImage, fileNames, count):
    rows, cols, channels = refImage.shape
    resultArray = []
    for r in xrange(rows):
        row = []
        for c in xrange(cols):
            row.append([0, 0, 0])
        resultArray.append(row)

    imageCount = 0
    # for filename in os.listdir(folderName)[1:]:
    for filename in fileNames:
        imageCount += 1
        imgName = folderName + "/" + filename
        image = cv2.imread(imgName)
        for i in xrange(rows):
            for j in xrange(cols):
                resultArray[i][j][0] += image[i, j][0]
                resultArray[i][j][1] += image[i, j][1]
                resultArray[i][j][2] += image[i, j][2]

    newImage = refImage.copy()
    rows, cols, channels = newImage.shape

    for r in xrange(rows):
        for c in xrange(cols):
            newImage[r,c][0] = resultArray[r][c][0] / imageCount
            newImage[r,c][1] = resultArray[r][c][1] / imageCount
            newImage[r,c][2] = resultArray[r][c][2] / imageCount


    cv2.imwrite(str(count) + "_parsed.jpg", newImage)
    print("done")


def openImages(folderName):
    blockCount = 10
    currentCount = 0
    fileNames = []

    refImageName = os.listdir(folderName)[3]
    refImage = cv2.imread(folderName + "/" + refImageName)
    totalCount = 0

    for filename in os.listdir(folderName):
        currentCount += 1
        fileNames.append(filename)
        if (currentCount == blockCount):
            currentCount = 1
            totalCount += 1
            openImagesFromFolder(refImage, fileNames, totalCount)
            fileNames = []


    
folderName = sys.argv[1]

openImages(folderName)

