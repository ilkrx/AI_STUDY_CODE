import numpy as np
import matplotlib.pyplot as plt


def softmax(x):
    vals = np.exp(x)
    return vals / np.sum(vals)


def softmax_derivative(x):
    s = softmax(x)
    return np.diagflat(s) - np.outer(s, s)