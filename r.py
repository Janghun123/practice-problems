import numpy as np
import matplotlib.pyplot as plt

# 샘플 데이터 생성
from sklearn.datasets import make_blobs
X, _ = make_blobs(n_samples = 300, centers = 2, random_state = 42)

# K-means 구현
def k_means(X, k, max_iters = 100):
    # 초기 중심점 무작위 선택
    np.random.seed(0)
    indices = np.random.choice(len(X), k, replace = False)
    centroids = X[indices]
    
    for _ in range(max_iters):
        # 각 점을 가장 가까운 중심점에 할당
        distance = np.linalg.norm(X[:, np.newaxis] - centroids, axis = 2)
        labels = np.argmin(distance, axis = 1)

        # 새로운 중심점 계산
        new_centroids = np.array([X[labels == i].mean(axis = 0) for i in range(k)])
        
        # 변화가 없으면 종료
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    # 값 반환환
    return centroids, labels

# 실행 (클러스터 개수 = N)
k = 2
# 센터로이드, 라벨 수
centorids, labels = k_means(X, k)

# 시각화
plt.scatter(X[:, 0], # 데이터의 첫 번째 열 (X 좌표)
            X[:, 1], # 데이터의 두 번째 열 (Y 좌표)
            c = labels, # 각 데이터 포인트에 클러스터 번호에 따라 색을 지정함
            cmap = 'viridis', # 색상 맵 (보->파->초->노)
            s = 30) # 점의 크기 
# 산점도 (2차원 데이더의 분포를 시각화)
plt.scatter(centorids[:,0 ], # 클러스터 중심점 X 좌표
            centorids[:, 1], # 클러스터 중심점 Y 좌표
            c = 'red', # 색
            marker = 'X', # 마커
            s = 200) # 중심점 강조
# 클러스터 센트로이드 색, 마크
plt.title("K-means Clustering")
plt.show()