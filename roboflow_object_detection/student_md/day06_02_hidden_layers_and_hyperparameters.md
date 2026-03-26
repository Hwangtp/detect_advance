# Day 06-2. 은닉층과 하이퍼파라미터 비교

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 목표</h2>
  <p style="margin:0; line-height:1.8;">MLP에서 hidden_layer_sizes, max_iter, activation 같은 하이퍼파라미터가 결과에 어떤 영향을 주는지 이해합니다.</p>
</div>

## 오늘 확인할 내용

- 하이퍼파라미터가 무엇인지
- `hidden_layer_sizes`를 바꾸면 어떤 차이가 나는지
- `max_iter`와 `activation`이 어떤 역할을 하는지

## 핵심 설명

하이퍼파라미터는 모델이 스스로 배우는 값이 아니라 사람이 먼저 정해 주는 설정값입니다. 같은 MLP라도 하이퍼파라미터를 바꾸면 학습 결과가 달라질 수 있습니다.

오늘 실습에서는 구조의 크기, 반복 횟수, 활성화 방식을 바꿔 보며 결과가 어떻게 달라지는지 비교합니다.

## 수업 체크포인트

- 하이퍼파라미터를 한 문장으로 설명할 수 있는가?
- `hidden_layer_sizes`, `max_iter`, `activation`의 역할을 구분할 수 있는가?

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.neural_network import MLPClassifier

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
print("하이퍼파라미터는 모델의 구조와 학습 방식을 정하는 설정값입니다.")
print("hidden_layer_sizes는 구조의 크기, max_iter는 반복 횟수, activation은 내부 계산 방식을 정합니다.")
```