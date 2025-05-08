from pandas import read_csv
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from pathlib import Path
from sys import path
import numpy as np

# Загрузка набора данных
base_path = Path(path[0])
csv_path = base_path / 'housing_data_modified.csv'
df = read_csv(csv_path)

# Разделение признаков и целевой переменной
features = df.drop(columns=['PRICE'])
target = df['PRICE']

# Повторная оценка модели для стабильности
r2_total, rmse_total = 0, 0
iterations = 20

for i in range(iterations):
    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=i
    )

    reg_model = LinearRegression()
    reg_model.fit(x_train, y_train)
    predictions = reg_model.predict(x_test)

    r2 = r2_score(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions, squared=False)

    print(f'Итерация {i + 1}: R2 = {r2:.3f}, RMSE = {rmse:.2f}')
    r2_total += r2
    rmse_total += rmse

print(f'\nСредние метрики за {iterations} запусков:')
print(f'R2: {r2_total / iterations:.3f}')
print(f'RMSE: {rmse_total / iterations:.2f}')
