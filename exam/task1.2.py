import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Загрузка данных
data = np.load("data1.npz")
x, y = data['x'], data['y']

# Выделяем линейную часть выборки:
# Условие: x и y положительные и находятся в пределах [0, 10]
mask = (x > 0) & (x < 10) & (y > 0) & (y < 10)
x_linear = x[mask].reshape(-1, 1)
y_linear = y[mask]

# Обучение модели линейной регрессии
model = LinearRegression()
model.fit(x_linear, y_linear)
y_pred = model.predict(x_linear)

# Коэффициенты модели
slope = model.coef_[0]
intercept = model.intercept_

# Визуализация результата
plt.figure(figsize=(8, 6))
plt.scatter(x_linear, y_linear, color='blue', label='Linear Part (Selected)')
plt.plot(x_linear, y_pred, color='red', linewidth=2, label='Regression Line')
plt.title(f'Linear Regression: y = {slope:.2f}x + {intercept:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
