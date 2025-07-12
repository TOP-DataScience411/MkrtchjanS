import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from pathlib import Path
import os

def prepare_boston_data():
    """
    Функция для подготовки данных Boston Housing:
    - Загрузка данных
    - Удаление выбросов
    - Отбор признаков
    - Нормализация данных
    - Сохранение обработанных данных
    """
    
    project_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    input_file = project_dir / "boston.csv"
    output_file = project_dir / "boston_filter.csv"
    
    # Загрузка данных с пропуском строк, начинающихся с '#'
    housing_data = pd.read_csv(input_file, comment='#')
    
    # Удаление записей с максимальной стоимостью (выбросы)
    max_price = housing_data["MEDV"].max()
    housing_data = housing_data[housing_data["MEDV"] != max_price].copy()
    
    # Отбор признаков:
    # Удаляем признаки с высокой корреляцией между собой (>0.7)
    # или с низкой корреляцией с целевой переменной
    features_to_drop = ["DIS", "CHAS", "NOX", "TAX", "MEDV"]
    selected_features = housing_data.drop(features_to_drop, axis=1)
    
    # Нормализация данных (Z-score нормализация)
    scaler = StandardScaler()
    normalized_data = pd.DataFrame(
        scaler.fit_transform(selected_features),
        columns=selected_features.columns
    )
    
    # Добавляем целевую переменную (без нормализации)
    normalized_data["MEDV"] = housing_data["MEDV"]
    
    # Сохраняем обработанные данные
    normalized_data.to_csv(output_file, index=False)
    
    # Визуализация корреляций (закомментировано по умолчанию)
    # plot_correlation_matrix(normalized_data, 'boston_filter.png')
    
    return normalized_data

def plot_correlation_matrix(data, filename):
    """
    Вспомогательная функция для визуализации матрицы корреляций
    """
    corr_matrix = data.corr().round(2)
    fig, axs = plt.subplots(len(data.columns), len(data.columns), figsize=(28, 28))
    
    for i, col1 in enumerate(data.columns):
        for j, col2 in enumerate(data.columns):
            axs[i, j].scatter(data[col1], data[col2], s=7)
            axs[i, j].text(
                data[col1].max(), 
                data[col2].max(),
                f'r={corr_matrix.loc[col1, col2]}\n',
                ha='right',
                va='top',
            )
            axs[i, j].set(
                xticks=[], 
                yticks=[],
                xlabel=col1,
                ylabel=col2,
            )
    
    plt.savefig(Path(filename), dpi=200)
    plt.close()

if __name__ == "__main__":
    processed_data = prepare_boston_data()
    print("Данные успешно обработаны и сохранены в boston_filter.csv")
    print(f"Использовано признаков: {len(processed_data.columns)-1}")