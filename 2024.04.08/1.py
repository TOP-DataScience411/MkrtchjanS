from pandas import DataFrame, Series
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from numpy import fliplr
import numpy as np

dataset = load_breast_cancer()
features = DataFrame(dataset.data, columns=dataset.feature_names)
labels = Series(dataset.target)

normalized = (features - features.mean()) / features.std()

means_0 = normalized[labels == 0].mean()
means_1 = normalized[labels == 1].mean()
diffs = abs(means_0 - means_1)

ranking = DataFrame({
    "avg_0": means_0,
    "avg_1": means_1,
    "abs_diff": diffs
}).sort_values("abs_diff", ascending=False)

print("Model Evaluation Results:\n")

for idx in range(0, 30, 6):
    top_features = ranking.index[idx:idx+6]
    X = normalized[top_features]
    y = labels

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    cm = confusion_matrix(1 - y_test, 1 - y_pred)
    acc = round(1 - sum(fliplr(cm).diagonal()) / sum(cm.diagonal()), 2)

    print(f"Top features {idx+1}-{idx+6}:")
    print(f"Accuracy: {acc}")
    print(cm, end="\n\n")
