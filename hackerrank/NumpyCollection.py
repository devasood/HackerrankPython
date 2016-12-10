import numpy as np

def getreversenumpyarrayview(arr):
    return arr[::-1]


def reversenumpyarray(arr):
    return np.fliplr([arr])[0]


def createnumpyarray(listy):
    return np.array(listy, float)


def transposeandflattennumpy(arr):
    return arr.T.flatten()


def concatenatetwonumpyarrayNxPandMxP(nxp, mxp):
    return np.concatenate(nxp, mxp)