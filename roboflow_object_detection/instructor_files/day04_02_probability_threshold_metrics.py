# pip install pandas scikit-learn

"""Day 04-2. 확률, 임계값, 분류 지표.

이 파일은 predict_proba, 임계값, 혼동행렬, 정밀도, 재현율, F1 점수를
하나의 흐름으로 연결해 설명하는 강사용 실습 파일이다.
모든 결과는 random_state=42로 고정해 항상 같은 출력이 나오도록 맞췄다.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

# 예상 출력 핵심:
# - 기본 confusion matrix는 [[34, 2], [1, 263]]으로 출력된다.
# - precision은 0.9925, recall은 0.9962, f1은 0.9943으로 출력된다.
# - threshold를 0.3, 0.5, 0.7로 바꾸면 정밀도/재현율의 균형이 달라진다.

print("=== Day 04-2: 확률, 임계값, 분류 지표 ===")

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

print("\n[실습 3] 임계값 비교")
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
print("\n[실습 4] 확률표 일부")
print(summary_df.to_string(index=False))

print("\n[실습 5] 오늘 핵심 정리")
print("모델은 확률을 계산하고, 우리는 threshold로 어디서 0과 1을 나눌지 정한다.")
print("threshold를 올리면 보통 정밀도는 좋아질 수 있지만 재현율은 낮아질 수 있다.")