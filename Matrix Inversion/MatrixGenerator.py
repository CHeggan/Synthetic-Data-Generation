################################################################################
# IMPORTS
################################################################################
import torch


################################################################################
# MATRIX GENERATOR CLASS
################################################################################
class MatrixGenerator():
    def __init__(self, size, low, high, data_type='int'):

        self.size = int(size)
        self.low = low
        self.high = high
        self.data_type = data_type

    def create_random_matrix(self):
        # Create matrix with only ints
        if self.data_type == 'int':
            matrix = torch.randint(low=int(self.low), 
                high=int(self.high),
                size=(self.size, self.size)).to(dtype=float)
        
        # Create matrix with only floats
        elif self.data_type == 'float':
            matrix = (self.low-self.high)*torch.randn(
                size=(self.size, self.size)) + self.high

        return matrix


    def calc_determinant(self, matrix):
        det = torch.linalg.det(matrix)
        return det


gen = MatrixGenerator(2, 0, 10, 'int')
gen.create_random_matrix()
