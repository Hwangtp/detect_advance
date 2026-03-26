# pip install pandas scikit-learn

"""Day 02-2. 전처리와 표준화.

이 파일은 거리 기반 모델에서 스케일 차이가 왜 중요한지,
그리고 같은 KNN이라도 표준화를 하면 결과 해석이 어떻게 달라지는지를 보여 주기 위한 강사용 실습 파일이다.
모든 결과는 random_state=42로 고정해 항상 같은 출력이 나오도록 맞췄다.
"""

# pandas는 CSV 파일을 읽고, 입력 데이터와 예시 샘플을 표 형태로 다룰 때 사용한다.
import pandas as pd

# train_test_split은 데이터를 학습용과 시험용으로 나눠 공정하게 평가할 때 사용한다.
from sklearn.model_selection import train_test_split

# KNeighborsClassifier는 가까운 이웃들의 다수결로 예측하는 분류 모델이라 스케일 차이 설명에 잘 맞는다.
from sklearn.neighbors import KNeighborsClassifier

# StandardScaler는 각 특징의 평균을 0 근처로, 표준편차를 1 근처로 맞춰 스케일을 비슷하게 만들어 준다.
from sklearn.preprocessing import StandardScaler

# make_pipeline은 전처리와 모델을 한 줄 흐름으로 묶어서 학습과 예측 순서를 실수 없이 유지하게 해 준다.
from sklearn.pipeline import make_pipeline

# 예상 출력 핵심:
# - 전처리 전 시험 점수는 1.0으로 출력된다.
# - 스케일러 평균은 [20.22, 148.88, 5.98], 표준편차는 [6.93, 129.77, 2.02] 근처로 출력된다.
# - 같은 샘플이라도 원본 예측은 ['perch', 'smelt', 'perch'], 표준화 후 예측은 ['bream', 'smelt', 'perch']로 달라진다.
# - k를 241까지 크게 키우면 원본 점수는 0.9792로 떨어지지만, 표준화한 점수는 1.0을 유지한다.

# 수업 제목을 먼저 출력해 학생이 지금 배우는 주제를 바로 파악하게 한다.
print("=== Day 02-2: 전처리와 표준화 ===")

# 생선 데이터를 읽는다.
# 이번 수업도 길이, 무게, 꼬리 길이로 생선 종류를 맞히는 같은 데이터를 사용한다.
df = pd.read_csv("data/market_fish_extended.csv")

# 모델 입력값 X와 정답 y를 분리한다.
X = df[["length_cm", "weight_g", "tail_cm"]]
y = df["species"]

# 학습용 데이터와 시험용 데이터를 나눈다.
# 같은 기준으로 비교하기 위해 day02_01과 동일한 분리 조건을 사용한다.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

# 먼저 전처리를 하지 않은 원본 데이터로 KNN 모델을 만든다.
# n_neighbors=5는 가까운 5개의 이웃 의견으로 생선 종류를 정하겠다는 뜻이다.
raw_model = KNeighborsClassifier(n_neighbors=5)
raw_model.fit(X_train, y_train)

# 전처리 없이도 점수가 얼마나 나오는지 먼저 확인한다.
# 이렇게 해야 나중에 표준화 결과와 비교가 가능하다.
print("\n[실습 1] 전처리 전 점수")
print(round(raw_model.score(X_test, y_test), 4))

# StandardScaler 객체를 만든다.
# 이 객체는 학습용 데이터의 평균과 표준편차를 기억해 두었다가 같은 기준으로 변환한다.
scaler = StandardScaler()

# fit_transform은 학습용 데이터로 기준을 배우고 바로 변환까지 수행한다.
# 학습용 데이터 기준을 먼저 잡는 이유는 시험용 데이터 정보를 미리 보면 안 되기 때문이다.
X_train_scaled = scaler.fit_transform(X_train)

