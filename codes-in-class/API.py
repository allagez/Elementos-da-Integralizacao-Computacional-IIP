# Exercício 2: API REST sob Carga
# Problema:

# A taxa de chamadas a uma API é aproximada por  f(t)=100sin(t)+200  chamadas por minuto em  t∈[0,π]  minutos.

# Implemente riemann_sum que suporte métodos left, right, midpoint 
# e compare as aproximações com o valor de referência dado pela integral simbólica.

# limite inferior = 0 (a)
# limite superior = 3.14 (b)
# numero de retangulos = n

import numpy as np

def calculo_abaixo_curva(a, b, n):
  largura_ret = (b - a) / n
  area_total = 0

  for i in range(n):
    x1 = a + i * largura_ret
    x2 = x1 + largura_ret
