import numpy as np
import sympy as sp

a = 0
b = 10
n = int(input("Quantos retângulos serão somados para encontrar a área da curva? "))

t_sym = sp.symbols('t') # t é um símbolo algébrico agora
func_c = (0.5 * t_sym**2) + 3

integral_simbolica = sp.integrate(func_c, (t_sym, a, b)) # (função,(varável, início, fim))
integral_simbolica = float(integral_simbolica)
print(f"Integral simbólica: {integral_simbolica:.2f}")

def func_c2(t):
    return (0.5 * t**2) + 3

base = (b - a) / n

midpoint = np.linspace(a + base/2, b - base/2, n)
riemann = np.sum(func_c2(midpoint) * base)
print(f"Soma de Riemman (Midpoint): {riemann:.2f}")

print(f"\nO erro/diferença entre os dois valores foi de: {(integral_simbolica - riemann):.2f}")
