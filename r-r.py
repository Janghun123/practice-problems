import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# 📌 3차원 데이터 생성
X, _ = make_blobs(n_samples=300, centers=5, n_features=3, random_state=42)

# 📌 K-Means 클러스터링
kmeans = KMeans(n_clusters=5, random_state=42)
labels = kmeans.fit_predict(X)
centroids = kmeans.cluster_centers_

# 📊 3차원 시각화
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')  # 3D 그래프 생성

# 데이터 포인트 시각화
ax.scatter(X[:, 0], X[:, 1], X[:, 2], 
           c=labels, cmap='viridis', s=30)

# 중심점 시각화
ax.scatter(centroids[:, 0], 
           centroids[:, 1], 
           centroids[:, 2],
           c='red', 
           marker='X', 
           s=200)

ax.set_title("3D K-Means Clustering")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.show()
