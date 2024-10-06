# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:28:39 2023

@author: rpm
"""
import numpy as np
import WrightTools as wt
import matplotlib.pyplot as plt 
import pathlib

wt.artists.apply_rcparams(kind="publication")

here = pathlib.Path(__file__).resolve().parent
save = True
fontsize = 18

r = 5 #radius of contour

def contour(k):
    return np.sqrt(r**2 - k**2) 

x = np.linspace(-r, r, 50000)

#make figure
cols = [1, 1] 
aspects = [[[0, 0], 1], [[1, 0], 1]] 

fig, gs = wt.artists.create_figure(width="dissertation", nrows=1, cols=cols, aspects=aspects, hspace=0.7, wspace=1.2) 

###Anti-correlated modes###
ax0 = plt.subplot(gs[0,0]) 

#insert the poles
poles = [2, -2, -2.6, -3.5]
points = [0, 0, 2, 3]


#plot it
ax0.plot(x, contour(x), linewidth = '2', color = 'black')
for i in [0,1,2,3]:
    ax0.scatter(points[i], poles[i], color = 'blue')
    label = [r'$\mathsf{i \sigma}$', r'$\mathsf{-i \sigma}$', r'$\mathsf{\Delta_{ga}}$', r'$\mathsf{\Delta_{ba}}$']
    ax0.text(points[i]+0.1, poles[i]+0.1, label[i], fontsize = 24)


###Correlated modes###
ax1 = plt.subplot(gs[0,1]) 

#insert the poles
poles = [2, -2, -2.6, 3.5]
points = [0, 0, 2, -3]


#plot it
for i in [0,1,2,3]:
    ax1.scatter(points[i], poles[i], color = 'blue')
    label = [r'$\mathsf{i \sigma}$', r'$\mathsf{-i \sigma}$', r'$\mathsf{\Delta_{ga}}$', r'$\mathsf{-\Delta_{ba}}$']
    ax1.text(points[i]+0.1, poles[i]+0.1, label[i], fontsize = 24)
ax0.set_title('Anti-Correlated (c = -1)')

ax1.plot(x,contour(x), linewidth = '2', color = 'black')
ax1.set_title('Correlated (c = 1)')

#beautification
for ax in [ax0, ax1]:
    # ax.set_yscale('log')
    ax.set_ylabel(r'$\mathsf{Im(\xi)}$', fontsize = fontsize)
    ax.set_xlabel(r'$\mathsf{Re(\xi)}$', fontsize = fontsize)
    ax.set_xlim(-5.4, 5.4)
    ax.set_ylim(-5.4, 5.4)
    ax.hlines(xmin=-r, xmax =r, y = 0, color = 'black', linestyle = '-', linewidth = 2)
    ax.hlines(xmin=-10, xmax =10, y = 0, color = 'grey', linestyle = '--', linewidth = 1, zorder = 1)
    ax.vlines(ymin=-10, ymax =10, x = 0, color = 'grey', linestyle = '--', linewidth = 1, zorder = 1)
    ax.set_yticks(ticks = [])
    ax.set_xticks(ticks = [])
    
    # j = [0]
    # for i in j:
    #     ax.text(i-.1, contour(i)-.17, r'$\mathsf{<}$', fontsize = 24, alpha = 1, color = 'r', weight='bold')    
    #     ax.text(i-.1, -.17, r'$\mathsf{>}$', fontsize = 24, color = 'r') 
    
    
for i, ax in enumerate(fig.axes):
    wt.artists.corner_text("abcd"[i], ax=ax, corner = 'UL', distance = 0.2, bbox = True, fontsize = fontsize, background_alpha=0.75)

if save:
    wt.artists.savefig(here / "contour.png", transparent = True, bbox_inches='tight')
