# Day 09-1. 객체 탐지 데이터셋 구조 이해

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 개요</h2>
  <p style="margin:0; line-height:1.8;">객체 탐지 데이터가 이미지 파일명, 클래스, 바운딩 박스 좌표, split 정보를 함께 저장한다는 점을 CSV 예제로 확인합니다.</p>
</div>

<div style="background-color:#eff6ff; border:1px solid #93c5fd; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#1d4ed8;">오늘 실습 구성</h3>
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
<li>탐지 주석 CSV의 열 구조 읽기</li>
<li>클래스별 개수와 split별 개수 세기</li>
<li>정규화 좌표를 픽셀 좌표로 바꾸기</li>
<li>박스 면적 계산과 요약 통계 확인</li>
  </ul>
</div>

<div style="background-color:#f0fdf4; border:1px solid #86efac; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#15803d;">수업 체크포인트</h3>
  <ol style="margin:0; padding-left:20px; line-height:1.8;">
<li>탐지 데이터 한 줄이 어떤 정보를 담는지 설명할 수 있다.</li>
<li>정규화 좌표와 픽셀 좌표의 차이를 구분할 수 있다.</li>
<li>split 열이 학습과 평가 분리를 위해 필요하다는 점을 이해한다.</li>
  </ol>
</div>

<div style="background-color:#fff7ed; border:1px solid #fdba74; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#c2410c;">학습 가이드</h3>
  <p style="margin:0; line-height:1.9;">객체 탐지 수업은 모델보다 데이터 구조를 먼저 잡아 두는 것이 중요합니다. 이미지 분류와 달리 위치 정보가 함께 들어간다는 점을 계속 의식하면서 표를 읽어 보면 YOLO 형식도 훨씬 쉽게 이해됩니다.</p>
</div>

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
import pandas as pd


print("=== Day 09-1: 객체 탐지 데이터셋 구조 이해 ===")


df = pd.read_csv("data/detection_annotations_extended.csv")

print("\n[실습 1] 데이터 개수와 열 이름")
print(df.shape)
print(df.columns.tolist())


print("\n[실습 2] 앞부분 5개 행")
print(df.head().to_string(index=False))


print("\n[실습 3] 클래스별 개수")
print(df['label'].value_counts().to_dict())


print("\n[실습 4] split별 개수")
print(df['split'].value_counts().to_dict())


row = df.iloc[0]
image_width = int(row['image_width'])
image_height = int(row['image_height'])
x_center = float(row['x_center']) * image_width
y_center = float(row['y_center']) * image_height
box_width = float(row['box_width']) * image_width
box_height = float(row['box_height']) * image_height
x1 = round(x_center - box_width / 2, 1)
y1 = round(y_center - box_height / 2, 1)
x2 = round(x_center + box_width / 2, 1)
y2 = round(y_center + box_height / 2, 1)

print("\n[실습 5] 첫 번째 박스의 픽셀 좌표 변환")
print({
    'image_id': row['image_id'],
    'label': row['label'],
    'x1': x1,
    'y1': y1,
    'x2': x2,
    'y2': y2,
})


df['box_area'] = (df['box_width'] * df['image_width']) * (df['box_height'] * df['image_height'])
print("\n[실습 6] 박스 면적 요약")
print(df['box_area'].describe().round(2))
```
