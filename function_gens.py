"""
Contains the base functions needed to generate data. Each function takes a set of 
    operating parameters defined elsewhere and a noise parameter which is used to 
    generate a additive noise ona  sample-wise basis.

We have:
    - different variant for each function
    - a random noise addition to y values
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
    if variant == 'any':
        variant = random.choice(['exponent', 'mult'])
        sample, variant, n = random_exp_sample()

    
###########################
# 2D
###########################
def exp_2d(x_space, ):
    pass