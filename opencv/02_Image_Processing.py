# 02_Image_Processing.py
# 기본 이미지 처리
# 이미지 크기 조절, 회전, 반전 등 기본적인 이미지 처리를 학습합니다.
# 설치: pip install opencv-python numpy
# 실행: python 02_Image_Processing.py

import cv2  # OpenCV 라이브러리
import numpy as np  # NumPy 라이브러리

print("OpenCV 기본 이미지 처리")
print("=" * 50)

# ========== 샘플 이미지 생성 ==========

print("\n1. 샘플 이미지 생성")

# 기본 이미지 생성
img = np.zeros((300, 400, 3), dtype=np.uint8)

# 여러 색상의 도형 그리기
cv2.rectangle(img, (50, 50), (150, 100), (255, 0, 0), -1)    # 파란색
cv2.circle(img, (200, 150), 40, (0, 255, 0), -1)             # 초록색
cv2.rectangle(img, (250, 200), (350, 250), (0, 0, 255), -1)  # 빨간색

print("샘플 이미지를 생성했습니다.")

# ========== 이미지 크기 조절 ==========

print("\n2. 이미지 크기 조절")

# 이미지 표시 (원본)
cv2.imshow('Original', img)
cv2.waitKey(1000)  # 1초 대기

# 크기 확대 (2배)
resized_up = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Resized Up', resized_up)
cv2.waitKey(1000)

# 크기 축소 (0.5배)
resized_down = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Resized Down', resized_down)
cv2.waitKey(1000)

# 특정 크기로 조절
resized_specific = cv2.resize(img, (200, 150))  # 200x150으로 조절
cv2.imshow('Resized Specific', resized_specific)
cv2.waitKey(1000)

print("이미지 크기 조절을 완료했습니다.")

# ========== 이미지 회전 ==========

print("\n3. 이미지 회전")

# 회전 중심점 계산
height, width = img.shape[:2]
center = (width // 2, height // 2)

# 45도 회전
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_45 = cv2.warpAffine(img, rotation_matrix, (width, height))
cv2.imshow('Rotated 45 degrees', rotated_45)
cv2.waitKey(1000)

# 90도 회전
rotation_matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated_90 = cv2.warpAffine(img, rotation_matrix, (width, height))
cv2.imshow('Rotated 90 degrees', rotated_90)
cv2.waitKey(1000)

print("이미지 회전을 완료했습니다.")

# ========== 이미지 반전 ==========

print("\n4. 이미지 반전")

# 좌우 반전
flipped_horizontal = cv2.flip(img, 1)
cv2.imshow('Flipped Horizontal', flipped_horizontal)
cv2.waitKey(1000)

# 상하 반전
flipped_vertical = cv2.flip(img, 0)
cv2.imshow('Flipped Vertical', flipped_vertical)
cv2.waitKey(1000)

# 상하좌우 반전
flipped_both = cv2.flip(img, -1)
cv2.imshow('Flipped Both', flipped_both)
cv2.waitKey(1000)

print("이미지 반전을 완료했습니다.")

# ========== 이미지 자르기 ==========

print("\n5. 이미지 자르기")

# 관심 영역(ROI) 설정
roi = img[50:200, 100:300]  # [y1:y2, x1:x2]
cv2.imshow('ROI', roi)
cv2.waitKey(1000)

# 자른 영역을 다른 위치에 붙이기
img_copy = img.copy()
img_copy[50:200, 50:250] = roi
cv2.imshow('Pasted ROI', img_copy)
cv2.waitKey(1000)

print("이미지 자르기를 완료했습니다.")

# ========== 모든 창 닫기 ==========

cv2.destroyAllWindows()
print("\n모든 처리가 완료되었습니다.")

# ========== 미션 ==========
print("\n" + "="*50)
print("미션: 이미지 처리 실습")
print("1. 이미지를 1.5배로 확대해보세요.")
print("2. 이미지를 30도 회전해보세요.")
print("3. 이미지의 중앙 부분을 잘라내세요.")
print("4. 잘라낸 부분을 다른 위치에 붙여보세요.")

print("\n정답:")
print("""
import cv2
import numpy as np

# 샘플 이미지 생성
img = np.zeros((300, 400, 3), dtype=np.uint8)
cv2.rectangle(img, (50, 50), (150, 100), (255, 0, 0), -1)

# 1. 1.5배 확대
resized = cv2.resize(img, None, fx=1.5, fy=1.5)
cv2.imshow('1.5x', resized)
cv2.waitKey(0)

# 2. 30도 회전
h, w = img.shape[:2]
center = (w//2, h//2)
matrix = cv2.getRotationMatrix2D(center, 30, 1.0)
rotated = cv2.warpAffine(img, matrix, (w, h))
cv2.imshow('Rotated 30', rotated)
cv2.waitKey(0)

# 3. 중앙 부분 자르기
roi = img[75:225, 100:300]
cv2.imshow('ROI', roi)
cv2.waitKey(0)

# 4. 다른 위치에 붙이기
img_copy = img.copy()
img_copy[0:150, 0:200] = roi
cv2.imshow('Pasted', img_copy)
cv2.waitKey(0)

cv2.destroyAllWindows()
""")

print("\n다음 강의: 03_Drawing_Shapes.py")