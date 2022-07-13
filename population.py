import random
import conversions


def int2binary9(n):
    bb = ""
    tmp = n
    while(tmp > 0):
        if(tmp % 2 == 1):
            bb += "1"
        else:
            bb += "0"
        tmp = tmp//2
    while(len(bb) < 9):
        bb += "0"
    tt = bb[::-1]
    return tt


def genPopulation(iter):
    # import conversions

    population = []*iter
    for i in range(iter):
        xOffset = random.randrange(0, 512)
        yOffset = random.randrange(0, 512)
        sbPole = random.randrange(0, 2)
        sbDir = random.randrange(0, 2)
        # xOffsetBin = conversions.int2binary9(xOffset)
        # yOffsetBin = conversions.int2binary9(yOffset)
        finalChrome = str(sbDir) + str(sbPole)
        population.append(finalChrome)

    return population
