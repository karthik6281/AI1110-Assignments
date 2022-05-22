import numpy as np
# A IS THE EVENT OF FALLING EITHER 5 OR 6
# B IS THE EVENT OF FALLING OF 1 ,2 , 3 OR 4
# C IS THE EVENT OF GETTING THE NUMBER OF HEADS IS 1
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