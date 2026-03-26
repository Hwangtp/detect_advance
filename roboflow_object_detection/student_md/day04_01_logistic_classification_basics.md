# Day 04-1. 로지스틱 분류의 기초

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 목표</h2>
  <p style="margin:0; line-height:1.8;">로지스틱 회귀가 확률을 계산한 뒤 최종 클래스를 정하는 분류 모델이라는 점을 이해합니다.</p>
</div>

## 오늘 확인할 내용

- `fit()`으로 분류 모델을 학습시키는 방법
- `score()`로 정확도를 보는 방법
- `predict()`와 `predict_proba()`의 차이
- 계수와 절편이 왜 중요한지

## 핵심 설명

로지스틱 회귀는 이름에 회귀가 들어가지만, 여기서는 합격과 불합격처럼 둘 중 하나를 나누는 분류 문제에 사용합니다. 모델은 먼저 각 클래스의 확률을 계산하고, 그 다음 최종적으로 0 또는 1을 예측합니다.

계수는 각 특징이 결과에 얼마나 영향을 주는지 보여주는 값입니다. 절편은 입력이 모두 0이라고 가정했을 때의 기본 출발점 역할을 합니다. 계수를 보면 모델이 어떤 특징을 더 중요하게 보는지 힌트를 얻을 수 있습니다.

## 수업 체크포인트

- 클래스 분포를 먼저 보는 이유를 설명할 수 있는가?
- `predict()`와 `predict_proba()`의 차이를 말할 수 있는가?
- 계수가 크다는 것이 무엇을 뜻하는지 설명할 수 있는가?

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

print("=== Day 04-1: 로지스틱 분류의 기초 ===")

df = pd.read_csv("data/student_learning_extended.csv")

print("\n[실습 1] 클래스 분포")
print(df["passed"].value_counts().sort_index().to_string())

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
    LogisticRegression(max_iter=1000, random_state=42),
)
model.fit(X_train, y_train)

print("\n[실습 2] 학습용과 시험용 정확도")
print("학습용:", round(model.score(X_train, y_train), 4))
print("시험용:", round(model.score(X_test, y_test), 4))

logit_model = model.named_steps["logisticregression"]
coef_df = pd.DataFrame({
    "feature": X.columns,
    "coefficient": logit_model.coef_[0].round(4),
})
print("\n[실습 3] 계수와 절편")
print(coef_df.to_string(index=False))
print("절편:", round(logit_model.intercept_[0], 4))

print("\n[실습 4] 계수 해석")
print("계수가 양수이면 해당 특징이 커질수록 1번 클래스(합격) 쪽으로 기울 수 있습니다.")
print("이번 모델에서는 study_hours 계수가 가장 커서 공부 시간이 합격 판단에 가장 큰 영향을 줍니다.")

sample_df = pd.DataFrame([
    {"study_hours": 3.5, "practice_hours": 1.0, "sleep_hours": 6.0},
    {"study_hours": 6.0, "practice_hours": 3.5, "sleep_hours": 7.0},
    {"study_hours": 4.5, "practice_hours": 2.0, "sleep_hours": 6.5},
])

print("\n[실습 5] 샘플 예측 클래스와 확률")
print(model.predict(sample_df).tolist())
print(model.predict_proba(sample_df).round(4))

print("\n[실습 6] 오늘 핵심 정리")
print("로지스틱 회귀는 먼저 확률을 계산하고, 그 확률을 바탕으로 최종 클래스를 결정합니다.")
print("predict()는 최종 클래스, predict_proba()는 클래스별 확률을 보여줍니다.")
```