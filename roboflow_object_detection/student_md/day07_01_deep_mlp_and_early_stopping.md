# Day 07-1. 깊은 MLP와 early stopping

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 개요</h2>
  <p style="margin:0; line-height:1.8;">얕은 모델과 깊은 모델을 비교하고 early stopping 개념을 이해합니다.</p>
</div>

<div style="background-color:#eff6ff; border:1px solid #93c5fd; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#1d4ed8;">실습 흐름</h3>
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li>얕은/깊은 모델 비교</li>
    <li>반복 횟수 확인</li>
    <li>최고 검증 점수 확인</li>
  </ul>
</div>

<div style="background-color:#f0fdf4; border:1px solid #86efac; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#15803d;">체크포인트</h3>
  <ol style="margin:0; padding-left:20px; line-height:1.8;">
    <li>early stopping의 목적을 설명할 수 있다.</li>
    <li>얕은 모델과 깊은 모델을 비교할 수 있다.</li>
    <li>검증 점수의 의미를 말할 수 있다.</li>
  </ol>
</div>

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
from pathlib import Path

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

from sklearn.neural_network import MLPClassifier

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
```
