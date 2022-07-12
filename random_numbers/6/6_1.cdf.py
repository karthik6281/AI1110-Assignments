#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
#if using termux
import subprocess
import shlex
#end if



maxrange=50
maxlim=10.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
x1=np.linspace(-maxlim,maxlim,maxrange*5)
simlen = int(999963) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1)
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('chi.dat',dtype='double')


for i in range(0,maxrange-1):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
def chisquare(x):
    if (x<=0):
       return 1e-5
    elif (x>=0):
        return (1 - math.exp(-x/2))
    
	
chi_cdf = scipy.vectorize(chisquare)

plt.plot(x[0:(maxrange-1)].T,err,'x')
plt.plot(x1,chi_cdf(x1))#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window
