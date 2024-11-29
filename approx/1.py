import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.exp(x)

x_data = np.linspace(0, 6, 100)
y_data = f(x_data)

# cтепень многочлена:
m = 3

# коэффициенты многочлена степени m:
coefficients = np.polyfit(x_data, y_data, m)

# функция многочлена на основе найденных коэффициентов:
polynomial = np.poly1d(coefficients)

# значения для многочлена:
y_fit = polynomial(x_data)

plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data, label='Исходная функция', color='blue')
plt.plot(x_data, y_fit, label=f'Аппроксимация многочленом степени {m}', color='red', linestyle='--')
plt.legend()
plt.title('Аппроксимация функции многочленом')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()
