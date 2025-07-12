import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error as mae,
    mean_squared_error as mse,
    r2_score as r2,
    root_mean_squared_error as rmse
)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingRegressor
import os
from pathlib import Path

def evaluate_regression_model():
    """
    Основная функция для оценки модели предсказания цен на жилье.
    Загружает данные, обучает модель и выводит метрики качества.
    """
    # Загрузка и подготовка данных
    project_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    housing_data = pd.read_csv(project_dir / "boston_filter.csv")
    
    y = housing_data["MEDV"]
    X = housing_data.drop("MEDV", axis=1)

    # Разделение данных
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, 
        test_size=0.3, 
        random_state=42
    )

    # Создание и обучение модели
    ensemble_regressor = BaggingRegressor(
        base_estimator=LinearRegression(),
        n_estimators=20,
        bootstrap=True,
        n_jobs=-1,
        random_state=42
    )
    
    ensemble_regressor.fit(X_train, y_train)
    y_pred = ensemble_regressor.predict(X_test)

    metrics = {
        "Средняя абсолютная ошибка (MAE)": mae(y_test, y_pred),
        "Среднеквадратичная ошибка (MSE)": mse(y_test, y_pred),
        "Корень из MSE (RMSE)": rmse(y_test, y_pred),
        "Коэффициент детерминации (R²)": r2(y_test, y_pred)
    }

    print("Результаты оценки регрессионной модели:")
    for name, value in metrics.items():
        print(f"{name}: {value:.4f}")

if __name__ == "__main__":
    evaluate_regression_model()