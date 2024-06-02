# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:40:11 2024

@author: rpm
"""

import WrightTools as wt
import pathlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({
"text.usetex": True,
"font.family": "mathptmx"
})
plt.rcParams['figure.dpi'] = 800

here = pathlib.Path(__file__).resolve().parent
# here = here.parent

data_dir = here.parent / "data" 

dir0 = data_dir / "2024-04-04 39092 grid_scan_wp cobalamin_thin_transmission_wig c38ec440"
dir1 = data_dir / "2024-04-04 37050 grid_scan_wp cobalamin_thin_transmission_wig_TSF ef139d32"

data0  = wt.open(dir0/'primary.wt5')
data1  = wt.open(dir1/'primary.wt5')

for data in [data0, data1]:
    data.create_channel(name = 'normalized', values = data.daq_w1pr[:]/data.daq_pyro_1[:] /data.daq_pyro_3[:])
    data.smooth(2, channel = 'normalized')
    channel = data.normalized
    data.transform('w1_points', 'D1_points')
    split = True
if split:
        data0 = data0.split('w1_points', [1300,1700], units = 'wn')[1]
        data1 = data1.split('w1_points', [1300,1700], units = 'wn')[1]
        for data in [data0, data1]:
            channel = data.normalized
            channel.normalize()
# else: channel.normalize()

##ftir from pandas
spectrum = pd.read_excel(data_dir / "cobir.xlsx")
d2 = wt.Data(name = 'ftir')
d2.create_variable(name = 'energy', units = 'wn', values = spectrum.energy.to_numpy())
d2.create_channel(name = 'signal', values = spectrum.intensity.to_numpy())
    



#plot
cols = [1, 1, "cbar"] 
aspects = [[[0, 0], 0.2], [[1, 0], 0.9]] 

fig, gs = wt.artists.create_figure(width="dissertation", nrows=2, cols=cols, aspects=aspects, wspace=0.6) 

##1d slice
w1pts = data0.w1_points[:]
ax0 = plt.subplot(gs[0,0])
ax1 = plt.subplot(gs[0,1])
j = [0] #chop point at zero delay

d0 = data0.chop('w1_points', at={'D1_points':[j[0], 'ps']})[0]
d1 = data1.chop('w1_points', at={'D1_points':[j[0], 'ps']})[0]

#ftir
# d2= wt.data.from_Tensor27(data_dir/'cn_ftir.dpt')
d2 = d2.split('energy', [1300, 1700], units = 'wn')[1]
d2_0 = d2.signal
d2.create_channel('normalized', values = (d2_0[:] - d2_0.min()) / (d2_0.max() - d2_0.min()))
#fwm

for ax in [ax0,ax1]:
    ax.plot(d2.energy[:], d2.normalized[:], color = 'red', linewidth = 2)
    ax.grid()
    ax.set_xlim(w1pts.min(), w1pts.max())
    xticks = np.linspace(1300, 1700, 5)
    ax.set_xticks(ticks = xticks)
    yticks = [0, 0.2, 0.4, 0.6, 0.8, 1]
    ax.set_yticks(ticks = yticks)

ax0.plot(d0.w1_points[:], d0.normalized[:], color = 'blue', linewidth = 2)
ax1.plot(d1.w1_points[:], d1.normalized[:], color = 'blue', linewidth = 2)

#2d
ax2 = plt.subplot(gs[(1,0)])
ax3 = plt.subplot(gs[(1,1)])
    
ax2.pcolormesh(data0, channel="normalized")
ax3.pcolormesh(data1, channel="normalized")

for ax in [ax2, ax3]:
    ax.grid()
    axissize = 18
    # ax.set_ylabel("$\\tau_{13}$ (ps)", size = axissize)
    # ax.set_xlabel("$\omega_1$ (cm$^{-1}$)", size = axissize)
    ax.tick_params(axis='both', which='major', labelsize=axissize)
    ax.hlines(0, xmin = data0.w1_points.min(), xmax = data0.w1_points.max(), alpha = 0.2, color = 'blue', linewidth = 6)
    ax.set_ylim(-1,1)
    ax.set_xlim(w1pts.min(), w1pts.max())
    ax.set_xticks(ticks = xticks)


# ax.set_ylim(-0.02, 0.02)
# yticks = np.linspace(-0.02, 0.02, 5)
# ax.set_yticks(ticks = yticks)


#beautification   
for i, ax in enumerate(fig.axes):
    ax.grid(visible=True, color="k", lw=0.5, linestyle=":")
    wt.artists.corner_text("abcd"[i], ax=ax, corner = 'UL', distance = 0.25, bbox = True, fontsize = 16, background_alpha=0.75)


wt.artists.set_fig_labels(xlabel = r'$\mathsf{\omega_1} \ (\mathsf{cm}^{-1})$', ylabel = '$\mathsf{\\tau_{12}} \ (\mathsf{ps})$', col = slice(0,1), label_fontsize = 18)
for ax in [ax0, ax3]:
    ax.set_ylabel("")

#colorbar
cax = plt.subplot(gs[1, -1]) 
wt.artists.plot_colorbar(cax=cax, label=r"$\mathsf{Signal \ Intensity \ (norm.)}$", tick_fontsize=18, label_fontsize = 18, extend = 'min')


Save = True
if Save:
    wt.artists.savefig(here / "cob.png", bbox_inches='tight', dpi=800, transparent = 'false')