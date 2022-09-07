"""
Want to generate synthetic function data that can be used for ML pipelines. 
Specifically we are interested in the following:
    -> Simple Classification problem
    -> Multi-label problems where we superimpose functions
    -> 1d and 2d problems
    -> Functions:
        - Linear
        - Exponential
        - Logarithm
        - Circular
        - Trig
"""
################################################################################
# IMPORTS
################################################################################
import os
import sys
import math
import torch
import numpy as np
import matplotlib.pyplot as plt

from function_gens import exp_1d


################################################################################
# MAIN
################################################################################
if __name__ == '__main__':

    x_space = np.linspace(0, 10, 1000)
    print(x_space)

    y_space, variant, n = exp_1d(x_space, 0, 0.5, 'any')

    print(y_space)

    print(n)
    plt.plot(x_space, y_space)
    plt.show()
