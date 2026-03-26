# Roboflow Object Detection Course

이 폴더는 `roboflow_object_detection` 전체 강의 자료를 담고 있습니다. 이 과정의 최종 목적은 데이터분석이 아니라 객체탐지입니다. 학생들은 Roboflow로 직접 데이터셋을 만들고, YOLOv8 이상 버전으로 학습한 뒤, 웹캠과 영상에서 원하는 물체를 탐지하는 프로젝트를 완성하게 됩니다.

## 핵심 특징
- 코랩 기준으로 이해하기 쉬운 실습 흐름을 사용합니다.
- 강사용 `.py` 파일에는 import 이유와 실습 이유가 주석으로 들어 있습니다.
- 학생용 `md`에는 복사해서 실행할 수 있는 코드 블록이 들어 있습니다.
- 과정 후반부는 객체탐지 프로젝트에 가장 큰 비중을 둡니다.
- Roboflow 데이터셋 제작, YOLOv8 학습, webcam / video inference까지 연결합니다.

## 주요 폴더
- `instructor_files`: 강사용 실습 코드와 강사용 대본
- `student_md`: 학생용 정리 자료
- `supplements`: 보충 실습 코드
- `supplement_md`: 보충 설명 자료
- `data`: 수업용 데이터 파일

## 객체탐지 핵심 흐름
1. Roboflow에서 이미지 업로드와 라벨링을 진행합니다.
2. YOLO 형식과 `data.yaml` 구조를 확인합니다.
3. YOLOv8 이상 버전으로 학습해 `best.pt`를 만듭니다.
4. `best.pt`로 웹캠과 영상에서 객체탐지를 실행합니다.
5. confidence, IoU, threshold를 조정하며 결과를 해석합니다.

자세한 날짜별 구성은 [Overview.md](/c:/detect_advance/roboflow_object_detection/Overview.md)에서 확인할 수 있습니다.