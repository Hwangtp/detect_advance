# pip install pandas scikit-learn

"""Day 01-2. 첫 KNN 분류기 만들기.

이 파일은 규칙 기반 분류와 KNN 분류를 비교하며 머신러닝의 첫 실행 경험을 만든다.
모든 출력은 고정 샘플과 고정 데이터로 재현 가능하다.
"""

# math는 거리 계산이나 제곱근처럼 수학 공식을 코드로 직접 보여 줄 때 사용한다.
import math

# pandas는 CSV 표 데이터를 읽고, 열 이름 기준으로 선택하고, 통계를 확인할 때 가장 많이 사용하는 라이브러리다.
import pandas as pd

# KNeighborsClassifier는 가장 가까운 이웃 정보를 기준으로 분류하는 입문용 모델이라 거리 개념 설명에 적합하다.
from sklearn.neighbors import KNeighborsClassifier

# 예상 출력 핵심:
# - 규칙 기반 분류기 정확도는 0.9967로 출력된다.
# - 샘플 예측 결과는 [bream, smelt, perch]로 고정된다.
# - 전체 데이터 정확도는 1.0이며 첫 샘플 최근접 이웃 거리도 고정 값으로 출력된다.

print("=== Day 01-2: 첫 KNN 분류기 만들기 ===")

fish_df = pd.read_csv("data/market_fish_extended.csv")

def rule_predict(row):
    # 규칙 기반 분류기는 사람이 직접 기준을 적는 방법을 보여 주기 위해 먼저 사용한다.
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
