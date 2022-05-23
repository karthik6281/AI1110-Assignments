# RAVULA KARTHIK AI21BTECH11024
# X/S denotes the probability of X arriving before Y
# Y/S denotes the probability of Y and X meet at the station
#
import numpy as np

S = 400

X = 200
Y = 159.5
prob_C = float(X/S)
print(prob_C)
prob_D = float(Y/S)
print(prob_D)

prob_C_And_D = float(72/400)

prob_C_by_D = float(prob_C_And_D/prob_D)

print(prob_C_by_D)
