import math


def computeFitness(z, originalImage, stegoImage):
    x = 1/(z*z)
    y = 0
    for i in range(512):
        for j in range(i):
            dataCng = originalImage[i][j] - stegoImage[i][j]
            dataCng = dataCng * dataCng
            y = y + dataCng

    mse = x * y
    allPix = 255
    psnr = 20 * math.log10(allPix/math.sqrt(mse))
    print("Computed Fitness")
    return psnr
