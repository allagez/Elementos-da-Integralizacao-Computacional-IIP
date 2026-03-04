# Problema:

# Um modelo contínuo para o "custo instantâneo" de um algoritmo em função do tamanho de entrada  n  é  g(n)=0.01n2+2n  unidades de tempo por unidade de  n , para  n∈[0,1000] .

# Use SciPy para calcular  ∫10000g(n)dn  (custo total acumulado)
# Interprete o resultado

from scipy.integrate import quad as inte

def g(n):
    return (0.01 * n**2) + 2 * n

resultado, erro = inte(g, 0, 1000)

print(f"Custo Total Acumulado: {resultado:.2f}")
print(f"Erro: {erro}")

# A integrada desse caso no scipy foi feita diretamente pela quadratura de Gauss. Diferente dos outros exemplos que foram feitos com
# a biblioteca numpy e sympy, essa é mais simples e prática. A função inte (que representa quad) retorna dois valores, o resultado (custo total acumulado) e o erro,
# provando que o programa é preciso.