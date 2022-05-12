import numpy as np
# A IS THE EVENT OF FALLING EITHER 5 OR 6
# B IS THE EVENT OF FALLING OF 1 ,2 , 3 OR 4
# C IS THE EVENT OF GETTING THE NUMBER OF HEADS IS 1
S = {1,2,3,4,5,6}

B = {1,2,3,4}
prob_B = float(len(B)/len(S))

A = {5,6}
prob_A = float(len(A)/len(S))
prob_C = float(11/24)
prob_A_And_B = float(len(A&B)/len(S))
prob_A_And_C = float(1/3)

prob_A_by_B = float(prob_A_And_B/prob_B)

prob_B_by_A = float(prob_A_And_B/prob_A)

prob_A_by_C = float(prob_A_And_C/prob_C)

print(prob_A_by_C)

