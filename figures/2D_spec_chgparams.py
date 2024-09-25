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

#define harmonic wells and coordinates
d = 0.5 #offset for es
do = 0 #gs placement

#make figure
cols = [1, 1] 
aspects = [[[0, 0], 1], [[1, 0], 1]] 

fig, gs = wt.artists.create_figure(width="dissertation", nrows=2, cols=cols, aspects=aspects, hspace=0.7, wspace=1.2) 

#define Franck-Condon factors following page 164 of Roger Carlson's thesis in terms of 'q', the offset
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

#define Herzberg Teller overlap integrals following page 165 of Roger Carlson's thesis in terms of q
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
Mge0 = 0.1 #M^eg_0
Lge0 = 0.01 #Lambda^eg_0
dLeg0 = 0.0007 #dLambda^eg / dQ
dMgedQ0 = 0.007 #dM^eg / dQ


#define terms
y = np.linspace(10000, 60000, 2750000)

def A(Mge, Lge):
    return Mge * Lge * (f01(d)*f00(d)*Deltaevgo(0,y,0) + f11(d)*f10(d)*Deltaevgo(1,y,1) + f21(d)*f20(d)*Deltaevgo(2,y,2)) #there must be a simpler way to do this but idk

#B1 terms
def B1(Mge, dLeg):
    return Mge*f01(d) * (dLeg * h00(d)) * Deltaevgo(0, y, 0) + Mge*f11(d) * (dLeg* h10(d)) * Deltaevgo(1, y, 1) + Mge*f21(d) * (dLeg * h20(d)) * Deltaevgo(2, y, 2) #the v' = 2 term

#B2 terms
def B2(Lge, dMgedQ):
    return dMgedQ * Lge *(h01(d) * f00(d)) * Deltaevgo(0, y, 0) + dMgedQ * Lge *(h11(d) * f10(d)) * Deltaevgo(1, y, 1) + dMgedQ * Lge *(h21(d) * f20(d)) * Deltaevgo(2, y, 2) #the v' = 2 term

# #Real parts
# totRe = A.real + B1.real + B2.real
# ARe = A.real / totRe.max()
# BRe = (B1+B2).real / totRe.max()
# B1Re = B1.real / totRe.max()
# B2Re = B2.real / totRe.max()

# #Im parts
# totIm = A.imag + B1.imag + B2.imag
# AIm = A.imag / totIm.max()
# BIm = (B1+B2).imag / totIm.max()
# B1Im = B1.imag / totIm.max()
# B2Im = B2.imag / totIm.max()


# absolute value
def tot(Mge, Lge, dLeg, dMgedQ):
    return np.abs(A(Mge, Lge) + B1(Mge, dLeg) + B2(dMgedQ, Lge))
# abs_max = tot.max()

#plot the A and B
ax0 = plt.subplot(gs[0,0])

ax0.plot(y, tot(Mge0, Lge0, dLeg0, dMgedQ0) / tot(Mge0, Lge0, dLeg0, dMgedQ0).max(), linewidth = '2', label = r'$\mathsf{++++}$', zorder = 4)
ax0.plot(y, tot(-Mge0, Lge0, dLeg0, dMgedQ0) / tot(-Mge0, Lge0, dLeg0, dMgedQ0).max(), linewidth = '2', label = r'$\mathsf{-+++}$', zorder = 4)
ax0.plot(y, tot(Mge0, -Lge0, dLeg0, dMgedQ0) / tot(Mge0, -Lge0, dLeg0, dMgedQ0).max(), linewidth = '2', label = r'$\mathsf{+-++}$', zorder = 4)
ax0.plot(y, tot(Mge0, Lge0, -dLeg0, dMgedQ0) / tot(Mge0, Lge0, -dLeg0, dMgedQ0).max(), linewidth = '2', label = r'$\mathsf{++-+}$', zorder = 4)



ax1 = plt.subplot(gs[0,1])
ax1.plot(y, tot(-Mge0, Lge0, dLeg0, dMgedQ0) / tot(-Mge0, Lge0, dLeg0, dMgedQ0).max(), linewidth = '2', label = r'$\mathsf{|A + B|}$', color = 'black', zorder = 4)

for ax in [ax0, ax1]:
    ax.set_ylabel(r'$\mathsf{Amplitude \ (norm.)}$', fontsize = fontsize)
    ax.set_xlabel(r'$\mathsf{2\omega_2} \ (\mathsf{cm}^{-1})$', fontsize = fontsize)
    
    ax.set_yscale('log')
    ax.set_xlim(20000, 45000)
    xticks = np.linspace(20000, 45000, 6)
    ax.set_xticks(xticks)
    ax.set_ylim(0.001, 2)
    ax.legend(loc = 1)


#put lines at the vibronic resonances
    for i in [0,1,2]:
        ax.vlines(x = 30000+1600*i, ymin = 0.0005, ymax = 4, color = 'gray', linestyle = '--', linewidth = 1)

for i, ax in enumerate(fig.axes):
    # ax.grid(visible=True, color="k", lw=0.5, linestyle=":")
    wt.artists.corner_text("abcd"[i], ax=ax, corner = 'UL', distance = 0.25, bbox = True, fontsize = fontsize, background_alpha=0.75)

if save:
    wt.artists.savefig(here / "drsive_spectrum.png", transparent = True, bbox_inches='tight')
