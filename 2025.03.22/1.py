import numpy as np
from scipy import stats

# Исходные данные
N = np.array([492, 581, 673, 522, 756, 555, 602, 531, 472, 411])
R = np.array([741, 731, 802, 723, 743, 722, 775, 706, 747, 719, 847, 684, 765, 673])

alpha = 0.05  # Уровень значимости

# 1. Проверка крайних членов вариационных рядов с помощью критерия Ирвина
def check_extreme_values(data, alpha=0.05):
    sorted_data = np.sort(data)
    n = len(sorted_data)
    lambda_table = {10: 1.5, 14: 1.6}  # Табличные значения критерия Ирвина для n=10 и n=14
    
    # Для первого и последнего элементов
    lambda_1 = (sorted_data[1] - sorted_data[0]) / np.std(data, ddof=1)
    lambda_n = (sorted_data[-1] - sorted_data[-2]) / np.std(data, ddof=1)
    
    lambda_critical = lambda_table.get(n, 1.5)  # Берем табличное значение или 1.5 по умолчанию
    
    print(f"Критерий Ирвина для минимального значения: {lambda_1:.3f}, критическое значение: {lambda_critical}")
    print(f"Критерий Ирвина для максимального значения: {lambda_n:.3f}, критическое значение: {lambda_critical}")
    
    if lambda_1 > lambda_critical:
        print("Минимальное значение является выбросом (гипотеза отвергается)")
    else:
        print("Минимальное значение не является выбросом (гипотеза принимается)")
    
    if lambda_n > lambda_critical:
        print("Максимальное значение является выбросом (гипотеза отвергается)")
    else:
        print("Максимальное значение не является выбросом (гипотеза принимается)")

print("Проверка крайних значений для N:")
check_extreme_values(N)
print("\nПроверка крайних значений для R:")
check_extreme_values(R)

# 2. Проверка гипотезы о равенстве дисперсий (F-тест)
def check_variances(a, b, alpha=0.05):
    var_a = np.var(a, ddof=1)
    var_b = np.var(b, ddof=1)
    
    if var_a > var_b:
        f_value = var_a / var_b
        df1, df2 = len(a) - 1, len(b) - 1
    else:
        f_value = var_b / var_a
        df1, df2 = len(b) - 1, len(a) - 1
    
    p_value = stats.f.sf(f_value, df1, df2) * 2  # Двусторонний тест
    
    print(f"\nF-тест на равенство дисперсий:")
    print(f"F-значение: {f_value:.3f}, p-значение: {p_value:.4f}")
    
    if p_value < alpha:
        print(f"Гипотеза о равенстве дисперсий отвергается (p < {alpha})")
    else:
        print(f"Гипотеза о равенстве дисперсий принимается (p >= {alpha})")
    
    return p_value >= alpha

equal_variances = check_variances(N, R, alpha)

# 3. Проверка гипотезы о равенстве средних (t-тест)
def check_means(a, b, alpha=0.05, equal_var=True):
    t_stat, p_value = stats.ttest_ind(a, b, equal_var=equal_var)
    
    print(f"\nT-тест на равенство средних (равенство дисперсий: {equal_var}):")
    print(f"t-значение: {t_stat:.3f}, p-значение: {p_value:.4f}")
    
    if p_value < alpha:
        print(f"Гипотеза о равенстве средних отвергается (p < {alpha})")
    else:
        print(f"Гипотеза о равенстве средних принимается (p >= {alpha})")

check_means(N, R, alpha, equal_variances)

# 4. Проверка гипотезы о нормальном распределении (Шапиро-Уилк)
def check_normality(data, name, alpha=0.05):
    stat, p_value = stats.shapiro(data)
    
    print(f"\nТест Шапиро-Уилка для {name}:")
    print(f"Статистика: {stat:.3f}, p-значение: {p_value:.4f}")
    
    if p_value < alpha:
        print(f"Гипотеза о нормальном распределении отвергается (p < {alpha})")
    else:
        print(f"Гипотеза о нормальном распределении принимается (p >= {alpha})")

check_normality(N, "N")
check_normality(R, "R")
