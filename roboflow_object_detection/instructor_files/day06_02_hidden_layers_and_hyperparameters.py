# pip install pandas scikit-learn

"""Day 06-2. 은닉층과 하이퍼파라미터 비교.

이 파일은 MLPClassifier에서 hidden_layer_sizes, max_iter, activation 같은 하이퍼파라미터를 바꿔 보며
결과가 어떻게 달라지는지 감각을 익히게 하는 강사용 실습 파일이다.
모든 결과는 random_state=42로 고정해 항상 같은 출력이 나오도록 맞췄다.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.neural_network import MLPClassifier

# 예상 출력 핵심:
# - hidden_units=1일 때 시험 정확도는 0.88로 낮고, 4 이상부터는 0.99 이상이 나온다.
# - max_iter 비교에서는 200, 500, 2000 모두 0.99 수준으로 안정적으로 나온다.
# - activation 비교에서는 relu=0.99, tanh=0.9967, logistic=0.99로 출력된다.

print("=== Day 06-2: 은닉층과 하이퍼파라미터 비교 ===")

df = pd.read_csv("data/student_learning_extended.csv")
X = df[["study_hours", "practice_hours", "sleep_hours"]]
y = df["passed"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

print("\n[실습 1] hidden_layer_sizes 비교")
for hidden_units in [1, 4, 8, 16]:
    model = make_pipeline(
        StandardScaler(),
        MLPClassifier(
            hidden_layer_sizes=(hidden_units,),
            activation="relu",
            solver="lbfgs",
            max_iter=2000,
            random_state=42,
        ),
    )
    model.fit(X_train, y_train)
    print(f"hidden_units={hidden_units} -> test_accuracy={model.score(X_test, y_test):.4f}")

print("\n[실습 2] max_iter 비교")
for max_iter in [200, 500, 2000]:
    model = make_pipeline(
        StandardScaler(),
        MLPClassifier(
            hidden_layer_sizes=(8,),
            activation="relu",
            solver="lbfgs",
            max_iter=max_iter,
            random_state=42,
        ),
    )
    model.fit(X_train, y_train)
    print(f"max_iter={max_iter} -> test_accuracy={model.score(X_test, y_test):.4f}")

print("\n[실습 3] activation 비교")
for activation in ["relu", "tanh", "logistic"]:
    model = make_pipeline(
        StandardScaler(),
        MLPClassifier(
            hidden_layer_sizes=(8,),
            activation=activation,
            solver="lbfgs",
            max_iter=2000,
            random_state=42,
        ),
    )
    model.fit(X_train, y_train)
    print(f"activation={activation} -> test_accuracy={model.score(X_test, y_test):.4f}")

print("\n[실습 4] 오늘 핵심 정리")
print("하이퍼파라미터는 모델이 데이터를 어떻게 배울지 정하는 설정값이다.")
print("hidden_layer_sizes는 은닉층 크기, max_iter는 반복 횟수, activation은 비선형 처리 방식을 정한다.")
print("즉 같은 MLP라도 설정을 바꾸면 결과가 달라질 수 있다.")