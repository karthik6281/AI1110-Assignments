#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import math

#if using termux
import subprocess
import shlex
#end if



x = np.linspace(-4,4,60)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('gau3.dat',dtype='double')
#randvar = np.loadtxt('gau4.dat',dtype='double')
for i in range(0,60):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def chidist(x):
    if (x<=0):
       return 0
    elif (x>=0):
        return (1 - math.exp(-x/2))
    
theoritical = []
for i in range(len(x)):
   theoritical.append(chidist(x[i]))
plt.plot(x,err,'x')#plotting the CDF
plt.plot(x,theoritical)	
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window
