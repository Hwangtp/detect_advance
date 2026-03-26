# Day 01-1. AI, 머신러닝, 딥러닝의 큰 지도

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 개요</h2>
  <p style="margin:0; line-height:1.8;">AI, 머신러닝, 딥러닝의 관계와 데이터 표의 기본 구조를 이해합니다.</p>
</div>

<div style="background-color:#eff6ff; border:1px solid #93c5fd; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#1d4ed8;">실습 흐름</h3>
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li>생선 데이터 읽기</li>
    <li>열 이름과 클래스 종류 확인</li>
    <li>요약 통계 보기</li>
    <li>클래스별 평균 특징 비교</li>
  </ul>
</div>

<div style="background-color:#f0fdf4; border:1px solid #86efac; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#15803d;">체크포인트</h3>
  <ol style="margin:0; padding-left:20px; line-height:1.8;">
    <li>특성과 정답을 구분할 수 있다.</li>
    <li>클래스 개수와 데이터 크기를 설명할 수 있다.</li>
    <li>평균 특징 비교가 왜 필요한지 말할 수 있다.</li>
  </ol>
</div>

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
import pandas as pd


print("=== Day 01-1: AI, 머신러닝, 딥러닝의 큰 지도 ===")
print("AI는 넓은 개념, 머신러닝은 데이터에서 규칙을 배우는 방법, 딥러닝은 신경망을 깊게 쌓은 방법입니다.")

fish_df = pd.read_csv("data/market_fish_extended.csv")


print("\n[실습 1] 데이터 앞 5행")
print(fish_df.head().to_string(index=False))
print("\n[실습 2] 열 이름 확인")
print(fish_df.columns.tolist())
print("\n[실습 3] 데이터 크기와 종류")
print("행 개수:", len(fish_df))
print("생선 종류:", sorted(fish_df["species"].unique().tolist()))
print("\n[실습 4] 클래스별 개수")
print(fish_df["species"].value_counts().sort_index().to_string())
print("\n[실습 5] 숫자 열 요약 통계")
print(fish_df[["length_cm", "weight_g", "tail_cm"]].describe().round(2).to_string())
print("\n[실습 6] 생선 종류별 평균 특징")
print(
    fish_df.groupby("species")[["length_cm", "weight_g", "tail_cm"]]
    .mean()
    .round(2)
    .to_string()
)
print("\n[실습 7] 특성과 정답 설명")
print("특성(feature): 모델이 보고 배우는 입력값")
print("정답(label): 모델이 맞혀야 하는 목표값")
print("현재 특성 열: ['length_cm', 'weight_g', 'tail_cm']")
print("현재 정답 열: ['species']")
print("\n정리: 오늘은 데이터를 읽고, 어떤 값이 입력이고 어떤 값이 정답인지 구분하는 연습을 했습니다.")
```
