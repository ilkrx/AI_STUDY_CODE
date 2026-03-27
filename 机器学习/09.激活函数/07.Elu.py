import numpy as np
import matplotlib.pyplot as plt


def relu(x):
    return np.maximum(0, x)


def elu(x, alpha=0.25):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))


def elu_derivative(x, alpha=0.25):
    return np.where(x > 0, 1, alpha * np.exp(x))
