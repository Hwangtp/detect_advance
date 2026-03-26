# pip install pandas scikit-learn joblib

"""Day 07-2. 모델 저장과 다시 불러오기.

이 파일은 학습한 sklearn 모델을 파일로 저장하고 다시 불러와 재사용하는 흐름을 보여 준다.
"""

# os는 코랩 현재 작업 폴더에 저장한 파일이 존재하는지 확인하고 삭제할 때 사용한다.
import os

# pandas는 CSV 표 데이터를 읽고, 열 이름 기준으로 선택하고, 통계를 확인할 때 가장 많이 사용하는 라이브러리다.
import pandas as pd

# dump와 load는 학습한 sklearn 모델을 파일로 저장하고 다시 불러올 때 사용한다.
from joblib import dump, load

# train_test_split은 데이터를 학습용과 시험용으로 공정하게 나누어 일반화 성능을 확인할 때 사용한다.
from sklearn.model_selection import train_test_split

# StandardScaler는 특징값의 평균과 스케일을 맞춰 거리 기반 모델과 신경망 학습을 더 안정적으로 만든다.
from sklearn.preprocessing import StandardScaler

# make_pipeline은 전처리와 모델을 한 줄로 묶어서 같은 흐름으로 학습과 예측을 수행하게 해 준다.
from sklearn.pipeline import make_pipeline

# MLPClassifier는 sklearn 안에서 다층 퍼셉트론 신경망을 쉽게 실습할 수 있게 해 주는 분류 모델이다.
from sklearn.neural_network import MLPClassifier

# 예상 출력 핵심:
# - 저장 전 시험 정확도와 불러온 모델 점수는 모두 0.9933으로 같다.
# - 저장 파일 이름은 day07_saved_model.joblib으로 출력된다.
# - 불러온 모델 예측은 [1, 1]이고, 마지막에 임시 저장 파일 삭제 완료가 출력된다.

print("=== Day 07-2: 모델 저장과 다시 불러오기 ===")
df = pd.read_csv("data/student_learning_extended.csv")
X = df[["study_hours", "practice_hours", "sleep_hours"]]
y = df["passed"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
model = make_pipeline(StandardScaler(), MLPClassifier(hidden_layer_sizes=(24, 12), activation="relu", solver="adam", early_stopping=True, validation_fraction=0.2, n_iter_no_change=15, learning_rate_init=0.003, max_iter=500, random_state=42))
model.fit(X_train, y_train)
print("\n[실습 1] 저장 전 시험 정확도")
print(round(model.score(X_test, y_test), 4))
model_path = "day07_saved_model.joblib"
dump(model, model_path)
print("\n[실습 2] 저장 파일 경로")
print(model_path)
loaded_model = load(model_path)
print("\n[실습 3] 불러온 모델 점수")
print(round(loaded_model.score(X_test, y_test), 4))
sample_df = pd.DataFrame([{"study_hours": 4.0, "practice_hours": 1.5, "sleep_hours": 6.5}, {"study_hours": 6.0, "practice_hours": 3.0, "sleep_hours": 7.0}])
print("\n[실습 4] 불러온 모델 예측")
print(loaded_model.predict(sample_df).tolist())
print(loaded_model.predict_proba(sample_df).round(4))
if os.path.exists(model_path):
    os.remove(model_path)
    print("\n[실습 5] 임시 저장 파일 삭제 완료")
