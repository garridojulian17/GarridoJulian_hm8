import numpy as np
from scipy import curvefit
import matplotlib.pyplot as plt
# se crea la funcion normal_dist

def normal_dist(x,mean,sigma):
	normal_dist = np.random.normal(mean, sigma,x)
	return normal_dist

def get_fit(filename):
	data = np.loadtxt(filename)
	freqs,bins = np.histogram(data)
	y = freqs
	x = 0.5*(bins[:-1]+bins[1:])
	a,b =scipy.optimize.curve_fit(normal_dist,x,y)

	plt.plot(hist(x))

	plt.savefig(hist.jpg)
	

