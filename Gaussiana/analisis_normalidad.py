import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd

# Preguntar al usuario por los parámetros de la distribución
media = float(input("Introduce la media de papel desechado por semana (kg): "))
desviacion_estandar = float(input("Introduce la desviación estándar (kg): "))
valor_a_contrastar = float(input("Introduce la cantidad de papel a contrastar (kg): "))

# Calcular la probabilidad y graficar la distribución normal
x = np.linspace(media - 4*desviacion_estandar, media + 4*desviacion_estandar, 1000)
y = norm.pdf(x, media, desviacion_estandar)
z = (valor_a_contrastar - media) / desviacion_estandar
probabilidad = 1 - norm.cdf(z)

# Graficar la distribución normal y el área bajo la curva de interés
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Distribución Normal')
plt.fill_between(x, y, where=x > valor_a_contrastar, color='red', alpha=0.5, label=f'P(X > {valor_a_contrastar} kg) = {probabilidad:.2f}')
plt.title('Distribución Normal de Papel Desechado por Hogares')
plt.xlabel('Cantidad de papel (kg)')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(True)
plt.show()

# Datos reales (esto sería una lista de valores reales que tengas)
# Ejemplo: datos_reales = [3.5, 4.2, 5.1, 6.3, 4.5, ...]
datos_reales = [...]  # Reemplaza esto con tus datos reales

# Si hay datos reales, comparar con el modelo ideal
if datos_reales:
    media_real = np.mean(datos_reales)
    desviacion_estandar_real = np.std(datos_reales, ddof=1)
    comparacion = pd.DataFrame({
        'Modelo': ['Ideal', 'Real'],
        'Media': [media, media_real],
        'Desviación Estándar': [desviacion_estandar, desviacion_estandar_real]
    })

    valores_z_reales = [(x - media_real) / desviacion_estandar_real for x in datos_reales]
    tabla_z = pd.DataFrame({
        'Datos Reales': datos_reales,
        'Valor Z': valores_z_reales
    })

    print("Comparación de la media y desviación estándar del modelo ideal y los datos reales:")
    print(comparacion)
    print("\nTabla de valores Z de los datos reales:")
    print(tabla_z)
