# pip install pandas scikit-learn

"""Day 03-1. 회귀의 기본.

이 파일은 분류와 회귀의 차이를 설명하고,
선형회귀가 숫자 예측을 어떤 방식으로 수행하는지 초심자도 따라올 수 있게 보여 주는 강사용 실습 파일이다.
모든 결과는 고정된 데이터와 random_state=42를 사용해 항상 같은 출력이 나오도록 맞췄다.
"""

# pandas는 CSV 파일을 읽고, 표 형태 데이터를 선택하고, 결과를 보기 좋게 출력할 때 사용한다.
import pandas as pd

# train_test_split은 데이터를 학습용과 시험용으로 나눠 공정하게 성능을 확인할 때 사용한다.
from sklearn.model_selection import train_test_split

# LinearRegression은 선형회귀 모델을 만드는 함수형 클래스다.
# fit()으로 학습하고, predict()로 숫자를 예측하고, score()로 기본 R^2 점수를 확인할 수 있다.
from sklearn.linear_model import LinearRegression

# 예상 출력 핵심:
# - 평균 시험 점수는 94.55로 출력된다.
# - 공부 시간과 시험 점수의 상관계수는 0.8986으로 가장 크게 보인다.
# - 학습용 R^2는 0.9906, 시험용 R^2는 0.9902로 출력된다.
# - 계수는 [6.8618, 4.9764, 1.8183], 절편은 36.6444로 출력된다.
# - 새 학생 점수 예측은 [99.55, 66.25]로 출력된다.

# 수업 제목을 먼저 출력해 학생이 지금 배우는 주제를 바로 파악할 수 있게 한다.
print("=== Day 03-1: 회귀의 기본 ===")

# 학생 학습 데이터 파일을 읽는다.
# 이 데이터는 공부 시간, 복습 시간, 수면 시간을 보고 시험 점수를 예측하는 회귀 문제다.
df = pd.read_csv("data/student_learning_extended.csv")

# 앞 5행을 출력해 한 행이 학생 1명이라는 점과 열 이름의 의미를 먼저 확인한다.
print("\n[실습 1] 데이터 앞 5행")
print(df.head().to_string(index=False))

# 평균 점수를 출력해 전체 데이터의 대략적인 중심값을 먼저 감 잡게 한다.
# 회귀에서는 이런 평균값이 예측값 해석의 기준선 역할을 한다.
print("\n[실습 2] 평균 점수")
print(round(df["exam_score"].mean(), 2))

# 상관계수는 어떤 특징이 시험 점수와 더 강하게 함께 움직이는지 보는 지표다.
# 값이 1에 가까울수록 양의 방향으로 함께 움직이는 경향이 크다고 설명할 수 있다.
print("\n[실습 3] 점수와의 상관계수")
print(
    df[["study_hours", "practice_hours", "sleep_hours", "exam_score"]]
    .corr()
    .round(4)["exam_score"]
    .to_string()
)

# X는 모델 입력값(feature)이고, y는 모델이 맞혀야 하는 정답(target)이다.
# 회귀에서는 target이 이름표가 아니라 연속적인 숫자라는 점이 중요하다.
X = df[["study_hours", "practice_hours", "sleep_hours"]]
y = df["exam_score"]

# 데이터를 학습용과 시험용으로 나눈다.
# 회귀 모델도 훈련 점수와 시험 점수를 나눠 봐야 과하게 외운 것인지 확인할 수 있다.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

# LinearRegression 객체를 만든다.
# 아직 아무것도 배운 상태가 아니며, fit()을 호출해야 비로소 데이터 패턴을 학습한다.
model = LinearRegression()

# fit(X_train, y_train)은 입력값과 정답값의 관계를 학습하는 함수다.
# 선형회귀는 각 특징에 적절한 가중치(계수)를 찾아 예측식을 만든다.
model.fit(X_train, y_train)

# score(X, y)는 기본적으로 R^2 값을 반환한다.
# 1에 가까울수록 실제 점수 흐름을 잘 설명한다고 해석할 수 있다.
print("\n[실습 4] 학습용/시험용 R^2 점수")
print("학습용 R^2:", round(model.score(X_train, y_train), 4))
print("시험용 R^2:", round(model.score(X_test, y_test), 4))

# coef_는 각 특징 앞에 붙는 기울기 역할 숫자다.
# 값이 클수록 해당 특징이 예측 점수에 더 큰 영향을 준다고 볼 수 있다.
# intercept_는 모든 특징값이 0이라고 가정했을 때의 시작점 역할 숫자다.
print("\n[실습 5] 계수와 절편")
print("계수:", model.coef_.round(4))
print("절편:", round(model.intercept_, 4))

# 계수를 표 형태로 다시 보여 주면 어떤 특징이 얼마나 중요한지 한눈에 읽기 쉽다.
coef_df = pd.DataFrame({
    "feature": X.columns,
    "coefficient": model.coef_.round(4),
})
print("\n[실습 6] 특징별 계수 표")
print(coef_df.to_string(index=False))

# 절편과 계수의 의미를 짧은 문장으로 출력해 학생이 숫자의 역할을 바로 연결할 수 있게 한다.
print("\n[실습 7] 계수와 절편 해석")
print("study_hours 계수는 공부 시간이 1 늘어날 때 예측 점수가 얼마나 달라지는지 보여 준다.")
print("practice_hours 계수는 복습 시간이 1 늘어날 때의 변화량을 뜻한다.")
print("sleep_hours 계수는 수면 시간이 1 늘어날 때의 변화량을 뜻한다.")
print("절편은 모든 입력이 0일 때의 시작값 역할을 하며, 예측식의 출발점으로 이해하면 된다.")

# 새 학생 2명의 정보를 만든다.
# 이 데이터는 model.predict()가 실제로 어떻게 쓰이는지 보여 주는 입력 예제다.
sample_students = pd.DataFrame([
    {"study_hours": 5.5, "practice_hours": 2.5, "sleep_hours": 7.0},
    {"study_hours": 2.0, "practice_hours": 1.0, "sleep_hours": 6.0},
])

# predict(X)는 학습한 모델로 새로운 입력의 숫자 결과를 예측하는 함수다.
# 회귀에서는 최종 결과가 범주 이름이 아니라 연속적인 숫자로 나온다.
predictions = model.predict(sample_students)
print("\n[실습 8] 새 학생 점수 예측")
print(predictions.round(2).tolist())

# 이번에는 예측식을 직접 계산해 본다.
# 선형회귀는 절편 + (특징값 x 계수)의 합으로 결과가 만들어진다는 점을 직접 보여 주기 위한 실습이다.
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

# predict() 결과와 직접 계산한 결과를 나란히 보여 주면
# 선형회귀가 내부적으로 어떤 방식으로 점수를 만드는지 학생이 눈으로 확인할 수 있다.
comparison_df = pd.DataFrame({
    "predict_result": predictions.round(2),
    "manual_formula_result": manual_predictions,
})
print("\n[실습 10] 함수 결과와 직접 계산 결과 비교")
print(comparison_df.to_string(index=False))