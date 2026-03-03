# Exercício 2: API REST sob Carga
# Problema:

# A taxa de chamadas a uma API é aproximada por  f(t)=100sin(t)+200  chamadas por minuto em  t∈[0,π]  minutos.

# Implemente riemann_sum que suporte métodos left, right, midpoint 
# e compare as aproximações com o valor de referência dado pela integral simbólica.

# limite inferior = 0 (a)
# limite superior = 3.14 (b)
# numero de retangulos = n

import numpy as np

resposta_integral = 828

def calculo_abaixo_curva(a, b, n):
  largura_ret = (b - a) / n
  area_total = 0

  for i in range(n):
    x1 = a + i * largura_ret
    x2 = x1 + largura_ret
    altura_ret = funcao((x1 + x2) / 2) 
    area_ret = largura_ret * altura_ret
    area_total += area_ret
  return area_total 


limite_inferior = 0
limite_superior = 3.14
num_retangulos = 20

def funcao(t):
    return 100 * np.sin(t) + 200  # Substitua esta função pela função que você deseja calcular a área sob


# a, limite inferior
# b, limite superior
# n, numero de retangulos

def calcular_area_retangulos(a, b, n):
    largura_retangulo = (b - a) / n
    area_total = 0

    for i in range(n):
        x1 = a + i * largura_retangulo
        x2 = x1 + largura_retangulo
        altura_retangulo = funcao((x1 + x2) / 2)  # Usando o ponto médio
        area_retangulo = largura_retangulo * altura_retangulo
        area_total += area_retangulo

    return area_total

# Defina os limites de integração e o número de retângulos (mais retângulos = maior precisão)
limite_inferior = 0
limite_superior = 3.14
num_retangulos = 40

area_aproximada = calculo_area_retangulos(limite_inferior, limite_superior, num_retangulos)
print("Área aproximada sob a curva de acordo com a soma de rimann:", area_aproximada)
print("Área aproxima de acordo com a integral:", resposta_integral)
print("A diferença entre o valor da soma de rimel e o calculo pela integral e:", area_aproximada - resposta_integral)

