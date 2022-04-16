# determinant of [[a,b,b+c],[c,a,c+a],[b,c,a+b]]
import numpy as np
import sympy as sym
from sympy import *
from sympy.matrices import Matrix
a,b,c = sym.symbols('a,b,c')
H=np.array([[a,b,b+c],[c,a,c+a],[b,c,a+b]])
M = sym.Matrix(H)
print(M.det())