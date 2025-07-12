import pandas as pd
from sklearn.ensemble import StackingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import (fbeta_score, confusion_matrix, 
                           precision_score, recall_score,
                           accuracy_score, f1_score)
from sklearn.model_selection import train_test_split
from pathlib import Path
import os

def evaluate_banknote_authentication():
    """
    Оценивает модель аутентификации банкнот с использованием стекинга классификаторов.
    Выводит основные метрики качества классификации.
    """
    
    # 1. Загрузка и подготовка данных
    project_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    data_path = project_dir / "banknote-auth.csv"
    
    try:
        banknote_data = pd.read_csv(data_path)
    except FileNotFoundError:
        print(f"Ошибка: Файл данных не найден по пути {data_path}")
        return
    
    # Разделение на признаки и целевую переменную
    features = banknote_data.drop("class", axis=1)
    target = banknote_data["class"]
    
    # 2. Разделение данных
    X_train, X_test, y_train, y_test = train_test_split(
        features,
        target,
        train_size=0.2,      
        random_state=42,     
        stratify=target     
    )
    
    # 3. Создание ансамблевой модели (стекинг)
    base_models = [
        ('random_forest', RandomForestClassifier(
            n_estimators=50,  
            max_depth=10,
            random_state=42
        )),
        ('decision_tree', DecisionTreeClassifier(
            max_depth=8,      
            min_samples_split=5,
            random_state=42
        )),
        ('svm', LinearSVC(
            C=1.0,            
            random_state=42,
            max_iter=10000     
        ))
    ]
    
    ensemble = StackingClassifier(
        estimators=base_models,
        final_estimator=LogisticRegression(
            penalty='l2',      
            C=0.1,
            solver='liblinear',
            random_state=42
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
    
    # Расчет метрик
    metrics = {
        'Точность (Accuracy)': accuracy_score(y_test, y_pred),
        'Специфичность': recall_score(y_test, y_pred, pos_label=0),
        'Точность предсказания (Precision)': precision_score(y_test, y_pred),
        'Полнота (Recall)': recall_score(y_test, y_pred),
        'F1-мера': f1_score(y_test, y_pred),
        'F-бета (β=0.5)': fbeta_score(y_test, y_pred, beta=0.5)
    }
    
    # 6. Вывод результатов
    print("\nОЦЕНКА АНСАМБЛЕВОЙ МОДЕЛИ")
    print("=" * 50)
    for metric_name, value in metrics.items():
        print(f"{metric_name}: {value:.1%}")
    
    # 7. Дополнительная информация
    print("\nМатрица ошибок:")
    print(confusion_matrix(y_test, y_pred))
    
    print("\nВажность базовых моделей:")
    for name, model in ensemble.named_estimators_.items():
        print(f"{name}: {model.score(X_test, y_test):.1%}")

if __name__ == "__main__":
    evaluate_banknote_authentication()