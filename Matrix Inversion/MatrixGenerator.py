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
        if self.data_type == 'int':

            matrix = torch.randint(low=int(self.low), 
                high=int(self.high),
                size=(self.size, self.size))

        print(matrix)
        print(matrix.shape)


gen = MatrixGenerator(3, 0, 10, 'int')
gen.create_random_matrix()
