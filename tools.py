from __future__ import division
import sys
import os


class Functions(object):
    def __init__(self):
        return

    #histogram
    def histogram(self, x):
        y ={}
        for i,a in enumerate(x):
            if y.has_key(x[i]):
                y[x[i]] = y[x[i]]+1
            else:
                y[x[i]] = 1
        return y

    #mean of array
    def mean(self, x):
        return sum(x)/len(x)
