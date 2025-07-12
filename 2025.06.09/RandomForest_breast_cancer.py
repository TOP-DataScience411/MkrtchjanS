import pandas as pd
from sklearn.metrics import (fbeta_score, confusion_matrix, 
                            precision_score, recall_score, 
                            accuracy_score, f1_score)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from pathlib import Path
import os

def evaluate_breast_cancer_model():
    """
    Оценивает модель классификации рака груди с использованием RandomForest.
    Выводит основные метрики качества классификации.
    """
    
    # 1. Загрузка и подготовка данных
    project_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    data_path = project_dir / "breast_cancer_filter.csv"
    
    try:
        cancer_data = pd.read_csv(data_path)
    except FileNotFoundError:
        print(f"Ошибка: Файл данных не найден по пути {data_path}")
        return
    
    # Разделение на признаки и целевую переменную
    features = cancer_data.drop("target", axis=1)
    diagnosis = cancer_data["target"]  # 0 - злокачественная, 1 - доброкачественная
    
    # 2. Разделение данных на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(
        features,
        diagnosis,
        test_size=0.2,
        random_state=42,  # Фиксируем random_state для воспроизводимости
        stratify=diagnosis  # Сохраняем распределение классов
    )
    
    # 3. Создание и обучение модели
    classifier = RandomForestClassifier(
        n_estimators=50,       # Увеличено количество деревьев
        max_depth=8,           # Увеличена глубина деревьев
        min_samples_split=5,   # Добавлены параметры регуляризации
        min_samples_leaf=2,
        bootstrap=True,
        n_jobs=-1,
        random_state=42,
        class_weight='balanced'  # Учет дисбаланса классов
    )
    
    print("Обучение модели RandomForest...")
    classifier.fit(X_train, y_train)
    
    # 4. Предсказание и оценка модели
    y_pred = classifier.predict(X_test)
    
    # 5. Расчет метрик
    metrics = {
        'Точность (Accuracy)': accuracy_score(y_test, y_pred),
        'Специфичность (True Negative Rate)': recall_score(y_test, y_pred, pos_label=0),
        'Точность предсказания (Precision)': precision_score(y_test, y_pred),
        'Полнота (Recall/Sensitivity)': recall_score(y_test, y_pred),
        'F1-мера': f1_score(y_test, y_pred),
        'F-бета метрика (β=0.5)': fbeta_score(y_test, y_pred, beta=0.5)
    }
    
    # 6. Вывод результатов
    print("\nОЦЕНКА МОДЕЛИ КЛАССИФИКАЦИИ РАКА ГРУДИ")
    print("=" * 60)
    for metric_name, value in metrics.items():
        print(f"{metric_name}: {value:.1%}")
    
    # 7. Дополнительная информация
    print("\nМатрица ошибок:")
    print(confusion_matrix(y_test, y_pred))
    
    print("\nВажность признаков:")
    for feature, importance in zip(features.columns, classifier.feature_importances_):
        print(f"{feature}: {importance:.3f}")

if __name__ == "__main__":
    evaluate_breast_cancer_model()