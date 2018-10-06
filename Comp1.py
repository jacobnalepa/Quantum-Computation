"""
Created on Thu Oct  4 13:43:53 2018

@author: Jacob Nalepa
"""

#This Program takes a given wave function in the square well, 
#calculates the first 30 overlaps with the eigenstates of the square well,
#and plots the sum of the products between the coeffiencents with the 
#eigenstates to reproduce the original function



##Imports libraries for use in the program
import numpy as np
import matplotlib.pyplot as plt

#Sets limits of integration and step size in x
a = -1
b = 1
N=1000

#Creates a set of x values for calculations and plotting
xvals = np.linspace(a, b, N)

#Defines the normalized chosen wavefunction
def f(x):
    return (105/16)**(0.5)*(x**3-x)
    
#Creates a set of y values for plotting my chosen function
yvals=f(xvals)

#Initializes empty arrays for eigenstates and coefficients
eigenstates = []
Cn = []

#Loop that creates some number of square well eigenstates
o=1
while o < 31:
    psi = np.sin(o*np.pi*xvals)
    eigenstates.append(psi)
    
    o = o+1

#Loop that calculates a given number of coefficients "Cn" by Fourier's Trick
m=1
while m<31:
    
    #Initializes the integral at 0
    integral = 0.0

    #Sums the function values
    for i in range(N):
        integral += f(xvals[i])*np.sin(m*np.pi*xvals[i])

    #mulitplies the sum of the function values by a differential width to get the area or integral value, "Cn"
    answer = (b-a)/float(N)*integral
    
    m = m+1
    
    Cn.append(answer)
#mulitplies the Cn coefficient matrix and the matrix containing the xvalues of the eigenstates 
Psi = np.matmul(Cn, eigenstates)

#Formats and displays the relevent results
print("Overlap coefficients Cn, C1 through C30:    ",Cn)

f = plt.figure(1)
plt.plot(xvals,yvals,'k', label = "\u03A8")
plt.legend()
plt.title("Wavefunction in an Infinite Square Well")
plt.xlabel("x values")
plt.ylabel("\u03A8")
plt.grid()

p = plt.figure(2)
plt.plot(xvals,Psi,'C1', label = "\u03A3 (Cn*\u03A8n)")
plt.legend()
plt.title("\u03A3 (Cn*\u03A8n) in an Infinite Square Well")
plt.xlabel("x values")
plt.ylabel("\u03A3 (Cn*\u03A8n)")
plt.grid()