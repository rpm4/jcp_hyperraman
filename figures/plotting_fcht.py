# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:28:39 2023

@author: rpm
"""
import numpy as np
import WrightTools as wt
import matplotlib.pyplot as plt 
from matplotlib.patches import FancyArrowPatch

wt.artists.apply_rcparams(kind="publication")

save = False
fontsize = 18

#define harmonic wells and coordinates
d = np.linspace(0, 5, 5000)

#make figure
cols = [1, 1] 
aspects = [[[0, 0], 1], [[1, 0], 1]] 



#todo: make an array so I can just call specific matrix element of the fc and ht factors, then do a for loop over that array, should work out well.


#define Franck-Condon factors following page 164 of Roger Carlson's thesis in terms of 'q', the offset
def f00(q): #<0|0>
    return np.e**(-q**2/4)

def f01(q): #<0|1>
    return -q/(np.sqrt(2)) * f00(q)

def f10(q): #<1|0>
    return -1*f01(q)

def f11(q): #<1|1>
    return (1 - q**2/2) *f00(q)

def f02(q): #<0|2>
    return q**2/(2*np.sqrt(2)) * f00(q)

def f20(q): #<2|0>
    return f02(q)

def f12(q): #<1|2>
    return -q * (1 - q**2/4) *f00(q)
    

#define Herzberg Teller overlap integrals following page 165 of Roger Carlson's thesis in terms of q
def h00(q): #<0|Q|0>
    return -q/2 * f00(q)

def h01(q): #<0|Q|1>
    return 1/np.sqrt(2) * (1 + q**2 /2) * f00(q)

def h10(q): #<1|Q|0>
    return 1/np.sqrt(2) * (1 - q**2 /2) * f00(q)

def h11(q): #<1|Q|1>
    return -q/2 * (1 - q**2 / 2) * f00(q)

def h12(q): #<1|Q|2>
    return (1 + q**2/4 - q**4/8) * f00(q)

def h20(q): #<2|Q|0>
    return -q/np.sqrt(2) * (1 - q**2 /4) * f00(q)


#plot
fig, gs = wt.artists.create_figure(width="dissertation", nrows=2, cols=cols, aspects=aspects, wspace=1) 
ax0 = plt.subplot(gs[0,0])
ax0.plot(d, f00(d), linewidth = '2', label = r'$\mathsf{00}$', color = 'black', zorder = 4)
ax0.plot(d, f01(d), linewidth = '2', label = r'$\mathsf{01}$', color = 'cyan', zorder = 3)
ax0.plot(d, f10(d), linewidth = '2', label = r'$\mathsf{10}$', color = 'red', zorder = 3)
ax0.plot(d, f11(d), label = r'$\mathsf{11}$', color = 'orange', zorder = 2)
ax0.plot(d, f02(d), linewidth = '2', label = r'$\mathsf{02}$', color = 'green', zorder = 1)
ax0.plot(d, f20(d), linewidth = '2', label = r'$\mathsf{20}$', color = 'pink', zorder = 1)
ax0.plot(d, f12(d), linewidth = '2', label = r'$\mathsf{12}$', color = 'yellow', zorder = 1)
ax0.set_ylabel(r'$\mathsf{Integral \ Value \ (norm.)}$', fontsize = fontsize)

# ax0.text(20000, 2, r'$\mathsf{\Delta = 1/\sqrt{2}}$', fontsize = 16)


#plot the A and B

ax1 = plt.subplot(gs[0,1])
ax1.plot(d, h00(d), linewidth = '2', label = r'$\mathsf{00}$', color = 'black', zorder = 4)
ax1.plot(d, h01(d), linewidth = '2', label = r'$\mathsf{01}$', color = 'cyan', zorder = 3)
ax1.plot(d, h10(d), linewidth = '2', label = r'$\mathsf{10}$', color = 'red', zorder = 3)
ax1.plot(d, h11(d), label = r'$\mathsf{11}$', color = 'orange', zorder = 2)
ax1.plot(d, h20(d), linewidth = '2', label = r'$\mathsf{20}$', color = 'green', zorder = 1)
ax1.plot(d, h12(d), linewidth = '2', label = r'$\mathsf{12}$', color = 'pink', zorder = 1)

for ax in [ax0, ax1]:
    # ax.set_yscale('log')
    ax.set_xlim(0,3)
    ax.set_xlabel(r'$\mathsf{\Delta}$', fontsize = fontsize)
    # xticks = np.linspace(15000, 45000, 7)
    # ax.set_xticks(xticks)
    ax.set_ylim(-1/np.sqrt(2), 2)
    ax.legend(loc = 1)
    for d in [np.sqrt(2), 1/np.sqrt(2)]:
        ax.vlines(x = d, ymin = -1, ymax = 2, color = 'gray', linestyle = '--', linewidth = 1)
        ax.hlines(xmin=0, xmax =5, y = 0, color = 'gray', linestyle = '--', linewidth = 1)
    

#put lines at the vibronic resonances


# others = False #debating if to include the Re and Im parts of gamma
# if others:
#     #plot Re A and B
#     ax2 = plt.subplot(gs[1,0])
#     # ax2.plot(y, totRe , linewidth = '2', label = '$\mathsf{A + B}$', color = 'black', zorder = 4)
#     ax2.plot(y, ARe, linewidth = '2', label = r'$\mathsf{A}$', color = 'cyan', zorder = 3)
#     ax2.plot(y, B1Re, linewidth = '2', label = r'$\mathsf{B_1}$', color = 'orange', zorder = 2)
#     ax2.plot(y, B2Re, linewidth = '2', label = r'$\mathsf{B_2}$', color = 'green', zorder = 1)
#     ax2.set_ylabel(r'$\mathsf{Re(\gamma) \ (norm.)}$', fontsize = fontsize)
#     ax2.set_xlabel(r'$\mathsf{2\omega_2} \ (\mathsf{cm}^{-1})$', fontsize = fontsize)
    
#     #ax2.set_yscale('log')
#     ax2.set_xlim(20000, 40000)
#     # ax2.set_ylim(0.001, 2.2)
#     ax2.legend(loc = 1)
    
#     #plot Im A and B
#     ax3 = plt.subplot(gs[1,1])
#     # ax3.plot(y, totIm , linewidth = '2', label = '$\mathsf{A + B}$', color = 'black', zorder = 4)
#     ax3.plot(y, AIm, linewidth = '2', label = r'$\mathsf{A}$', color = 'cyan', zorder = 3)
#     ax3.plot(y, B1Im, linewidth = '2', label = r'$\mathsf{B_1}$', color = 'orange', zorder = 2)
#     ax3.plot(y, B2Im, linewidth = '2', label = r'$\mathsf{B_2}$', color = 'green', zorder = 1)
#     ax3.set_ylabel(r'$\mathsf{Im(\gamma) \ (norm.)}$', fontsize = fontsize)
#     ax3.set_xlabel(r'$\mathsf{2\omega_2} \ (\mathsf{cm}^{-1})$', fontsize = fontsize)
    
#     # ax3.set_yscale('log')
#     ax3.set_xlim(20000, 40000)
#     # ax2.set_ylim(0.001, 2.2)
#     ax3.legend(loc = 1)

for i, ax in enumerate(fig.axes):
    # ax.grid(visible=True, color="k", lw=0.5, linestyle=":")
    wt.artists.corner_text("abcd"[i], ax=ax, corner = 'UL', distance = 0.35, bbox = True, fontsize = fontsize, background_alpha=0.75)

if save:
    wt.artists.savefig("drsive_spectrum.png", transparent = True, bbox_inches='tight')
