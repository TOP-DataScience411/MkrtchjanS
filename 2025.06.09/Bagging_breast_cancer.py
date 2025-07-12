# Импорт необходимых библиотек
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import fbeta_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
import os
from pathlib import Path

def evaluate_breast_cancer_model():
    """
    Функция для оценки модели классификации рака груди.
    Загружает данные, обучает модель и выводит метрики качества.
    """

    current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    
    # Загружаем данные о диагностике рака груди
    cancer_data = pd.read_csv(current_dir / "breast_cancer_filter.csv")
    
    # Целевая переменная (диагноз)
    diagnosis = cancer_data["target"]
    
    # Признаки (все столбцы кроме target)
    features = cancer_data.drop("target", axis=1)

    # Разделение данных на обучающую и тестовую выборки
    # 80% - обучение, 20% - тестирование
    X_train, X_test, y_train, y_test = train_test_split(
        features, diagnosis,
        test_size=0.2,
        random_state=42  
    )

    # Создание и обучение ансамблевой модели
    # Используем бэггинг с логистической регрессией
    ensemble_model = BaggingClassifier(
        estimator=LogisticRegression(max_iter=1000), 
        n_estimators=10,           
        bootstrap=True,            
        n_jobs=-1,                
        random_state=42                
    )
    
    # Обучение модели
    ensemble_model.fit(X_train, y_train)
    
    # Предсказание на тестовых данных
    predictions = ensemble_model.predict(X_test)

    # Расчет матрицы ошибок
    conf_matrix = confusion_matrix(y_test, predictions)
    # Распаковываем матрицу ошибок
    true_neg, false_pos, false_neg, true_pos = conf_matrix.ravel()

    # Вычисление метрик качества
    metrics = {
        'Точность': (true_pos + true_neg) / (true_pos + false_pos + false_neg + true_neg),
        'Специфичность': true_neg / (true_neg + false_pos),
        'Точность (Precision)': true_pos / (false_pos + true_pos),
        'Полнота (Recall)': true_pos / (false_neg + true_pos),
        'F1-мера': 2 * (true_pos / (false_pos + true_pos)) * (true_pos / (false_neg + true_pos)) / 
                  ((true_pos / (false_pos + true_pos)) + (true_pos / (false_neg + true_pos))),
        'F-бета метрика (β=0.5)': fbeta_score(y_test, predictions, beta=0.5)
    }

    print("\nОЦЕНКА МОДЕЛИ КЛАССИФИКАЦИИ РАКА ГРУДИ")
    print("="*50)
    for name, value in metrics.items():
        print(f"{name}: {value:.1%}")

if __name__ == "__main__":
    evaluate_breast_cancer_model()