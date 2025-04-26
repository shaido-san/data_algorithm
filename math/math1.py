from sympy import *

x, y = symbols("x y")

expr = factor(x**3 + 8*x**2 + 3*x*y + 24*y)
print(expr)