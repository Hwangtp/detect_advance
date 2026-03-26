# pip install pandas scikit-learn

"""Day 03-2. 회귀 평가와 비교.

이 파일은 회귀 모델을 어떤 지표로 읽는지,
그리고 단순 회귀와 다중 회귀를 비교하면 어떤 차이가 보이는지 초심자도 이해할 수 있게 보여 주는 강사용 실습 파일이다.
모든 결과는 고정된 데이터와 random_state=42를 사용해 항상 같은 출력이 나오도록 맞췄다.
"""

# pandas는 CSV 데이터를 읽고, 실제값/예측값/오차를 표로 만들어 비교할 때 사용한다.
import pandas as pd

# train_test_split은 데이터를 학습용과 시험용으로 나눠 공정하게 평가할 때 사용한다.
from sklearn.model_selection import train_test_split

# LinearRegression은 회귀 모델을 만들고 fit(), predict(), score() 같은 핵심 함수를 제공한다.
from sklearn.linear_model import LinearRegression

# mean_absolute_error, mean_squared_error, r2_score는 회귀 성능을 여러 기준으로 읽을 때 사용하는 함수들이다.
# MAE는 평균 절대 오차, MSE는 제곱 오차 평균, R^2는 설명력에 해당한다.
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 예상 출력 핵심:
# - 다중 회귀의 R^2는 0.9902, MAE는 1.3119, RMSE는 1.5064로 출력된다.
# - 단순 회귀의 R^2는 0.806, MAE는 5.5617, RMSE는 6.6966으로 출력된다.
# - 실제값 비교 표에서 다중 회귀가 단순 회귀보다 더 안정적으로 실제값 근처에 붙는다.

# 수업 제목을 먼저 출력해 학생이 지금부터 평가 지표를 다룬다는 점을 알게 한다.
print("=== Day 03-2: 회귀 평가와 비교 ===")

# 학생 학습 데이터를 읽는다.
df = pd.read_csv("data/student_learning_extended.csv")

# 다중 회귀는 3개 특징을 모두 입력값으로 사용한다.
X = df[["study_hours", "practice_hours", "sleep_hours"]]

# 예측 목표는 시험 점수다.
y = df["exam_score"]

# 데이터를 학습용과 시험용으로 나눈다.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

# 다중 회귀 모델을 만든다.
# 여러 특징을 함께 사용하므로 학생의 점수를 더 풍부한 정보로 예측하게 된다.
multi_model = LinearRegression()

# fit()으로 학습 데이터를 보고 예측식을 만든다.
multi_model.fit(X_train, y_train)

# predict()는 시험용 입력값에 대해 실제 예측 점수를 계산해 준다.
multi_pred = multi_model.predict(X_test)

# R^2는 전체 흐름을 얼마나 잘 설명하는지 보는 지표다.
# MAE는 평균적으로 몇 점 정도 틀렸는지 직관적으로 보여 준다.
# RMSE는 큰 실수를 더 무겁게 보는 오차 지표다.
print("\n[실습 1] 다중 회귀 지표")
print("R^2:", round(r2_score(y_test, multi_pred), 4))
print("MAE:", round(mean_absolute_error(y_test, multi_pred), 4))
print("RMSE:", round(mean_squared_error(y_test, multi_pred) ** 0.5, 4))

# score() 함수도 내부적으로 R^2를 반환한다.
# r2_score()와 같은 결과가 나오는지 보여 주면 함수 사용법 설명에 도움이 된다.
print("다중 회귀 score() 결과:", round(multi_model.score(X_test, y_test), 4))

# 이번에는 공부 시간 한 개만 사용하는 단순 회귀 모델을 만든다.
# 이렇게 해야 특징이 줄어들었을 때 성능이 얼마나 달라지는지 비교할 수 있다.
simple_model = LinearRegression()
simple_model.fit(X_train[["study_hours"]], y_train)
simple_pred = simple_model.predict(X_test[["study_hours"]])

print("\n[실습 2] 단순 회귀 지표")
print("R^2:", round(r2_score(y_test, simple_pred), 4))
print("MAE:", round(mean_absolute_error(y_test, simple_pred), 4))
print("RMSE:", round(mean_squared_error(y_test, simple_pred) ** 0.5, 4))
print("단순 회귀 score() 결과:", round(simple_model.score(X_test[["study_hours"]], y_test), 4))

# 실제값과 예측값을 함께 보면 지표 숫자가 왜 그렇게 나왔는지 눈으로 확인할 수 있다.
comparison_df = pd.DataFrame({
    "actual": y_test.head(5).round(2).tolist(),
    "multi_pred": multi_pred[:5].round(2).tolist(),
    "simple_pred": simple_pred[:5].round(2).tolist(),
    "multi_error": (multi_pred[:5] - y_test.head(5).to_numpy()).round(2).tolist(),
    "simple_error": (simple_pred[:5] - y_test.head(5).to_numpy()).round(2).tolist(),
})
print("\n[실습 3] 실제값과 예측값 비교")
print(comparison_df.to_string(index=False))

# 다중 회귀와 단순 회귀의 오차를 문장으로 다시 정리해 준다.
# 학생이 숫자만 보지 말고 "어떤 모델이 더 안정적인가"를 말로 설명할 수 있게 하는 장면이다.
print("\n[실습 4] 지표 해석 요약")
print("MAE가 작을수록 평균적으로 실제 점수와 더 가깝게 맞혔다고 볼 수 있다.")
print("RMSE가 크면 큰 실수가 더 자주 또는 더 크게 나타났다고 해석할 수 있다.")
print("이번 예제에서는 다중 회귀가 단순 회귀보다 R^2는 높고 오차는 더 작다.")

# 회귀 모델도 coef_와 intercept_를 통해 어떤 특징을 얼마나 반영하는지 볼 수 있다.
# Day 03-1과 연결되는 복습 역할을 하도록 다중 회귀의 계수를 다시 출력한다.
coef_summary_df = pd.DataFrame({
    "feature": X.columns,
    "coefficient": multi_model.coef_.round(4),
})
print("\n[실습 5] 다중 회귀 계수 다시 보기")
print(coef_summary_df.to_string(index=False))
print("절편:", round(multi_model.intercept_, 4))

# 마지막으로 왜 특징을 여러 개 쓰면 성능이 좋아지는지 문장으로 정리한다.
print("\n[실습 6] 왜 다중 회귀가 더 좋게 나왔는가")
print("공부 시간만 보면 놓치는 정보가 있지만, 복습 시간과 수면 시간까지 함께 보면 점수 패턴을 더 잘 설명할 수 있다.")
print("즉 특징을 풍부하게 사용하면 모델이 정답에 더 가까운 예측을 만들 가능성이 커진다.")