import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import fbeta_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
import os
from pathlib import Path

# Загрузка данных
current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
dataset = pd.read_csv(current_dir / "banknote-auth.csv")

# Подготовка данных
target_var = dataset["class"]
features = dataset.drop("class", axis=1)

# Разделение на обучающую и тестовую выборки
X_train, X_test, Y_train, Y_test = train_test_split(
    features, target_var, test_size=0.2, random_state=42
)

# Создание и обучение модели
ensemble_model = BaggingClassifier(
    base_estimator=LogisticRegression(max_iter=1000),
    n_estimators=10,
    bootstrap=True,
    n_jobs=-1,
    random_state=42
)

ensemble_model.fit(X_train, Y_train)
predictions = ensemble_model.predict(X_test)

# Оценка модели
conf_matrix = confusion_matrix(Y_test, predictions)
true_neg, false_pos, false_neg, true_pos = conf_matrix.ravel()

model_accuracy = (true_neg + true_pos) / (true_neg + false_pos + false_neg + true_pos)
true_negative_rate = true_neg / (true_neg + false_pos)
positive_predictive_value = true_pos / (false_pos + true_pos)
sensitivity = true_pos / (false_neg + true_pos)

f1_measure = 2 * (positive_predictive_value * sensitivity) / (positive_predictive_value + sensitivity)
custom_fbeta = fbeta_score(Y_test, predictions, beta=0.5)

print("Результаты оценки модели:")
print(f"Точность: {model_accuracy:.1%}")
print(f"Специфичность: {true_negative_rate:.1%}")
print(f"Прецизионность: {positive_predictive_value:.1%}")
print(f"Полнота: {sensitivity:.1%}")
print(f"F1-мера: {f1_measure:.1%}")
print(f"F-бета метрика (β=0.5): {custom_fbeta:.1%}")
