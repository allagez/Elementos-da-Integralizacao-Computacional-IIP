# Exercício 2: API REST sob Carga
# Problema:

# A taxa de chamadas a uma API é aproximada por  f(t)=100sin(t)+200  chamadas por minuto em  t∈[0,π]  minutos.

# Implemente riemann_sum que suporte métodos left, right, midpoint 
# e compare as aproximações com o valor de referência dado pela integral simbólica.

# limite inferior = 0 (a)
# limite superior = 3.14 (b)
# numero de retangulos = n

import numpy as np

a = 0
b = 3.14
n = int(input("Em quantos retângulos serão divididos? "))