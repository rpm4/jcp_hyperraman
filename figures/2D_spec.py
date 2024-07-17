# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:28:39 2023

@author: rpm
"""

import math
from sympy import *
import numpy as np
import WrightTools as wt
import matplotlib.pyplot as plt 
import matplotlib


#define harmonic wells
def gs(k):
    return 0.1*k**2

def es(k):
    return 0.1*(k-0.5)**2 + 0.65


#coordinate#
kg = np.linspace(-2.5, 2.5, 500) #ground state coordinates
ke = np.linspace(-2, 3, 500) #excited state coordinates

#plots#

#make plot

fig, ax = plt.subplots(figsize=(3.5, 3.5), layout='constrained')
plt.rcParams['figure.dpi'] = 1000

plt.plot(kg,gs(kg), linewidth = '4',label = '$C_{\chi = + 1}$', color = 'cyan')
plt.plot(ke,es(ke), linewidth = '4',label = '$C_{\chi = - 1}$', color = 'orange')
# delta
plt.axvline(x=0.5, color = 'purple', linestyle='--', label = '$\Delta$')

#beautificiation#

matplotlib.rcParams.update({'font.size': 10})

plt.xlabel(r'q (arb.)')
plt.xticks(ticks = [])
plt.yticks(ticks = [])
plt.ylabel(r'Energy')
plt.xlim(-3.5,3.5)
plt.ylim(-0.1, 1.4)

matplotlib.rcParams.update({'font.size': 10})

# plt.legend(loc = 'upper center')   


plt.show()

##make the 2d plot

#define Franck-Condon factors following page 164 of Roger Carlson's thesis in terms of Delta
def f00(q): #<0|0>
    return np.e**(-q**2/4)

def f01(q): #<0|1>
    return -q/(np.sqrt(2)) * f00(q)

def f10(q): #<1|0>
    return -1*f01(q)

def f11(q):
    return (1 - q**2/2) *f00(q)

def f02(q): #<0|2>
    return q**2/(2*np.sqrt(2)) * f00(q)

def f20(q): #<2|0>
    return f02(q)

def f12(q): #<1|2>
    return -q * (1 - q**2/4) *f00(q)
    

#define Herzberg Teller overlap integrals following page 165 of Roger Carlson's thesis in terms of Delta
def h00(q): #<0|Q|0>
    return -q/2 * f00(q)

def h01(q): #<0|Q|1>
    return 1/np.sqrt(2) * (1 + q**2 /2) * f00(q)

def h10(q): #<1|Q|0>
    return 1/np.sqrt(2) * (1 - q**2 /2) * f00(q)

def h11(q): #<1|Q|1>
    return -q/2 * (1 - q**2 / 2) * f00(q)

#define resonance denominator
def Deltaevgo(v,x,j):
    Gammaev =[500, 500, 500]
    weg = 30000
    return 1/(weg + 1500*v - x - 1j*Gammaev[j])


#define numbers for AB terms
Mge = 0.1
alphage = 0.01
dMegedQ = 0.05
dMem = 0.025
dMmg = 0.025

#define terms
x = np.linspace(29000, 35000, 6000)

A = Mge * alphage * (f10(0.5)*f00(0.5)*Deltaevgo(0,x,0) + f11(0.5)*f10(0.5)*Deltaevgo(1,x,1) + f12(0.5)*f20(0.5)*Deltaevgo(2,x,2))

B1 = 


