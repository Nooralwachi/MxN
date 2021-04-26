# MxN
Given an MxN array object, implement the methods update_value and get_sum.

update_value should receive the x and y coordinate of a point, and the value to insert at that point.

get_sum should receive the x and y coordinates of two points, and return the sum of the values that fall within the rectangle formed by those two points.



MATRIX = [[1,1,1],[1,1,1],[1,1,1]]


class MXN:

    def __init__(self, matrix):
    
        self.mxn = matrix
        

    def update_value(self, x, y, value):
    
        pass

    def get_sum(self, x1, y1, x2, y2):
    
        pass


matrix = MXN(MATRIX)

matrix.update_value(5, 1, 5)

matrix.get_sum(1, 1, 2, 2)
