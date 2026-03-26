# Day 10-3. YOLOv8 웹캠과 영상 탐지 실행 흐름

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 목표</h2>
  <p style="margin:0; line-height:1.8;">학습된 best.pt 가중치를 사용해 웹캠과 영상에서 객체탐지를 실행하는 흐름을 이해합니다.</p>
</div>

## 오늘 확인할 내용

- `best.pt`가 왜 중요한지
- 웹캠 탐지와 영상 탐지 코드 예시
- `source`, `conf`, `iou`, `save` 옵션 의미
- 학습 단계와 추론 단계의 연결

## 핵심 설명

학습이 끝나면 `best.pt`라는 가중치 파일이 만들어집니다. 이 파일이 실제 객체탐지의 핵심 결과물입니다.

웹캠 탐지는 `source=0`처럼 카메라 입력을 사용하고, 영상 탐지는 `source="파일경로.mp4"`처럼 영상 파일을 사용합니다. 입력은 달라도 내부에서는 같은 YOLOv8 탐지 모델을 사용합니다.

## 수업 체크포인트

- `best.pt`가 무엇인지 설명할 수 있는가?
- 웹캠 탐지와 영상 탐지의 차이를 말할 수 있는가?
- `conf`와 `iou`가 결과에 어떤 영향을 주는지 설명할 수 있는가?

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
from textwrap import dedent

print("=== Day 10-3: YOLOv8 웹캠과 영상 탐지 실행 흐름 ===")

print("\n[실습 1] 추론 시작점")
print("객체탐지 추론은 학습이 끝난 뒤 만들어진 best.pt 가중치 파일에서 시작합니다.")
print("즉 Roboflow로 데이터를 준비하고 YOLOv8을 학습한 결과물이 이제 실제 탐지에 쓰입니다.")

print("\n[실습 2] 웹캠 탐지 코드 예시")
webcam_code = dedent(
    """
    from ultralytics import YOLO

    model = YOLO("runs_detect/helmet_project/weights/best.pt")
    model.predict(source=0, show=True, conf=0.5, iou=0.5)
    """
).strip()
print(webcam_code)

print("\n[실습 3] 영상 탐지 코드 예시")
video_code = dedent(
    """
    from ultralytics import YOLO

    model = YOLO("runs_detect/helmet_project/weights/best.pt")
    model.predict(
        source="videos/test_video.mp4",
        save=True,
        conf=0.5,
        iou=0.5,
        project="runs_predict",
        name="video_result",
    )
    """
).strip()
print(video_code)

print("\n[실습 4] 주요 옵션 설명")
options = {
    "source": "웹캠 번호 또는 영상 파일 경로를 뜻합니다.",
    "show": "실시간 화면으로 결과를 바로 띄울지 정합니다.",
    "save": "결과 이미지나 영상을 저장할지 정합니다.",
    "conf": "confidence threshold로, 너무 약한 예측을 버리는 기준입니다.",
    "iou": "겹치는 박스를 정리할 때 사용하는 기준입니다.",
}
for key, value in options.items():
    print(f"- {key}: {value}")

print("\n[실습 5] 웹캠과 영상의 공통점")
print("웹캠도 영상도 같은 best.pt 가중치를 사용합니다.")
print("즉 잘 학습된 모델 하나를 만들면 입력만 바꿔 다양한 탐지 환경에 적용할 수 있습니다.")

print("\n[실습 6] 최종 프로젝트 점검표")
checklist = [
    "- best.pt 경로를 알고 있다.",
    "- source=0 으로 웹캠 탐지를 실행할 수 있다.",
    "- mp4 파일 경로를 넣어 영상 탐지를 실행할 수 있다.",
    "- conf 와 iou 값을 바꾸며 결과를 비교할 수 있다.",
]
for item in checklist:
    print(item)

print("\n[정리]")
print("객체탐지 프로젝트의 마지막 단계는 학습된 best.pt를 웹캠과 영상에서 실제로 사용하는 것입니다.")
```