# 시험용 데이터는 transform만 한다.
# 이미 학습용 데이터에서 배운 평균/표준편차 기준을 그대로 적용해야 공정하다.
X_test_scaled = scaler.transform(X_test)

# 스케일러가 실제로 어떤 기준으로 데이터를 바꾸는지 출력한다.
# 평균과 표준편차를 보여 주면 왜 무게 열이 다른 열보다 범위가 큰지 설명하기 좋다.
print("\n[실습 2] 스케일러 기준값")
print("평균:", scaler.mean_.round(2))
print("표준편차:", scaler.scale_.round(2))

# 이번에는 표준화가 끝난 데이터로 KNN 모델을 다시 학습한다.
scaled_model = KNeighborsClassifier(n_neighbors=5)
scaled_model.fit(X_train_scaled, y_train)

# 전처리 후 점수를 확인한다.
# 이번 데이터는 쉬워서 점수 자체는 같지만, 뒤의 샘플 예측에서 판단 과정 차이가 드러난다.
print("\n[실습 3] 전처리 후 점수")
print(round(scaled_model.score(X_test_scaled, y_test), 4))

# 경계 근처에 있는 샘플 3개를 따로 만들어 본다.
# 이런 샘플은 전처리 전후 예측 차이를 보여 주기에 좋다.
sample_df = pd.DataFrame([
    {"length_cm": 25.0, "weight_g": 150.0, "tail_cm": 8.1},
    {"length_cm": 12.0, "weight_g": 14.0, "tail_cm": 3.7},
    {"length_cm": 19.0, "weight_g": 90.0, "tail_cm": 5.9},
])

# 원본 데이터 기준 예측을 먼저 출력한다.
# 이 결과는 길이, 무게, 꼬리 길이의 원래 크기 차이가 그대로 반영된 판단이다.
print("\n[실습 4] 원본 예측")
print(raw_model.predict(sample_df).tolist())

# 같은 샘플을 표준화한 뒤 예측한다.
# 첫 번째 샘플 결과가 달라지는 것이 스케일 차이의 영향을 보여 주는 핵심 예시다.
print("\n[실습 5] 표준화 후 예측")
print(scaled_model.predict(scaler.transform(sample_df)).tolist())

# 파이프라인은 "표준화 -> KNN" 순서를 하나로 묶어 준다.
# 실전에서는 이 방식을 많이 써야 전처리 순서를 빼먹지 않는다.
pipeline_model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
pipeline_model.fit(X_train, y_train)

# 파이프라인 점수도 확인해, 직접 표준화했을 때와 같은 흐름으로 동작함을 보여 준다.
print("\n[실습 6] 파이프라인 점수")
print(round(pipeline_model.score(X_test, y_test), 4))

# 이번에는 n_neighbors 값을 바꿔 보며 표준화 전후를 비교한다.
# k가 매우 커지면 원본 데이터에서는 성능이 떨어지지만, 표준화한 데이터에서는 더 안정적인 모습을 볼 수 있다.
print("\n[실습 7] k 값 변화와 표준화 비교")
for k in [1, 5, 61, 241]:
    raw_compare_model = KNeighborsClassifier(n_neighbors=k)
    raw_compare_model.fit(X_train, y_train)

    scaled_compare_model = KNeighborsClassifier(n_neighbors=k)
    scaled_compare_model.fit(X_train_scaled, y_train)

    print(
        f"k={k}: 원본 점수={round(raw_compare_model.score(X_test, y_test), 4)}, "
        f"표준화 점수={round(scaled_compare_model.score(X_test_scaled, y_test), 4)}"
    )

# 마지막으로 오늘 배운 핵심을 문장으로 정리한다.
print("\n[실습 8] 오늘 핵심 정리")
print("KNN은 거리로 판단하므로, 숫자 크기가 크게 다른 열이 있으면 특정 열의 영향이 커질 수 있다.")
print("StandardScaler는 각 열의 기준을 비슷하게 맞춰 모델이 더 공평하게 비교하도록 도와준다.")