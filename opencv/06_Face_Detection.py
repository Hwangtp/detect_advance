# 06_Face_Detection.py
# 얼굴 검출
# Haar Cascade 분류기를 사용하여 이미지에서 얼굴을 검출하는 방법을 학습합니다.
# 설치: pip install opencv-python numpy
# 실행: python 06_Face_Detection.py

import cv2  # OpenCV 라이브러리
import numpy as np  # NumPy 라이브러리

print("OpenCV 얼굴 검출")
print("=" * 50)

# ========== 샘플 이미지 생성 ==========

print("\n1. 샘플 이미지 생성")

# 얼굴이 있는 듯한 간단한 이미지 생성
sample_img = np.ones((400, 600, 3), dtype=np.uint8) * 255

# 얼굴 모양의 타원
cv2.ellipse(sample_img, (150, 200), (80, 100), 0, 0, 360, (0, 165, 255), -1)  # 얼굴
cv2.ellipse(sample_img, (130, 180), (25, 30), 0, 0, 360, (255, 255, 255), -1)  # 왼쪽 눈
cv2.ellipse(sample_img, (170, 180), (25, 30), 0, 0, 360, (255, 255, 255), -1)  # 오른쪽 눈
cv2.ellipse(sample_img, (130, 180), (10, 15), 0, 0, 360, (0, 0, 0), -1)       # 왼쪽 눈동자
cv2.ellipse(sample_img, (170, 180), (10, 15), 0, 0, 360, (0, 0, 0), -1)       # 오른쪽 눈동자
cv2.ellipse(sample_img, (150, 230), (15, 10), 0, 0, 360, (255, 0, 0), -1)     # 코
cv2.ellipse(sample_img, (150, 260), (30, 15), 0, 0, 360, (255, 0, 0), -1)     # 입

# 두 번째 얼굴
cv2.ellipse(sample_img, (450, 200), (70, 90), 0, 0, 360, (0, 200, 0), -1)     # 얼굴
cv2.ellipse(sample_img, (430, 180), (20, 25), 0, 0, 360, (255, 255, 255), -1)  # 왼쪽 눈
cv2.ellipse(sample_img, (470, 180), (20, 25), 0, 0, 360, (255, 255, 255), -1)  # 오른쪽 눈
cv2.ellipse(sample_img, (430, 180), (8, 12), 0, 0, 360, (0, 0, 0), -1)        # 왼쪽 눈동자
cv2.ellipse(sample_img, (470, 180), (8, 12), 0, 0, 360, (0, 0, 0), -1)        # 오른쪽 눈동자
cv2.ellipse(sample_img, (450, 220), (12, 8), 0, 0, 360, (255, 0, 0), -1)      # 코
cv2.ellipse(sample_img, (450, 250), (25, 12), 0, 0, 360, (255, 0, 0), -1)     # 입

print("간단한 얼굴 모양의 샘플 이미지를 생성했습니다.")

# ========== Haar Cascade 분류기 로드 ==========

print("\n2. Haar Cascade 분류기 로드")

# OpenCV에 내장된 얼굴 검출용 Haar Cascade 분류기 로드
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

if face_cascade.empty():
    print("얼굴 검출용 Haar Cascade 파일을 로드할 수 없습니다.")
else:
    print("얼굴 검출용 Haar Cascade 분류기를 로드했습니다.")

if eye_cascade.empty():
    print("눈 검출용 Haar Cascade 파일을 로드할 수 없습니다.")
else:
    print("눈 검출용 Haar Cascade 분류기를 로드했습니다.")

# ========== 얼굴 검출 적용 ==========

print("\n3. 얼굴 검출 적용")

# 그레이스케일 변환 (Haar Cascade는 그레이스케일에서 작동)
gray_img = cv2.cvtColor(sample_img, cv2.COLOR_BGR2GRAY)

# 얼굴 검출
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

print(f"검출된 얼굴 수: {len(faces)}")

# 검출된 얼굴에 사각형 그리기
for (x, y, w, h) in faces:
    cv2.rectangle(sample_img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray_img[y:y+h, x:x+w]
    roi_color = sample_img[y:y+h, x:x+w]

    # 얼굴 영역에서 눈 검출
    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=3, minSize=(10, 10))
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

print("얼굴과 눈에 사각형을 그렸습니다.")

# ========== 실시간 얼굴 검출 시뮬레이션 ==========

