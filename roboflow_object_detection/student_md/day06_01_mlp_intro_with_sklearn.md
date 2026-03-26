# Day 06-1. sklearn MLP 입문

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 목표</h2>
  <p style="margin:0; line-height:1.8;">MLPClassifier로 신경망의 기본 사용법과 hidden_layer_sizes의 의미를 이해합니다.</p>
</div>

## 오늘 확인할 내용

- `MLPClassifier`를 사용하는 기본 흐름
- `hidden_layer_sizes`가 무엇인지
- `predict()`와 `predict_proba()`를 어떻게 읽는지

## 핵심 설명

MLP는 여러 층을 거치며 판단하는 기본 신경망 모델입니다. 오늘은 내부 수학보다도, sklearn에서 신경망을 어떤 함수로 학습하고 예측하는지 익히는 것이 목표입니다.

`hidden_layer_sizes`는 숨은층에 몇 개의 뉴런을 둘지 정하는 하이퍼파라미터입니다. 값이 달라지면 모델이 표현할 수 있는 구조와 성능도 달라질 수 있습니다.

## 수업 체크포인트

- MLP를 기본 신경망 모델이라고 설명할 수 있는가?
- `hidden_layer_sizes`를 쉬운 말로 설명할 수 있는가?
- `predict()`와 `predict_proba()` 차이를 말할 수 있는가?

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.neural_network import MLPClassifier

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
print("MLP는 입력층, 숨은층, 출력층으로 이어지는 기본 신경망 모델입니다.")
print("hidden_layer_sizes는 숨은층 뉴런 수를 정하는 하이퍼파라미터입니다.")
print("predict()는 최종 클래스, predict_proba()는 클래스별 확률을 보여줍니다.")
```