# pip install pandas scikit-learn

"""Day 07-1. 깊은 MLP와 early stopping.

이 파일은 얕은 모델과 깊은 모델을 비교하고 early_stopping의 개념을 소개한다.
"""

# pandas는 CSV 표 데이터를 읽고, 열 이름 기준으로 선택하고, 통계를 확인할 때 가장 많이 사용하는 라이브러리다.
import pandas as pd

# train_test_split은 데이터를 학습용과 시험용으로 공정하게 나누어 일반화 성능을 확인할 때 사용한다.
from sklearn.model_selection import train_test_split

# StandardScaler는 특징값의 평균과 스케일을 맞춰 거리 기반 모델과 신경망 학습을 더 안정적으로 만든다.
from sklearn.preprocessing import StandardScaler

# make_pipeline은 전처리와 모델을 한 줄로 묶어서 같은 흐름으로 학습과 예측을 수행하게 해 준다.
from sklearn.pipeline import make_pipeline

# MLPClassifier는 sklearn 안에서 다층 퍼셉트론 신경망을 쉽게 실습할 수 있게 해 주는 분류 모델이다.
from sklearn.neural_network import MLPClassifier

# 예상 출력 핵심:
# - 얕은 모델 점수는 0.95, 깊은 모델 점수는 0.9933으로 출력된다.
# - early stopping 설정에서는 반복 횟수 40, 검증 점수 0.9958이 출력된다.
# - 깊게 만드는 것과 적절히 멈추는 것을 함께 해석하는 수업이다.

print("=== Day 07-1: 깊은 MLP와 early stopping ===")
df = pd.read_csv("data/student_learning_extended.csv")
X = df[["study_hours", "practice_hours", "sleep_hours"]]
y = df["passed"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
shallow = make_pipeline(StandardScaler(), MLPClassifier(hidden_layer_sizes=(8,), activation="relu", solver="adam", early_stopping=True, validation_fraction=0.2, n_iter_no_change=10, max_iter=400, random_state=42))
deep = make_pipeline(StandardScaler(), MLPClassifier(hidden_layer_sizes=(24, 12), activation="relu", solver="adam", early_stopping=True, validation_fraction=0.2, n_iter_no_change=15, learning_rate_init=0.003, max_iter=500, random_state=42))
shallow.fit(X_train, y_train)
deep.fit(X_train, y_train)
print("\n[실습 1] 얕은 모델과 깊은 모델 비교")
print("shallow:", round(shallow.score(X_test, y_test), 4))
print("deep:", round(deep.score(X_test, y_test), 4))
deep_inner = deep.named_steps["mlpclassifier"]
print("\n[실습 2] early stopping 관련 값")
print("실제 반복 횟수:", deep_inner.n_iter_)
print("최고 검증 점수:", round(deep_inner.best_validation_score_, 4))
