# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 10:53:49 2024

@author: rpm
"""

import matplotlib.pyplot as plt 
from WrightTools.diagrams import WMEL
import pathlib


here = pathlib.Path(__file__).resolve().parent

fig = WMEL.Artist([2,1], [0, 0.2, 0.6, 1], state_names=("$\mathsf{| g, 0\\rangle}$",
                                                                   "$\mathsf{|g, v\\rangle}$", 
                                                                   "$\mathsf{|m, n\\rangle}$",
                                                                   "$\mathsf{|e, \\tilde{v}'\\rangle}$"), number_of_interactions=5, state_font_size=9, state_text_buffer = 0.6, virtual = [2])

fig.add_arrow([0,0], 0, [0,1], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
fig.add_arrow([0,0], 1, [0,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
fig.add_arrow([0,0], 2, [2,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
fig.add_arrow([0,0], 3, [3,1], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)

fig.add_arrow([1,0], 0, [0,1], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
fig.add_arrow([1,0], 1, [1,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
fig.add_arrow([1,0], 2, [2,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
fig.add_arrow([1,0], 3, [3,0], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)

fig.label_columns(['$\mathsf{HDFG}$', '$\mathsf{HSFG}$'], font_size = 9)

plt.savefig(here / "toc.png", bbox_inches='tight')

