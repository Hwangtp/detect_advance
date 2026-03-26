# pip install pandas

"""Day 09-1. 객체 탐지 데이터셋 구조 이해.

이 파일은 탐지용 CSV 예제를 읽고 이미지 이름, 클래스, 박스 좌표, 학습 분할 정보가
어떻게 함께 저장되는지 확인하도록 만든다.
"""

# pandas는 CSV 표 데이터를 읽고, 열 이름 기준으로 선택하고, 통계를 확인할 때 가장 많이 사용하는 라이브러리다.
import pandas as pd

# 예상 출력 핵심:
# - 데이터 shape는 (1200, 9)이고 클래스별 개수는 helmet, vest, person 각 400개로 출력된다.
# - split 개수는 train 900, valid 150, test 150으로 나온다.
# - 첫 박스의 픽셀 좌표 변환 결과는 x1 51.2, y1 70.4, x2 140.8, y2 185.6이다.

print("=== Day 09-1: 객체 탐지 데이터셋 구조 이해 ===")

# 탐지 데이터는 이미지마다 박스 하나가 한 줄에 저장된다고 가정하고 CSV를 읽는다.
df = pd.read_csv("data/detection_annotations_extended.csv")

print("\n[실습 1] 데이터 개수와 열 이름")
print(df.shape)
print(df.columns.tolist())

# head()를 보면 한 줄이 이미지 파일명, 클래스명, 박스 위치를 함께 가진다는 점을 바로 볼 수 있다.
print("\n[실습 2] 앞부분 5개 행")
print(df.head().to_string(index=False))

# 클래스 개수를 세면 어떤 물체가 많이 등장하는지 빠르게 파악할 수 있다.
print("\n[실습 3] 클래스별 개수")
print(df['label'].value_counts().to_dict())

# split 열은 train, valid, test처럼 데이터를 나누는 용도로 사용된다.
print("\n[실습 4] split별 개수")
print(df['split'].value_counts().to_dict())

# 첫 행 하나를 골라 정규화 좌표가 실제 픽셀 좌표로 어떻게 바뀌는지 계산한다.
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

# 박스 면적을 구하면 큰 물체와 작은 물체의 차이를 수치로 볼 수 있다.
df['box_area'] = (df['box_width'] * df['image_width']) * (df['box_height'] * df['image_height'])
print("\n[실습 6] 박스 면적 요약")
print(df['box_area'].describe().round(2))
