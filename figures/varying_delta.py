import numpy as np
import WrightTools as wt
import matplotlib.pyplot as plt 
import pathlib

wt.artists.apply_rcparams(kind="publication")

save = True
fontsize = 18
here = pathlib.Path(__file__).resolve().parent

#make figure
cols = [1, 1] 
aspects = [[[0, 0], 1], [[1, 0], 1]] 



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
def Deltaevgo(n,x,l,G):
    weg = 30000
    return 1/(weg + l*n - x - 1j*G) #assuming the |0> -> |n> transiton is l*n  cm^-1


#define numbers for AB terms
Mge = 1 #M^eg_0
dMgedQ = 0.04 #dM^eg / dQ
Lge = 0.1 #Lambda^eg_0
dLeg = 0.004 #dLambda^eg / dQ


#define terms
y = np.linspace(12000, 52000, 3000000)



def A(d, w, G):
    return Mge * Lge * (f01(d)*f00(d)*Deltaevgo(0,y,w,G) + f11(d)*f10(d)*Deltaevgo(1,y,w,G) + f21(d)*f20(d)*Deltaevgo(2,y,w,G)) #there must be a simpler way to do this but idk

#B1 terms
def B1(d,w, G):
    return Mge*f01(d) * (dLeg * h00(d)) * Deltaevgo(0, y, w, G) + Mge*f11(d) * (dLeg* h10(d)) * Deltaevgo(1, y, w, G) + Mge*f21(d) * (dLeg * h20(d)) * Deltaevgo(2, y, w, G)

#B2 terms
def B2(d,w, G):
    return dMgedQ * Lge *(h01(d) * f00(d)) * Deltaevgo(0, y, w, G) + dMgedQ * Lge *(h11(d) * f10(d)) * Deltaevgo(1, y, w, G) + dMgedQ * Lge *(h21(d) * f20(d)) * Deltaevgo(2, y, w, G) 

def tot(d,w,G):
    tot = np.abs(A(d,w, G)+B1(d,w,G)+B2(d,w,G))
    return tot

textplace = 18000 #where words will live

#plot
fig, gs = wt.artists.create_figure(width="dissertation", nrows=2, cols=cols, aspects=aspects, hspace=0.7, wspace=1.2) 
d1 = 0.87 #offset
wvib = 1190 #vib frequency
width = 175 #linewidth
abs_max = tot(d1, wvib, width).max()
ax0 = plt.subplot(gs[0,0])#\Delta = 0.1
ax0.plot(y, tot(d1, wvib, width)/abs_max, linewidth = '2', label = r'$\mathsf{|A + B|}$', color = 'black', zorder = 4)
ax0.plot(y, np.abs(A(d1, wvib, width)) / abs_max, linewidth = '2', label = r'$\mathsf{|A|}$', zorder = 3)
ax0.plot(y, np.abs(B1(d1, wvib, width)+B2(d1, wvib, width)) / abs_max, linewidth = '2', label = r'$\mathsf{|B|}$', zorder = 3)

ax0.set_ylabel(r'$\mathsf{Amplitude \ (norm.)}$', fontsize = fontsize)
ax0.set_xlabel(r'$\mathsf{2\omega_2} \ (\mathsf{cm}^{-1})$', fontsize = fontsize)
ax0.text(textplace, 0.8, r'$\mathsf{\Delta = 0.87}$', fontsize = 16)
ax0.text(textplace, 0.4, r'$\mathsf{\omega_{g1,g0} = 1190 \ cm^{-1}}$', fontsize = 16)
ax0.text(textplace, 0.2, r'$\mathsf{\Gamma = 175 \ cm^{-1}}$', fontsize = 16)


ax1 = plt.subplot(gs[0,1])
d2 = 0.26 #offset
wvib_1 = 932 #vib frequency
width1 = 175 #linewidth
abs_max1 = tot(d2, wvib_1, width1).max()
ax1.plot(y, tot(d2, wvib_1, width1)/abs_max1, linewidth = '2', label = r'$\mathsf{|A + B|}$', color = 'black', zorder = 4)
ax1.plot(y, np.abs(A(d2, wvib_1, width1)) / abs_max1, linewidth = '2', label = r'$\mathsf{|A|}$', zorder = 3)
ax1.plot(y, np.abs(B1(d2, wvib_1, width1)+B2(d2, wvib_1, width1)) / (abs_max1), linewidth = '2', label = r'$\mathsf{|B|}$', zorder = 3)
ax1.text(textplace, 0.8, r'$\mathsf{\Delta = 0.26}$', fontsize = 16)
ax1.text(textplace, 0.4, r'$\mathsf{\omega_{g1,g0} = 932 \ cm^{-1}}$', fontsize = 16)
ax1.text(textplace, 0.2, r'$\mathsf{\Gamma = 175 \ cm^{-1}}$', fontsize = 16)


