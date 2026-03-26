# Day 04-2. 확률, 임계값과 분류 지표

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 목표</h2>
  <p style="margin:0; line-height:1.8;">혼동행렬과 정밀도, 재현율, F1 점수, threshold의 의미를 이해합니다.</p>
</div>

## 오늘 확인할 내용

- 혼동행렬이 무엇인지
- `precision`, `recall`, `f1`이 무엇을 뜻하는지
- threshold를 바꾸면 결과가 어떻게 달라지는지
- `predict_proba()`를 왜 같이 봐야 하는지

## 핵심 설명

분류 모델은 종종 최종 클래스만 보여주지만, 실제로는 먼저 확률을 계산하는 경우가 많습니다. 이때 어느 확률 이상이면 1로 볼 것인지 정하는 기준이 threshold입니다.

threshold를 낮추면 더 많은 샘플을 1로 예측하게 되고, threshold를 높이면 더 조심스럽게 1로 예측하게 됩니다. 그래서 정밀도와 재현율은 서로 균형을 맞추며 해석해야 합니다.

## 수업 체크포인트

- 혼동행렬의 네 칸을 말로 설명할 수 있는가?
- 정밀도와 재현율의 차이를 설명할 수 있는가?
- threshold를 높이거나 낮추면 어떤 변화가 생기는지 말할 수 있는가?

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

print("=== Day 04-2: 확률, 임계값과 분류 지표 ===")

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
    LogisticRegression(max_iter=1000, random_state=42),
)
model.fit(X_train, y_train)

pred = model.predict(X_test)
prob = model.predict_proba(X_test)[:, 1]

print("\n[실습 1] 혼동행렬과 기본 지표")
print(confusion_matrix(y_test, pred))
print("precision:", round(precision_score(y_test, pred), 4))
print("recall:", round(recall_score(y_test, pred), 4))
print("f1:", round(f1_score(y_test, pred), 4))

sample_df = pd.DataFrame([
    {"study_hours": 3.5, "practice_hours": 1.0, "sleep_hours": 6.0},
    {"study_hours": 4.5, "practice_hours": 2.0, "sleep_hours": 6.5},
    {"study_hours": 6.0, "practice_hours": 3.5, "sleep_hours": 7.0},
])
print("\n[실습 2] 샘플 확률과 예측")
print(model.predict_proba(sample_df).round(4))
print(model.predict(sample_df).tolist())

print("\n[실습 3] threshold 비교")
for threshold in [0.3, 0.5, 0.7]:
    threshold_pred = (prob >= threshold).astype(int)
    print(f"threshold={threshold}")
    print(confusion_matrix(y_test, threshold_pred))
    print("precision:", round(precision_score(y_test, threshold_pred), 4))
    print("recall:", round(recall_score(y_test, threshold_pred), 4))
    print("f1:", round(f1_score(y_test, threshold_pred), 4))

summary_df = pd.DataFrame({
    "actual": y_test.head(10).tolist(),
    "probability": prob[:10].round(4).tolist(),
    "prediction": pred[:10].tolist(),
})
print("\n[실습 4] 확률 표 읽기")
print(summary_df.to_string(index=False))

print("\n[실습 5] 오늘 핵심 정리")
print("모델은 확률을 계산하고, threshold는 그 확률을 어디서 0과 1로 나눌지 정하는 기준입니다.")
print("threshold를 바꾸면 정밀도와 재현율의 균형도 달라질 수 있습니다.")
```