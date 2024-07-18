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

save = True


#define harmonic wells and coordinates
def grs(k):
    return 0.1*k**2

def es(k):
    return 0.1*(k-0.5)**2 + 0.65

kg = np.linspace(-2.5, 2.5, 500) #ground state coordinates
ke = np.linspace(-2, 3, 500) #excited state coordinates


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

def h12(q):
    return (1 + q**2/4 - q**4/8) * f00(q)

def h20(q): #<2|Q|0>
    return -q/np.sqrt(2) * (1 - q**2 /4) * f00(q)


#define resonance denominator
def Deltaevgo(v,x,l):
    weg = 30000
    G = [1000, 1000, 1000] #linewidths
    return 1/(weg + 1500*v - x - 1j*G[l]) #assuming the |0> -> |n> transiton is 1500*n 


#define numbers for AB terms
Mge = 0.1
alphage = 0.01
dMem = 0.0025
dMmg = 0.0025
dMgedQ = 0.05


#define terms
y = np.linspace(25000, 35000, 10000)
d = 0.5 #offset

A = Mge * alphage * (f10(d)*f00(d)*Deltaevgo(0,y,0) + f11(d)*f10(d)*Deltaevgo(1,y,1) + f12(d)*f20(d)*Deltaevgo(2,y,2)) #there must be a simpler way to do this but idk

#B1 terms
B10 = Mge*f10(d) * (dMem * h00(d) + dMmg * h00(d)) * Deltaevgo(0, y, 0) #the v' = 0 term
B11 = Mge*f11(d) * (dMem * h10(d) + dMmg * h10(d)) * Deltaevgo(1, y, 1) #the v' = 1 term
B12 = Mge*f12(d) * (dMem * h20(d) + dMmg * h20(d)) * Deltaevgo(2, y, 2) #the v' = 2 term

B1 = B10 + B11 + B12

#B2 terms
B20 = dMgedQ * alphage *(h10(d) * f00(d)) * Deltaevgo(0, y, 0) #the v' = 0 term
B21 = dMgedQ * alphage *(h11(d) * f10(d)) * Deltaevgo(1, y, 1) #the v' = 1 term
B22 = dMgedQ * alphage *(h12(d) * f20(d)) * Deltaevgo(2, y, 2) #the v' = 2 term

B2 = B20 + B21 + B22

cols = [1, 1] 
aspects = [[[0, 0], 1], [[1, 0], 0.2]] 

fig, gs = wt.artists.create_figure(width="dissertation", nrows=2, cols=cols, aspects=aspects, wspace=1) 

ax0 = plt.subplot(gs[0,0])
ax0.plot(kg,grs(kg), linewidth = '4',label = '$C_{\chi = + 1}$', color = 'cyan')
ax0.plot(ke,es(ke), linewidth = '4',label = '$C_{\chi = - 1}$', color = 'orange')
# delta
ax0.axvline(x=0.5, color = 'purple', linestyle='--', label = '$\Delta$')

ax0.set_ylabel('$\mathsf{Energy}$')
ax0.set_xlabel('$\mathsf{Q \ (arb)}$')
plt.ylim(-0.1, 1.4)
plt.xlim(-3.5,3.5)
plt.yticks(ticks = [])
plt.xticks(ticks = [])


ax1 = plt.subplot(gs[0,1])
ax1.plot(y, 10**7*A, linewidth = '2',label = '$A$', color = 'cyan')
ax1.plot(y, 10**7*B1, linewidth = '2',label = '$B_1$', color = 'orange')
ax1.plot(y, 10**7*B2, linewidth = '2',label = '$B_2$', color = 'green')
ax1.plot(y, (A+B1+B2)*10**7, linewidth = '2',label = '$A+B$', color = 'black')
ax1.set_ylabel('$\mathsf{Amplitude \ (arb.)}$')
ax1.set_xlabel(r'$\mathsf{\omega_2 + \omega_3} \ (\mathsf{cm}^{-1})$')

plt.legend()

if save:
    wt.artists.savefig("drsive_spectrum.png", transparent = True, bbox_inches='tight')
