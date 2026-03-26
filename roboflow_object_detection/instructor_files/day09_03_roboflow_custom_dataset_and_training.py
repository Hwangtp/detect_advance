# pip install ultralytics roboflow

"""Day 09-3. Roboflow 데이터셋 제작과 YOLOv8 학습 흐름.

이 파일은 사용자가 직접 정의한 물체를 탐지하기 위해
Roboflow에서 데이터를 준비하고, YOLOv8으로 학습을 시작하는 과정을
순서대로 설명하는 강사용 실습 파일이다.
실제 학습은 환경과 시간에 따라 달라질 수 있으므로,
여기서는 반드시 알아야 할 흐름과 명령어 의미를 확실하게 설명하는 데 집중한다.
"""

# textwrap.dedent는 여러 줄 예시 코드를 보기 좋게 정리해서 출력할 때 사용한다.
from textwrap import dedent

# 예상 출력 핵심:
# - Roboflow 프로젝트 준비 단계가 순서대로 출력된다.
# - data.yaml, train 명령어, Python 학습 코드 예시가 함께 출력된다.
# - epochs, imgsz, batch, model 같은 핵심 하이퍼파라미터 의미가 표처럼 정리된다.

print("=== Day 09-3: Roboflow 데이터셋 제작과 YOLOv8 학습 흐름 ===")

# 먼저 Roboflow에서 어떤 순서로 프로젝트를 만드는지 큰 흐름부터 보여 준다.
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

# data.yaml은 YOLO 학습의 시작점이라서 학생들이 구조를 꼭 알아야 한다.
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

# CLI 방식은 코랩이나 터미널에서 가장 빨리 실행할 수 있으므로 먼저 소개한다.
print("\n[실습 3] YOLOv8 CLI 학습 명령어 예시")
cli_command = (
    "yolo task=detect mode=train model=yolov8n.pt "
    "data=data.yaml epochs=50 imgsz=640 batch=16"
)
print(cli_command)

# Python 방식은 스크립트나 노트북에서 조금 더 유연하게 쓰기 좋다.
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

# 하이퍼파라미터가 무엇을 뜻하는지 미리 설명해 두면 실제 학습 명령어가 덜 낯설다.
print("\n[실습 5] 핵심 하이퍼파라미터 설명")
hyperparameters = {
    "model": "어떤 기본 가중치에서 시작할지 정합니다. 예: yolov8n.pt",
    "epochs": "데이터 전체를 몇 번 반복해서 학습할지 정합니다.",
    "imgsz": "입력 이미지 크기입니다. 보통 640을 많이 사용합니다.",
    "batch": "한 번에 몇 장씩 학습할지 정합니다.",
}
for key, value in hyperparameters.items():
    print(f"- {key}: {value}")

# 학습이 끝난 뒤 어떤 파일이 중요한지도 미리 알려 주면 프로젝트 마무리가 쉬워진다.
print("\n[실습 6] 학습 후 꼭 확인할 결과물")
print("- runs/detect/.../weights/best.pt : 가장 중요한 최종 가중치 파일")
print("- results.png : 학습 진행 그래프")
print("- confusion_matrix.png : 클래스별 오분류 확인 자료")

# 객체탐지 프로젝트가 실제로 어디서 완성되는지 연결해 주는 문장이다.
print("\n[실습 7] 오늘 핵심 정리")
print("Roboflow는 데이터 준비를, YOLOv8은 학습과 탐지를 담당합니다.")
print("즉 사용자 정의 객체탐지는 '라벨링 -> export -> 학습 -> best.pt 사용'의 흐름으로 완성됩니다.")