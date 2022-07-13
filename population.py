import random
import conversions


def genPopulation(iter):

    population = []*iter
    for i in range(iter):
        xOffset = random.randrange(0, 512)
        yOffset = random.randrange(0, 512)
        sbPole = random.randrange(0, 2)
        sbDir = random.randrange(0, 2)
        xOffsetBin = conversions.int2binary9(xOffset)
        yOffsetBin = conversions.int2binary9(yOffset)
        finalChrome = str(sbDir) + str(sbPole) + \
            str(yOffsetBin) + str(xOffsetBin)
        population.append(finalChrome)

    return population
