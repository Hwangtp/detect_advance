# Day 03-1. 회귀의 기본

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 개요</h2>
  <p style="margin:0; line-height:1.8;">숫자 예측 문제인 회귀를 처음 이해하고, 선형회귀가 계수와 절편으로 어떻게 예측값을 만드는지까지 확인합니다.</p>
</div>

<div style="background-color:#eff6ff; border:1px solid #93c5fd; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#1d4ed8;">실습 흐름</h3>
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li>점수 데이터 읽기</li>
    <li>평균 점수와 상관계수 확인</li>
    <li>선형회귀 학습과 R^2 점수 확인</li>
    <li>계수와 절편 읽기</li>
    <li>predict() 결과와 직접 계산한 결과 비교</li>
  </ul>
</div>

<div style="background-color:#f0fdf4; border:1px solid #86efac; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#15803d;">체크포인트</h3>
  <ol style="margin:0; padding-left:20px; line-height:1.8;">
    <li>회귀와 분류의 차이를 설명할 수 있다.</li>
    <li>계수와 절편의 의미를 말할 수 있다.</li>
    <li>predict()와 직접 계산한 결과가 왜 같은지 설명할 수 있다.</li>
  </ol>
</div>

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

print("=== Day 03-1: 회귀의 기본 ===")

df = pd.read_csv("data/student_learning_extended.csv")
print("\n[실습 1] 데이터 앞 5행")
print(df.head().to_string(index=False))
print("\n[실습 2] 평균 점수")
print(round(df["exam_score"].mean(), 2))
print("\n[실습 3] 점수와의 상관계수")
print(
    df[["study_hours", "practice_hours", "sleep_hours", "exam_score"]]
    .corr()
    .round(4)["exam_score"]
    .to_string()
)
X = df[["study_hours", "practice_hours", "sleep_hours"]]
y = df["exam_score"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)
model = LinearRegression()
model.fit(X_train, y_train)
print("\n[실습 4] 학습용/시험용 R^2 점수")
print("학습용 R^2:", round(model.score(X_train, y_train), 4))
print("시험용 R^2:", round(model.score(X_test, y_test), 4))
print("\n[실습 5] 계수와 절편")
print("계수:", model.coef_.round(4))
print("절편:", round(model.intercept_, 4))
coef_df = pd.DataFrame({
    "feature": X.columns,
    "coefficient": model.coef_.round(4),
})
print("\n[실습 6] 특징별 계수 표")
print(coef_df.to_string(index=False))
print("\n[실습 7] 계수와 절편 해석")
print("study_hours 계수는 공부 시간이 1 늘어날 때 예측 점수가 얼마나 달라지는지 보여 준다.")
print("practice_hours 계수는 복습 시간이 1 늘어날 때의 변화량을 뜻한다.")
print("sleep_hours 계수는 수면 시간이 1 늘어날 때의 변화량을 뜻한다.")
print("절편은 모든 입력이 0일 때의 시작값 역할을 하며, 예측식의 출발점으로 이해하면 된다.")
sample_students = pd.DataFrame([
    {"study_hours": 5.5, "practice_hours": 2.5, "sleep_hours": 7.0},
    {"study_hours": 2.0, "practice_hours": 1.0, "sleep_hours": 6.0},
])
predictions = model.predict(sample_students)
print("\n[실습 8] 새 학생 점수 예측")
print(predictions.round(2).tolist())
manual_predictions = []
for student in sample_students.to_dict("records"):
    manual_score = (
        model.intercept_
        + student["study_hours"] * model.coef_[0]
        + student["practice_hours"] * model.coef_[1]
        + student["sleep_hours"] * model.coef_[2]
    )
    manual_predictions.append(float(round(manual_score, 2)))
print("\n[실습 9] 예측식을 직접 계산한 결과")
print(manual_predictions)
comparison_df = pd.DataFrame({
    "predict_result": predictions.round(2),
    "manual_formula_result": manual_predictions,
})
print("\n[실습 10] 함수 결과와 직접 계산 결과 비교")
print(comparison_df.to_string(index=False))
```