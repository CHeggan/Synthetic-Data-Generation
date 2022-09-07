"""
Contains the base functions needed to generate data. Each function takes a set of 
    operating parameters defined elsewhere and a noise parameter which is used to 
    generate a additive noise ona  sample-wise basis.

We have:
    - different variant for each function
    - a random noise addition to y values

Initial problem:
    - want to generate a library for each function (not discriminate between variants
        of each)
"""

################################################################################
# IMPORTS
################################################################################
import random
import numpy as np




################################################################################
# EXPONENTIAL
################################################################################
###########################
# 1D
###########################
def exp_1d(x_space, n_min, n_max, variant='any'):
    # variant: exp(x^n), exp (x*n), exp(x/n)
    if variant == 'exponent':
        n = random.uniform(n_min, n_max)
        mod_x_space = x_space**n
        y_space = np.exp(mod_x_space)

    elif variant == 'mult':
        n = random.uniform(n_min, n_max)
        mod_x_space = x_space*n
        y_space = np.exp(mod_x_space) 

    elif variant == 'any':
        variant = random.choice(['exponent', 'mult'])
        y_space, variant, n = exp_1d(x_space, n_min, n_max, variant)

    return y_space, variant, n



    
###########################
# 2D
###########################
def exp_2d(x_space, ):
    pass