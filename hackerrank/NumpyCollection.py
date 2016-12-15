import numpy as np


def getreversearrayview(arr):
    return arr[::-1]


def reversearray(arr):
    return np.fliplr([arr])[0]


def createarray(listy):
    return np.array(listy, float)


def transposeandflatten(arr):
    return arr.T.flatten()


def concatenatetwonumpyarrayNxPandMxP(nxp, mxp):
    return np.concatenate(nxp, mxp)


def ones(alist):
    return np.ones(alist, dtype=int)


def zeros(alist):
    return np.zeros(alist, dtype=int)


def identity(anum):
    return np.identity(anum)


def eyeupperdiagonal(alist, positive=1):
    return np.eye(*alist, k=positive)


def eyemaindiagonal(alist):
    return np.eye(*alist, k=0)


def eyelowerdiagonal(alist, negative=-2):
    return np.eye(*alist, k=negative)


def determinant(multilevellist):
    return np.linalg.det(multilevellist)


def eigenvaluesandvectors(multilevellist):
    return np.linalg.eig(multilevellist)


def inverse(multilevellist):
    return np.linalg.inv(multilevellist)
