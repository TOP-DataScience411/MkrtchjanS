import pandas as pd
from sklearn.ensemble import StackingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression, RidgeCV
from sklearn.svm import LinearSVR
from sklearn.metrics import (mean_absolute_error, mean_squared_error,
                           root_mean_squared_error, r2_score)
from sklearn.model_selection import train_test_split
from pathlib import Path
import os

def evaluate_boston_housing_model():
    """
    Оценивает модель предсказания цен на жилье в Бостоне
    с использованием стекинга регрессоров.
    Выводит основные метрики качества регрессии.
    """
    
    # 1. Загрузка и подготовка данных
    project_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    data_path = project_dir / "boston_filter.csv"
    
    try:
        housing_data = pd.read_csv(data_path)
    except FileNotFoundError:
        print(f"Ошибка: Файл данных не найден по пути {data_path}")
        return
    
    # Разделение на признаки и целевую переменную
    features = housing_data.drop("MEDV", axis=1)
    target = housing_data["MEDV"]  # Медианная стоимость домов (в $1000)
    
    # 2. Разделение данных
    X_train, X_test, y_train, y_test = train_test_split(
        features,
        target,
        train_size=0.3,       # 30% на обучение
        random_state=42,      # Фиксируем random_state для воспроизводимости
        shuffle=True          # Перемешивание данных перед разделением
    )
    
    # 3. Создание ансамблевой модели (стекинг)
    base_models = [
        ('ridge', RidgeCV(
            alphas=[0.1, 1.0, 10.0],  # Диапазон параметров регуляризации
            cv=5                      # Количество фолдов для кросс-валидации
        )),
        ('linear', LinearRegression(
            copy_X=True,
            n_jobs=-1
        )),
        ('svr', LinearSVR(
            C=1.0,             # Параметр регуляризации
            random_state=42,
            max_iter=10000     # Увеличение числа итераций
        ))
    ]
    
    ensemble = StackingRegressor(
        estimators=base_models,
        final_estimator=RandomForestRegressor(
            n_estimators=100,  # Увеличено количество деревьев
            max_depth=10,
            min_samples_split=5,
            random_state=42,
            n_jobs=-1
        ),
        cv=5,                 # Количество фолдов для кросс-валидации
        n_jobs=-1             # Использование всех ядер
    )
    
    # 4. Обучение и оценка модели
    print("Обучение ансамблевой модели...")
    ensemble.fit(X_train, y_train)
    
    # Оценка производительности
    train_score = ensemble.score(X_train, y_train)
    test_score = ensemble.score(X_test, y_test)
    print(f"\nR² на обучающей выборке: {train_score:.4f}")
    print(f"R² на тестовой выборке: {test_score:.4f}")
    
    # 5. Предсказания и метрики
    y_pred = ensemble.predict(X_test)
    
    # Расчет метрик регрессии
    metrics = {
        'Средняя абсолютная ошибка (MAE)': mean_absolute_error(y_test, y_pred),
        'Среднеквадратичная ошибка (MSE)': mean_squared_error(y_test, y_pred),
        'Корень из MSE (RMSE)': root_mean_squared_error(y_test, y_pred),
        'Коэффициент детерминации (R²)': r2_score(y_test, y_pred)
    }
    
    # 6. Вывод результатов
    print("\nОЦЕНКА АНСАМБЛЕВОЙ РЕГРЕССИОННОЙ МОДЕЛИ")
    print("=" * 60)
    for metric_name, value in metrics.items():
        print(f"{metric_name}: {value:.4f}")
    
    # 7. Дополнительная информация
    print("\nПроизводительность базовых моделей:")
    for name, model in ensemble.named_estimators_.items():
        print(f"{name}: R² = {model.score(X_test, y_test):.4f}")

if __name__ == "__main__":
    evaluate_boston_housing_model()