import numpy as np
import matplotlib.pyplot as plt


def relu(x):
    return np.maximum(0, x)


def Prelu(x, alpha=0.25):
    return np.where(x > 0, x, alpha * x)


def Prelu_derivative(x, alpha=0.25):
    return np.where(x > 0, 1, alpha)