

import conversions
import cv2
import hilbert


def genPoint(offsetX, offsetY, x, y):
    for i in range(512*512):
        x[i] = (x[i]+offsetX) % 512
    for i in range(512*512):
        y[i] = (y[i]+offsetY) % 512
    return x, y


def encodeImage(image, x, y, sbDir, sbPole, secretData):
    secretDataIndex = 0
    if sbDir == 1:
        if sbPole == 1:
            for i in range(512*512):
                r = conversions.int2binary(image[x[i]][y[i]])
                image[x[i]][y[i]] = int(
                    r[:-3] + str(1-int(secretData[secretDataIndex+2])) + str(1-int(secretData[secretDataIndex+1])) + str(1-int(secretData[secretDataIndex])), 2)
                secretDataIndex = secretDataIndex+3
        else:
            for i in range(512*512):
                r = conversions.int2binary(image[x[i]][y[i]])
                image[x[i]][y[i]] = int(
                    r[:-3] + str(secretData[secretDataIndex+2]) + str(secretData[secretDataIndex+1]) + str(secretData[secretDataIndex]), 2)
                secretDataIndex = secretDataIndex+3
    else:
        if sbPole == 1:
            for i in range(512*512):
                r = conversions.int2binary(image[x[i]][y[i]])
                image[x[i]][y[i]] = int(
                    r[:-3] + str(1-int(secretData[secretDataIndex])) + str(1-int(secretData[secretDataIndex+1])) + str(1-int(secretData[secretDataIndex+2])), 2)
                secretDataIndex = secretDataIndex+3
        else:
            for i in range(512*512):
                r = conversions.int2binary(image[x[i]][y[i]])
                image[x[i]][y[i]] = int(
                    r[:-3] + str(secretData[secretDataIndex]) + str(secretData[secretDataIndex+1]) + str(secretData[secretDataIndex+2]), 2)
                secretDataIndex = secretDataIndex+3

    file_name = "encoded_image.bmp"
    cv2.imwrite(file_name, image)

    return cv2.imread(file_name, 0)


def encodeFunction(strr, image, secretData):
    sbDir = strr[0]
    sbPole = strr[1]
    yValue = strr[2:11]
    xValue = strr[11:20]

    xOff = int(xValue, 2)
    yOff = int(yValue, 2)
    x, y = hilbert.genHilbert(512, 512)
    x, y = genPoint(xOff, yOff, x, y)
    stegoImage = encodeImage(image, x, y, int(sbDir), int(sbPole), secretData)

    return stegoImage
