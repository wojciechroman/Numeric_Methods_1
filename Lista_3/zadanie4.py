
import numpy as np
from scipy import linalg

# 1

A = np.matrix([[0,0,2,1,2],[0,1,0,2,-1],[1,2,0,-2,0],[0,0,0,-1,1],[0,1,-1,1,-1]])
b = np.matrix([[1],[1],[-4],[-2],[-1]])

x = linalg.solve(A,b)
print(x,"\n")

# 2

L = np.matrix([[1, 0, 0], [3/2, 1, 0], [1/2, 11/13, 1]])
U = np.matrix([[2, -3, -1], [0, 13/2, -7/2], [0, 0, 32/13]])
b = np.matrix([[1], [-1], [2]])

y = linalg.solve(L, b)
x = linalg.solve(U, y)
print(x)