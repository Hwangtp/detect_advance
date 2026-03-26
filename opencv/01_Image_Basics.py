# 01_Image_Basics.py
# 이미지 읽기/쓰기/표시 기초
# OpenCV로 이미지를 불러오고, 표시하고, 저장하는 방법을 학습합니다.
# 설치: pip install opencv-python numpy
# 실행: python 01_Image_Basics.py

import cv2  # OpenCV 라이브러리
import numpy as np  # NumPy 라이브러리

print("OpenCV 이미지 기초 학습")
print("=" * 50)

# ========== 이미지 읽기 ==========

print("\n1. 이미지 읽기")

# 샘플 이미지 생성 (색종이처럼)
img = np.zeros((400, 600, 3), dtype=np.uint8)

# 빨간색 원 그리기
cv2.circle(img, (150, 200), 80, (0, 0, 255), -1)  # 빨간색

# 파란색 사각형 그리기
cv2.rectangle(img, (300, 100), (500, 300), (255, 0, 0), -1)  # 파란색

# 초록색 삼각형 그리기
pts = np.array([[450, 50], [550, 150], [350, 150]], np.int32)
cv2.fillPoly(img, [pts], (0, 255, 0))  # 초록색

print("샘플 이미지를 생성했습니다.")

# ========== 이미지 표시 ==========

print("\n2. 이미지 표시")

# 창 생성 및 이미지 표시
cv2.imshow('Sample Image', img)
print("이미지 창이 열렸습니다. 아무 키나 눌러 닫으세요.")

# 키 입력 대기 (0은 무한 대기)
cv2.waitKey(0)

# 모든 창 닫기
cv2.destroyAllWindows()
print("이미지 창을 닫았습니다.")

# ========== 이미지 저장 ==========

print("\n3. 이미지 저장")

# 이미지 파일로 저장
cv2.imwrite('sample_image.jpg', img)
print("sample_image.jpg 파일로 저장되었습니다.")

# ========== 이미지 정보 확인 ==========

print("\n4. 이미지 정보 확인")

# 이미지 크기 확인
height, width, channels = img.shape
print(f"이미지 높이: {height} 픽셀")
print(f"이미지 너비: {width} 픽셀")
print(f"색상 채널: {channels}개 (BGR)")

# 픽셀 값 확인 (좌상단 픽셀)
pixel = img[0, 0]  # [y, x] 좌표
print(f"좌상단 픽셀 값: {pixel}")  # [B, G, R]

# ========== 이미지 복사 및 수정 ==========

print("\n5. 이미지 복사 및 수정")

# 이미지 복사
img_copy = img.copy()

# 특정 영역을 노란색으로 변경
img_copy[50:150, 50:150] = [0, 255, 255]  # 노란색

# 수정된 이미지 표시
cv2.imshow('Modified Image', img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 수정된 이미지 저장
cv2.imwrite('modified_image.jpg', img_copy)
print("modified_image.jpg 파일로 저장되었습니다.")

# ========== 미션 ==========
print("\n" + "="*50)
print("미션: 이미지 기본 조작")
print("1. 새로운 이미지를 생성하고 빨간색 사각형을 그려보세요.")
print("2. 그린 이미지를 화면에 표시해보세요.")
print("3. 이미지를 파일로 저장해보세요.")
print("4. 이미지의 크기와 채널 정보를 출력해보세요.")

print("\n정답:")
print("""
import cv2
import numpy as np

# 1. 이미지 생성 및 사각형 그리기
img = np.zeros((300, 400, 3), dtype=np.uint8)
cv2.rectangle(img, (50, 50), (150, 150), (0, 0, 255), -1)

# 2. 이미지 표시
cv2.imshow('Red Rectangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. 이미지 저장
cv2.imwrite('red_rectangle.jpg', img)

# 4. 정보 출력
height, width, channels = img.shape
print(f"크기: {width}x{height}, 채널: {channels}")
""")

print("\n다음 강의: 02_Image_Processing.py")