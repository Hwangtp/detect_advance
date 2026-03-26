# Day 03-2. 회귀 평가와 비교

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 개요</h2>
  <p style="margin:0; line-height:1.8;">R^2, MAE, RMSE를 읽고 단순 회귀와 다중 회귀를 비교하며 왜 특징이 많아지면 성능이 좋아질 수 있는지 확인합니다.</p>
</div>

<div style="background-color:#eff6ff; border:1px solid #93c5fd; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#1d4ed8;">실습 흐름</h3>
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li>다중 회귀 지표 확인</li>
    <li>단순 회귀 지표 확인</li>
    <li>score()와 R^2 연결 확인</li>
    <li>실제값/예측값/오차 비교 표 읽기</li>
    <li>다중 회귀 계수 다시 보기</li>
  </ul>
</div>

<div style="background-color:#f0fdf4; border:1px solid #86efac; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#15803d;">체크포인트</h3>
  <ol style="margin:0; padding-left:20px; line-height:1.8;">
    <li>R^2, MAE, RMSE를 각각 설명할 수 있다.</li>
    <li>단순 회귀와 다중 회귀의 차이를 말할 수 있다.</li>
    <li>지표 숫자와 실제 오차 표를 연결해 해석할 수 있다.</li>
  </ol>
</div>

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("=== Day 03-2: 회귀 평가와 비교 ===")

df = pd.read_csv("data/student_learning_extended.csv")
X = df[["study_hours", "practice_hours", "sleep_hours"]]
y = df["exam_score"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)
multi_model = LinearRegression()
multi_model.fit(X_train, y_train)
multi_pred = multi_model.predict(X_test)
print("\n[실습 1] 다중 회귀 지표")
print("R^2:", round(r2_score(y_test, multi_pred), 4))
print("MAE:", round(mean_absolute_error(y_test, multi_pred), 4))
print("RMSE:", round(mean_squared_error(y_test, multi_pred) ** 0.5, 4))
print("다중 회귀 score() 결과:", round(multi_model.score(X_test, y_test), 4))
simple_model = LinearRegression()
simple_model.fit(X_train[["study_hours"]], y_train)
simple_pred = simple_model.predict(X_test[["study_hours"]])
print("\n[실습 2] 단순 회귀 지표")
print("R^2:", round(r2_score(y_test, simple_pred), 4))
print("MAE:", round(mean_absolute_error(y_test, simple_pred), 4))
print("RMSE:", round(mean_squared_error(y_test, simple_pred) ** 0.5, 4))
print("단순 회귀 score() 결과:", round(simple_model.score(X_test[["study_hours"]], y_test), 4))
comparison_df = pd.DataFrame({
    "actual": y_test.head(5).round(2).tolist(),
    "multi_pred": multi_pred[:5].round(2).tolist(),
    "simple_pred": simple_pred[:5].round(2).tolist(),
    "multi_error": (multi_pred[:5] - y_test.head(5).to_numpy()).round(2).tolist(),
    "simple_error": (simple_pred[:5] - y_test.head(5).to_numpy()).round(2).tolist(),
})
print("\n[실습 3] 실제값과 예측값 비교")
print(comparison_df.to_string(index=False))
print("\n[실습 4] 지표 해석 요약")
print("MAE가 작을수록 평균적으로 실제 점수와 더 가깝게 맞혔다고 볼 수 있다.")
print("RMSE가 크면 큰 실수가 더 자주 또는 더 크게 나타났다고 해석할 수 있다.")
print("이번 예제에서는 다중 회귀가 단순 회귀보다 R^2는 높고 오차는 더 작다.")
coef_summary_df = pd.DataFrame({
    "feature": X.columns,
    "coefficient": multi_model.coef_.round(4),
})
print("\n[실습 5] 다중 회귀 계수 다시 보기")
print(coef_summary_df.to_string(index=False))
print("절편:", round(multi_model.intercept_, 4))
print("\n[실습 6] 왜 다중 회귀가 더 좋게 나왔는가")
print("공부 시간만 보면 놓치는 정보가 있지만, 복습 시간과 수면 시간까지 함께 보면 점수 패턴을 더 잘 설명할 수 있다.")
print("즉 특징을 풍부하게 사용하면 모델이 정답에 더 가까운 예측을 만들 가능성이 커진다.")
```