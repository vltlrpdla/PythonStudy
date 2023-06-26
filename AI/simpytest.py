import sympy as sym
x, y = sym.symbols('x, y')

print(sym.diff(sym.poly(x**2 + 2*x*y + 3) + sym.cos(x + 2*y), x))