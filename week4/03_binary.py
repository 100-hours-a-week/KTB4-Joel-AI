from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.linear_model import Perceptron

# 3. 동일한 이진 분류 가상 데이터셋을 생성하고, Perceptron, SVM, Random Forest, Naive Bayes 네 가지 알고리즘으로 학습해 보세요.

SEED = 42
X, y = make_classification(
    n_samples=800,
    n_features=8,
    n_informative=5,
    n_redundant=1,
    n_classes=2,
    class_sep=1.2,
    flip_y=0.03,
    random_state=SEED,
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    stratify=y,
    random_state=SEED,
)

models = {
    "Perceptron": Pipeline([
        ("scaler", StandardScaler()),
        ("model", Perceptron(max_iter=1000, random_state=SEED)),
    ]),
    "SVM": Pipeline([
        ("scaler", StandardScaler()),
        ("model", SVC(kernel="rbf", random_state=SEED)),
    ]),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=SEED,
    ),
    "Naive Bayes": GaussianNB(),
}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("====================", name, "====================")
    print("정확도:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))
