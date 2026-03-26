# pip install pandas scikit-learn

"""Day 06-1. sklearn MLP 입문.

이 파일은 sklearn의 MLPClassifier로 신경망의 기본 구조를 소개하고,
predict()와 predict_proba()를 함께 읽는 방법을 보여 주는 강사용 실습 파일이다.
모든 결과는 random_state=42로 고정해 항상 같은 출력이 나오도록 맞췄다.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.neural_network import MLPClassifier

# 예상 출력 핵심:
# - 시험 정확도는 0.99로 출력된다.
# - 샘플 예측 결과는 [0, 1]로 출력된다.
# - predict_proba 결과는 첫 샘플이 0 쪽, 두 번째 샘플이 1 쪽으로 매우 강하게 기운다.
# - hidden_layer_sizes 비교에서 1개 노드는 0.88, 4개 이상부터는 0.99 이상이 나온다.

print("=== Day 06-1: sklearn MLP 입문 ===")

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

# hidden_layer_sizes=(8,)은 은닉층 1개에 노드 8개를 두겠다는 뜻이다.
model = make_pipeline(
    StandardScaler(),
    MLPClassifier(
        hidden_layer_sizes=(8,),
        activation="relu",
        solver="lbfgs",
        max_iter=2000,
        random_state=42,
    ),
)
model.fit(X_train, y_train)

# score()는 분류 문제에서 기본적으로 정확도를 반환한다.
print("\n[실습 1] 시험 정확도")
print(round(model.score(X_test, y_test), 4))

sample_df = pd.DataFrame([
    {"study_hours": 3.0, "practice_hours": 1.0, "sleep_hours": 6.0},
    {"study_hours": 5.0, "practice_hours": 2.5, "sleep_hours": 6.8},
])
print("\n[실습 2] 예측 클래스와 확률")
print(model.predict(sample_df).tolist())
print(model.predict_proba(sample_df).round(4))

print("\n[실습 3] hidden_layer_sizes 비교")
for hidden_units in [1, 4, 8, 16]:
    compare_model = make_pipeline(
        StandardScaler(),
        MLPClassifier(
            hidden_layer_sizes=(hidden_units,),
            activation="relu",
            solver="lbfgs",
            max_iter=2000,
            random_state=42,
        ),
    )
    compare_model.fit(X_train, y_train)
    print(f"hidden_units={hidden_units} -> test_accuracy={compare_model.score(X_test, y_test):.4f}")

print("\n[실습 4] 오늘 핵심 정리")
print("MLP는 입력층, 은닉층, 출력층으로 이루어진 기본 신경망 모델이다.")
print("hidden_layer_sizes는 은닉층의 크기를 정하는 하이퍼파라미터다.")
print("predict()는 최종 클래스, predict_proba()는 클래스별 확률을 보여 준다.")