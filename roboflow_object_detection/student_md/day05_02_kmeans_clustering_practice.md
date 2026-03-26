# Day 05-2. KMeans 군집 실습

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 목표</h2>
  <p style="margin:0; line-height:1.8;">KMeans로 데이터를 여러 군집으로 나누고 군집 중심과 예측 방법을 이해합니다.</p>
</div>

## 오늘 확인할 내용

- `n_clusters`가 무엇인지
- `inertia`를 어떻게 읽는지
- `cluster_centers_`가 무엇인지
- `predict()`가 어떤 군집 번호를 주는지

## 핵심 설명

KMeans는 비슷한 데이터끼리 자동으로 몇 개의 그룹으로 나누는 알고리즘입니다. 군집 번호 자체에는 특별한 뜻이 없고, 중요한 것은 같은 군집 안에 어떤 특징이 모였는가입니다.

`n_clusters`는 그룹 수를 정하는 값이고, `inertia`는 같은 군집 안의 데이터가 얼마나 촘촘하게 모였는지 참고하는 값입니다.

## 수업 체크포인트

- 군집 번호가 정답 이름이 아니라는 것을 설명할 수 있는가?
- `cluster_centers_`를 군집의 대표 위치로 설명할 수 있는가?

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
import os
import warnings
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("LOKY_MAX_CPU_COUNT", "1")
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn.cluster")
warnings.filterwarnings("ignore", category=UserWarning, module="joblib")

print("=== Day 05-2: KMeans 군집 실습 ===")

df = pd.read_csv("data/fruit_traits_extended.csv")
X = df[["sweetness", "crunch", "moisture"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\n[실습 1] k 값별 inertia")
for k in [2, 3, 4, 5]:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X_scaled)
    print(f"k={k} -> inertia={model.inertia_:.2f}")

km = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = km.fit_predict(X_scaled)
df["cluster"] = clusters

print("\n[실습 2] 군집 개수")
print(df["cluster"].value_counts().sort_index().to_string())

print("\n[실습 3] 실제 과일과 군집 번호 비교")
print(pd.crosstab(df["fruit"], df["cluster"]).to_string())

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
print("KMeans는 비슷한 특징을 가진 데이터를 자동으로 묶는 군집 알고리즘입니다.")
print("n_clusters는 군집 개수, inertia는 군집이 얼마나 촘촘한지 보여주는 참고값입니다.")
```