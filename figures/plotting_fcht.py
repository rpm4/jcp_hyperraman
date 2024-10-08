import numpy as np
import WrightTools as wt
import matplotlib.pyplot as plt
import pathlib

wt.artists.apply_rcparams(kind="publication")

save = True
fontsize =18
here = pathlib.Path(__file__).resolve().parent

#define harmonic wells and coordinates
d = np.linspace(-5, 5, 5000)

#make figure
cols = [1, 1] 
aspects = [[[0, 0], 1], [[1, 0], 1]] 


"""Defining Franck Condon and Herzberg Teller integrals"""
'''fc integrals'''
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

"""Plotting the Franck Condon and Herzberg Teller integrals"""
#plot
fig, gs = wt.artists.create_figure(width="dissertation", nrows=2, cols=cols, aspects=aspects, wspace=1) 
ax0 = plt.subplot(gs[0,0])
ax0.plot(d, f00(d), linewidth = '2', label = r'$\mathsf{\langle\tilde{0}|0\rangle}$', zorder = 4)
ax0.plot(d, f01(d), linewidth = '2', label = r'$\mathsf{\langle\tilde{0}|1\rangle}$', zorder = 3)
ax0.plot(d, f10(d), linewidth = '2', label = r'$\mathsf{\langle\tilde{1}|0\rangle}$', zorder = 3)
ax0.plot(d, f11(d), linewidth = '2', label = r'$\mathsf{\langle\tilde{1}|1\rangle}$', zorder = 2)
# ax0.plot(d, f02(d), linewidth = '2', label = r'$\mathsf{02}$', color = 'green', zorder = 1)
ax0.plot(d, f20(d), linewidth = '2', label = r'$\mathsf{\langle\tilde{2}|0\rangle}$', zorder = 1)
ax0.plot(d, f21(d), linewidth = '2', label = r'$\mathsf{\langle\tilde{2}|1\rangle}$', zorder = 1)

# ax0.text(20000, 2, r'$\mathsf{\Delta = 1/\sqrt{2}}$', fontsize = 16)


#plot the A and B

ax1 = plt.subplot(gs[0,1])
ax1.plot(d, h00(d), linewidth = '2', label = r'$\mathsf{\langle\tilde{0}|q|0\rangle}$', zorder = 4)
ax1.plot(d, h01(d), linewidth = '2', label = r'$\mathsf{\langle\tilde{0}|q|1\rangle}$', zorder = 3)
ax1.plot(d, h10(d), linewidth = '2', label = r'$\mathsf{\langle\tilde{1}|q|0\rangle}$', zorder = 3)
ax1.plot(d, h11(d), linewidth = '2', label = r'$\mathsf{\langle\tilde{1}|q|1\rangle}$', zorder = 2)
ax1.plot(d, h20(d), linewidth = '2', label = r'$\mathsf{\langle\tilde{2}|q|0\rangle}$', zorder = 1)
ax1.plot(d, h21(d), linewidth = '2', label = r'$\mathsf{\langle\tilde{2}|q|1\rangle}$', zorder = 1)


for ax in [ax0, ax1]:
    # ax.set_yscale('log')
    ax.set_ylabel(r'$\mathsf{Integral \ Value \ (arb.)}$', fontsize = fontsize)
    ax.set_xlim(-2,2)
    ax.set_xlabel(r'$\mathsf{\Delta}$', fontsize = fontsize)
    # xticks = np.linspace(15000, 45000, 7)
    # ax.set_xticks(xticks)
    ax.set_ylim(-0.75, 1.6)
    ax.legend(loc = 1, ncol =2)
    for j in [0]:
        # ax.vlines(x = 0, ymin = -1, ymax = 2, color = 'gray', linestyle = '--', linewidth = 1)
        ax.hlines(xmin=-5, xmax =5, y = j, color = 'gray', linestyle = '--', linewidth = 1)


