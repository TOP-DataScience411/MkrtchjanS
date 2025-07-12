import pandas as pd
from sklearn.ensemble import StackingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import (confusion_matrix, fbeta_score, 
                           precision_score, recall_score,
                           accuracy_score, f1_score)
from sklearn.model_selection import train_test_split
from pathlib import Path
import os

def evaluate_breast_cancer_model():
    """
    Оценивает модель диагностики рака груди с использованием стекинга классификаторов.
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
    
    # 2. Разделение данных
    X_train, X_test, y_train, y_test = train_test_split(
        features,
        diagnosis,
        train_size=0.15,    
        random_state=42,     
        stratify=diagnosis   
    )
    
    # 3. Создание ансамблевой модели (стекинг)
    base_models = [
        ('random_forest', RandomForestClassifier(
            n_estimators=50, 
            max_depth=10,
            min_samples_split=5,
            random_state=42,
            class_weight='balanced'
        )),
        ('decision_tree', DecisionTreeClassifier(
            max_depth=8,       
            min_samples_split=5,
            random_state=42
        )),
        ('svm', LinearSVC(
            C=1.0,            
            random_state=42,
            max_iter=10000,   
            dual=False
        ))
    ]
    
    ensemble = StackingClassifier(
        estimators=base_models,
        final_estimator=LogisticRegression(
            penalty='l2',      # L2 регуляризация
            C=0.1,
            solver='liblinear',
            random_state=42,
            max_iter=1000
        ),
        cv=5,                 
        n_jobs=-1             
    )
    
    # 4. Обучение и оценка модели
    print("Обучение ансамблевой модели...")
    ensemble.fit(X_train, y_train)
    
    # Оценка точности
    train_score = ensemble.score(X_train, y_train)
    test_score = ensemble.score(X_test, y_test)
    print(f"\nТочность на обучающей выборке: {train_score:.1%}")
    print(f"Точность на тестовой выборке: {test_score:.1%}")
    
    # 5. Предсказания и метрики
    y_pred = ensemble.predict(X_test)
    
    # Расчет метрик классификации
    metrics = {
        'Точность (Accuracy)': accuracy_score(y_test, y_pred),
        'Специфичность (для класса 0)': recall_score(y_test, y_pred, pos_label=0),
        'Точность предсказаний (Precision)': precision_score(y_test, y_pred),
        'Полнота (Recall)': recall_score(y_test, y_pred),
        'F1-мера': f1_score(y_test, y_pred),
        'F-бета метрика (β=0.5)': fbeta_score(y_test, y_pred, beta=0.5)
    }
    
    # 6. Вывод результатов
    print("\nОЦЕНКА МОДЕЛИ ДИАГНОСТИКИ РАКА ГРУДИ")
    print("=" * 60)
    for metric_name, value in metrics.items():
        print(f"{metric_name}: {value:.1%}")
    
    # 7. Дополнительная информация
    print("\nМатрица ошибок:")
    print(confusion_matrix(y_test, y_pred))
    
    print("\nПроизводительность базовых моделей:")
    for name, model in ensemble.named_estimators_.items():
        print(f"{name}: {model.score(X_test, y_test):.1%}")

if __name__ == "__main__":
    evaluate_breast_cancer_model()