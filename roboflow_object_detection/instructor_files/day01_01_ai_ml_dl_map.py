# pip install pandas

"""Day 01-1. AI, 머신러닝, 딥러닝의 큰 지도.

이 파일은 초심자가 AI, 머신러닝, 딥러닝의 관계를 말로만 듣지 않고,
작은 데이터 표를 보며 차이를 설명할 수 있게 만드는 첫 수업 파일이다.
모든 출력은 고정 데이터로 재현 가능하다.
"""

# pandas는 CSV 표 데이터를 읽고, 열 이름 기준으로 선택하고, 통계를 확인할 때 가장 많이 사용하는 라이브러리다.
import pandas as pd

# 예상 출력 핵심:
# - 행 개수는 1200, 생선 종류는 bream, perch, smelt 세 가지로 출력된다.
# - 클래스별 개수는 각 400개로 균형 있게 나온다.
# - 종류별 평균 특징은 bream이 가장 크고 smelt가 가장 작게 보이는 패턴이 나온다.

print("=== Day 01-1: AI, 머신러닝, 딥러닝의 큰 지도 ===")
print("AI는 넓은 개념, 머신러닝은 데이터에서 규칙을 배우는 방법, 딥러닝은 신경망을 깊게 쌓은 방법입니다.")

fish_df = pd.read_csv("data/market_fish_extended.csv")
# 첫 수업에서는 분류 실습에 사용할 생선 데이터를 먼저 읽는다.

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
