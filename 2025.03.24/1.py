import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

science_df = pd.read_csv('science_investetions.csv', delim_whitespace=True, skiprows=20, header=None)
science_df.columns = ['Year', 'Investments']
science_df['Year'] = science_df['Year'].astype(int)
science_df['Investments'] = science_df['Investments'].astype(float)

malignancy_df = pd.read_csv('early_malignancy.csv', delim_whitespace=True, skiprows=19, header=None, usecols=[0, 1])
malignancy_df.columns = ['Year', 'Malignancy']
malignancy_df['Year'] = malignancy_df['Year'].astype(int)
malignancy_df['Malignancy'] = malignancy_df['Malignancy'].astype(float)

df = pd.merge(science_df, malignancy_df, on='Year').sort_values('Year')

def compute_lags(df, max_lag=5):
    for lag in range(-max_lag, max_lag + 1):
        temp = df.copy()
        if lag > 0:
            temp['Investments'] = temp['Investments'].shift(lag)
        elif lag < 0:
            temp['Malignancy'] = temp['Malignancy'].shift(-lag)
        temp = temp.dropna()
        if not temp.empty:
            r = np.corrcoef(temp['Investments'], temp['Malignancy'])[0, 1]
            print("Сдвиг:", lag, "лет")
            print("Investments:", temp['Investments'].tolist())
            print("Malignancy:", temp['Malignancy'].tolist())
            print("Корреляция:", round(r, 4), "\n")

compute_lags(df)

scaler = MinMaxScaler()
norm = scaler.fit_transform(df[['Investments', 'Malignancy']])
df[['Investments_norm', 'Malignancy_norm']] = norm

plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['Investments_norm'], label='Investments (norm)', marker='o')
plt.plot(df['Year'], df['Malignancy_norm'], label='Malignancy (norm)', marker='s')
plt.title('Нормализованные данные')
plt.xlabel('Год')
plt.ylabel('Нормализованные значения')
plt.grid(True)
plt.legend()
plt.savefig('task1_correlation_plot.png', dpi=300)
