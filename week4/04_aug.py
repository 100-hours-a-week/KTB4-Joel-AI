import numpy as np
from sklearn.datasets import make_moons
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# 4. 가상 데이터셋을 준비하고, 증강(Data Augmentation) 기법을 적용했을 때와 적용하지 않았을 때 모델 성능을 비교하세요.

SEED = 7
rng = np.random.default_rng(SEED)

X, y = make_moons( # 서로 마주 보는 두 개의 초승달 모양 클러스터를 가진 2차원 가상 데이터셋을 생성하는 함수
    n_samples=160,
    noise=0.2,
    random_state=SEED,
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.6,
    stratify=y,
    random_state=SEED,
)

# 테스트 데이터에도
X_test = X_test + rng.normal(loc=0.0, scale=0.12, size=X_test.shape)

def build_model():
    return Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000)),
    ])

def augment_with_noise(X_data, y_data, repeat=8, noise_scale=0.1):
    augmented_X = [X_data]
    augmented_y = [y_data]

    for _ in range(repeat):
        noise = rng.normal(loc=0.0, scale=noise_scale, size=X_data.shape)
        augmented_X.append(X_data + noise)
        augmented_y.append(y_data)

    return np.vstack(augmented_X), np.concatenate(augmented_y)


plain_model = build_model()
plain_model.fit(X_train, y_train)
plain_pred = plain_model.predict(X_test)

X_train_aug, y_train_aug = augment_with_noise(X_train, y_train)

aug_model = build_model()
aug_model.fit(X_train_aug, y_train_aug)
aug_pred = aug_model.predict(X_test)

print("# before aug.:", len(X_train))
print("# after aug.:", len(X_train_aug))
print("Acc. before aug.:", accuracy_score(y_test, plain_pred))
print("Acc. after aug.:", accuracy_score(y_test, aug_pred)) # 왜 같지 근데 -> seed 바꾸기!
