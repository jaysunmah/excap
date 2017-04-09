import os
import shutil
import cv2
import sys
import threading

resultArray = []

def mergeFiles(left, right):
    lIndex = 0
    rIndex = 0
    results = []
    while lIndex < len(left) and rIndex < len(right):
        leftVal = int(left[lIndex].rstrip(".jpg"))
        rightVal = int(right[rIndex].rstrip(".jpg"))
        if (leftVal < rightVal):
            results.append(left[lIndex])
            lIndex += 1
        else:
            results.append(right[rIndex])
            rIndex += 1
    if (lIndex < len(left)):
        results += left[lIndex:]
    if (rIndex < len(right)):
        results += right[rIndex:]
    return results

def mergeFileSort(files):
    if len(files) < 2:
        return files
    result = []
    pivot = len(files) / 2
    left = mergeFileSort(files[:pivot])
    right = mergeFileSort(files[pivot:])
    return mergeFiles(left, right)

def loadResultArray(startRow, endRow, startCol, endCol, image):
    global resultArray
    for i in xrange(startRow, endRow):
        for j in xrange(startCol, endCol):
            resultArray[i][j][0] += image[i, j][0]
            resultArray[i][j][1] += image[i, j][1]
            resultArray[i][j][2] += image[i, j][2]
            

def openImagesFromFolder(outputDir,refImage, fileNames, count):
    threadCount = 32
    divisions = threadCount / 2

    global resultArray

    resultArray = []

    rows, cols, channels = refImage.shape
    print(rows, cols)
    for r in xrange(rows):
        row = []
        for c in xrange(cols):
            row.append([0, 0, 0])
        resultArray.append(row)

    print("done 1", fileNames)
    imageCount = 0
    for filename in fileNames:
        thread_list = []

        imageCount += 1
        imgName = folderName + "/" + filename
        image = cv2.imread(imgName)

        for threadCol in xrange(divisions): #0 -> 7
            for threadRow in xrange(divisions):
                rowPartition = rows / divisions
                colPartition = cols / divisions

                t = threading.Thread(target=loadResultArray,
                    args=(threadRow * rowPartition, (threadRow + 1) * rowPartition, 
                          threadCol * colPartition, (threadCol + 1) * colPartition, image))
                t.daemon = True
                thread_list.append(t)

        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()

        print("done with parsing 1 image")


    print("done 2")
    newImage = refImage.copy()
    rows, cols, channels = newImage.shape


    for r in xrange(rows):
        for c in xrange(cols):
            newImage[r,c][0] = resultArray[r][c][0] / imageCount
            newImage[r,c][1] = resultArray[r][c][1] / imageCount
            newImage[r,c][2] = resultArray[r][c][2] / imageCount

    print("done 3")
    cv2.imwrite(outputDir + "/" + str(count) + "_parsed.jpg", newImage[90:630, 0:960])
    print("done 4")



def openImages(folderName):
    blockCount = 4
    maxPhotos = 10
    currentCount = 0
    fileNames = []

    refImageName = os.listdir(folderName)[0]
    refImage = cv2.imread(folderName + "/" + refImageName)

    totalCount = 0
    try:
        shutil.rmtree(folderName + "_parsed")
        os.mkdir(folderName + "_parsed")
    except:
        os.mkdir(folderName + "_parsed")

    files = os.listdir(folderName)
    
    filteredFiles = [x for x in files if not ".DS_Store" in x]

    sortedFiles = mergeFileSort(filteredFiles)
    print(sortedFiles)

    for filename in sortedFiles:
        currentCount += 1
        fileNames.append(filename)
        if (currentCount == blockCount):
            currentCount = 0
            totalCount += 1
            openImagesFromFolder(folderName + "_parsed", refImage, fileNames, totalCount)
            fileNames = []
        if totalCount == maxPhotos:
            break

    print("done")


    
folderName = sys.argv[1]

openImages(folderName)

