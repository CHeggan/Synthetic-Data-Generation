# Matrix Inversion
## Motivation
Inverting matrices becomes increasingly expensive as the dimensionality goes up 
    (O(n^3) I think). This process could be amortised by using machine learning.
    We can look at this from a variety of directions but for the sake of simplicity 
    we consider the most conceptually easy.

## Data structure
In this easiest setting, we would aim to learn a direct transformation between a 
    matrix and its inverse. This comes with the following observations:
- Training Data: Valid matrices that can be analytically inverted (i.e a solution actually exists). We don't want to be learning transformation rules from matrices that are not invertible in the first place
- Learning Objective: This is mainly where the problem statement variation could come in but I think we will go with the inverted matrix here. This makes the learning objective a type of autoencoding or regression task over a whole matrix.

## Possible Problems
Although we don't do any actual machine learning here, can foresee a few possible problems/areas that require some additional thought. In no particular order
 - When inverting a matrix we have some determinant factor that acts on the whole matrix. Learning this implicitly may be tough and require the use of a more specialised network architecture (i.e no batch norm or extra scaling)
 - Should the loss be point-wise or should it be reference to semantics about the inverted matrix (determinant, covariance, some other important statistical property that needs to be preserved etc)

## Matrix Generation
### Rules
 - Matrix must be square
 - Determinant must not be 0 (singular matrix)

## Tools Used
We do not handcraft a matrix solver and instead look to common tools. In the 
    interest of consistency across our synthetic data experiments and ML pipelines
     we use torch as much as possible