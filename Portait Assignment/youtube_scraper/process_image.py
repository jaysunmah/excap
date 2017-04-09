import cv2
import sys

imw = 98
imh = 55
jwidth = imw / 2
jheight = imh / 2

print(jwidth, jheight)

# image = cv2.imread("jaysunmah@gmail.com/" + sys.argv[1]  + ".jpg")
image = cv2.imread("source.jpg")
rows,cols, channels = image.shape
avgRed = 0
avgGreen = 0
avgBlue = 0

print(type(image))
newImage = image.copy()


def getAveragePixels(r, c):
    rVal = 0
    gVal = 0
    bVal = 0

    for i in xrange(r, r + imw):
        for j in xrange(c, c + imh):
            if (i < rows and j < cols):
                rVal += image[i, j][2]
                gVal += image[i, j][1]
                bVal += image[i, j][0]

    rVal = rVal / (imw * imh)
    gVal = gVal / (imw * imh)
    bVal = bVal / (imw * imh)

    return (rVal, gVal, bVal)


print(getAveragePixels(0,0))
print(rows, cols)


for i in range(0, rows, imh):
    for j in range(0, cols, imw):
        (rAvg, gAvg, bAvg) = getAveragePixels(i, j)
        for k in range(i, i + imh):
            for l in range(j, j + imw):
                if (k < rows and l < cols):
                    newImage[k, l] = [bAvg, gAvg, rAvg]

        # avgRed += image[i, j][2]
        # avgGreen += image[i, j][1]
        # avgBlue += image[i, j][0]
        # newImage[i, j] = image[i,j]
        # newImage[i,j][2] = 0

# avgRed = avgRed / (rows * cols)
# avgGreen = avgGreen / (rows * cols)
# avgBlue = avgBlue / (rows * cols)

# print(avgRed, avgGreen, avgBlue)

cv2.imwrite("output.jpg", newImage)

