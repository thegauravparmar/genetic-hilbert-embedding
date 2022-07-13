def selection(fitnessArray, usedPop):
    global bestFittest

    dict_obj = {}

    for i in range(iter):
        dict_obj[fitnessArray[i]] = usedPop[i]

    for x in sorted(dict_obj.keys(), reverse=True):
        selectionArray[x] = dict_obj[x]
        break
