
"""
from scipy.optimize import root
from math import cos

def eqn(x):
    return x + cos(x)

myroot = root(eqn,0)

print(myroot.x)
print (myroot)
"""
#Minimizing a Function

from scipy.optimize import minimize

def eqn(x):
    return x ** 3 + x + 2

mymin=minimize(eqn,0,method='BFGS')

print(mymin)

