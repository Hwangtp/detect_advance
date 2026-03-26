# pip install pandas

"""Day 05-1. 비지도 학습 입문.

이 파일은 라벨이 없는 데이터에서도 비슷한 패턴을 찾을 수 있다는 점을
과일 특징 데이터로 설명하는 강사용 실습 파일이다.
"""

import pandas as pd

# 예상 출력 핵심:
# - 과일 데이터 앞 5행과 과일별 평균 특징이 출력된다.
# - apple, banana, orange는 sweetness, crunch, moisture 평균값 차이로 구분되는 패턴이 보인다.
# - 비지도 학습은 정답 없이 구조를 찾는다는 설명 문장이 출력된다.

print("=== Day 05-1: 비지도 학습 입문 ===")

df = pd.read_csv("data/fruit_traits_extended.csv")

# 실제 수업에서는 fruit 열이 정답처럼 보이지만,
# 비지도 학습에서는 이런 라벨 없이도 비슷한 것끼리 묶을 수 있다는 점을 강조한다.
print("\n[실습 1] 데이터 앞 5행")
print(df.head().to_string(index=False))

# 실제 라벨이 있다고 가정하고 평균 특징을 먼저 본다.
print("\n[실습 2] 실제 과일별 평균 특징")
print(
    df.groupby("fruit")[["sweetness", "crunch", "moisture"]]
    .mean()
    .round(2)
    .to_string()
)

# 비지도 학습에서는 보통 정답 라벨 없이 특징값만 사용한다.
unlabeled_X = df[["sweetness", "crunch", "moisture"]]
print("\n[실습 3] 라벨 없이 본 특징 데이터 앞 5행")
print(unlabeled_X.head().to_string(index=False))

print("\n[실습 4] 패턴 읽기")
print("apple은 crunch가 높고 moisture가 낮은 편이다.")
print("banana는 sweetness가 높고 crunch가 낮은 편이다.")
print("orange는 moisture가 높고 crunch는 중간 수준이다.")

print("\n[실습 5] 비지도 학습 핵심 문장")
print("비지도 학습은 정답 라벨 없이 데이터의 구조를 찾는 방법입니다.")
print("군집은 비슷한 데이터끼리 묶는 작업입니다.")