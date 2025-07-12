import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from pathlib import Path
import os

def prepare_breast_cancer_data():
    """
    Подготавливает данные о раке груди:
    1. Загружает исходные данные
    2. Создает DataFrame с признаками и целевой переменной
    3. Нормализует данные (Z-нормализация)
    4. Сохраняет в CSV файл
    """
    
    # Получаем путь к директории проекта
    project_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    output_file = project_dir / "breast_cancer_filter.csv"
    
    # Загрузка встроенного набора данных о раке груди
    cancer_data = load_breast_cancer()
    
    # Создаем DataFrame с признаками
    features_df = pd.DataFrame(
        data=cancer_data['data'],
        columns=cancer_data['feature_names']
    )
    
    # Создаем Series с целевой переменной (0 - злокачественная, 1 - доброкачественная)
    target_series = pd.Series(
        data=cancer_data['target'],
        name='diagnosis'  # Более понятное имя целевой переменной
    )
    
    # Нормализация данных (Z-score нормализация)
    # Используем описательные статистики для вычисления среднего и стандартного отклонения
    normalized_features = (features_df - features_df.mean()) / features_df.std()
    
    # Объединяем нормализованные признаки и целевую переменную
    normalized_data = normalized_features.copy()
    normalized_data['diagnosis'] = target_series
    
    # Сохраняем обработанные данные в CSV файл
    normalized_data.to_csv(output_file, index=False)
    
    print(f"Данные успешно сохранены в файл: {output_file}")
    print(f"Количество признаков: {len(normalized_features.columns)}")
    print(f"Количество образцов: {len(normalized_data)}")
    
    return normalized_data

if __name__ == "__main__":
    processed_data = prepare_breast_cancer_data()
    print("\nПервые 5 записей обработанных данных:")
    print(processed_data.head())