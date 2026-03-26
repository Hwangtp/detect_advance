# 07_Haar_Cascades.py
# Haar Cascade 고급
# Haar Cascade 분류기를 사용하여 다양한 객체를 검출하는 고급 기법을 학습합니다.
# 설치: pip install opencv-python numpy
# 실행: python 07_Haar_Cascades.py

import cv2  # OpenCV 라이브러리
import numpy as np  # NumPy 라이브러리

print("OpenCV Haar Cascade 고급")
print("=" * 50)

# ========== 샘플 이미지 생성 ==========

print("\n1. 샘플 이미지 생성")

# 다양한 객체가 있는 샘플 이미지 생성
sample_img = np.ones((500, 700, 3), dtype=np.uint8) * 255

# 자동차 모양 (간단한 사각형으로 표현)
cv2.rectangle(sample_img, (50, 200), (200, 350), (0, 0, 255), -1)  # 차체
cv2.rectangle(sample_img, (70, 220), (120, 270), (255, 255, 255), -1)  # 앞 유리
cv2.rectangle(sample_img, (140, 220), (180, 270), (255, 255, 255), -1)  # 뒷 유리
cv2.circle(sample_img, (80, 380), 20, (0, 0, 0), -1)  # 왼쪽 바퀴
cv2.circle(sample_img, (170, 380), 20, (0, 0, 0), -1)  # 오른쪽 바퀴

# 사람 모양 (간단한 스틱맨)
cv2.line(sample_img, (350, 200), (350, 300), (0, 0, 0), 3)  # 몸통
cv2.line(sample_img, (350, 230), (320, 260), (0, 0, 0), 3)  # 왼쪽 팔
cv2.line(sample_img, (350, 230), (380, 260), (0, 0, 0), 3)  # 오른쪽 팔
cv2.line(sample_img, (350, 300), (330, 350), (0, 0, 0), 3)  # 왼쪽 다리
cv2.line(sample_img, (350, 300), (370, 350), (0, 0, 0), 3)  # 오른쪽 다리
cv2.circle(sample_img, (350, 180), 20, (255, 200, 150), -1)  # 머리
cv2.circle(sample_img, (345, 175), (3), (0, 0, 0), -1)  # 왼쪽 눈
cv2.circle(sample_img, (355, 175), (3), (0, 0, 0), -1)  # 오른쪽 눈

# 책 모양
cv2.rectangle(sample_img, (500, 150), (600, 250), (139, 69, 19), -1)  # 책등
cv2.rectangle(sample_img, (480, 140), (500, 260), (210, 180, 140), -1)  # 책 페이지

# 시계 모양
cv2.circle(sample_img, (150, 100), 40, (0, 0, 0), 2)  # 시계 테두리
cv2.line(sample_img, (150, 100), (150, 70), (0, 0, 0), 2)  # 12시
cv2.line(sample_img, (150, 100), (170, 100), (0, 0, 0), 2)  # 3시
cv2.line(sample_img, (150, 100), (150, 130), (0, 0, 0), 2)  # 6시
cv2.line(sample_img, (150, 100), (130, 100), (0, 0, 0), 2)  # 9시

print("다양한 객체가 있는 샘플 이미지를 생성했습니다.")

# ========== 다양한 Haar Cascade 분류기 로드 ==========

print("\n2. 다양한 Haar Cascade 분류기 로드")

# 사용 가능한 Haar Cascade 분류기들
cascades = {
    'face': cv2.data.haarcascades + 'haarcascade_frontalface_default.xml',
    'eye': cv2.data.haarcascades + 'haarcascade_eye.xml',
    'smile': cv2.data.haarcascades + 'haarcascade_smile.xml',
    'upperbody': cv2.data.haarcascades + 'haarcascade_upperbody.xml',
    'fullbody': cv2.data.haarcascades + 'haarcascade_fullbody.xml',
    'car': cv2.data.haarcascades + 'haarcascade_car.xml',
}

# 분류기 로드
classifiers = {}
for name, path in cascades.items():
    classifier = cv2.CascadeClassifier(path)
    if classifier.empty():
        print(f"{name} 분류기를 로드할 수 없습니다: {path}")
    else:
        classifiers[name] = classifier
        print(f"{name} 분류기를 로드했습니다.")

# ========== 다중 객체 검출 ==========

print("\n3. 다중 객체 검출")

gray_img = cv2.cvtColor(sample_img, cv2.COLOR_BGR2GRAY)

# 각 분류기로 객체 검출
detection_results = {}

for name, classifier in classifiers.items():
    try:
        objects = classifier.detectMultiScale(
            gray_img,
            scaleFactor=1.1,
            minNeighbors=3,
            minSize=(20, 20),
            maxSize=(200, 200)
        )
        detection_results[name] = objects
        print(f"{name}: {len(objects)}개 검출")
    except:
        print(f"{name} 검출 중 오류 발생")
        detection_results[name] = []

# ========== 검출 결과 시각화 ==========

print("\n4. 검출 결과 시각화")

