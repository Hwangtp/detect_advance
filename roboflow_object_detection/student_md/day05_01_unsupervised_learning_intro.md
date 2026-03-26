# Day 05-1. 비지도학습 입문

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 목표</h2>
  <p style="margin:0; line-height:1.8;">정답이 없는 데이터에서도 비슷한 구조를 찾는 비지도학습의 개념을 이해합니다.</p>
</div>

## 오늘 확인할 내용

- 지도학습과 비지도학습의 차이
- 라벨 없이 특징만 보는 방법
- 과일 데이터에서 보이는 패턴

## 핵심 설명

지도학습은 정답 라벨이 있는 데이터를 사용합니다. 반면 비지도학습은 정답 라벨 없이 데이터 자체의 비슷한 구조를 찾으려는 방법입니다.

오늘 실습에서는 과일의 단맛, 아삭함, 수분 같은 특징을 보고, 정답 이름이 없어도 비슷한 과일끼리 묶일 수 있겠다는 감을 잡는 것이 목표입니다.

## 수업 체크포인트

- 비지도학습을 한 문장으로 설명할 수 있는가?
- 라벨이 없어도 특징만으로 패턴을 볼 수 있다는 점을 이해했는가?

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
import pandas as pd

print("=== Day 05-1: 비지도학습 입문 ===")

df = pd.read_csv("data/fruit_traits_extended.csv")

print("\n[실습 1] 데이터 앞 5행")
print(df.head().to_string(index=False))

print("\n[실습 2] 실제 과일별 평균 특징")
print(
    df.groupby("fruit")[["sweetness", "crunch", "moisture"]]
    .mean()
    .round(2)
    .to_string()
)

unlabeled_X = df[["sweetness", "crunch", "moisture"]]
print("\n[실습 3] 라벨 없이 보는 특징 데이터 앞 5행")
print(unlabeled_X.head().to_string(index=False))

print("\n[실습 4] 패턴 읽기")
print("apple은 crunch가 높고 moisture가 중간인 편입니다.")
print("banana는 sweetness가 높고 crunch가 낮은 편입니다.")
print("orange는 moisture가 높고 crunch는 중간 수준입니다.")

print("\n[실습 5] 비지도학습 핵심 문장")
print("비지도학습은 정답 라벨 없이 데이터의 구조를 찾는 방법입니다.")
print("비슷한 특징을 가진 데이터끼리 묶는 작업과 연결할 수 있습니다.")
```