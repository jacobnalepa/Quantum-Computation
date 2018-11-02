# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 22:18:57 2018

@author: jacob
"""
#Imports libraries and special functions
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import brentq

#Sets the depth of the well
Vo = 18
en = np.linspace(1e-10, Vo, 100) #Does not start from 0 to avoid "divide by 
#zero error" in the transcendental equations.

#Defines the finite square well
def V(x):
    L = 1
    if abs(x) > L:
        return Vo
    else:
        return 0
    
#Plots an outline of the potential well
plt.xlim(right=2, left=-2)
plt.hlines(y=Vo, xmin=-2, xmax=-1, color='k')
plt.hlines(y=Vo, xmin=1, xmax=2, color='k')
plt.hlines(y=0, xmin=-1, xmax=1, color='k')
plt.vlines(x=-1, ymin=0, ymax=Vo, color='k')
plt.vlines(x=1, ymin=0, ymax=Vo, color='k')

#Transcendental equations were taken from Griffiths
z = np.sqrt(2*en)
z0 = np.sqrt(2*Vo)
z_zeros_sym = []
z_zeros_asym = []
f_sym = lambda z: np.tan(z)-np.sqrt((z0/z)**2-1)      #Symmetric solution eqn
f_asym = lambda z: -1/np.tan(z)-np.sqrt((z0/z)**2-1)  #Antisymm solution eqn
 
#Finding the zeros for the symmetric case
s = np.sign(f_sym(z))
for i in range(len(s)-1):
   if s[i]+s[i+1] == 0:
       zero = brentq(f_sym, z[i], z[i+1]) #Uses Brent's Method to find zeros
       z_zeros_sym.append(zero)
print("Symmetric solution energies: ")
for i in range(0, len(z_zeros_sym),2):
    print("%.4f" %(z_zeros_sym[i]**2/2))
    plt.hlines(y=(z_zeros_sym[i]**2/2), xmin=-1, xmax=1, color = 'purple')
    
#Finding the zeros for the asymmetric case
s = np.sign(f_asym(z))
for j in range(len(s)-1):
    if s[j]+s[j+1] == 0:
        zero = brentq(f_asym, z[j], z[j+1])
        z_zeros_asym.append(zero)
print("Antisymmetric solution energies: ")
for j in range(0, len(z_zeros_asym),2):
    print( "%.4f" %(z_zeros_asym[j]**2/2))
    plt.hlines(y=(z_zeros_asym[j]**2/2), xmin=-1, xmax=1, color = 'purple')

#Sets initial conditions to solve for the wave functions
N = 1000                  # number of points
psi = np.zeros([N,2])
psi0 = np.array([0,1])    # Wave function initial states
b = 2                     # point outside of well
x = np.linspace(-b, b, N) # x-axis

#Defines the Schrodinger equation, returns the first and second derivative 
def SchrodEqn(psi, x):
    psiprime = psi[1]
    psi2prime = 2.0*(V(x) - E)*psi[0]
    return np.array([psiprime, psi2prime])

#Calculates the wave functions for a given energy from the schrodinger eqn
def Wave_function(energy):
    global psi
    global E
    E = energy
    psi = odeint(SchrodEqn, psi0, x)
    return psi[-1,0]

#Calculates the wave functions for each energy, normalizes them, and plots them
for i in range(0, len(z_zeros_sym),2):
    Wave_function(z_zeros_sym[i]**2/2)
    Area=np.trapz((psi[:,0])**2,x=None, dx=.001)
    A=np.sqrt(1/Area)
    plt.plot(x, A*psi[:,0]+z_zeros_sym[i]**2/2)
for j in range(0, len(z_zeros_asym),2):
    Wave_function(z_zeros_asym[j]**2/2)
    Area=np.trapz((psi[:,0])**2,x=None, dx=.001)
    A=np.sqrt(1/Area) 
    plt.plot(x, A*psi[:,0]+z_zeros_asym[j]**2/2)
    
plt.title('Energy Levels and Wave Functions in the Finite Square Well')
plt.xlabel('x')
plt.ylabel('E, $\Psi(x)$')