# 색상 정의
colors = {
    'face': (255, 0, 0),      # 파랑
    'eye': (0, 255, 0),       # 초록
    'smile': (0, 0, 255),     # 빨강
    'upperbody': (255, 255, 0), # 시안
    'fullbody': (255, 0, 255),  # 마젠타
    'car': (0, 255, 255),     # 노랑
}

result_img = sample_img.copy()

# 각 검출 결과에 사각형 그리기
for obj_type, objects in detection_results.items():
    color = colors.get(obj_type, (128, 128, 128))
    for (x, y, w, h) in objects:
        cv2.rectangle(result_img, (x, y), (x+w, y+h), color, 2)

        # 객체 타입 라벨 추가
        cv2.putText(result_img, obj_type, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

print("검출 결과를 시각화했습니다.")

# ========== 커스텀 Haar Cascade 시뮬레이션 ==========

print("\n5. 커스텀 Haar Cascade 시뮬레이션")

# 간단한 객체 검출을 위한 커스텀 로직 (실제로는 학습된 cascade 파일 필요)
def detect_custom_objects(image, min_size=(30, 30)):
    """커스텀 객체 검출 시뮬레이션"""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 엣지 검출로 후보 영역 찾기
    edges = cv2.Canny(gray, 50, 150)

    # 윤곽선 찾기
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    custom_objects = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w >= min_size[0] and h >= min_size[1]:
            custom_objects.append((x, y, w, h))

    return custom_objects

# 커스텀 객체 검출 적용
custom_objects = detect_custom_objects(sample_img)
print(f"커스텀 검출: {len(custom_objects)}개 객체")

# 커스텀 객체 표시
for (x, y, w, h) in custom_objects:
    cv2.rectangle(result_img, (x, y), (x+w, y+h), (128, 128, 128), 1)
    cv2.putText(result_img, 'custom', (x, y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (128, 128, 128), 1)

# ========== 성능 비교 ==========

print("\n6. 성능 비교")

import time

# 각 분류기의 성능 측정
performance_results = {}

for name, classifier in classifiers.items():
    start_time = time.time()
    try:
        objects = classifier.detectMultiScale(gray_img, 1.1, 3)
        end_time = time.time()
        performance_results[name] = {
            'time': end_time - start_time,
            'detections': len(objects)
        }
        print(".3f")
    except:
        performance_results[name] = {'time': 0, 'detections': 0}

# ========== 결과 표시 및 저장 ==========

print("\n7. 결과 표시 및 저장")

cv2.imshow('Original Sample', sample_img)
cv2.imshow('Detection Results', result_img)

# 검출 결과 텍스트 표시
info_img = np.ones((300, 400, 3), dtype=np.uint8) * 255
y_offset = 30

cv2.putText(info_img, 'Detection Results:', (10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
y_offset += 30

for obj_type, objects in detection_results.items():
    text = f'{obj_type}: {len(objects)} detected'
    cv2.putText(info_img, text, (10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    y_offset += 25

cv2.putText(info_img, f'Custom: {len(custom_objects)} detected', (10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (128, 128, 128), 1)

cv2.imshow('Detection Info', info_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 이미지 저장
cv2.imwrite('haar_cascade_sample.jpg', sample_img)
cv2.imwrite('haar_cascade_results.jpg', result_img)
cv2.imwrite('haar_cascade_info.jpg', info_img)

print("결과를 이미지 파일로 저장했습니다.")

# ========== 미션 ==========
print("\n" + "="*50)
print("미션: Haar Cascade 고급 실습")
print("1. 다른 Haar Cascade 분류기(코, 입, 몸통 등)를 로드하여 테스트해보세요.")
print("2. 검출 파라미터(scaleFactor, minNeighbors)를 최적화해보세요.")
print("3. 여러 객체 타입을 동시에 검출하는 함수를 만들어보세요.")
print("4. 검출 결과를 JSON 형식으로 저장하는 코드를 작성해보세요.")

print("\n정답:")
print("""
import cv2
import numpy as np
import json

# 1. 추가 Haar Cascade 분류기 로드
nose_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_mcs_nose.xml')
mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_mcs_mouth.xml')

# 2. 파라미터 최적화
def optimize_detection(image, classifier, param_grid):
    best_params = None
    best_detections = 0

    for scale in param_grid['scaleFactor']:
        for neighbors in param_grid['minNeighbors']:
            detections = classifier.detectMultiScale(image, scale, neighbors)
            if len(detections) > best_detections:
                best_detections = len(detections)
                best_params = {'scaleFactor': scale, 'minNeighbors': neighbors}

    return best_params, best_detections

# 3. 다중 객체 검출 함수
def detect_multiple_objects(image, classifiers):
    results = {}
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    for name, classifier in classifiers.items():
        objects = classifier.detectMultiScale(gray, 1.1, 4)
        results[name] = [{'x': int(x), 'y': int(y), 'w': int(w), 'h': int(h)} for x, y, w, h in objects]

    return results

# 4. JSON으로 결과 저장
detection_results = detect_multiple_objects(sample_img, classifiers)
with open('detection_results.json', 'w') as f:
    json.dump(detection_results, f, indent=2)

print("Detection results saved to detection_results.json")
""")

print("\n다음 강의: 08_YOLO_Detection.py")