for i, ax in enumerate(fig.axes):
    # ax.grid(visible=True, color="k", lw=0.5, linestyle=":")
    wt.artists.corner_text("abcd"[i], ax=ax, corner = 'UL', distance = 0.35, bbox = True, fontsize = fontsize, background_alpha=0.75)

if save:
    wt.artists.savefig(here / "fcht.png", transparent = True, bbox_inches='tight')
    
    
"""Plotting the FC and HT integral products present in defintiions of A and B in the main text"""

cols1 = [1, 1, 1] 
aspects1 = [[[0, 0], 1], [[1, 0], 1], [[2, 0], 1]] 

fig1, gs1 = wt.artists.create_figure(width="dissertation", nrows=1, cols=cols1, aspects=aspects1, wspace=1) 

ax01 = plt.subplot(gs1[0,0])

ax01.plot(d, f00(d)*f01(d), linewidth = '2', label = r'$\mathsf{\langle1|\tilde{0}\rangle  \langle\tilde{0}|0\rangle}$', zorder = 4)

ax01.plot(d, f10(d)*f11(d), linewidth = '2', label = r'$\mathsf{\langle 1 | \tilde{1} \rangle \langle\tilde{1}|0\rangle}$', zorder = 3)

ax01.plot(d, f20(d) * f21(d), linewidth = '2', label = r'$\mathsf{\langle 1 | \tilde{2} \rangle \langle \tilde{2} | 0\rangle  }$', zorder = 1)

ax01.set_title(r'$\mathsf{A \ term}$')
ax01.set_ylim(-0.6, 1.1)

ax11 = plt.subplot(gs1[0,1])

ax11.plot(d, h00(d) * f01(d), linewidth = '2', label = r'$\mathsf{\langle1|\tilde{0}\rangle  \langle\tilde{0}|q|0\rangle}$', zorder = 4)

ax11.plot(d, h10(d) *f11(d), linewidth = '2', label = r'$\mathsf{\langle 1 | \tilde{1} \rangle  \langle\tilde{1}|q|0\rangle}$', zorder = 3)

ax11.plot(d, h20(d) * f21(d), linewidth = '2', label = r'$\mathsf{\langle 1 | \tilde{2} \rangle  \langle\tilde{2}|q|0\rangle}$', zorder = 1)

ax11.set_title(r'$\mathsf{B_1 \ term}$')
ax11.set_ylim(-0.2, 1.3)

ax21 = plt.subplot(gs1[0,2])

ax21.plot(d, h01(d) * f00(d), linewidth = '2', label = r'$\mathsf{\langle1|q|\tilde{0}\rangle  \langle\tilde{0}|0\rangle}$', zorder = 3)

ax21.plot(d, h11(d) * f10(d), linewidth = '2', label = r'$\mathsf{\langle1|q|\tilde{1}\rangle  \langle\tilde{1}|0\rangle}$', zorder = 2)

ax21.plot(d, h21(d) * f20(d), linewidth = '2', label = r'$\mathsf{\langle1|q|\tilde{2}\rangle  \langle\tilde{2}|0\rangle}$', zorder = 1)

ax21.set_title(r'$\mathsf{B_2 \ term}$')
ax21.set_ylim(-0.2, 1.35)


for ax in [ax01, ax11, ax21]:
    ax.set_ylabel(r'$\mathsf{Integral \ Value \ (arb.)}$', fontsize = fontsize)
    ax.set_xlim(-2,2)
    ax.set_xlabel(r'$\mathsf{\Delta}$', fontsize = fontsize)
    ax.legend()
    for d in [0]:
        ax.hlines(xmin=-5, xmax =5, y = d, color = 'gray', linestyle = '--', linewidth = 1)


for i, ax in enumerate(fig1.axes):
    wt.artists.corner_text("abcd"[i], ax=ax, corner = 'UL', distance = 0.35, bbox = True, fontsize = fontsize, background_alpha=0.75)

if save:
    wt.artists.savefig(here / "fchtproduct.png", transparent = True, bbox_inches='tight')
