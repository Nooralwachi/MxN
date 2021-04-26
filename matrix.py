class MXN:
    def __init__(self, matrix):
        self.mxn = matrix

    def update_value(self, x, y, value):
        if x> len(self.mxn) or y> len(self.mxn[x]):
            return 'error' 
        self.mxn[x][y] = value
        return self.mxn
    def get_sum(self, x1, y1, x2, y2):
        result=0
        print('start:',self.mxn[x1][y1])
        print('end  :', self.mxn[x2][y2])
        if x2<x1 or y2<y1:
            return 'The point are not forming a rectangular'
        if x2> len(self.mxn) or y2> len(self.mxn[x2]):
            return 'Error'
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                print(i, j, self.mxn[i][j])
                result +=int(self.mxn[i][j])
        return result
        

MATRIX = [[1,1,1],[1,1,1],[1,1,1]]
matrix = MXN(MATRIX)
print(matrix.update_value(1, 1, 5))
print(matrix.update_value(5, 1, 5))
MATRIX = [[1,2,3],[2,4,6],[3,6,9]]
matrix = MXN(MATRIX)
print(matrix.get_sum(0, 1, 2, 2))
print(matrix.get_sum(0, 1, 1, 1))
print(matrix.get_sum(1, 1, 0, 0))
