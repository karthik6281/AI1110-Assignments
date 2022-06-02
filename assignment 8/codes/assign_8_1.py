import numpy as np
from matplotlib.pyplot import *

# function for plotting negative sign opening of |x+3|
def f1(x):
    return -x+7.5;

# function for plotting positive sign opening of |x+3|
def f2(x):
    return -x+7;
fig = figure()
x3,y3 = [2,2],[-1,10]
x4,y4 = [5,5],[-1,10]
x5,y5 = [7,7],[-1,10]
x6,y6 = [10,10],[-3,10]


# generating values for plotting graph from x = -3 to 3
x1 = np.arange(-2,10,0.01)
y1 = f1(x1)
# generating values for plotting graph from x = -6 to -3
x2 = np.arange(-2,10,0.01)
y2 = f2(x2)
# labeling axis
xlabel("x-axis")
ylabel("y-axis")

ax = gca()

# plotting graph from x = -3 to 3
ax.plot(x1, y1,"r",label="x+y=z")
# plotting graph from x = -6 to -3
ax.plot(x2, y2,"g",label="x+y=z+del(z)")

ax.plot(x3,y3,"b")
ax.plot(x4,y4,"b")
ax.plot(x5,y5,"b")
ax.plot(x6,y6,"b")

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

ax.legend()

show()