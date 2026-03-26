# pip install pandas scikit-learn

"""Day 04-1. 로지스틱 분류의 기본.

이 파일은 합격/불합격 이진 분류 문제를 통해
로지스틱 회귀가 확률을 계산한 뒤 최종 클래스를 정하는 흐름을 보여 주는 강사용 실습 파일이다.
모든 결과는 random_state=42로 고정해 항상 같은 출력이 나오도록 맞췄다.
"""

# pandas는 CSV 파일을 읽고, 입력 데이터와 예시 샘플을 표 형태로 다룰 때 사용한다.
import pandas as pd

# train_test_split은 데이터를 학습용과 시험용으로 나눠 공정하게 성능을 확인할 때 사용한다.
from sklearn.model_selection import train_test_split

# LogisticRegression은 이진 분류에서 확률과 최종 클래스를 함께 설명하기 좋은 기본 분류 모델이다.
# fit()으로 학습하고, predict()로 최종 클래스, predict_proba()로 클래스 확률을 확인할 수 있다.
from sklearn.linear_model import LogisticRegression

# StandardScaler는 숫자 크기를 비슷한 기준으로 맞춰 로지스틱 회귀가 더 안정적으로 학습되게 돕는다.
from sklearn.preprocessing import StandardScaler

# make_pipeline은 전처리와 모델을 한 줄 흐름으로 묶어 학습과 예측 순서를 실수 없이 유지하게 한다.
from sklearn.pipeline import make_pipeline

# 예상 출력 핵심:
# - 합격 클래스 분포는 0이 182개, 1이 1318개로 출력된다.
# - 학습용 정확도는 0.9825, 시험용 정확도는 0.99로 출력된다.
# - 로지스틱 회귀 계수는 [6.3138, 3.3035, 0.8428], 절편은 9.2479 근처로 출력된다.
# - 샘플 확률은 [[0.3824, 0.6176], [0.0, 1.0], [0.0013, 0.9987]] 순서로 출력된다.

print("=== Day 04-1: 로지스틱 분류의 기본 ===")

df = pd.read_csv("data/student_learning_extended.csv")

# 먼저 정답 클래스 분포를 확인한다.
# 분류 문제에서는 한쪽 클래스가 너무 많으면 정확도 해석이 왜곡될 수 있다.
print("\n[실습 1] 합격 클래스 분포")
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

# score()는 분류 문제에서 기본적으로 정확도를 반환한다.
print("\n[실습 2] 학습용/시험용 정확도")
print("학습용:", round(model.score(X_train, y_train), 4))
print("시험용:", round(model.score(X_test, y_test), 4))

# 파이프라인 안쪽 로지스틱 회귀 모델의 계수와 절편을 읽는다.
logit_model = model.named_steps["logisticregression"]
coef_df = pd.DataFrame({
    "feature": X.columns,
    "coefficient": logit_model.coef_[0].round(4),
})
print("\n[실습 3] 계수와 절편")
print(coef_df.to_string(index=False))
print("절편:", round(logit_model.intercept_[0], 4))

print("\n[실습 4] 계수 해석")
print("계수가 양수이면 해당 특징이 커질수록 1번 클래스(합격) 쪽으로 기울기 쉽다.")
print("이번 모델에서는 study_hours 계수가 가장 커서 공부 시간이 합격 판단에 가장 큰 영향을 준다.")

sample_df = pd.DataFrame([
    {"study_hours": 3.5, "practice_hours": 1.0, "sleep_hours": 6.0},
    {"study_hours": 6.0, "practice_hours": 3.5, "sleep_hours": 7.0},
    {"study_hours": 4.5, "practice_hours": 2.0, "sleep_hours": 6.5},
])

# predict()는 최종 클래스, predict_proba()는 클래스별 확률을 반환한다.
print("\n[실습 5] 샘플 예측 클래스와 확률")
print(model.predict(sample_df).tolist())
print(model.predict_proba(sample_df).round(4))

print("\n[실습 6] 오늘 핵심 정리")
print("로지스틱 회귀는 먼저 합격 확률을 계산하고, 그 확률을 바탕으로 최종 클래스를 결정한다.")
print("predict()는 최종 클래스, predict_proba()는 클래스별 확률을 보여 준다.")