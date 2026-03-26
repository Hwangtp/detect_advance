# Day 02-1. train/test 분리의 기초

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 개요</h2>
  <p style="margin:0; line-height:1.8;">왜 데이터를 나눠야 하는지와 stratify의 역할을 이해합니다.</p>
</div>

<div style="background-color:#eff6ff; border:1px solid #93c5fd; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#1d4ed8;">실습 흐름</h3>
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li>분리 전 전체 정확도 보기</li>
    <li>train/test 분리</li>
    <li>클래스 비율 확인</li>
    <li>분리 후 시험 정확도 확인</li>
  </ul>
</div>

<div style="background-color:#f0fdf4; border:1px solid #86efac; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#15803d;">체크포인트</h3>
  <ol style="margin:0; padding-left:20px; line-height:1.8;">
    <li>공정한 평가를 위해 데이터를 나누는 이유를 설명할 수 있다.</li>
    <li>stratify가 왜 필요한지 말할 수 있다.</li>
    <li>학습용 점수와 시험용 점수의 차이를 읽을 수 있다.</li>
  </ol>
</div>

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
import pandas as pd


from sklearn.model_selection import train_test_split


from sklearn.neighbors import KNeighborsClassifier


print("=== Day 02-1: train/test 분리의 기초 ===")

df = pd.read_csv("data/market_fish_extended.csv")
X = df[["length_cm", "weight_g", "tail_cm"]]
y = df["species"]
full_model = KNeighborsClassifier(n_neighbors=5)
full_model.fit(X, y)
print("\n[실습 1] 전체 데이터를 한 번에 학습하고 평가")
print("정확도:", round(full_model.score(X, y), 4))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print("\n[실습 2] 분리된 데이터 크기")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("\n[실습 3] 학습용 클래스 분포")
print(y_train.value_counts().sort_index().to_string())
print("\n[실습 4] 시험용 클래스 분포")
print(y_test.value_counts().sort_index().to_string())
split_model = KNeighborsClassifier(n_neighbors=5)
split_model.fit(X_train, y_train)
print("\n[실습 5] 분리 후 학습용/시험용 점수")
print("학습용 정확도:", round(split_model.score(X_train, y_train), 4))
print("시험용 정확도:", round(split_model.score(X_test, y_test), 4))
sample_df = pd.DataFrame([{"length_cm": 25.2, "weight_g": 240.0, "tail_cm": 8.3}])
print("\n[실습 6] 새 샘플 예측")
print(split_model.predict(sample_df).tolist())
```
