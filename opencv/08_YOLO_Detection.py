# 08_YOLO_Detection.py
# YOLO 객체 검출
# YOLO(You Only Look Once) 알고리즘을 사용하여 실시간 객체 검출을 학습합니다.
# 설치: pip install opencv-python numpy
# 실행: python 08_YOLO_Detection.py

import cv2  # OpenCV 라이브러리
import numpy as np  # NumPy 라이브러리

print("OpenCV YOLO 객체 검출")
print("=" * 50)

# ========== YOLO 모델 파일 경로 설정 ==========

print("\n1. YOLO 모델 설정")

# YOLOv3 모델 파일들 (OpenCV의 dnn 모듈에서 제공하는 예제 모델)
# 실제 사용시에는 공식 YOLO 모델 파일들을 다운로드해야 합니다.
config_path = cv2.data.dnn + 'yolov3.cfg' if hasattr(cv2.data, 'dnn') else None
weights_path = cv2.data.dnn + 'yolov3.weights' if hasattr(cv2.data, 'dnn') else None

# COCO 데이터셋 클래스 이름들
classes = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
           "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
           "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack",
           "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball",
           "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket",
           "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
           "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake",
           "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop",
           "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink",
           "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]

print(f"COCO 데이터셋 클래스 수: {len(classes)}")

# ========== 샘플 이미지 생성 ==========

print("\n2. 샘플 이미지 생성")

# YOLO 검출을 시뮬레이션할 샘플 이미지 생성
sample_img = np.ones((600, 800, 3), dtype=np.uint8) * 255

