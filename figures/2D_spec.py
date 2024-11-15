# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:28:39 2023

@author: rpm
"""
import numpy as np
import WrightTools as wt
import matplotlib.pyplot as plt 
from matplotlib.patches import FancyArrowPatch
import pathlib

wt.artists.apply_rcparams(kind="publication")

save = False
fontsize = 18
here = pathlib.Path(__file__).resolve().parent

"""define harmonic wells and coordinates"""
d = 0.5 #offset for es
do = 0 #gs placement

def grs(k):
    return 0.125*(k-do)**2 #arbitrary curvature

def es(k):
    return 0.125*(k-d-do)**2 + 0.7 #arbitrary curvature and vertical offset

kg = np.linspace(-2, 2, 500) #ground state coordinates
ke = np.linspace(-1.75, 2.75, 500) #excited state coordinates

#make figure
cols = [1, 1] 
aspects = [[[0, 0], 1], [[1, 0], 1]] 

fig, gs = wt.artists.create_figure(width="dissertation", nrows=2, cols=cols, aspects=aspects, hspace=0.7, wspace=1.2) 

ax0 = plt.subplot(gs[0,0])

"""Add the arrows and other beautification efforts"""
#hbar omega_eg arrow insert
yarrow = [grs(0.6), es(1.3)] #where the arrows start and end
yarrowstop = [(grs(0.6) + es(1.3))/2 - 0.06, (grs(0.6) + es(1.3))/2 + 0.06] #to put in the hbaromegaeg
myArrow0 = FancyArrowPatch(posA=(-0.35, yarrow[0]), posB=(-0.35, yarrowstop[0]), arrowstyle='<|-', color='blue',
                           mutation_scale=25, shrinkA=0, shrinkB=0, linewidth = 4)
myArrow1 = FancyArrowPatch(posA=(-0.35, yarrowstop[1]), posB=(-0.35, yarrow[1]), arrowstyle='-|>', color='blue', 
                           mutation_scale=25, shrinkA=0, shrinkB=0, linewidth = 4)
ax0.add_artist(myArrow0)
ax0.add_artist(myArrow1)

ax0.text(-0.65, (grs(0.6) + es(1.3))/2 - 0.023, r'$\mathsf{\hbar \omega_{eg}}$', fontsize = 24)

#xi line 
ax0.vlines(x = do, ymin = -0.0257, ymax = grs(do), color = 'gray', linestyle = '--', linewidth = 1)
ax0.vlines(x = d, ymin = -0.0257, ymax = es(d), color = 'gray', linestyle = '--', linewidth = 1)

#xi arrow insert
xarrow = [do, d] #where the arrows start and end
xiarrow = FancyArrowPatch(posA=(xarrow[0], -0.0257), posB=(xarrow[1], -0.0257), arrowstyle='<|-|>', color='blue',  mutation_scale=12, shrinkA=0, shrinkB=0, linewidth = 1)
ax0.add_artist(xiarrow)


ax0.text((do+d)/2-0.133, -0.103, r'$\mathsf{\Delta}$', fontsize = 24)

#labeling vibrational states
jgs = [0.6, 1.0, 1.29965]
jes = [1.3, 1.7, 1.9965]

for i in [0,1,2]:
    kets = [r'$\mathsf{|0\rangle}$', r'$\mathsf{|1\rangle}$', r'$\mathsf{|2\rangle}$']
    ekets = [r'$\mathsf{|\tilde{0}\rangle}$', r'$\mathsf{|\tilde{1}\rangle}$', r'$\mathsf{|\tilde{2}\rangle}$']
    ax0.hlines(y = grs(jgs[i]), xmin = -jgs[i], xmax = jgs[i], color = 'black', linestyle = '-', linewidth = 2) #gs states
    ax0.hlines(y = es(jes[i]), xmin = -jes[i]+2*d, xmax = jes[i], color = 'black', linestyle = '-', linewidth = 2) #es states
    ax0.text(jgs[i] + 0.25, grs(jgs[i])-0.03, kets[i], fontsize = 16) #labeling gs
    ax0.text(jes[i] + 0.25, es(jes[i])-0.03, ekets[i], fontsize = 16) #labeling es
    
#harmonic surface labels
ax0.text(kg.max()+0.12, grs(kg.max())-0.05, r'$\mathsf{|g)}$', fontsize = 24)
ax0.text(ke.max()+0.12, es(ke.max())-0.05, r'$\mathsf{|e)}$', fontsize = 24)

#plot it
ax0.plot(kg,grs(kg), linewidth = '4', color = 'cornflowerblue')
ax0.plot(ke,es(ke), linewidth = '4', color = 'cornflowerblue')
ax0.set_ylabel(r'$\mathsf{Energy \ (cm^{-1})}$', fontsize = fontsize)
ax0.set_xlabel(r'$\mathsf{q}$', fontsize = fontsize)
plt.ylim(-0.13, 1.4)
plt.xlim(-2.2,3.25)
plt.yticks(ticks = [])
plt.xticks(ticks = [])



"""Defining Franck Condon and Herzberg Teller integrals"""
'''fc integrals'''
#<a|b> == |a> is on the ES and |b> is on the GS.

def f00(q): #<0|0>
    return np.exp(-q**2/4)

def f01(q): #<0|1>
    return q/(np.sqrt(2)) * f00(q)

def f10(q): #<1|0>
    return -1*f01(q)

def f11(q): #<1|1>
    return (1 - q**2/2) *f00(q)

def f02(q): #<0|2>
    return q**2/(2*np.sqrt(2)) * f00(q)

def f20(q): #<2|0>
    return f02(q)
   
def f21(q): #<2|1>
    return -q * (1 - q**2/4) *f00(q)

'''ht integrals'''
def h00(q): #<0|Q|0>
    return q/2 * f00(q)

def h01(q): #<0|Q|1>
    return 1/np.sqrt(2) * (1 + q**2 /2) * f00(q)

def h10(q): #<1|Q|0>
    return 1/np.sqrt(2) * (1 - q**2 /2) * f00(q)

def h11(q): #<1|Q|1>
    return -q/2 * (-1 + q**2 / 2) * f00(q)

def h12(q): #<1|Q|2>
    return (-1/8) * (q**4 - 2*q**2 - 8) * f00(q)

def h21(q): #<2|Q|1>
    return (1/8)*(8 - 6*q**2 + q**4) * f00(q)

def h20(q): #<2|Q|0>
    return -q/np.sqrt(2) * (1 - q**2 /4) * f00(q)

#define resonance denominator
def Deltaevgo(v,x,l):
    weg = 30000
    G = [400, 400, 400] #linewidths
    return 1/(weg + 1600*v - x - 1j*G[l]) #assuming the |0> -> |n> transiton is 1600*n  cm^-1


#define numbers for AB terms
Mge = 1 #M^eg_0
dMgedQ = 0.04 #dM^eg / dQ
Lge = 0.1 #Lambda^eg_0
dLeg = 0.004 #dLambda^eg / dQ


"""Define the A and B terms"""
y = np.linspace(5000, 60000, 2750000) #the frequency


A = Mge * Lge * (f01(d)*f00(d)*Deltaevgo(0,y,0) + f11(d)*f10(d)*Deltaevgo(1,y,1) + f21(d)*f20(d)*Deltaevgo(2,y,2)) 

#B1 terms
B10 = Mge*f01(d) * (dLeg * h00(d)) * Deltaevgo(0, y, 0) #the v' = 0 term
B11 = Mge*f11(d) * (dLeg* h10(d)) * Deltaevgo(1, y, 1) #the v' = 1 term
B12 = Mge*f21(d) * (dLeg * h20(d)) * Deltaevgo(2, y, 2) #the v' = 2 term

B1 = B10 + B11 + B12

#B2 terms
B20 = dMgedQ * Lge *(h01(d) * f00(d)) * Deltaevgo(0, y, 0) #the v' = 0 term
B21 = dMgedQ * Lge *(h11(d) * f10(d)) * Deltaevgo(1, y, 1) #the v' = 1 term
B22 = dMgedQ * Lge *(h21(d) * f20(d)) * Deltaevgo(2, y, 2) #the v' = 2 term

B2 = B20 + B21 + B22

#Real parts
totRe = A.real + B1.real + B2.real
ARe = A.real / totRe.max()
BRe = (B1+B2).real / totRe.max()
B1Re = B1.real / totRe.max()
B2Re = B2.real / totRe.max()

#Im parts
totIm = A.imag + B1.imag + B2.imag
AIm = A.imag / totIm.max()
BIm = (B1+B2).imag / totIm.max()
B1Im = B1.imag / totIm.max()
B2Im = B2.imag / totIm.max()


# absolute value
tot = np.abs(A+B1+B2)
abs_max = tot.max() #need to scale
"""Plot the A and B terms"""

ax1 = plt.subplot(gs[0,1])

ax1.plot(y, tot / abs_max, linewidth = '2', label = r'$\mathsf{|A + B|}$', color = 'black', zorder = 4)
ax1.plot(y, np.abs(A) / abs_max, linewidth = '2', label = r'$\mathsf{|A|}$', zorder = 3)
ax1.plot(y, np.abs(B1+B2) / abs_max, linewidth = '2', label = r'$\mathsf{|B|}$', zorder = 3)
ax1.plot(y, np.abs(B1) / abs_max, linewidth = '2', label = r'$\mathsf{|B_1|}$', zorder = 2)
ax1.plot(y, np.abs(B2) / abs_max, linewidth = '2', label = r'$\mathsf{|B_2|}$', zorder = 1)

ax1.set_ylabel(r'$\mathsf{Amplitude \ (norm.)}$', fontsize = fontsize)
ax1.set_xlabel(r'$\mathsf{2\omega_2} \ (\mathsf{cm}^{-1})$', fontsize = fontsize)

ax1.set_yscale('log')
ax1.set_ylim(0.0001, 2)


#put lines at the vibronic resonances
for i in [0,1,2]:
    ax1.vlines(x = 30000+1600*i, ymin = 0.00005, ymax = 4, color = 'gray', linestyle = '--', linewidth = 1)

"""The Real and Imaginary Parts of Gamma"""


#plot Re A and B
ax2 = plt.subplot(gs[1,0])
ax2.plot(y, totRe / totRe.max(), linewidth = '2', label = '$\mathsf{A + B}$', color = 'black', zorder = 4)
ax2.plot(y, ARe, linewidth = '2', label = r'$\mathsf{A}$', zorder = 3)
ax2.plot(y, BRe, linewidth = '2', label = r'$\mathsf{B}$', zorder = 3)
ax2.plot(y, B1Re, linewidth = '2', label = r'$\mathsf{B_1}$', zorder = 2)
ax2.plot(y, B2Re, linewidth = '2', label = r'$\mathsf{B_2}$', zorder = 1)
ax2.set_ylabel(r'$\mathsf{Re(\gamma)}$', fontsize = fontsize)
ax2.set_xlabel(r'$\mathsf{2\omega_2} \ (\mathsf{cm}^{-1})$', fontsize = fontsize)

#plot Im A and B
ax3 = plt.subplot(gs[1,1])
ax3.plot(y, totIm / totIm.max(), linewidth = '2', label = '$\mathsf{A + B}$', color = 'black', zorder = 4)
ax3.plot(y, AIm, linewidth = '2', label = r'$\mathsf{A}$', zorder = 3)
ax3.plot(y, BIm, linewidth = '2', label = r'$\mathsf{B}$', zorder = 3)
ax3.plot(y, B1Im, linewidth = '2', label = r'$\mathsf{B_1}$', zorder = 2)
ax3.plot(y, B2Im, linewidth = '2', label = r'$\mathsf{B_2}$', zorder = 1)
ax3.set_ylabel(r'$\mathsf{Im(\gamma)}$', fontsize = fontsize)
ax3.set_xlabel(r'$\mathsf{2\omega_2} \ (\mathsf{cm}^{-1})$', fontsize = fontsize)
    
    
for ax in [ax1, ax2, ax3]:
    ax.set_xlim(20000, 45000)
    xticks = np.linspace(20000, 45000, 6)
    ax.set_xticks(xticks)
    ax.legend(loc = 1)
    ax.hlines(xmin=10000, xmax =50000, y = 0, color = 'gray', linestyle = '--', linewidth = 1)

for i, ax in enumerate(fig.axes):
    # ax.grid(visible=True, color="k", lw=0.5, linestyle=":")
    wt.artists.corner_text("abcd"[i], ax=ax, corner = 'UL', distance = 0.25, bbox = True, fontsize = fontsize, background_alpha=0.75)

if save:
    wt.artists.savefig(here / "drsive_spectrum.png", transparent = True, bbox_inches='tight')
