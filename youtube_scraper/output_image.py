import cv2
import os

def generateImage():
    with open('parsed.txt', 'r') as parsedData:
        images = parsedData.readlines()
        pixelsImages = []
        for image in images:
            pixelsImage = image.split("#")
            for pixel in pixelsImage:
                pixelData = pixel.split(",")
                if (len(pixelData) == 5):
                    if(pixelData[0] == '0' and pixelData[1] == '0'):
                        print("HERE")

                    imageData = dict()
                    imageData["i"] = pixelData[0]
                    imageData["j"] = pixelData[1]
                    imageData["r"] = pixelData[2]
                    imageData["g"] = pixelData[3]
                    imageData["b"] = pixelData[4]
                    pixelsImages.append(imageData)

        overallImage = dict()

        numRows = 0
        numCols = 0

        for data in pixelsImages:
            if data['i'] not in overallImage:
                numRows += 1
                overallImage[data['i']] = dict()
            if data['j'] not in overallImage[data['i']]:
                numCols += 1
                overallImage[data['i']][data['j']] = dict()
            if 'count' not in overallImage[data['i']][data['j']]:
                overallImage[data['i']][data['j']]['count'] = 0
            if 'r' not in overallImage[data['i']][data['j']]:
                overallImage[data['i']][data['j']]['r'] = 0
            if 'g' not in overallImage[data['i']][data['j']]:
                overallImage[data['i']][data['j']]['g'] = 0
            if 'b' not in overallImage[data['i']][data['j']]:
                overallImage[data['i']][data['j']]['b'] = 0

            overallImage[data['i']][data['j']]['r'] += int(data['r'])
            overallImage[data['i']][data['j']]['g'] += int(data['g'])
            overallImage[data['i']][data['j']]['b'] += int(data['b'])
            overallImage[data['i']][data['j']]['count'] += 1

        # print(overallImage)
        numCols = numCols / numRows
        print(numRows, numCols)

        image = cv2.imread("undefined/0.jpg")
        newImage = image.copy()

        for r in xrange(numRows):
            for c in xrange(numCols):
                print(overallImage[r][c])
                # newImage[r, c] = [overallImage[r][c]['b'] / overallImage[r][c]['count'], overallImage[r][c]['g'] / overallImage[r][c]['count'], overallImage[r][c]['r'] / overallImage[r][c]['count']]

        cv2.imwrite("wei.jpg", newImage)
                

generateImage()

            
        
    
