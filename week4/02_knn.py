from sklearn.datasets import make_blobs
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# 2. 가상 데이터셋을 생성하고, K-최근접이웃(K-NN) 알고리즘으로 학습·예측을 수행해 보세요.

SEED = 42
X, y = make_blobs( # Clustering 알고리즘 테스트용
    n_samples=500,
    centers=3,
    n_features=2,
    cluster_std=1.4,
    random_state=SEED,
)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    stratify=y,
    random_state=SEED,
)

# 데이터 정규화 (K-NN은 거리 기반 알고리즘이므로 스케일 조정이 중요)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled) # 정확도
print(accuracy_score(y_test, y_pred)) # K-NN 정확도
