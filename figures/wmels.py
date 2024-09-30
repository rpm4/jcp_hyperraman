import matplotlib.pyplot as plt 
from WrightTools.diagrams import WMEL
import WrightTools as wt

wt.artists.apply_rcparams(kind="publication")


comparisonwmel = False
test = False
hdfg = False
timeorderedwmel = True
timeorderedwmel2 = True
drwmel = False

if comparisonwmel:
    fig = WMEL.Artist([6,1], [0, 0.2, 0.6, 1], state_names=("$\mathsf{| g\\rangle}$",
                                                                   "$\mathsf{|v\\rangle}$", 
                                                                   "$\mathsf{|m\\rangle}$",
                                                                   "$\mathsf{|n\\rangle}$"), number_of_interactions=4, state_font_size=9, state_text_buffer = 0.6, virtual = [2,3])


    fig.add_arrow([0,0], 0, [0,1], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([0,0], 1, [0,3], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([0,0], 2, [3,1], kind='out', color="blue", label = "$\mathsf{3}$", head_length = 0.075)
    
    fig.add_arrow([1,0], 0, [0,1], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([1,0], 1, [1,3], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([1,0], 2, [3,0], kind='out', color="blue", label = "$\mathsf{3}$", head_length = 0.075)
    
    fig.add_arrow([2,0], 0, [0,3], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([2,0], 1, [3,1], kind='bra', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([2,0], 2, [0,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)    
    fig.add_arrow([2,0], 3, [3,1], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)

    fig.add_arrow([3,0], 0, [0,1], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([3,0], 1, [0,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([3,0], 2, [2,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    fig.add_arrow([3,0], 3, [3,1], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    fig.add_arrow([4,0], 0, [0,1], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([4,0], 1, [1,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([4,0], 2, [2,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    fig.add_arrow([4,0], 3, [3,0], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    fig.add_arrow([5,0], 0, [0,2], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([5,0], 0, [2,3], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([5,0], 1, [3,1], kind='bra', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([5,0], 2, [0,2], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)    
    fig.add_arrow([5,0], 2, [2,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    fig.add_arrow([5,0], 3, [3,1], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)     

    fig.label_columns(['$\mathsf{DFG}$','$\mathsf{SFG}$','$\mathsf{Raman}$', '$\mathsf{HDFG}$', '$\mathsf{HSFG}$','$\mathsf{Hyper-Raman}$'], font_size = 9)
    
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
    fig = WMEL.Artist([4,1], [0, 0.2, 0.4, 0.8, 1], state_names=("$\mathsf{| g, 0\\rangle}$",
                                                                   "$\mathsf{|m, n\\rangle}$", 
                                                                   "$\mathsf{|g, v\\rangle}$",
                                                                   "$\mathsf{|m', n'\\rangle}$",
                                                                   "$\mathsf{|e, v'\\rangle}$"), number_of_interactions=4, state_font_size=9, state_text_buffer = 0.6, virtual = [1,3])

    fig.add_arrow([0,0], 0, [0,2], kind='ket', color="orange", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([0,0], 1, [0,1], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([0,0], 2, [2,4], kind='ket', color="r", label = "$\mathsf{3}$", head_length = 0.075)
    fig.add_arrow([0,0], 3, [4,1], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    
    fig.add_arrow([1,0], 0, [0,2], kind='ket', color="orange", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([1,0], 1, [2,1], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([1,0], 2, [1,3], kind='ket', color="r", label = "$\mathsf{3}$", head_length = 0.075)
    fig.add_arrow([1,0], 3, [3,0], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    fig.add_arrow([2,0], 0, [0,2], kind='ket', color="orange", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([2,0], 1, [2,4], kind='ket', color="r", label = "$\mathsf{3}$", head_length = 0.075)
    fig.add_arrow([2,0], 2, [0,1], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([2,0], 3, [4,1], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    
    fig.add_arrow([3,0], 0, [0,2], kind='ket', color="orange", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([3,0], 1, [2,4], kind='ket', color="r", label = "$\mathsf{3}$", head_length = 0.075)
    fig.add_arrow([3,0], 2, [4,3], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([3,0], 3, [3,0], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)

    fig.label_columns(['$(\mathsf{c})$','$(\mathsf{d})$', '$(\mathsf{e})$', '$(\mathsf{f})$'], font_size = 9)
    # fig.label_rows(['$\mathsf{II}$'], font_size=15, text_buffer=1.5)
    plt.savefig("timeorderedwmel.png", bbox_inches='tight')

if timeorderedwmel2:
    fig = WMEL.Artist([2,1], [0, 0.2, 0.6, 1], state_names=("$\mathsf{| g, 0\\rangle}$",
                                                                   "$\mathsf{|g, v\\rangle}$", 
                                                                   "$\mathsf{|m, n\\rangle}$",
                                                                   "$\mathsf{|e, v'\\rangle}$"), number_of_interactions=4, state_font_size=9, state_text_buffer = 0.6, virtual = [2])


    fig.add_arrow([0,0], 0, [0,1], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([0,0], 1, [0,2], kind='ket', color="orange", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([0,0], 2, [2,3], kind='ket', color="r", label = "$\mathsf{3}$", head_length = 0.075)
    fig.add_arrow([0,0], 3, [3,1], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    fig.add_arrow([1,0], 0, [0,1], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig.add_arrow([1,0], 1, [0,2], kind='ket', color="r", label = "$\mathsf{3}$", head_length = 0.075)
    fig.add_arrow([1,0], 2, [2,3], kind='ket', color="orange", label = "$\mathsf{2}$", head_length = 0.075)
    fig.add_arrow([1,0], 3, [3,1], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)

    fig.label_columns(['$(\mathsf{a})$','$(\mathsf{b})$'], font_size = 10)
    # fig.label_rows(['$\mathsf{I}$'], font_size=15, text_buffer=1.5)
    plt.savefig("testing123.png", bbox_inches='tight')

    
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
    
    
if test:
    fig0 = WMEL.Artist([2,1], [0, 0.2, 1], state_names=("$\mathsf{|g\\rangle}$",
                                                                   "$\mathsf{|v\\rangle}$", 
                                                                   "$\mathsf{|e\\rangle}$"), number_of_interactions=4, state_font_size=9, state_text_buffer = 0.6)

    fig0.add_arrow([0,0], 0, [0,1], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig0.add_arrow([0,0], 1, [0,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig0.add_arrow([0,0], 2, [2,1], kind='out', color="blue", label = "$\mathsf{3}$", head_length = 0.075)
    
    fig0.add_arrow([1,0], 0, [0,1], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig0.add_arrow([1,0], 1, [1,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig0.add_arrow([1,0], 2, [2,0], kind='out', color="blue", label = "$\mathsf{3}$", head_length = 0.075)    
    fig0.label_columns(['$\mathsf{vDFG}$','$\mathsf{vSFG}$'], font_size = 9)
    plt.savefig("test.png", bbox_inches='tight')


    
    fig1 = WMEL.Artist([2,1], [0, 0.2, 0.6, 1], state_names=("$\mathsf{| g\\rangle}$",
                                                                    "$\mathsf{|v\\rangle}$", 
                                                                    "$\mathsf{|m\\rangle}$",
                                                                    "$\mathsf{|e\\rangle}$"), number_of_interactions=5, state_font_size=9, state_text_buffer = 0.6, virtual = [2])

    fig1.add_arrow([0,0], 0, [0,1], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig1.add_arrow([0,0], 1, [0,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig1.add_arrow([0,0], 2, [2,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    fig1.add_arrow([0,0], 3, [3,1], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    fig1.add_arrow([1,0], 0, [0,1], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig1.add_arrow([1,0], 1, [1,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig1.add_arrow([1,0], 2, [2,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    fig1.add_arrow([1,0], 3, [3,0], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    fig1.label_columns(['$\mathsf{HDFG}$', '$\mathsf{HSFG}$'], font_size = 10)

    
    fig11 = WMEL.Artist([1,1], [0, 0.2, 1], state_names=("$\mathsf{| g\\rangle}$",
                                                                    "$\mathsf{|v\\rangle}$", 
                                                                    "$\mathsf{|e\\rangle}$"), number_of_interactions=5, state_font_size=9, state_text_buffer = 0.6)
    
    fig11.add_arrow([0,0], 0, [0,2], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig11.add_arrow([0,0], 1, [2,1], kind='bra', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig11.add_arrow([0,0], 2, [0,2], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)    
    fig11.add_arrow([0,0], 3, [2,1], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    fig11.label_columns(['$\mathsf{Raman / RISRS}$'], font_size = 10)

    
    
    fig2 = WMEL.Artist([1,1], [0, 0.2, 0.6, 1], state_names=("$\mathsf{| g\\rangle}$",
                                                                    "$\mathsf{|v\\rangle}$", 
                                                                    "$\mathsf{|m\\rangle}$",
                                                                    "$\mathsf{|e\\rangle}$"), number_of_interactions=5, state_font_size=9, state_text_buffer = 0.6, virtual = [2])

    fig2.add_arrow([0,0], 0, [0,2], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig2.add_arrow([0,0], 0, [2,3], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig2.add_arrow([0,0], 1, [3,1], kind='bra', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig2.add_arrow([0,0], 2, [0,2], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)    
    fig2.add_arrow([0,0], 2, [2,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    fig2.add_arrow([0,0], 3, [3,1], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    fig2.label_columns(['$\mathsf{Hyper-Raman}$'], font_size = 10)

    
    fig31 = WMEL.Artist([2,1], [0, 0.2, 0.8, 1], state_names=("$\mathsf{| g\\rangle}$",
                                                                    "$\mathsf{|v\\rangle}$", 
                                                                    "$\mathsf{|e'\\rangle}$",
                                                                    "$\mathsf{|e\\rangle}$"), number_of_interactions=5, state_font_size=9, state_text_buffer = 0.6)

    fig31.add_arrow([0,0], 0, [0,2], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig31.add_arrow([0,0], 1, [2,1], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig31.add_arrow([0,0], 2, [1,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)    
    fig31.add_arrow([0,0], 3, [3,0], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    fig31.add_arrow([1,0], 0, [0,2], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig31.add_arrow([1,0], 1, [2,1], kind='bra', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig31.add_arrow([1,0], 2, [0,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)    
    fig31.add_arrow([1,0], 3, [3,1], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    
    
    fig31.label_columns(['$\mathsf{CARS}$', '$\mathsf{CSRS}$'], font_size = 10)

    
    fig3 = WMEL.Artist([2,1], [0, 0.2, 0.35, 1], state_names=("$\mathsf{| g\\rangle}$",
                                                                    "$\mathsf{|v\\rangle}$", 
                                                                    "$\mathsf{|v'\\rangle}$",
                                                                    "$\mathsf{|e\\rangle}$"), number_of_interactions=5, state_font_size=9, state_text_buffer = 0.6)

    fig3.add_arrow([0,0], 0, [0,1], kind='bra', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig3.add_arrow([0,0], 1, [0,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig3.add_arrow([0,0], 2, [2,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)    
    fig3.add_arrow([0,0], 3, [3,1], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    fig3.add_arrow([1,0], 0, [0,1], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig3.add_arrow([1,0], 1, [1,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig3.add_arrow([1,0], 2, [2,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)    
    fig3.add_arrow([1,0], 3, [3,0], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    fig3.label_columns(['$\mathsf{DOVE}$','$\mathsf{TSF}$'], font_size = 10)
    
    fig4 = WMEL.Artist([1,1], [0, 0.2, 0.6, 0.85, 1], state_names=("$\mathsf{|g\\rangle}$",
                                                                    "$\mathsf{|v\\rangle}$", 
                                                                    "$\mathsf{|m\\rangle}$",
                                                                    "$\mathsf{|e'\\rangle}$",
                                                                    "$\mathsf{|e\\rangle}$"), number_of_interactions=5, state_font_size=9, state_text_buffer = 0.6, virtual = [2])

    fig4.add_arrow([0,0], 0, [0,2], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig4.add_arrow([0,0], 0, [2,3], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig4.add_arrow([0,0], 1, [3,1], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig4.add_arrow([0,0], 2, [1,2], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)    
    fig4.add_arrow([0,0], 2, [2,4], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    fig4.add_arrow([0,0], 3, [4,0], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    fig4.label_columns(['$\mathsf{CAHRS}$'], font_size = 10)
    
    fig5 = WMEL.Artist([1,1], [0, 0.2, 0.35, 0.73, 0.85, 1], state_names=("$\mathsf{|g\\rangle}$",
                                                                    "$\mathsf{|v\\rangle}$", 
                                                                    "$\mathsf{|v'\\rangle}$", 
                                                                    "$\mathsf{|e''\\rangle}$",
                                                                    "$\mathsf{|e'\\rangle}$",
                                                                    "$\mathsf{|e\\rangle}$"), number_of_interactions=6, state_font_size=9, state_text_buffer = 0.6)

    fig5.add_arrow([0,0], 0, [0,3], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig5.add_arrow([0,0], 1, [3,1], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig5.add_arrow([0,0], 2, [1,4], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    fig5.add_arrow([0,0], 3, [4,2], kind='ket', color="k", label = "$\mathsf{4}$", head_length = 0.075)    
    fig5.add_arrow([0,0], 4, [2,5], kind='ket', color="k", label = "$\mathsf{5}$", head_length = 0.075)
    fig5.add_arrow([0,0], 5, [5,0], kind='out', color="blue", label = "$\mathsf{6}$", head_length = 0.075)
    
    fig5.label_columns(['$\mathsf{2D-Raman}$'], font_size = 10)
    
    
    fig11 = WMEL.Artist([2,1], [0, 0.2, 0.35, 0.8, 1], state_names=("$\mathsf{| g\\rangle}$",
                                                                    "$\mathsf{|v\\rangle}$", 
                                                                    "$\mathsf{|v'\\rangle}$", 
                                                                    "$\mathsf{|e'\\rangle}$",
                                                                    "$\mathsf{|e\\rangle}$"), number_of_interactions=5, state_font_size=9, state_text_buffer = 0.6)

    fig31.add_arrow([0,0], 0, [0,2], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    fig31.add_arrow([0,0], 1, [2,1], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    fig31.add_arrow([0,0], 2, [1,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)    
    fig31.add_arrow([0,0], 3, [3,0], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)

    
    #makewt figure?
   
    # fig.add_arrow([1,0], 0, [0,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    # fig.add_arrow([1,0], 1, [2,4], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    # fig.add_arrow([1,0], 2, [4,3], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    # fig.add_arrow([1,0], 3, [3,0], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    # fig.add_arrow([0,1], 0, [0,1], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    # fig.add_arrow([0,1], 1, [1,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    # fig.add_arrow([0,1], 2, [2,4], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    # fig.add_arrow([0,1], 3, [4,0], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075)
    
    
    # fig.add_arrow([1,1], 0, [0,2], kind='ket', color="k", label = "$\mathsf{2}$", head_length = 0.075)
    # fig.add_arrow([1,1], 1, [2,3], kind='ket', color="k", label = "$\mathsf{3}$", head_length = 0.075)
    # fig.add_arrow([1,1], 2, [3,4], kind='ket', color="k", label = "$\mathsf{1}$", head_length = 0.075)
    # fig.add_arrow([1,1], 3, [4,0], kind='out', color="blue", label = "$\mathsf{4}$", head_length = 0.075) 

    # fig.label_columns(['$(\mathsf{a})$','$(\mathsf{b})$'], font_size = 10)
    # fig.label_rows(['$\mathsf{I}$','$\mathsf{II}$'], font_size=15, text_buffer=1.5)
    
    
    
    # plt.savefig("test.png")
