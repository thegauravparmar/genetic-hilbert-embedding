import hilbert
import embed
import conversions


def decodeImage(image, x, y, sbDir, sbPole):
    secretData = ""
    cnt = 0
    if sbDir == 1:
        if sbPole == 1:
            for i in range(512*512):
                r = conversions.int2binary(image[x[i]][y[i]])
                secretData += str(1-int(r[7])) + \
                    str(1-int(r[6]))+str(1-int(r[5]))
        else:
            for i in range(512*512):
                r = conversions.int2binary(image[x[i]][y[i]])
                secretData += str(r[7]) + str(r[6])+str(r[5])
    else:
        if sbPole == 1:
            for i in range(512*512):
                r = conversions.int2binary(image[x[i]][y[i]])
                secretData += str(1-int(r[5])) + \
                    str(1-int(r[6]))+str(1-int(r[7]))
        else:
            for i in range(512*512):
                r = conversions.int2binary(image[x[i]][y[i]])
                secretData += str(r[5])+str(r[6])+str(r[7])
    secretFile = open("decodedData.txt", 'w')
    secretFile.write(secretData)


def decodeFunction(strr, image):
    sbDir = strr[0]
    sbPole = strr[1]
    yValue = strr[2:11]
    xValue = strr[11:20]

    xOff = int(xValue, 2)
    yOff = int(yValue, 2)
    x, y = hilbert.genHilbert(512, 512)
    x, y = embed.genPoint(xOff, yOff, x, y)
    decodeImage(image, x, y, sbDir, sbPole)
