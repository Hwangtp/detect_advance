# Day 09-3. Roboflow 데이터셋 제작과 YOLOv8 학습

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 목표</h2>
  <p style="margin:0; line-height:1.8;">Roboflow로 직접 만든 데이터셋이 YOLOv8 학습으로 이어지는 전체 흐름을 이해합니다.</p>
</div>

## 오늘 확인할 내용

- Roboflow 프로젝트 준비 순서
- `data.yaml`이 왜 필요한지
- YOLOv8 CLI와 Python 학습 방법
- `epochs`, `imgsz`, `batch`의 의미

## 핵심 설명

사용자 정의 객체탐지는 단순히 모델을 불러오는 것만으로 끝나지 않습니다. 먼저 Roboflow에서 데이터를 모으고, bounding box를 그리고, train/valid/test 구조를 준비한 뒤, YOLOv8 형식으로 export 해야 합니다.

그 다음 `data.yaml`을 기준으로 YOLOv8 학습을 실행하면 `best.pt` 같은 가중치 파일이 만들어지고, 이 파일을 웹캠이나 영상 탐지에 사용할 수 있습니다.

## 수업 체크포인트

- Roboflow와 YOLOv8의 역할을 구분할 수 있는가?
- `data.yaml`이 어떤 정보를 담는지 설명할 수 있는가?
- `epochs`, `imgsz`, `batch`를 쉬운 말로 설명할 수 있는가?

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
from textwrap import dedent

print("=== Day 09-3: Roboflow 데이터셋 제작과 YOLOv8 학습 흐름 ===")

print("\n[실습 1] Roboflow 프로젝트 준비 순서")
roboflow_steps = [
    "1) 어떤 물체를 탐지할지 정하고 클래스 이름을 확정합니다.",
    "2) 그 물체가 보이는 이미지나 영상 프레임을 모읍니다.",
    "3) Roboflow에서 새 프로젝트를 만들고 이미지들을 업로드합니다.",
    "4) 모든 물체에 bounding box를 그리고 클래스 이름을 붙입니다.",
    "5) train / valid / test 비율을 확인합니다.",
    "6) 전처리와 augmentation 설정을 검토합니다.",
    "7) YOLOv8 형식으로 export 합니다.",
]
for step in roboflow_steps:
    print(step)

print("\n[실습 2] data.yaml 예시")
data_yaml_example = dedent(
    """
    train: ../train/images
    val: ../valid/images
    test: ../test/images

    nc: 3
    names: [helmet, person, vest]
    """
).strip()
print(data_yaml_example)

print("\n[실습 3] YOLOv8 CLI 학습 명령어 예시")
cli_command = (
    "yolo task=detect mode=train model=yolov8n.pt "
    "data=data.yaml epochs=50 imgsz=640 batch=16"
)
print(cli_command)

print("\n[실습 4] YOLOv8 Python 학습 코드 예시")
python_train_example = dedent(
    """
    from ultralytics import YOLO

    model = YOLO(\"yolov8n.pt\")
    model.train(
        data=\"data.yaml\",
        epochs=50,
        imgsz=640,
        batch=16,
        project=\"runs_detect\",
        name=\"helmet_project\",
    )
    """
).strip()
print(python_train_example)

print("\n[실습 5] 핵심 하이퍼파라미터 설명")
hyperparameters = {
    "model": "어떤 기본 가중치에서 시작할지 정합니다. 예: yolov8n.pt",
    "epochs": "데이터 전체를 몇 번 반복해서 학습할지 정합니다.",
    "imgsz": "입력 이미지 크기입니다. 보통 640을 많이 사용합니다.",
    "batch": "한 번에 몇 장씩 학습할지 정합니다.",
}
for key, value in hyperparameters.items():
    print(f"- {key}: {value}")

print("\n[실습 6] 학습 후 꼭 확인할 결과물")
print("- runs/detect/.../weights/best.pt : 가장 중요한 최종 가중치 파일")
print("- results.png : 학습 진행 그래프")
print("- confusion_matrix.png : 클래스별 오분류 확인 자료")

print("\n[실습 7] 오늘 핵심 정리")
print("Roboflow는 데이터 준비를, YOLOv8은 학습과 탐지를 담당합니다.")
print("즉 사용자 정의 객체탐지는 '라벨링 -> export -> 학습 -> best.pt 사용'의 흐름으로 완성됩니다.")
```