# Day 02-2. 전처리와 표준화

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 개요</h2>
  <p style="margin:0; line-height:1.8;">표준화가 거리 기반 모델에 왜 중요한지 비교 실습으로 이해합니다.</p>
</div>

<div style="background-color:#eff6ff; border:1px solid #93c5fd; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#1d4ed8;">실습 흐름</h3>
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li>전처리 전 점수 확인</li>
    <li>StandardScaler 기준값 읽기</li>
    <li>전처리 후 점수 비교</li>
    <li>원본 예측과 표준화 예측 비교</li>
    <li>파이프라인 사용</li>
  </ul>
</div>

<div style="background-color:#f0fdf4; border:1px solid #86efac; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#15803d;">체크포인트</h3>
  <ol style="margin:0; padding-left:20px; line-height:1.8;">
    <li>fit_transform과 transform의 차이를 말할 수 있다.</li>
    <li>표준화가 거리 계산에 왜 영향을 주는지 설명할 수 있다.</li>
    <li>파이프라인을 쓰는 이유를 말할 수 있다.</li>
  </ol>
</div>

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
from pathlib import Path


import pandas as pd


from sklearn.model_selection import train_test_split


from sklearn.neighbors import KNeighborsClassifier


from sklearn.preprocessing import StandardScaler


from sklearn.pipeline import make_pipeline


print("=== Day 02-2: 전처리와 표준화 ===")

df = pd.read_csv("data/market_fish_extended.csv")
X = df[["length_cm", "weight_g", "tail_cm"]]
y = df["species"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
raw_model = KNeighborsClassifier(n_neighbors=5)
raw_model.fit(X_train, y_train)
print("\n[실습 1] 전처리 전 점수")
print(round(raw_model.score(X_test, y_test), 4))
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("\n[실습 2] 스케일러 기준값")
print("평균:", scaler.mean_.round(2))
print("표준편차:", scaler.scale_.round(2))
scaled_model = KNeighborsClassifier(n_neighbors=5)
scaled_model.fit(X_train_scaled, y_train)
print("\n[실습 3] 전처리 후 점수")
print(round(scaled_model.score(X_test_scaled, y_test), 4))
sample_df = pd.DataFrame([
    {"length_cm": 25.0, "weight_g": 150.0, "tail_cm": 8.1},
    {"length_cm": 12.0, "weight_g": 14.0, "tail_cm": 3.7},
    {"length_cm": 19.0, "weight_g": 90.0, "tail_cm": 5.9},
])
print("\n[실습 4] 원본 예측")
print(raw_model.predict(sample_df).tolist())
print("\n[실습 5] 표준화 후 예측")
print(scaled_model.predict(scaler.transform(sample_df)).tolist())
pipeline_model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
pipeline_model.fit(X_train, y_train)
print("\n[실습 6] 파이프라인 점수")
print(round(pipeline_model.score(X_test, y_test), 4))
```
