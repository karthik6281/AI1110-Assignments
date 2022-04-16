# Ravula Karthik
# AI21BTECH11024
import numpy as np
# NumPy's np.linalg.solve() function can be used to solve this system of equations for the variables x,y,z
# The steps to solve the system of linear equations with np.linalg.solve() are below:
# Create NumPy array A as a 2 by 2 array of the coefficients
# Create a NumPy array b as the right-hand side of the equations
# Solve for the values of x , y.

A = np.array([[0, -2], [2, 0]])
b = np.array([4, 6])
x = np.linalg.solve(A, b)
print(x)