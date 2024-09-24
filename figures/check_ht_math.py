""" math checks on derivation
"""

import matplotlib.pyplot as plt
import numpy as np
import sympy
from sympy import hermite

factorial = sympy.functions.combinatorial.factorials.factorial

x = sympy.symbols("x")
y = sympy.symbols("y")
n = sympy.symbols("n")
l = sympy.symbols("l")

def term_n0(x, n, y, l):
    """ summand terms for <n|q|0>"""
    return (-1)**y  / (2**(2*y)*factorial(y)) * (-1j/2)**(l+1) \
    * (-x)**(n-2*y-l) / (factorial(l)*factorial(n-2*y-l)) \
    * hermite(l+1, 1j * x / 2)

for n, expression in enumerate([
    # <0|q|0>
    sympy.simplify(term_n0(x, 0, 0, 0)),
    # <1|q|0>
    sympy.simplify(term_n0(x, 1, 0, 0) + term_n0(x, 1, 0, 1)),
    # <2|q|0>
    sympy.simplify(term_n0(x, 2, 0, 0) + term_n0(x, 2, 0, 1) + term_n0(x, 2, 0, 2) + term_n0(x, 2, 1, 0)),]
):
    print(f"<{n}|q|0>: {expression}")


def term_n1(x, n, y, l):
    """terms for <n|q|1>"""
    return (-1)**y  / (2**(2*y)*factorial(y)) * (-1j/2)**(l+2) \
    * (-x)**(n-2*y-l) / (factorial(l)*factorial(n-2*y-l)) \
    * hermite(l+2, 1j*x/2)

for n, expression in enumerate([
    # <0|q|0>
    sympy.simplify(term_n1(x, 0, 0, 0)),
    # <1|q|0>
    sympy.simplify(term_n1(x, 1, 0, 0) + term_n1(x, 1, 0, 1)),
    # <2|q|0>
    sympy.simplify(term_n1(x, 2, 0, 0) + term_n1(x, 2, 0, 1) + term_n1(x, 2, 0, 2) + term_n1(x, 2, 1, 0)),]
):
    print(f"<{n}|q|1>: {expression}")



d = np.linspace(-4,4)

f0 = np.exp(-d**2 / 4)
f_00 = 0.5 * d * f0
f_10 = 2**0.5 / 4 * (2-d**2) * f0
f_20 = 2**0.5 / 16 * (d**3 - 4*d) * f0

f_01 = 2**0.5 * (.25*d**2 + 0.5) * f0
f_11 = 2 * (0.25*d - 0.125*d**2) * f0
f_21 = 8**0.5 * (.03125*d**4 - 0.1875*d**2 +0.25) * f0

fig, ax = plt.subplots()
ax.plot(d, f_00, label="<0|q|0>")
ax.plot(d, f_10, label="<1|q|0>")
ax.plot(d, f_20, label="<2|q|0>")
ax.plot(d, f_01, label="<0|q|1>")
ax.plot(d, f_11, label="<1|q|1>")
ax.plot(d, f_21, label="<2|q|1>")
ax.legend()
plt.show()
