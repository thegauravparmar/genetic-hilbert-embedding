def selectionFunction(fitnessArray, usedPop, selectionArray):

    dict_obj = {}

    for i in range(4):
        dict_obj[fitnessArray[i]] = usedPop[i]

    for x in sorted(dict_obj.keys(), reverse=True):
        selectionArray[x] = dict_obj[x]
        break
