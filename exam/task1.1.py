import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Загрузка данных
data = np.load("data1.npz")
x, y = data['x'], data['y']

# Объединение x и y в двумерный массив
points = np.column_stack((x, y))

# Кластеризация с помощью KMeans
kmeans = KMeans(n_clusters=2, random_state=42)
labels = kmeans.fit_predict(points)
centroids = kmeans.cluster_centers_

# Визуализация
plt.figure(figsize=(8, 6))
plt.scatter(points[:, 0], points[:, 1], c=labels, cmap='viridis', s=30, label='Points')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title('KMeans Clustering (2 Clusters)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
