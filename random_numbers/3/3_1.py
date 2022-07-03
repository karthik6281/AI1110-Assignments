#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

#if using termux
# import subprocess
# import shlex
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
randvar = np.loadtxt('n_uni.dat',dtype='double')


for i in range(0,maxrange-1):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
 

def cdf_V(x):
	if x<0: 
		x=0 # The Distribution is uniform so the function is constant so it's value can be taken to be f(0)
	return 1-np.exp(-x/2)
	
vect_cdf = scipy.vectorize(cdf_V)

plt.plot(x[0:(maxrange-1)].T,err,'x')
plt.plot(x1,vect_cdf(x1))#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$F_X(x_i)$')
plt.legend(["Numerical","Theory"])

# #if using termux
# plt.savefig('../figs/V_pdf.pdf')
#plt.savefig('../figs/uni_pdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_pdf.pdf"))
#if using termux
#plt.savefig('./V_cdf.pdf')
# plt.savefig('./V_cdf.eps')
# subprocess.run(shlex.split("termux-open ../figs/gauss_pdf.pdf"))
#else
plt.show() #opening the plot window
