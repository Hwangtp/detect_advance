# Day 07-2. 모델 저장과 다시 불러오기

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 개요</h2>
  <p style="margin:0; line-height:1.8;">학습한 모델을 joblib으로 저장하고 다시 불러와 예측에 재사용합니다.</p>
</div>

<div style="background-color:#eff6ff; border:1px solid #93c5fd; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#1d4ed8;">실습 흐름</h3>
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li>저장 전 점수 확인</li>
    <li>dump로 저장</li>
    <li>load로 재사용</li>
    <li>불러온 모델 예측</li>
  </ul>
</div>

<div style="background-color:#f0fdf4; border:1px solid #86efac; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#15803d;">체크포인트</h3>
  <ol style="margin:0; padding-left:20px; line-height:1.8;">
    <li>모델 저장이 왜 필요한지 설명할 수 있다.</li>
    <li>dump와 load의 역할을 구분할 수 있다.</li>
    <li>불러온 모델로 다시 예측할 수 있다.</li>
  </ol>
</div>

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
import os

import pandas as pd

from joblib import dump, load

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

from sklearn.neural_network import MLPClassifier

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
```
