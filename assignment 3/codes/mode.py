

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

# x is the data given.
x = [14,25,14,28,18,17,18,14,23,22,14,18]
#y is a bin (class interval of length 10)
y = [0,10,20,30]
plt.hist(x,y)
#labelling axes of the graph
plt.xlabel("class intervals (X axis)")
plt.ylabel("frequency (Y axis)");
plt.title("Mode Determination")

a = [10,20]
b = [8,4]
c = [0,8]
d = [5.33,0]
e = [16.66,16.66]

plt.plot(a,b)
plt.plot(a,c)
plt.plot(16.66,5.33,marker='o',markersize=5,markerfacecolor='Black',markeredgecolor='Black')
plt.annotate("M--(POI)",xy=(16.6,5.3))
plt.plot(e,d)
plt.plot(16.66,0,marker='o',markersize=5,markerfacecolor='Black',markeredgecolor='Black')
plt.annotate("B(MODE)",xy=(16.7,0.09))
plt.plot(10,8,marker='o',markersize=5,markerfacecolor='Black',markeredgecolor='Black')
plt.annotate("R",xy=(8,8))
plt.plot(20,8,marker='o',markersize=5,markerfacecolor='Black',markeredgecolor='Black')
plt.annotate("P",xy=(21,8))
plt.plot(10,0,marker='o',markersize=5,markerfacecolor='Black',markeredgecolor='Black')
plt.annotate("Q",xy=(8,0.09,))
plt.plot(20,4,marker='o',markersize=5,markerfacecolor='Black',markeredgecolor='Black')
plt.annotate("S",xy=(21,4))
#Point of Intersection [POI] = mode = 16.66
mode_approx = 16.66

plt.show()

if(mode_approx//1 == 14):print("Correct value of mode ") #mode = 14


# In[ ]:





# In[ ]:
