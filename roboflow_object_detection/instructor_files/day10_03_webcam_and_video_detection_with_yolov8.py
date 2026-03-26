# pip install ultralytics opencv-python

"""Day 10-3. YOLOv8 웹캠/영상 탐지 실행 흐름.

이 파일은 학습이 끝난 뒤 만들어진 best.pt 가중치를 사용해
웹캠과 영상에서 실제 객체탐지를 어떻게 실행하는지 설명하는 강사용 실습 파일이다.
수업에서는 이 파일을 통해 입력 소스만 다를 뿐 핵심 모델 사용법은 비슷하다는 점을 강조한다.
"""

# textwrap.dedent는 여러 줄 코드 예시를 정돈해서 출력할 때 사용한다.
from textwrap import dedent

# 예상 출력 핵심:
# - 웹캠 탐지 코드 예시와 영상 탐지 코드 예시가 각각 출력된다.
# - conf, iou, source, save 같은 주요 옵션 설명이 출력된다.
# - best.pt 하나로 webcam 과 video 추론을 모두 연결할 수 있다는 문장이 출력된다.

print("=== Day 10-3: YOLOv8 웹캠과 영상 탐지 실행 흐름 ===")

# 먼저 best.pt가 어디서 왔는지 다시 연결해 주면 학습 단계와 추론 단계가 하나의 흐름으로 묶인다.
print("\n[실습 1] 추론 시작점")
print("객체탐지 추론은 학습이 끝난 뒤 만들어진 best.pt 가중치 파일에서 시작합니다.")
print("즉 Roboflow로 데이터를 준비하고 YOLOv8을 학습한 결과물이 이제 실제 탐지에 쓰입니다.")

# 웹캠 예시는 실시간 탐지의 핵심 흐름을 가장 짧게 보여 주는 코드라서 꼭 별도로 소개한다.
print("\n[실습 2] 웹캠 탐지 코드 예시")
webcam_code = dedent(
    """
    from ultralytics import YOLO

    model = YOLO("runs_detect/helmet_project/weights/best.pt")
    model.predict(source=0, show=True, conf=0.5, iou=0.5)
    """
).strip()
print(webcam_code)

# 영상 탐지는 파일 경로를 source로 넣고 결과를 저장하는 방식이 자주 쓰인다.
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

# 주요 옵션이 무엇을 의미하는지 정리해 주면 학생들이 코드를 수정할 수 있게 된다.
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

# 웹캠과 영상은 source만 다르고 best.pt 사용 흐름은 같다는 점을 다시 확인한다.
print("\n[실습 5] 웹캠과 영상의 공통점")
print("웹캠도 영상도 같은 best.pt 가중치를 사용합니다.")
print("즉 잘 학습된 모델 하나를 만들면 입력만 바꿔 다양한 탐지 환경에 적용할 수 있습니다.")

# 마지막으로 실전 점검표를 출력하면 학생들이 혼자서 프로젝트를 재현하기 쉽다.
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