import pandas as pd
from datetime import datetime
from numpy import array
from matplotlib import pyplot as plt
from scipy.stats import linregress

# Русские месяцы
rus_to_eng_months = {
    'янв': 'Jan', 'фев': 'Feb', 'мар': 'Mar', 'апр': 'Apr',
    'май': 'May', 'июн': 'Jun', 'июл': 'Jul', 'авг': 'Aug',
    'сен': 'Sep', 'окт': 'Oct', 'ноя': 'Nov', 'дек': 'Dec'
}

# Загрузка и преобразование
def load_and_translate_dates(file_path):
    raw_data = pd.read_csv(file_path, header=None).iloc[:, 0]
    parsed = []
    for row in raw_data:
        parts = row.split()
        for rus, eng in rus_to_eng_months.items():
            parts[0] = parts[0].replace(rus, eng)
        date_obj = datetime.strptime(parts[0], "%d.%b.%y")
        parsed.append((date_obj, float(parts[1].replace(',', '.'))))
    return parsed

dizel_data = load_and_translate_dates("dizel_fuel_rus_prices.csv")
urals_data = load_and_translate_dates("urals_oil_rus_export_prices.csv")

# Совмещение
merged_data = []
for d_date, d_val in dizel_data:
    for u_date, u_val in urals_data:
        if d_date.year == u_date.year and d_date.month == u_date.month:
            merged_data.append((d_date, d_val, u_val))
merged_data = array(merged_data)

# Корреляции по сдвигам
max_shift = len(merged_data) - 2
results = []
for shift in range(-max_shift, max_shift + 1):
    if shift > 0:
        x = merged_data[:-shift, 1].astype(float)
        y = merged_data[shift:, 2].astype(float)
    elif shift < 0:
        x = merged_data[-shift:, 1].astype(float)
        y = merged_data[:shift, 2].astype(float)
    else:
        x = merged_data[:, 1].astype(float)
        y = merged_data[:, 2].astype(float)
    if len(x) > 2:
        r = round(pd.Series(x).corr(pd.Series(y)), 4)
        print(f"Сдвиг: {shift} мес\nКорреляция: {r}")
        results.append((r, shift, x, y))

# Лучшая корреляция
best_r, best_shift, best_x, best_y = max(results, key=lambda x: abs(x[0]))
reg = linregress(best_x, best_y)

print(f"\nЛучшая корреляция: r = {best_r}, сдвиг: {best_shift} месяцев")
print(f"Уравнение регрессии: y = {reg.intercept:.2f} + {reg.slope:.2f} * x")

# График
plt.figure(figsize=(10, 6))
plt.scatter(best_x, best_y, s=10, label="Данные")
plt.plot(best_x, reg.intercept + reg.slope * best_x, color='red',
         label=f"y = {reg.intercept:.2f} + {reg.slope:.2f} * x")
plt.title(f"Линейная регрессия (сдвиг: {best_shift} мес, r = {best_r})")
plt.xlabel("Цена дизельного топлива (руб./т)")
plt.ylabel("Цена Urals ($/баррель)")
plt.legend()
plt.grid(True)
plt.savefig("final_best_correlation_plot.png", dpi=300)