# 사람 모양
cv2.rectangle(sample_img, (100, 200), (180, 400), (255, 200, 150), -1)  # 몸통
cv2.circle(sample_img, (140, 160), 25, (255, 200, 150), -1)  # 머리
cv2.putText(sample_img, 'person', (100, 190), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

# 자동차 모양
cv2.rectangle(sample_img, (300, 250), (500, 350), (0, 0, 255), -1)  # 차체
cv2.rectangle(sample_img, (320, 270), (380, 320), (255, 255, 255), -1)  # 앞 유리
cv2.circle(sample_img, (340, 380), 20, (0, 0, 0), -1)  # 왼쪽 바퀴
cv2.circle(sample_img, (460, 380), 20, (0, 0, 0), -1)  # 오른쪽 바퀴
cv2.putText(sample_img, 'car', (300, 240), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

# 개 모양
cv2.ellipse(sample_img, (650, 300), (40, 30), 0, 0, 360, (139, 69, 19), -1)  # 몸통
cv2.circle(sample_img, (630, 270), 15, (139, 69, 19), -1)  # 머리
cv2.putText(sample_img, 'dog', (610, 260), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

# 의자 모양
cv2.rectangle(sample_img, (50, 450), (150, 550), (139, 69, 19), -1)  # 의자 등받이
cv2.rectangle(sample_img, (50, 550), (150, 570), (139, 69, 19), -1)  # 의자 좌석
cv2.putText(sample_img, 'chair', (50, 440), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

print("샘플 이미지에 다양한 객체를 그렸습니다.")

# ========== YOLO 시뮬레이션 ==========

print("\n3. YOLO 검출 시뮬레이션")

def simulate_yolo_detection(image):
    """YOLO 검출을 시뮬레이션하는 함수"""
    detections = []

    # 사람 검출 시뮬레이션
    person_conf = 0.85
    detections.append({
        'class_id': 0,  # person
        'confidence': person_conf,
        'bbox': [100, 200, 80, 200]  # x, y, w, h
    })

    # 자동차 검출 시뮬레이션
    car_conf = 0.92
    detections.append({
        'class_id': 2,  # car
        'confidence': car_conf,
        'bbox': [300, 250, 200, 100]
    })

    # 개 검출 시뮬레이션
    dog_conf = 0.78
    detections.append({
        'class_id': 16,  # dog
        'confidence': dog_conf,
        'bbox': [610, 270, 80, 60]
    })

    # 의자 검출 시뮬레이션
    chair_conf = 0.65
    detections.append({
        'class_id': 56,  # chair
        'confidence': chair_conf,
        'bbox': [50, 450, 100, 120]
    })

    return detections

# YOLO 검출 시뮬레이션 실행
detections = simulate_yolo_detection(sample_img)
print(f"시뮬레이션된 검출 수: {len(detections)}")

# ========== NMS (Non-Maximum Suppression) 시뮬레이션 ==========

print("\n4. NMS 적용")

def apply_nms(detections, iou_threshold=0.4):
    """NMS를 적용하는 함수"""
    if len(detections) == 0:
        return []

    # confidence로 정렬
    detections = sorted(detections, key=lambda x: x['confidence'], reverse=True)

    kept_detections = []

    while len(detections) > 0:
        # 가장 confidence가 높은 detection 선택
        best = detections.pop(0)
        kept_detections.append(best)

        # IoU 계산하여 겹치는 박스 제거
        remaining = []
        for det in detections:
            if calculate_iou(best['bbox'], det['bbox']) < iou_threshold:
                remaining.append(det)

        detections = remaining

    return kept_detections

def calculate_iou(box1, box2):
    """두 바운딩 박스의 IoU 계산"""
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2

    # 좌표 변환
    x1_min, y1_min = x1, y1
    x1_max, y1_max = x1 + w1, y1 + h1
    x2_min, y2_min = x2, y2
    x2_max, y2_max = x2 + w2, y2 + h2

    # 교집합 영역 계산
    inter_x_min = max(x1_min, x2_min)
    inter_y_min = max(y1_min, y2_min)
    inter_x_max = min(x1_max, x2_max)
    inter_y_max = min(y1_max, y2_max)

    inter_area = max(0, inter_x_max - inter_x_min) * max(0, inter_y_max - inter_y_min)

    # 합집합 영역 계산
    box1_area = w1 * h1
    box2_area = w2 * h2
    union_area = box1_area + box2_area - inter_area

    if union_area == 0:
        return 0

    return inter_area / union_area

# NMS 적용
nms_detections = apply_nms(detections, iou_threshold=0.3)
print(f"NMS 후 검출 수: {len(nms_detections)}")

# ========== 검출 결과 시각화 ==========

print("\n5. 검출 결과 시각화")

# 색상 맵
colors = np.random.uniform(0, 255, size=(len(classes), 3))

result_img = sample_img.copy()

for detection in nms_detections:
    class_id = detection['class_id']
    confidence = detection['confidence']
    bbox = detection['bbox']

    x, y, w, h = bbox
    x, y, w, h = int(x), int(y), int(w), int(h)

    # 바운딩 박스 그리기
    color = colors[class_id]
    cv2.rectangle(result_img, (x, y), (x + w, y + h), color, 2)

    # 클래스 이름과 confidence 표시
    class_name = classes[class_id] if class_id < len(classes) else f"class_{class_id}"
    label = ".2f"

    # 텍스트 배경
    (text_width, text_height), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
    cv2.rectangle(result_img, (x, y - text_height - 10), (x + text_width, y), color, -1)

    # 텍스트
    cv2.putText(result_img, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

print("검출 결과를 시각화했습니다.")

# ========== 실시간 검출 시뮬레이션 ==========

print("\n6. 실시간 검출 시뮬레이션")

def simulate_realtime_detection():
    """실시간 검출을 시뮬레이션"""
    # 여러 프레임 생성
    frames = []

    # 프레임 1: 기본 장면
    frame1 = sample_img.copy()
    frames.append(("Frame 1", frame1))

    # 프레임 2: 객체 이동
    frame2 = np.ones((600, 800, 3), dtype=np.uint8) * 255
    # 이동된 사람
    cv2.rectangle(frame2, (150, 200), (230, 400), (255, 200, 150), -1)
    cv2.circle(frame2, (190, 160), 25, (255, 200, 150), -1)
    cv2.putText(frame2, 'person', (150, 190), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    # 같은 자동차
    cv2.rectangle(frame2, (300, 250), (500, 350), (0, 0, 255), -1)
    cv2.rectangle(frame2, (320, 270), (380, 320), (255, 255, 255), -1)
    cv2.circle(frame2, (340, 380), 20, (0, 0, 0), -1)
    cv2.circle(frame2, (460, 380), 20, (0, 0, 0), -1)
    cv2.putText(frame2, 'car', (300, 240), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    frames.append(("Frame 2", frame2))

    # 각 프레임에 대해 검출 수행
    for frame_name, frame in frames:
        frame_detections = simulate_yolo_detection(frame)
        frame_nms = apply_nms(frame_detections)

        # 결과 시각화
        frame_result = frame.copy()
        for detection in frame_nms:
            class_id = detection['class_id']
            confidence = detection['confidence']
            bbox = detection['bbox']

            x, y, w, h = bbox
            x, y, w, h = int(x), int(y), int(w), int(h)

            color = colors[class_id]
            cv2.rectangle(frame_result, (x, y), (x + w, y + h), color, 2)

            class_name = classes[class_id] if class_id < len(classes) else f"class_{class_id}"
            label = ".2f"

            (text_width, text_height), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
            cv2.rectangle(frame_result, (x, y - text_height - 10), (x + text_width, y), color, -1)
            cv2.putText(frame_result, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        cv2.imshow(frame_name, frame_result)
        print(f"{frame_name}: {len(frame_nms)} objects detected")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

simulate_realtime_detection()

# ========== 결과 저장 ==========

print("\n7. 결과 저장")

cv2.imwrite('yolo_sample.jpg', sample_img)
cv2.imwrite('yolo_detection_result.jpg', result_img)

print("YOLO 검출 결과를 이미지 파일로 저장했습니다.")

# ========== 미션 ==========
print("\n" + "="*50)
print("미션: YOLO 객체 검출 실습")
print("1. confidence 임계값을 조절하여 검출 결과를 비교해보세요.")
print("2. IoU 임계값을 변경하여 NMS 결과를 확인해보세요.")
print("3. 특정 클래스만 필터링하여 표시하는 함수를 만들어보세요.")
print("4. 검출 결과를 CSV 파일로 저장하는 코드를 작성해보세요.")

print("\n정답:")
print("""
import cv2
import numpy as np
import csv

# 1. confidence 임계값 조절
def filter_by_confidence(detections, threshold=0.5):
    return [d for d in detections if d['confidence'] >= threshold]

# 다양한 임계값으로 테스트
for threshold in [0.3, 0.5, 0.7, 0.9]:
    filtered = filter_by_confidence(detections, threshold)
    print(f"Threshold {threshold}: {len(filtered)} detections")

# 2. IoU 임계값 변경
for iou_thresh in [0.1, 0.3, 0.5, 0.7]:
    nms_result = apply_nms(detections, iou_threshold=iou_thresh)
    print(f"IoU {iou_thresh}: {len(nms_result)} detections after NMS")

# 3. 특정 클래스 필터링
def filter_by_class(detections, target_classes):
    return [d for d in detections if classes[d['class_id']] in target_classes]

# 사람과 자동차만 필터링
person_car = filter_by_class(detections, ['person', 'car'])
print(f"Person/Car only: {len(person_car)} detections")

# 4. CSV로 결과 저장
def save_detections_to_csv(detections, filename='detections.csv'):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['class_name', 'confidence', 'x', 'y', 'width', 'height']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for detection in detections:
            class_name = classes[detection['class_id']]
            x, y, w, h = detection['bbox']
            writer.writerow({
                'class_name': class_name,
                'confidence': detection['confidence'],
                'x': x, 'y': y, 'width': w, 'height': h
            })

save_detections_to_csv(nms_detections)
print("Detections saved to detections.csv")
""")

print("\n다음 강의: 09_Bounding_Boxes.py")