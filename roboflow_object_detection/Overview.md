# roboflow_object_detection Overview

<div style="background: linear-gradient(135deg, #1d4ed8, #0f766e); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">과정 개요</h2>
  <p style="margin:0; line-height:1.8;">이 과정의 최종 목적은 데이터분석이 아니라 객체탐지입니다. 학생들은 Roboflow로 직접 데이터셋을 만들고, YOLOv8 이상 버전으로 학습한 뒤, 웹캠과 영상에서 물체를 탐지하는 흐름까지 완성하게 됩니다.</p>
</div>

## 이 과정의 핵심 목표
- 웹캠에서 물체를 실시간으로 탐지할 수 있다.
- 영상 파일에서도 같은 모델로 객체를 탐지할 수 있다.
- Roboflow를 사용해 사용자 정의 객체 데이터셋을 만들 수 있다.
- YOLOv8 이상 버전으로 사용자 정의 객체 탐지 모델을 학습할 수 있다.
- `best.pt`를 사용해 실제 프로젝트 결과를 실행할 수 있다.

## 폴더 구성
- `instructor_files`: 강사용 Python 파일과 강사용 대본
- `student_md`: 학생용 수업 정리 Markdown
- `supplements`: 보충 Python 자료
- `supplement_md`: 보충 Markdown 자료
- `data`: 코랩에서 바로 읽을 수 있는 고정 데이터

## 운영 방식
- `Day 00`은 코랩과 GPU 사용법을 소개하는 오리엔테이션입니다.
- 기본 운영은 하루 2개 파일이지만, 객체탐지 관련 구간은 필요하면 하루 3개 이상으로 확장합니다.
- 과정 후반부인 `Day 08 ~ Day 10`은 객체탐지 최종 프로젝트에 가장 큰 비중을 둡니다.
- 모든 `.py` 파일은 코랩 기준으로 이해하기 쉬운 경로와 실행 흐름을 사용합니다.

## 가장 중요한 흐름: 객체탐지 프로젝트
1. CNN과 객체탐지의 연결을 이해합니다.
2. 객체탐지와 이미지 분류의 차이를 이해합니다.
3. 탐지할 물체를 정하고 이미지를 수집합니다.
4. Roboflow에서 라벨링하고 train / valid / test 구조를 만듭니다.
5. YOLO 형식으로 export 하고 `data.yaml`을 준비합니다.
6. YOLOv8 이상 버전으로 학습하여 `best.pt`를 만듭니다.
7. `best.pt`를 사용해 웹캠 또는 영상에서 객체탐지를 실행합니다.
8. confidence, IoU, threshold를 조정해 결과를 개선합니다.

## 날짜별 흐름
0. Day 00: 코랩이 무엇인지, 왜 쓰는지, GPU를 왜 켜는지 이해하기
1. Day 01: AI / 머신러닝 / 딥러닝 관계 이해, 첫 분류 모델 만들기
2. Day 02: train/test split, 전처리와 스케일링 이해
3. Day 03: 회귀 기본, 회귀 지표 비교
4. Day 04: 로지스틱 분류, 확률과 threshold 이해
5. Day 05: 비지도학습, KMeans 군집
6. Day 06: MLP 기본, 하이퍼파라미터 비교
7. Day 07: 더 깊은 MLP, 모델 저장과 재사용
8. Day 08-1: CNN을 쉬운 글로 이해하기
9. Day 08-2: 이미지 데이터와 수동 합성곱
10. Day 08-3: sklearn으로 이미지 분류 맛보기
11. Day 08-4: 객체탐지 전체 목표와 최종 프로젝트 흐름
12. Day 09-1: 객체탐지 데이터셋 구조 이해
13. Day 09-2: YOLO 형식과 학습 준비 흐름
14. Day 09-3: Roboflow 사용자 정의 데이터셋 제작과 YOLOv8 학습
15. Day 10-1: IoU와 confidence 이해
16. Day 10-2: threshold와 탐지 평가 정리
17. Day 10-3: YOLOv8 웹캠 탐지와 영상 탐지 실행

## 객체탐지 강조 메모
- 이 과정의 중심 산출물은 표나 그래프가 아니라 `best.pt` 객체탐지 가중치입니다.
- 후반부 수업은 Roboflow, YOLOv8, webcam / video inference 흐름을 반복해서 연결합니다.
- 학생이 마지막에 말할 수 있어야 하는 문장은 "나는 직접 만든 데이터셋으로 웹캠과 영상에서 물체를 탐지할 수 있다"입니다.
