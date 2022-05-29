
# importing statistics module
from statistics import pvariance
 
# importing fractions module as F
from fractions import Fraction as F
 
 
dis1 = (1, 2, 3, 5, 4, 6, 1, 2, 2, 3, 1, 3,
         7, 8, 9, 1, 1, 1, 2, 6, 7, 8, 9, )
 
# Creating a population tree for
# a set of negative integers
dis2 = (-36, -35, -34, -32, -30, -31, -33, -33, -33,
             -38, -36, -35, -34, -38, -40, -31, -32)
 
# Creating a population tree for
# a set of fractional numbers
dis3 = (F(1, 3), F(2, 4), F(2, 3),
        F(3, 2), F(2, 5), F(2, 2),
        F(1, 1), F(1, 4), F(1, 2), F(2, 1))
 
# Creating a population tree for
# a set of decimal values
dis4 = (3.45, 3.2, 2.5, 4.6, 5.66, 6.43,
        4.32, 4.23, 6.65, 7.87, 9.87, 1.23,
            1.00, 1.45, 10.12, 12.22, 19.88)
 
# Print the population variance for
# the created population trees
print("Population variance of set 1 is % s"
                        %(pvariance(dis1)))
                         
print("Population variance of set 2 is % s"
                        %(pvariance(dis2)))
                         
print("Population variance of set 3 is % s"
                        %(pvariance(dis3)))
                         
print("Population variance of set 4 is % s"
                        %(pvariance(dis4)))