# Day 01-2. 첫 KNN 분류기 만들기

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 개요</h2>
  <p style="margin:0; line-height:1.8;">규칙 기반 분류와 KNN 분류를 비교하며 첫 머신러닝 예측을 수행합니다.</p>
</div>

<div style="background-color:#eff6ff; border:1px solid #93c5fd; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#1d4ed8;">실습 흐름</h3>
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li>규칙 기반 분류기 실행</li>
    <li>거리 계산으로 KNN 직관 만들기</li>
    <li>KNN 모델 학습</li>
    <li>샘플 3개 예측</li>
    <li>최근접 이웃 정보 확인</li>
  </ul>
</div>

<div style="background-color:#f0fdf4; border:1px solid #86efac; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#15803d;">체크포인트</h3>
  <ol style="margin:0; padding-left:20px; line-height:1.8;">
    <li>규칙 기반과 KNN의 차이를 말할 수 있다.</li>
    <li>KNN에서 거리 개념이 왜 중요한지 설명할 수 있다.</li>
    <li>fit, predict, score의 역할을 구분할 수 있다.</li>
  </ol>
</div>

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
import math


import pandas as pd


from sklearn.neighbors import KNeighborsClassifier


print("=== Day 01-2: 첫 KNN 분류기 만들기 ===")

fish_df = pd.read_csv("data/market_fish_extended.csv")

def rule_predict(row):

    if row["length_cm"] < 14:
        return "smelt"
    if row["weight_g"] > 220:
        return "bream"
    return "perch"

rule_predictions = fish_df.apply(rule_predict, axis=1)
rule_accuracy = (rule_predictions == fish_df["species"]).mean()
print("[실습 1] 규칙 기반 분류기 정확도")
print("정확도:", round(rule_accuracy, 4))

sample = {"length_cm": 26.5, "weight_g": 280.0, "tail_cm": 8.8}
reference_rows = fish_df.iloc[[0, 1, 2]][["species", "length_cm", "weight_g", "tail_cm"]]
distance_rows = []
for _, row in reference_rows.iterrows():
    distance = math.sqrt(
        (row["length_cm"] - sample["length_cm"]) ** 2
        + (row["weight_g"] - sample["weight_g"]) ** 2
        + (row["tail_cm"] - sample["tail_cm"]) ** 2
    )
    distance_rows.append({"species": row["species"], "distance": round(distance, 2)})
print("[실습 2] 거리 계산 예시")
print(pd.DataFrame(distance_rows).to_string(index=False))

X = fish_df[["length_cm", "weight_g", "tail_cm"]]
y = fish_df["species"]
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X, y)

sample_df = pd.DataFrame([
    {"length_cm": 26.5, "weight_g": 280.0, "tail_cm": 8.8},
    {"length_cm": 11.0, "weight_g": 13.0, "tail_cm": 3.6},
    {"length_cm": 19.0, "weight_g": 90.0, "tail_cm": 5.9},
])
print("[실습 3] KNN 샘플 예측")
print(model.predict(sample_df).tolist())
print("[실습 4] 전체 데이터 정확도")
print(round(model.score(X, y), 4))

distances, indices = model.kneighbors(sample_df.iloc[[0]])
print("[실습 5] 첫 샘플의 최근접 이웃 정보")
print("거리:", distances.round(2).tolist())
print("인덱스:", indices.tolist())
print("정리: 규칙 기반 분류와 KNN 분류를 비교하며 머신러닝이 데이터를 보고 판단하는 감각을 만들었습니다.")
```
