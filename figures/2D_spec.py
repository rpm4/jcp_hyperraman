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

save = True

fontsize = 18

#define harmonic wells and coordinates
d = 0.5 #offset for es
do = 0 #gs placement

def grs(k):
    return 0.125*(k-do)**2

def es(k):
    return 0.125*(k-d-do)**2 + 0.7

kg = np.linspace(-2, 2, 500) #ground state coordinates
ke = np.linspace(-1.75, 2.75, 500) #excited state coordinates

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


#define resonance denominator
def Deltaevgo(v,x,l):
    weg = 30000
    G = [1000, 1000, 1000] #linewidths
    return 1/(weg + 1500*v - x - 1j*G[l]) #assuming the |0> -> |n> transiton is 1500*n  cm^-1


#define numbers for AB terms
Mge = 0.1
alphage = 0.01
dMem = 0.00004
dMmg = 0.00004
dMgedQ = 0.0008


#define terms
y = np.linspace(15000, 45000, 120000)


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

#conjugate - This is because these quantities are imaginary. We need to plot sqrt(Re(A)^2 + Im(A)^2) to get the actual lineshape. Re(A) is just the dispersive lineshape (index of refraction)
A = A * A.conjugate()
B1 = B1 * B1.conjugate()
B2 = B2 * B2.conjugate()

#make figure
cols = [1, 1] 
aspects = [[[0, 0], 1], [[1, 0], 0.2]] 

fig, gs = wt.artists.create_figure(width="double", nrows=2, cols=cols, aspects=aspects, wspace=1) 

ax0 = plt.subplot(gs[0,0])

#hbar omega_eg arrow insert
yarrow = [grs(0.6), es(1.3)] #where the arrows start and end
yarrowstop = [(grs(0.6) + es(1.3))/2 - 0.06, (grs(0.6) + es(1.3))/2 + 0.06] #to put in the hbaromegaeg
myArrow0 = FancyArrowPatch(posA=(-0.35, yarrow[0]), posB=(-0.35, yarrowstop[0]), arrowstyle='<|-', color='blue',
                           mutation_scale=25, shrinkA=0, shrinkB=0, linewidth = 4)
myArrow1 = FancyArrowPatch(posA=(-0.35, yarrowstop[1]), posB=(-0.35, yarrow[1]), arrowstyle='-|>', color='blue', 
                           mutation_scale=25, shrinkA=0, shrinkB=0, linewidth = 4)
ax0.add_artist(myArrow0)
ax0.add_artist(myArrow1)

ax0.text(-0.7, (grs(0.6) + es(1.3))/2 - 0.023, '$\mathsf{\hbar \omega_{eg}}$', fontsize = 24)

#xi arrow insert
xarrow = [do, d] #where the arrows start and end
xiarrow = FancyArrowPatch(posA=(xarrow[0], -0.027), posB=(xarrow[1], -0.027), arrowstyle='<|-|>', color='blue',  mutation_scale=12, shrinkA=0, shrinkB=0, linewidth = 1)
ax0.add_artist(xiarrow)


ax0.text((do+d)/2-0.08, -0.081, '$\mathsf{\\xi}$', fontsize = 18)

#labeling vibrational states
jgs = [0.6, 1.0]
for i in [0,1]:
    ax0.hlines(y = grs(jgs[i]), xmin = -jgs[i], xmax = jgs[i], color = 'black', linestyle = '-', linewidth = 2)
    ax0.text(jgs[i] + 0.25, grs(jgs[i])-0.03, str(i), fontsize = 16)
    
jes = [1.3, 1.7, 1.9965]
for i in [0,1,2]:
    ax0.hlines(y = es(jes[i]), xmin = -jes[i]+2*d, xmax = jes[i], color = 'black', linestyle = '-', linewidth = 2)
    ax0.text(jes[i] + 0.25, es(jes[i])-0.03, str(i), fontsize = 16)
    
#harmonic surface labels
ax0.text(kg.max()+0.12, grs(kg.max())-0.05, '$\mathsf{|g \\rangle}$', fontsize = 24)
ax0.text(ke.max()+0.12, es(ke.max())-0.05, '$\mathsf{|e \\rangle}$', fontsize = 24)

#plot it
ax0.plot(kg,grs(kg), linewidth = '4', color = 'teal')
ax0.plot(ke,es(ke), linewidth = '4', color = 'teal')
ax0.set_ylabel('$\mathsf{Energy \ (cm^{-1})}$', fontsize = fontsize)
ax0.set_xlabel('$\mathsf{Q \ (arb.)}$', fontsize = fontsize)
plt.ylim(-0.1, 1.4)
plt.xlim(-3.35,3.35)
plt.yticks(ticks = [])
plt.xticks(ticks = [])

#math on the A and B so that we can log plot and normalize / inspect
tot = np.sqrt(A+B1+B2)
A = np.sqrt(A)/(tot.max())  ##normalizing wrt \sqrt(A+B) to demonstrate how each term contributes
B1 = np.sqrt(B1)/(tot.max())
B2 = np.sqrt(B2)/(tot.max())
tot[:] = (tot[:] - tot.min()) / (tot.max() - tot.min())

#plot the A and B
ax1 = plt.subplot(gs[0,1])
ax1.plot(y, tot , linewidth = '2', label = '$\mathsf{A + B}$', color = 'black', zorder = 4)
ax1.plot(y, A, linewidth = '2', label = '$\mathsf{A}$', color = 'cyan', zorder = 3)
ax1.plot(y, B1, linewidth = '2', label = '$\mathsf{B_1}$', color = 'orange', zorder = 2)
ax1.plot(y, B2, linewidth = '2', label = '$\mathsf{B_2}$', color = 'green', zorder = 1)
ax1.set_ylabel('$\mathsf{Amplitude \ (norm.)}$', fontsize = fontsize)
ax1.set_xlabel(r'$\mathsf{2\omega_2} \ (\mathsf{cm}^{-1})$', fontsize = fontsize)

ax1.set_yscale('log')
ax1.set_xlim(20000, 40000)
ax1.set_ylim(0.001, 2.2)


plt.legend(loc = 1)

for i, ax in enumerate(fig.axes):
    # ax.grid(visible=True, color="k", lw=0.5, linestyle=":")
    wt.artists.corner_text("abcd"[i], ax=ax, corner = 'UL', distance = 0.25, bbox = True, fontsize = fontsize, background_alpha=0.75)

if save:
    wt.artists.savefig("drsive_spectrum.png", transparent = True, bbox_inches='tight')