#mof

ax2 = plt.subplot(gs[1,0])
d2 = 0.0275 #offset
wvib_2 = 1200 #vib frequency
width2 = 300 #linewidth
abs_max1 = tot(d2, wvib_2, width2).max()

ax2.plot(y, tot(d2, wvib_2, width2)/abs_max1, linewidth = '2', label = r'$\mathsf{|A + B|}$', color = 'black', zorder = 4)
ax2.plot(y, np.abs(A(d2, wvib_2, width2)) / abs_max1, linewidth = '2', label = r'$\mathsf{|A|}$', zorder = 3)
ax2.plot(y, np.abs(B1(d2, wvib_2, width2)+B2(d2, wvib_2, width2)) / (abs_max1), linewidth = '2', label = r'$\mathsf{|B|}$', zorder = 3) #remember we need |A/B| ~ 0.1 even when not exactly the case...
ax2.text(textplace, 0.8, r'$\mathsf{\Delta = 0.0275}$', fontsize = 16)
ax2.text(textplace, 0.4, r'$\mathsf{\omega_{g1,g0} = 1200 \ cm^{-1}}$', fontsize = 16)
ax2.text(textplace, 0.2, r'$\mathsf{\Gamma = 300 \ cm^{-1}}$', fontsize = 16)

ax3 = plt.subplot(gs[1,1])
d3 = 0.1350 #offset
wvib_3 = 1610 #vib frequency
width3 = 300
abs_max1 = tot(d3, wvib_3, width3).max()

ax3.plot(y, tot(d3, wvib_3, width3)/abs_max1, linewidth = '2', label = r'$\mathsf{|A + B|}$', color = 'black', zorder = 4)
ax3.plot(y, np.abs(A(d3, wvib_3, width3)) / abs_max1, linewidth = '2', label = r'$\mathsf{|A|}$', zorder = 3)
ax3.plot(y, np.abs(B1(d3, wvib_3, width3)+B2(d3, wvib_3, width3)) / (abs_max1), linewidth = '2', label = r'$\mathsf{|B|}$', zorder = 3)
ax3.text(textplace, 0.8, r'$\mathsf{\Delta = 0.135}$', fontsize = 16)
ax3.text(textplace, 0.4, r'$\mathsf{\omega_{g1,g0} = 1610 \ cm^{-1}}$', fontsize = 16)
ax3.text(textplace, 0.2, r'$\mathsf{\Gamma = 300 \ cm^{-1}}$', fontsize = 16)

for ax in [ax0, ax1, ax2, ax3]:
    ax.set_yscale('log')
    ax.set_xlim(15000, 45000)
    xticks = np.linspace(15000, 45000, 7)
    ax.set_xticks(xticks)
    ax.set_ylim(0.000075, 1.6)
    ax.legend(loc = 1)
    ax.set_ylabel(r'$\mathsf{Amplitude \ (norm.)}$', fontsize = fontsize)
    ax.set_xlabel(r'$\mathsf{2\omega_2} \ (\mathsf{cm}^{-1})$', fontsize = fontsize)

#put lines at the vibronic resonances
for i in [0,1,2]:
    ax0.vlines(x = 30000+wvib*i, ymin = 0.00005, ymax = 4, color = 'gray', linestyle = '--', linewidth = 1)
    ax1.vlines(x = 30000+wvib_1*i, ymin = 0.00005, ymax = 4, color = 'gray', linestyle = '--', linewidth = 1)
    ax2.vlines(x = 30000+wvib_2*i, ymin = 0.00005, ymax = 4, color = 'gray', linestyle = '--', linewidth = 1)
    ax3.vlines(x = 30000+wvib_3*i, ymin = 0.00005, ymax = 4, color = 'gray', linestyle = '--', linewidth = 1)

for i, ax in enumerate(fig.axes):
    # ax.grid(visible=True, color="k", lw=0.5, linestyle=":")
    wt.artists.corner_text("abcd"[i], ax=ax, corner = 'UL', distance = 0.35, bbox = True, fontsize = fontsize, background_alpha=0.75)

if save:
    wt.artists.savefig(here / "changedelta.png", transparent = True, bbox_inches='tight')
