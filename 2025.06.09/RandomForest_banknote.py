import pandas as pd
from sklearn.metrics import (fbeta_score, confusion_matrix, 
                            precision_score, recall_score, 
                            accuracy_score, f1_score)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from pathlib import Path
import os

def evaluate_banknote_authentication():
    """
    Оценивает модель аутентификации банкнот с помощью RandomForest.
    Выводит основные метрики классификации.
    """
    
    # 1. Загрузка и подготовка данных
    project_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    data_path = project_dir / "banknote-auth.csv"
    
    banknote_data = pd.read_csv(data_path)
    features = banknote_data.drop("class", axis=1)
    target = banknote_data["class"]
    
    # 2. Разделение данных на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(
        features, target,
        test_size=0.2,
        random_state=42,  
        stratify=target
    )
    
    # 3. Создание и обучение модели
    model = RandomForestClassifier(
        n_estimators=50,      # Увеличено количество деревьев
        max_depth=5,
        bootstrap=True,
        n_jobs=-1,
        random_state=42,
        class_weight='balanced'  # Учет дисбаланса классов
    )
    
    model.fit(X_train, y_train)
    
    # 4. Предсказание и оценка модели
    y_pred = model.predict(X_test)
    
    # 5. Расчет метрик
    metrics = {
        'Точность (Accuracy)': accuracy_score(y_test, y_pred),
        'Специфичность': recall_score(y_test, y_pred, pos_label=0),
        'Точность (Precision)': precision_score(y_test, y_pred),
        'Полнота (Recall)': recall_score(y_test, y_pred),
        'F1-мера': f1_score(y_test, y_pred),
        'F-бета (β=0.5)': fbeta_score(y_test, y_pred, beta=0.5)
    }
    
    # 6. Вывод результатов
    print("\nОЦЕНКА МОДЕЛИ АУТЕНТИФИКАЦИИ БАНКНОТ")
    print("="*50)
    for name, value in metrics.items():
        print(f"{name}: {value:.1%}")
    
    # Дополнительно: вывод матрицы ошибок
    print("\nМатрица ошибок:")
    print(confusion_matrix(y_test, y_pred))

if __name__ == "__main__":
    evaluate_banknote_authentication()