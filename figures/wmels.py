# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 10:53:49 2024

@author: rpm
"""

import matplotlib.pyplot as plt 
from WrightTools.diagrams import WMEL
# import WrightTools as wt

comparisonwmel = True
hdfg = True
timeorderedwmel = True
drwmel = True

if comparisonwmel:
    fig = WMEL.Artist([4,1], [0, 0.2, 0.6, 1], state_names=("$\mathsf{| g\\rangle}$",
                                                                   "$\mathsf{|v\\rangle}$", 
                                                                   "$\mathsf{|m\\rangle}$",
                                                                   "$\mathsf{|n\\rangle}$"), number_of_interactions=5, state_font_size=9, state_text_buffer = 0.6, virtual = [2,3])


    fig.add_arrow([0,0], 0, [0,1], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([0,0], 1, [0,3], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([0,0], 2, [3,1], kind='out', color="blue", label = "$\mathsf{3}$", head_length = 0.075)
    
    fig.add_arrow([1,0], 0, [0,3], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([1,0], 1, [3,1], kind='bra', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([1,0], 2, [0,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)    
    fig.add_arrow([1,0], 3, [3,1], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)

    fig.add_arrow([2,0], 0, [0,1], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([2,0], 1, [0,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([2,0], 2, [2,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    fig.add_arrow([2,0], 3, [3,1], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    fig.add_arrow([3,0], 0, [0,2], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([3,0], 0, [2,3], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([3,0], 1, [3,1], kind='bra', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([3,0], 2, [0,2], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)    
    fig.add_arrow([3,0], 2, [2,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    fig.add_arrow([3,0], 3, [3,1], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)     

    fig.label_columns(['$\mathsf{DFG}$','$\mathsf{Raman}$', '$\mathsf{HDFG}$', '$\mathsf{Hyper-Raman}$'], font_size = 10)
    
    plt.savefig("comparisonwmel.png", bbox_inches='tight')

if hdfg:
    fig = WMEL.Artist([1,1], [0, 0.2, 0.6, 1], state_names=("$\mathsf{| g, 0\\rangle}$",
                                                                   "$\mathsf{|g, v\\rangle}$", 
                                                                   "$\mathsf{|m, n\\rangle}$",
                                                                   "$\mathsf{|e, v'\\rangle}$"), number_of_interactions=5, state_font_size=9, state_text_buffer = 0.6, virtual = [2])

    fig.add_arrow([0,0], 0, [0,1], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([0,0], 1, [0,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([0,0], 2, [2,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    fig.add_arrow([0,0], 3, [3,1], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    fig.label_columns(['$(\mathsf{b})$'], font_size = 10)

if timeorderedwmel:
    fig = WMEL.Artist([2,1], [0, 0.2, 0.6, 1], state_names=("$\mathsf{| g\\rangle}$",
                                                                   "$\mathsf{|m\\rangle}$", 
                                                                   "$\mathsf{|v''\\rangle}$",
                                                                   "$\mathsf{|n\\rangle}$"), number_of_interactions=5, state_font_size=9, state_text_buffer = 0.6, virtual = [1,3])

    fig.add_arrow([0,0], 0, [0,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([0,0], 1, [0,1], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([0,0], 2, [2,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    fig.add_arrow([0,0], 3, [3,1], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    
    fig.add_arrow([1,0], 0, [0,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([1,0], 1, [2,1], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([1,0], 2, [1,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    fig.add_arrow([1,0], 3, [3,0], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)

    fig.label_columns(['$(\mathsf{a})$','$(\mathsf{b})$'], font_size = 10)
    
    plt.savefig("timeorderedwmel.png", bbox_inches='tight')
    
if drwmel:
    fig = WMEL.Artist([2,2], [0, 0.2, 0.5, 0.8, 1], state_names=("$\mathsf{|g, 0\\rangle}$",
                                                                   "$\mathsf{|g, v\\rangle}$", 
                                                                   "$\mathsf{|m, n\\rangle}$",
                                                                   "$\mathsf{|e, 0\\rangle}$",
                                                                   "$\mathsf{|e, v'\\rangle}$"), number_of_interactions=5, state_font_size=9, state_text_buffer = 0.6, virtual = [2])

    fig.add_arrow([0,0], 0, [0,1], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([0,0], 1, [0,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([0,0], 2, [2,4], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    fig.add_arrow([0,0], 3, [4,1], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    
    fig.add_arrow([1,0], 0, [0,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([1,0], 1, [2,4], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    fig.add_arrow([1,0], 2, [4,3], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([1,0], 3, [3,0], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    fig.add_arrow([0,1], 0, [0,1], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([0,1], 1, [1,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([0,1], 2, [2,4], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    fig.add_arrow([0,1], 3, [4,0], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    
    fig.add_arrow([1,1], 0, [0,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([1,1], 1, [2,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    fig.add_arrow([1,1], 2, [3,4], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([1,1], 3, [4,0], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075) 

    fig.label_columns(['$(\mathsf{a})$','$(\mathsf{b})$'], font_size = 10)
    fig.label_rows(['$\mathsf{I}$','$\mathsf{II}$'], font_size=15, text_buffer=1.5)
    plt.savefig("drwmel.png", bbox_inches='tight')
    
