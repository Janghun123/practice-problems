import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = np.loadtxt("old_faithful_geyser.csv", delimiter = ",", skiprows = 1)

X = data

kmeans = KMeans(n_clusters = 2, random_state = 0)
kmeans.fit(X)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

print(f"SSE : {kmeans.inertia_:.2f}")
plt.figure(figsize=(8, 6))

plt.scatter(X[:, 0], X[:, 1], c = labels, s = 80, cmap = 'Accent', label = 'Points')

plt.scatter(centroids[:, 0], centroids[:, 1], c = 'red', marker = 'X', s = 200, label = 'Centroids')

plt.xlabel("Eruption duration (min)")
plt.ylabel("Waiting time (min)")
plt.title("K-means Clustering (NumPy only, no pandas)")
plt.legend()
plt.grid(True)
plt.show