# pip install pandas scikit-learn

"""Day 05-2. KMeans 군집 실습.

이 파일은 KMeans로 과일 데이터를 비슷한 그룹끼리 묶고,
군집 개수, inertia, 군집 중심, 새 샘플 예측을 읽는 방법을 보여 주는 강사용 실습 파일이다.
모든 결과는 random_state=42로 고정해 항상 같은 출력이 나오도록 맞췄다.
"""

import os
import warnings
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 실행 환경에 따라 나오는 군집 관련 경고를 줄여 수업 출력이 깔끔하게 보이게 한다.
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("LOKY_MAX_CPU_COUNT", "1")
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn.cluster")
warnings.filterwarnings("ignore", category=UserWarning, module="joblib")

# 예상 출력 핵심:
# - k=2,3,4,5에 대한 inertia가 순서대로 출력된다.
# - k=3에서 군집 개수는 450, 450, 450으로 균형 있게 나온다.
# - 군집 교차표에서 apple, banana, orange가 거의 완벽하게 분리된다.
# - 새 샘플 군집 예측 결과는 [1, 0]으로 출력된다.

print("=== Day 05-2: KMeans 군집 실습 ===")

df = pd.read_csv("data/fruit_traits_extended.csv")
X = df[["sweetness", "crunch", "moisture"]]

# 거리 기반 알고리즘이므로 표준화를 해 두는 편이 좋다.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\n[실습 1] k 값별 inertia")
for k in [2, 3, 4, 5]:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X_scaled)
    print(f"k={k} -> inertia={model.inertia_:.2f}")

# n_clusters는 몇 개 그룹으로 나눌지 정하는 하이퍼파라미터다.
km = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = km.fit_predict(X_scaled)
df["cluster"] = clusters

print("\n[실습 2] 군집 개수")
print(df["cluster"].value_counts().sort_index().to_string())

print("\n[실습 3] 실제 과일과 군집 번호 비교")
print(pd.crosstab(df["fruit"], df["cluster"]).to_string())

# cluster_centers_는 표준화된 공간의 군집 중심이므로 inverse_transform으로 원래 단위로 되돌려 읽는다.
centers = pd.DataFrame(
    scaler.inverse_transform(km.cluster_centers_),
    columns=["sweetness", "crunch", "moisture"],
).round(2)
print("\n[실습 4] 군집 중심")
print(centers.to_string(index=False))

sample_df = pd.DataFrame([
    {"sweetness": 65.0, "crunch": 78.0, "moisture": 55.0},
    {"sweetness": 83.0, "crunch": 27.0, "moisture": 73.0},
])
print("\n[실습 5] 새 샘플 군집 예측")
print(km.predict(scaler.transform(sample_df)).tolist())

print("\n[실습 6] 오늘 핵심 정리")
print("KMeans는 비슷한 특징을 가진 데이터를 자동으로 묶는 군집화 알고리즘이다.")
print("n_clusters는 군집 개수, inertia는 군집이 얼마나 촘촘한지 보는 참고값이다.")