# import numpy as np


import numpy as np


def int2binary(n):
    bb = ""
    tmp = n
    while(tmp > 0):
        if(tmp % 2 == 1):
            bb += "1"
        else:
            bb += "0"
        tmp = tmp//2
    while(len(bb) < 8):
        bb += "0"
    tt = bb[::-1]
    return tt


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


def data2binary(data):
    if type(data) == str:
        return ''.join([format(ord(i), "08b") for i in data])
    elif type(data) == bytes or type(data) == np.ndarray:
        return [format(i, "08b") for i in data]
