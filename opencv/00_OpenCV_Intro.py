# 00_OpenCV_Intro.py
# OpenCV 소개 및 설치
# OpenCV가 무엇인지, 왜 사용하는지, 어떻게 설치하는지 학습합니다.
# 설치: pip install opencv-python numpy
# 실행: python 00_OpenCV_Intro.py

import cv2  # OpenCV 라이브러리 임포트
import numpy as np  # NumPy 라이브러리 임포트

print("OpenCV 객체탐지 강의에 오신 것을 환영합니다!")
print("=" * 50)

# ========== NumPy 소개 ==========

print("\n0. NumPy란 무엇인가?")
print("- NumPy는 Numerical Python의 약자입니다.")
print("- 다차원 배열과 행렬 연산을 위한 파이썬 라이브러리입니다.")
print("- 과학 계산과 데이터 분석에 널리 사용됩니다.")

print("\n0-1. 왜 NumPy를 사용하는가?")
print("- OpenCV는 이미지를 NumPy 배열로 처리합니다.")
print("- NumPy 배열은 메모리 효율적이고 빠른 연산을 제공합니다.")
print("- 이미지 픽셀 값들을 효율적으로 저장하고 조작할 수 있습니다.")
print("- 수학적 연산(행렬 연산, 선형 대수 등)을 쉽게 수행할 수 있습니다.")

# ========== OpenCV 소개 ==========

print("\n1. OpenCV란 무엇인가?")
print("- OpenCV는 Open Source Computer Vision의 약자입니다.")
print("- 컴퓨터 비전과 머신러닝을 위한 오픈소스 라이브러리입니다.")
print("- 이미지와 비디오 처리를 위한 다양한 기능을 제공합니다.")

print("\n2. 왜 OpenCV를 사용하는가?")
print("- 무료로 사용할 수 있는 오픈소스 라이브러리입니다.")
print("- C++, Python, Java 등 다양한 언어를 지원합니다.")
print("- 실시간 이미지/비디오 처리가 가능합니다.")
print("- 객체 탐지, 얼굴 인식, 모션 추적 등 다양한 기능을 제공합니다.")

print("\n3. OpenCV의 주요 용도")
print("- 객체 탐지 (Object Detection)")
print("- 얼굴 인식 (Face Recognition)")
print("- 이미지 분류 (Image Classification)")
print("- 모션 추적 (Motion Tracking)")
print("- 증강 현실 (Augmented Reality)")

# ========== 버전 확인 ==========

print("\n4. OpenCV 버전 확인")
print(f"OpenCV 버전: {cv2.__version__}")
print(f"NumPy 버전: {np.__version__}")

# ========== 기본 기능 테스트 ==========

print("\n5. 기본 기능 테스트")

# 빈 이미지 생성 (검은색)
img = np.zeros((300, 400, 3), dtype=np.uint8)
print(f"생성된 이미지 크기: {img.shape}")  # (높이, 너비, 채널)

# 흰색 사각형 그리기
cv2.rectangle(img, (50, 50), (150, 150), (255, 255, 255), -1)
print("흰색 사각형을 그렸습니다.")

# 이미지 저장
cv2.imwrite('test_image.jpg', img)
print("test_image.jpg 파일로 저장되었습니다.")

print("\n6. 설치 확인 완료!")
print("OpenCV가 정상적으로 설치되었습니다.")

# ========== 미션 ==========
print("\n" + "="*50)
print("미션: OpenCV 설치 및 기본 기능 확인")
print("1. pip install opencv-python numpy 명령어로 설치하세요.")
print("2. 이 파일을 실행하여 버전 정보를 확인하세요.")
print("3. test_image.jpg 파일이 생성되었는지 확인하세요.")

print("\n정답:")
print("터미널에서 다음 명령어를 실행하세요:")
print("pip install opencv-python numpy")
print("python 00_OpenCV_Intro.py")

print("\n다음 강의: 01_Image_Basics.py")