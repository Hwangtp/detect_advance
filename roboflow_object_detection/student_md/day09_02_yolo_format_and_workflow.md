# Day 09-2. YOLO 형식과 학습 흐름

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 개요</h2>
  <p style="margin:0; line-height:1.8;">탐지 CSV를 YOLO 라벨 한 줄 형식으로 바꾸어 보며 class id, 정규화 좌표, data.yaml 구성을 함께 정리합니다.</p>
</div>

<div style="background-color:#eff6ff; border:1px solid #93c5fd; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#1d4ed8;">오늘 실습 구성</h3>
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
<li>클래스 이름을 class id로 매핑하기</li>
<li>YOLO 라벨 한 줄 만들기</li>
<li>이미지별 라벨 개수와 split 분포 확인</li>
<li>data.yaml 핵심 항목 정리</li>
<li>YOLO 프로젝트 준비 순서 요약</li>
  </ul>
</div>

<div style="background-color:#f0fdf4; border:1px solid #86efac; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#15803d;">수업 체크포인트</h3>
  <ol style="margin:0; padding-left:20px; line-height:1.8;">
<li>YOLO txt 한 줄의 다섯 값 의미를 설명할 수 있다.</li>
<li>data.yaml에 왜 경로와 클래스 이름이 필요한지 이해한다.</li>
<li>탐지 프로젝트 준비 순서를 말할 수 있다.</li>
  </ol>
</div>

<div style="background-color:#fff7ed; border:1px solid #fdba74; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#c2410c;">학습 가이드</h3>
  <p style="margin:0; line-height:1.9;">이 수업은 실제 학습 명령보다 먼저 라벨 구조를 머리에 넣는 단계입니다. class id와 정규화 좌표의 의미를 정확히 잡아 두면 이후 프레임워크가 바뀌어도 데이터 준비는 흔들리지 않습니다.</p>
</div>

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
import pandas as pd


print("=== Day 09-2: YOLO 형식과 학습 흐름 ===")


df = pd.read_csv("data/detection_annotations_extended.csv")
class_names = sorted(df['label'].unique().tolist())
class_to_id = {name: idx for idx, name in enumerate(class_names)}

print("\n[실습 1] 클래스 이름과 class id")
print(class_to_id)


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


image_counts = df.groupby('image_id').size().head(5)
print("\n[실습 3] 이미지별 라벨 개수 예시")
print(image_counts.to_dict())


print("\n[실습 4] split별 라벨 수")
print(df['split'].value_counts().to_dict())


data_yaml_preview = {
    'train': 'images/train',
    'val': 'images/valid',
    'test': 'images/test',
    'nc': len(class_names),
    'names': class_names,
}
print("\n[실습 5] data.yaml에 들어갈 핵심 정보")
print(data_yaml_preview)


workflow = [
    '1) 이미지와 라벨 txt를 같은 이름으로 준비한다.',
    '2) train/valid/test 폴더를 나눈다.',
    '3) data.yaml에 경로와 클래스 이름을 적는다.',
    '4) 모델 학습 후 confidence와 IoU 기준으로 결과를 해석한다.',
]
print("\n[실습 6] YOLO 프로젝트 준비 순서")
for step in workflow:
    print(step)
```
