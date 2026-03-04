import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad as inte

def m(t):
    return 50 * t + 100

valor_area, erro = inte(m, 0, 10)

valor_t = np.linspace(0, 10, 100)
valor_m = m(valor_t)

#################################################################################################################

plt.figure(figsize=(10, 6))

plt.plot(valor_t, valor_m, color='blue', label=r'$m(t) = 50t + 100$', linewidth=2)

plt.fill_between(valor_t, valor_m, color='skyblue', alpha=0.4, label='Memória Acumulada (MB*min)')


plt.title(f'Uso de Memória Acumulado: {valor_area:.0f} MB⋅min', fontsize=14)
plt.xlabel('Tempo (minutos)')
plt.ylabel('Uso de Memória (MB)')
plt.ylim(0, 700)    
plt.xlim(0, 10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()


plt.text(5, 200, f'Área = {valor_area:.0f}', fontsize=20, ha='center', color='darkblue')

plt.show()