# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 10:57:43 2018

@author: jacob
"""
#This program compares the exact solution for the energies of the Ammonia 
#molecule in a variable electric field to the energies calculated by 
#perturbation theory in high field and low field regimes.

import numpy as np
import matplotlib.pyplot as plt

#Set nonvariable parameters
E0 = 0
A = 1

#Setting variable electric field parameter
muE = np.linspace(1E-10,10,10000)

#Exact solution
def E_exact_plus(muE):
    return E0 + np.sqrt((muE**2)+A)
def E_exact_minus(muE):
    return E0 - np.sqrt((muE**2)+A)

#High field perterbation solutions
def E_high_plus(muE):
    return E0+muE+(A**2)/(2*muE)
def E_high_minus(muE):
    return E0-muE-(A**2)/(2*muE)

#Low field perterbation solutions
def E_low_plus(muE):
    return E0+A+(muE)**2/(2*A)
def E_low_minus(muE):
    return E0-A-(muE)**2/(2*A)

#Calculates the exact energy values
E_plus = E_exact_plus(muE)
E_minus = E_exact_minus(muE)

#Calculates the high field perterbation energies
E_hf_plus = E_high_plus(muE)
E_hf_minus = E_high_minus(muE)

#Calculates the low field perterbation energies
E_lf_plus = E_low_plus(muE)
E_lf_minus = E_low_minus(muE)

#Calculates the percent error at all values of the electric field for
#the low field regime
diff1 = np.abs((E_plus[:]-E_lf_plus[:]))/E_plus[:]*100 

#Sets the condition for an acceptable approximation with perterbation theory
condition1 = diff1 < 2.0

#Selects and displays the maximum electric field value at which the percent 
#error is < 2% for the low field regime
print('The max value of the electric field for an error in energies of less than 2 percent in the small field regime is %.4f'% max(np.extract(condition1,muE)))

#Calculates the percent error at all values of the electric field for the high
#field regime
diff2 = np.abs((E_plus[:]-E_hf_plus[:]))/E_plus[:]*100

#Sets the condition for an acceptable approximation with perterbation theory
condition2 = diff2 < 2.0

#Selects and displays the maximum electric field value at which the percent
#error is < 2% for the high field regime
print('The min value of the electric field for an error in energies of less than 2 percent in the large field regime is %.4f'% min(np.extract(condition2,muE)))

#Plots and labels the comparison of exact vs perterbation solutions in the 
#limit of a small applied electric field.
plt.figure(1)
plt.plot(muE,E_plus, label = 'Exact E+')
plt.plot(muE,E_minus, label = 'Exact E-')
plt.plot(muE,E_lf_plus, label = 'Low Field E+')
plt.plot(muE,E_lf_minus, label = 'Low Field E-')
plt.legend()
plt.xlim(left=0, right=3)
plt.ylim(bottom=-5, top=5)
plt.xlabel('Applied Electric Field')
plt.ylabel('Energy')
plt.title('Energy vs Electric Field')

#Plots and labels the comparison of exact vs perterbation solutinos in the 
#limit of a large applied electric field.
plt.figure(2)
plt.plot(muE,E_plus, label = 'Exact E+')
plt.plot(muE,E_minus, label = 'Exact E-')
plt.plot(muE,E_hf_plus, label = 'High Field E+')
plt.plot(muE,E_hf_minus, label = 'High Field E-')
plt.legend()
plt.xlim(left=0, right=3)
plt.ylim(bottom=-5, top=5)
plt.xlabel('Applied Electric Field')
plt.ylabel('Energy')
plt.title('Energy vs Electric Field')