print("\n4. 실시간 얼굴 검출 시뮬레이션")

# 웹캠 대신 샘플 이미지들을 사용하여 실시간 효과 시뮬레이션
def detect_faces_in_image(image, title):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow(title, image)
    return len(faces)

# 여러 샘플 이미지 생성 및 검출
sample_images = []

# 이미지 1: 하나의 큰 얼굴
img1 = np.ones((300, 400, 3), dtype=np.uint8) * 255
cv2.ellipse(img1, (200, 150), (60, 80), 0, 0, 360, (0, 165, 255), -1)
sample_images.append(("Sample 1", img1))

# 이미지 2: 두 개의 작은 얼굴
img2 = np.ones((300, 400, 3), dtype=np.uint8) * 255
cv2.ellipse(img2, (120, 150), (40, 50), 0, 0, 360, (0, 165, 255), -1)
cv2.ellipse(img2, (280, 150), (40, 50), 0, 0, 360, (0, 200, 0), -1)
sample_images.append(("Sample 2", img2))

# 이미지 3: 얼굴이 없는 이미지
img3 = np.ones((300, 400, 3), dtype=np.uint8) * 255
cv2.putText(img3, 'No Face Here', (100, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
sample_images.append(("Sample 3", img3))

# 각 이미지에서 얼굴 검출
for title, img in sample_images:
    faces_count = detect_faces_in_image(img.copy(), title)
    print(f"{title}: {faces_count}개의 얼굴 검출")

cv2.waitKey(0)
cv2.destroyAllWindows()

# ========== 파라미터 조절 실험 ==========

print("\n5. 파라미터 조절 실험")

# scaleFactor와 minNeighbors의 영향 테스트
test_img = sample_img.copy()

# 엄격한 조건
faces_strict = face_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=10, minSize=(50, 50))
print(f"엄격한 조건: {len(faces_strict)}개의 얼굴")

# 느슨한 조건
faces_loose = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=2, minSize=(20, 20))
print(f"느슨한 조건: {len(faces_loose)}개의 얼굴")

# ========== 결과 표시 및 저장 ==========

print("\n6. 결과 표시 및 저장")

cv2.imshow('Face Detection Result', sample_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('face_detection_sample.jpg', sample_img)
print("얼굴 검출 결과를 face_detection_sample.jpg로 저장했습니다.")

# ========== 미션 ==========
print("\n" + "="*50)
print("미션: 얼굴 검출 실습")
print("1. scaleFactor와 minNeighbors 파라미터를 조절하여 검출 결과를 비교해보세요.")
print("2. minSize와 maxSize 파라미터를 사용하여 특정 크기의 얼굴만 검출해보세요.")
print("3. Haar Cascade 대신 LBP Cascade를 사용해보세요.")
print("4. 검출된 얼굴 영역을 저장하는 코드를 작성해보세요.")

print("\n정답:")
print("""
import cv2
import numpy as np

# 샘플 이미지 로드

# 1. 파라미터 조절 비교
gray = cv2.cvtColor(sample_img, cv2.COLOR_BGR2GRAY)

# 다양한 파라미터로 테스트
params = [
    (1.05, 2, "Loose"),
    (1.1, 5, "Default"),
    (1.3, 10, "Strict")
]

for scale, neighbors, name in params:
    faces = face_cascade.detectMultiScale(gray, scaleFactor=scale, minNeighbors=neighbors)
    print(f"{name}: {len(faces)} faces detected")

# 2. 크기 제한
faces_medium = face_cascade.detectMultiScale(gray, minSize=(50, 50), maxSize=(200, 200))
print(f"Medium size faces: {len(faces_medium)}")

# 3. LBP Cascade 사용 (더 빠르지만 정확도가 낮을 수 있음)
# lbp_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'lbpcascade_frontalface.xml')
# lbp_faces = lbp_face_cascade.detectMultiScale(gray, 1.1, 4)

# 4. 검출된 얼굴 영역 저장
faces = face_cascade.detectMultiScale(gray, 1.1, 5)
for i, (x, y, w, h) in enumerate(faces):
    face_roi = sample_img[y:y+h, x:x+w]
    cv2.imwrite(f'face_{i}.jpg', face_roi)
    print(f'Face {i} saved as face_{i}.jpg')
""")

print("\n다음 강의: 07_Haar_Cascades.py")