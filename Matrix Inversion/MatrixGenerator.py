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
        self.data_type = data_type #int/float/random

    def create_random_matrix(self):
        if self.data_type == 'rand':
            randint = torch.randint(low=0, high=1, size=(1,))
            if randint == 0:
                matrix = self.int_matrix()
            elif randint == 1:
                matrix = self.float_matrix()
            else:
                raise ValueError('Something wrong with random functionality')

        # Create matrix with only ints
        elif self.data_type == 'int':
            matrix = self.int_matrix()
        
        # Create matrix with only floats
        elif self.data_type == 'float':
            matrix = self.float_matrix()

        else:
            raise ValueError('Type of matrix data is unrecognised')

        return matrix


    def int_matrix(self):
        matrix = torch.randint(low=int(self.low), 
            high=int(self.high),
            size=(self.size, self.size)).to(dtype=float)
        return matrix


    def float_matrix(self):
        matrix = (self.low-self.high)*torch.rand(size=(self.size, self.size)) + self.high
        return matrix


    def calc_determinant(self, matrix):
        det = torch.linalg.det(matrix)
        return det


    def invert_matrix(self, matrix):
        inv = torch.inverse(matrix)
        return inv


    def generate_n_matrices(self, n):

        matrices = torch.rand(size=(n, self.size, self.size))
        inverses = torch.rand(size=(n, self.size, self.size))

        for i in range(n):
            # We allow ourself to retry the generation if one is invalid
            while True:
                matrix = self.create_random_matrix()
                det = self.calc_determinant(matrix)
                # Matrix is valid id det doesn't equal 0, so we can break loop
                if det != 0:
                    break 
            
            inv = self.invert_matrix(matrix)

            matrices[i] = matrix
            inverses[i] = inv

        return matrices, inverses

        


gen = MatrixGenerator(2, 0, 10, 'int')
mat = gen.create_random_matrix()
print(mat)
inv = gen.invert_matrix(mat)
