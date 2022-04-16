# determinant of [[2,1,0],[c+a,a,0],[c+b,c,1]]
import numpy as np
import sympy as sym
from sympy import *
from sympy.matrices import Matrix
a,b,c = sym.symbols('a,b,c')
H=np.array([[2,1,0],[c+a,a,0],[c+b,c,1]])
M = sym.Matrix(H)
print(M.det())