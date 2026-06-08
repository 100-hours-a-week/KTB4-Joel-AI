from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# 가상 데이터셋을 생성한 뒤, 학습·검증·테스트 데이터셋으로 분할해 보세요

SEED = 42
X, y = make_classification(
    n_samples=1000,
    n_features=6,
    n_informative=4,
    n_redundant=1,
    n_classes=2,
    random_state=SEED,
)

# 테스트 데이터: 20% 
X_train_valid, X_test, y_train_valid, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=SEED,
)

# 남은 80%에서 검증 데이터 20%
# train 64%, valid 16%, test 20%
X_train, X_valid, y_train, y_valid = train_test_split(
    X_train_valid,
    y_train_valid,
    test_size=0.2,
    stratify=y_train_valid,
    random_state=SEED,
)
