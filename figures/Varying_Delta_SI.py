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
d = [0.1, 0.2, 0.6] #offset for es

#make figure
cols = [1, 1] 
aspects = [[[0, 0], 1], [[1, 0], 1]] 



#todo: make an array so I can just call specific matrix element of the fc and ht factors, then do a for loop over that array, should work out well.


#define Franck-Condon factors following page 164 of Roger Carlson's thesis in terms of 'q', the offset
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
    return 1/(weg + 1600*v - x - 1j*G[l]) #assuming the |0> -> |n> transiton is 2200*n  cm^-1


#define numbers for AB terms
Mge = 0.1 #M^eg_0
Lge = 0.01 #Lambda^eg_0
dLeg = 0.0007 #dLambda^eg / dQ
dMgedQ = 0.007 #dM^eg / dQ


#define terms
y = np.linspace(10000, 50000, 3000000)
# y = 31000

# d = np.linspace(0, 1, 1000)



def A(d):
    return Mge * Lge * (f01(d)*f00(d)*Deltaevgo(0,y,0) + f11(d)*f10(d)*Deltaevgo(1,y,1) + f21(d)*f20(d)*Deltaevgo(2,y,2)) #there must be a simpler way to do this but idk

#B1 terms
def B1(d):
    # B10 = Mge*f10(d) * (dLeg * h00(d)) * Deltaevgo(0, y, 0) #the v' = 0 term
    # B11 = Mge*f11(d) * (dLeg* h10(d)) * Deltaevgo(1, y, 1) #the v' = 1 term
    # B12 = Mge*f12(d) * (dLeg * h20(d)) * Deltaevgo(2, y, 2) #the v' = 2 term
    # return B10 + B11 + B12
    return Mge*f01(d) * (dLeg * h00(d)) * Deltaevgo(0, y, 0) + Mge*f11(d) * (dLeg* h10(d)) * Deltaevgo(1, y, 1) + Mge*f21(d) * (dLeg * h20(d)) * Deltaevgo(2, y, 2)

#B2 terms
def B2(d):
    # B20 = dMgedQ * Lge *(h10(d) * f00(d)) * Deltaevgo(0, y, 0) #the v' = 0 term
    # B21 = dMgedQ * Lge *(h11(d) * f10(d)) * Deltaevgo(1, y, 1) #the v' = 1 term
    # B22 = dMgedQ * Lge *(h12(d) * f20(d)) * Deltaevgo(2, y, 2) #the v' = 2 term
    # return B20 + B21 + B22
    return dMgedQ * Lge *(h01(d) * f00(d)) * Deltaevgo(0, y, 0) + dMgedQ * Lge *(h11(d) * f10(d)) * Deltaevgo(1, y, 1) + dMgedQ * Lge *(h21(d) * f20(d)) * Deltaevgo(2, y, 2) 

def tot(d):
    tot = np.abs(A(d)+B1(d)+B2(d))
    return tot

    # def B1B2(d):
    #     return np.abs(B1(d) + B2(d)) / abs_max
        
    # def A1(d):
    #     return np.abs(A(d))/abs_max

# #Real parts
# totRe = A.real + B1.real + B2.real
# ARe = A.real / totRe.max()
# B1Re = B1.real / totRe.max()
# B2Re = B2.real / totRe.max()

# #Im parts
# totIm = A.imag + B1.imag + B2.imag
# AIm = A.imag / totIm.max()
# B1Im = B1.imag / totIm.max()
# B2Im = B1.imag / totIm.max()

#try a data object
# d = wt.Data(name = 'test')
# d.create_variable('energy', values = y, units = 'wn')
# d.create_variable('delta', values = [0.1, 0.2, 0.6])



# absolute value


# tot = np.abs(A+B1+B2)
# abs_max = tot.max()



#plot
fig, gs = wt.artists.create_figure(width="dissertation", nrows=2, cols=cols, aspects=aspects, wspace=1) 
d1 = 0.5
abs_max = tot(d1).max()
ax0 = plt.subplot(gs[0,0])#\Delta = 0.1
ax0.plot(y, tot(d1)/abs_max, linewidth = '2', label = r'$\mathsf{|A + B|}$', color = 'black', zorder = 4)
ax0.plot(y, np.abs(A(d1)) / abs_max, linewidth = '2', label = r'$\mathsf{|A|}$', color = 'cyan', zorder = 3)
ax0.plot(y, np.abs(B1(d1)+B2(d1)) / abs_max, linewidth = '2', label = r'$\mathsf{|B|}$', color = 'red', zorder = 3)
# ax0.plot(y, np.abs(B1(d1)) / abs_max, linewidth = '2', label = r'$\mathsf{|B_1|}$', color = 'orange', zorder = 2)
# ax0.plot(y, np.abs(B2(d1)) / abs_max, linewidth = '2', label = r'$\mathsf{|B_2|}$', color = 'green', zorder = 1)
ax0.set_ylabel(r'$\mathsf{Amplitude \ (norm.)}$', fontsize = fontsize)
ax0.set_xlabel(r'$\mathsf{2\omega_2} \ (\mathsf{cm}^{-1})$', fontsize = fontsize)
ax0.text(20000, 2, r'$\mathsf{\Delta = 1/\sqrt{2}}$', fontsize = 16)


#plot the A and B

ax1 = plt.subplot(gs[0,1])
d2 = 0.09
abs_max1 = tot(d2).max()
ax1.plot(y, tot(d2) / abs_max1, linewidth = '2', label = r'$\mathsf{|A + B|}$', color = 'black', zorder = 4)
ax1.plot(y, np.abs(A(d2)) / abs_max1, linewidth = '2', label = r'$\mathsf{|A|}$', color = 'cyan', zorder = 3)
ax1.plot(y, np.abs(B1(d2)+B2(d2)) / abs_max1, linewidth = '2', label = r'$\mathsf{|B|}$', color = 'red', zorder = 3)
# ax1.plot(y, np.abs(B1(d2)) / abs_max1, linewidth = '2', label = r'$\mathsf{|B_1|}$', color = 'orange', zorder = 2)
# ax1.plot(y, np.abs(B2(d2)) / abs_max1, linewidth = '2', label = r'$\mathsf{|B_2|}$', color = 'green', zorder = 1)
ax1.set_ylabel(r'$\mathsf{Amplitude \ (norm.)}$', fontsize = fontsize)
ax1.set_xlabel(r'$\mathsf{2\omega_2} \ (\mathsf{cm}^{-1})$', fontsize = fontsize)

for ax in [ax0, ax1]:
    ax.set_yscale('log')
    ax.set_xlim(15000, 45000)
    xticks = np.linspace(15000, 45000, 7)
    ax.set_xticks(xticks)
    ax.set_ylim(0.0001, 3.4)
    ax.legend(loc = 1)
    for i in [0,1,2]:
        ax.vlines(x = 30000+2200*i, ymin = 0.00005, ymax = 4, color = 'gray', linestyle = '--', linewidth = 1)

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
    wt.artists.savefig("changedelta.png", transparent = True, bbox_inches='tight')
