# Exercício 2: API REST sob Carga
# Problema:

# A taxa de chamadas a uma API é aproximada por  f(t)=100sin(t)+200  chamadas por minuto em  t∈[0,π]  minutos.

# Implemente riemann_sum que suporte métodos left, right, midpoint 
# e compare as aproximações com o valor de referência dado pela integral simbólica.

# limite inferior = 0 (a)
# limite superior = 3.14 (b)
# numero de retangulos = n

import numpy as np

def f(t):   # Aqui iremos buscar o valor da taxa (que será equivalente à altura dos retângulos nos pontos t) (f = altura)
    return 100 * np.sin(t) + 200

def riemann(metodo, a, b, n):
    base = (b - a) / n

    if metodo == "M": # O midpoint, como o nome já diz, é a metade da base. Com ela chegaremos a sua altura f(t), que é onde o retângulo irá "bater" na curva
        # O linspace é como se fosse um laço de repetição. Em t_midpoint será armazenado uma lista com n pontos t de f(t) com o mesmo intervalo.
        t_point = np.linspace(a + base/2, b - base/2, n) 
    elif metodo == "L": # O leftpoint irá iniciar pelo ponto (a) e encerrará no ponto (b - base), já que os pontos serão das laterais esquerdas de cada retângulo
        t_point = np.linspace(a, b - base, n)
    elif metodo == "R":
        t_point = np.linspace(a + base, b, n) # O rightpoint será o oposto do leftpoint, ele iniciará no ponto (a + base) e encerrará no ponto (b)
    else:
        return "Erro"
    
    area_total = np.sum(f(t_point) * base) # A função sum irá somar a área de todos os n retângulos usando os n pontos que estão armazenados em (t_point)
    return area_total

a = 0
b = 3.14
n = int(input("Quantos retângulos serão utilizados para chegar a área sob a curva? "))
integral_simbolica = 828

soma_left = riemann("L", a, b, n)
soma_right = riemann("R", a, b, n)
soma_midpoint = riemann("M", a, b, n)

print(f"\n \nResultados com {n}:")
print(f"Leftpoint = {soma_left:.2f}")
print(f"Rightpoint {soma_right:.2f}")
print(f"Midpoint = {soma_midpoint:.2f}")
print(f"Integral simbólica = {integral_simbolica}")

print(f"\n \nDiferença/Erro:")
print(f"Dif. Left = {integral_simbolica - soma_left:.2f}")
print(f"Dif. Right = {integral_simbolica - soma_right:.2f}")
print(f"Dif. Midpoint = {integral_simbolica - soma_midpoint:.2f}")



    