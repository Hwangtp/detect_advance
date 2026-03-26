# pip install pandas

"""Day 09-2. YOLO 형식과 학습 흐름.

이 파일은 CSV 주석 데이터를 YOLO 텍스트 한 줄 형식으로 바꾸어 보면서
클래스 번호와 정규화 좌표가 어떻게 저장되는지 설명한다.
"""

# pandas는 CSV 표 데이터를 읽고, 열 이름 기준으로 선택하고, 통계를 확인할 때 가장 많이 사용하는 라이브러리다.
import pandas as pd

# 예상 출력 핵심:
# - class id 매핑은 helmet 0, person 1, vest 2로 출력된다.
# - YOLO 라벨 예시는 세 줄의 class_id x_center y_center width height 형식으로 출력된다.
# - data.yaml 핵심 정보에는 nc 3과 세 클래스 이름이 포함된다.

print("=== Day 09-2: YOLO 형식과 학습 흐름 ===")

# CSV를 읽은 뒤 클래스 이름을 정렬해 class id로 매핑하면 YOLO 라벨 파일을 만들 수 있다.
df = pd.read_csv("data/detection_annotations_extended.csv")
class_names = sorted(df['label'].unique().tolist())
class_to_id = {name: idx for idx, name in enumerate(class_names)}

print("\n[실습 1] 클래스 이름과 class id")
print(class_to_id)

# YOLO 형식은 class_id x_center y_center width height 다섯 값으로 한 줄을 만든다.
def to_yolo_line(row: pd.Series) -> str:
    return (
        f"{class_to_id[row['label']]} "
        f"{row['x_center']:.6f} {row['y_center']:.6f} "
        f"{row['box_width']:.6f} {row['box_height']:.6f}"
    )

sample_lines = [to_yolo_line(df.iloc[i]) for i in range(3)]
print("\n[실습 2] YOLO 라벨 예시 3줄")
for line in sample_lines:
    print(line)

# 이미지별로 라벨이 몇 개 들어가는지 세면 한 장에 객체가 하나 이상 있을 수 있다는 점을 설명할 수 있다.
image_counts = df.groupby('image_id').size().head(5)
print("\n[실습 3] 이미지별 라벨 개수 예시")
print(image_counts.to_dict())

# split 정보를 이용해 train/valid/test 파일 묶음을 어떻게 나누는지 요약한다.
print("\n[실습 4] split별 라벨 수")
print(df['split'].value_counts().to_dict())

# 실제 수업에서는 data.yaml에 클래스 목록과 경로를 적는다는 점을 간단한 문자열로 보여 준다.
data_yaml_preview = {
    'train': 'images/train',
    'val': 'images/valid',
    'test': 'images/test',
    'nc': len(class_names),
    'names': class_names,
}
print("\n[실습 5] data.yaml에 들어갈 핵심 정보")
print(data_yaml_preview)

# 학습 흐름을 단계로 요약하면 학생이 YOLO 프로젝트 준비 순서를 잡기 쉽다.
workflow = [
    '1) 이미지와 라벨 txt를 같은 이름으로 준비한다.',
    '2) train/valid/test 폴더를 나눈다.',
    '3) data.yaml에 경로와 클래스 이름을 적는다.',
    '4) 모델 학습 후 confidence와 IoU 기준으로 결과를 해석한다.',
]
print("\n[실습 6] YOLO 프로젝트 준비 순서")
for step in workflow:
    print(step)
