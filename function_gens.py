"""
Contains the base functions needed to generate data. Each function takes a set of 
    operating parameters defined elsewhere and a noise parameter which is used to 
    generate a additive noise ona  sample-wise basis 
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
def random_exp(x_space, variant='all'):
    # variant: exp(x^n), exp (x*n), exp(x/n)
    
###########################
# 2D
###########################