import pandas as pd
from sklearn.metrics import (
    mean_absolute_error, 
    mean_squared_error, 
    r2_score, 
    root_mean_squared_error
)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from pathlib import Path
import os

def train_and_evaluate_housing_model():
    """
    Обучает модель случайного леса для предсказания цен на жилье в Бостоне
    и оценивает ее производительность с помощью различных метрик.
    """
    
    # 1. Загрузка и подготовка данных
    project_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    data_path = project_dir / "boston_filter.csv"
    
    try:
        housing_data = pd.read_csv(data_path)
    except FileNotFoundError:
        print(f"Ошибка: Файл {data_path} не найден")
        return
    
    # Выделение признаков и целевой переменной
    features = housing_data.drop("MEDV", axis=1)
    target = housing_data["MEDV"]
    
    # 2. Разделение данных
    X_train, X_test, y_train, y_test = train_test_split(
        features, 
        target,
        test_size=0.3,
        random_state=42,  # Фиксируем random_state для воспроизводимости
        shuffle=True      # Перемешивание данных перед разделением
    )
    
    # 3. Создание и обучение модели
    regressor = RandomForestRegressor(
        n_estimators=150,    # Увеличено количество деревьев
        max_depth=15,
        min_samples_split=5, # Добавлены параметры для предотвращения переобучения
        min_samples_leaf=2,
        bootstrap=True,
        n_jobs=-1,
        random_state=42,
        verbose=1            # Вывод информации о процессе обучения
    )
    
    print("\nОбучение модели...")
    regressor.fit(X_train, y_train)
    
    # 4. Предсказание и оценка
    predictions = regressor.predict(X_test)
    
    # 5. Расчет метрик
    evaluation_metrics = {
        'Средняя абсолютная ошибка (MAE)': mean_absolute_error(y_test, predictions),
        'Среднеквадратичная ошибка (MSE)': mean_squared_error(y_test, predictions),
        'Корень из MSE (RMSE)': root_mean_squared_error(y_test, predictions),
        'Коэффициент детерминации (R²)': r2_score(y_test, predictions)
    }
    
    # 6. Вывод результатов
    print("\nРезультаты оценки модели:")
    print("=" * 50)
    for metric_name, value in evaluation_metrics.items():
        print(f"{metric_name}: {value:.4f}")
    
    # Дополнительная информация
    print(f"\nДополнительная информация:")
    print(f"- Количество деревьев: {regressor.n_estimators}")
    print(f"- Глубина деревьев: {regressor.max_depth}")
    print(f"- Обучено на {len(X_train)} образцах")
    print(f"- Протестировано на {len(X_test)} образцах")

if __name__ == "__main__":
    train_and_evaluate_housing_model()