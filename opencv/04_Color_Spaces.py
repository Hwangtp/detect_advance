# 04_Color_Spaces.py
# 색 공간 변환
# BGR, HSV, 그레이스케일 등 다양한 색 공간으로 변환하는 방법을 학습합니다.
# 설치: pip install opencv-python numpy
# 실행: python 04_Color_Spaces.py

import cv2  # OpenCV 라이브러리
import numpy as np  # NumPy 라이브러리

print("OpenCV 색 공간 변환")
print("=" * 50)

# ========== 샘플 이미지 생성 ==========

print("\n1. 샘플 이미지 생성")

# 다양한 색상을 가진 이미지 생성
sample_img = np.zeros((300, 400, 3), dtype=np.uint8)

# 빨간색 영역
sample_img[0:100, 0:133] = [0, 0, 255]  # BGR: 파랑, 초록, 빨강

# 초록색 영역
sample_img[0:100, 133:266] = [0, 255, 0]

# 파란색 영역
sample_img[0:100, 266:400] = [255, 0, 0]

# 노란색 영역
sample_img[100:200, 0:133] = [0, 255, 255]

# 마젠타 영역
sample_img[100:200, 133:266] = [255, 0, 255]

# 시안 영역
sample_img[100:200, 266:400] = [255, 255, 0]

# 흰색과 검은색 영역
sample_img[200:300, 0:200] = [255, 255, 255]  # 흰색
sample_img[200:300, 200:400] = [0, 0, 0]       # 검은색

print("다양한 색상을 가진 샘플 이미지를 생성했습니다.")

# ========== BGR에서 그레이스케일로 변환 ==========

print("\n2. BGR에서 그레이스케일로 변환")

# 그레이스케일 변환
gray_img = cv2.cvtColor(sample_img, cv2.COLOR_BGR2GRAY)
print("BGR 이미지를 그레이스케일로 변환했습니다.")

# ========== BGR에서 HSV로 변환 ==========

print("\n3. BGR에서 HSV로 변환")

# HSV 변환
hsv_img = cv2.cvtColor(sample_img, cv2.COLOR_BGR2HSV)
print("BGR 이미지를 HSV로 변환했습니다.")

# HSV 채널 분리
h, s, v = cv2.split(hsv_img)
print("HSV 채널을 분리했습니다 (H: 색상, S: 채도, V: 명도)")

# ========== 색상 범위로 마스크 생성 ==========

print("\n4. 색상 범위로 마스크 생성")

# 빨간색 범위 정의 (HSV)
lower_red1 = np.array([0, 50, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 50, 50])
upper_red2 = np.array([180, 255, 255])

# 빨간색 마스크 생성
mask_red1 = cv2.inRange(hsv_img, lower_red1, upper_red1)
mask_red2 = cv2.inRange(hsv_img, lower_red2, upper_red2)
mask_red = cv2.bitwise_or(mask_red1, mask_red2)

print("빨간색 범위의 마스크를 생성했습니다.")

# 초록색 범위 정의
lower_green = np.array([40, 50, 50])
upper_green = np.array([80, 255, 255])

# 초록색 마스크 생성
mask_green = cv2.inRange(hsv_img, lower_green, upper_green)
print("초록색 범위의 마스크를 생성했습니다.")

# ========== 마스크 적용 ==========

print("\n5. 마스크 적용")

# 원본 이미지에 마스크 적용
red_result = cv2.bitwise_and(sample_img, sample_img, mask=mask_red)
green_result = cv2.bitwise_and(sample_img, sample_img, mask=mask_green)

print("마스크를 적용하여 특정 색상만 추출했습니다.")

# ========== RGB 색 공간 변환 ==========

print("\n6. RGB 색 공간 변환")

# BGR에서 RGB로 변환
rgb_img = cv2.cvtColor(sample_img, cv2.COLOR_BGR2RGB)
print("BGR을 RGB로 변환했습니다.")

# ========== YUV 색 공간 변환 ==========

print("\n7. YUV 색 공간 변환")

# BGR에서 YUV로 변환
yuv_img = cv2.cvtColor(sample_img, cv2.COLOR_BGR2YUV)
print("BGR을 YUV로 변환했습니다.")

# ========== 결과 표시 ==========

print("\n8. 결과 표시")

# 모든 이미지를 하나의 창에 표시하기 위한 함수
def show_images(images, titles, rows=2, cols=4):
    fig, axes = plt.subplots(rows, cols, figsize=(15, 8))
    axes = axes.ravel()

    for i, (img, title) in enumerate(zip(images, titles)):
        if len(img.shape) == 2:  # 그레이스케일
            axes[i].imshow(img, cmap='gray')
        else:  # 컬러
            axes[i].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        axes[i].set_title(title)
        axes[i].axis('off')

    plt.tight_layout()
    plt.show()

# matplotlib이 설치되어 있지 않을 수 있으므로 OpenCV로 표시
cv2.imshow('Original BGR', sample_img)
cv2.imshow('Grayscale', gray_img)
cv2.imshow('HSV', hsv_img)
cv2.imshow('Red Mask', mask_red)
cv2.imshow('Green Mask', mask_green)
cv2.imshow('Red Extracted', red_result)
cv2.imshow('Green Extracted', green_result)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ========== 이미지 저장 ==========

print("\n9. 이미지 저장")

cv2.imwrite('color_spaces_original.jpg', sample_img)
cv2.imwrite('color_spaces_gray.jpg', gray_img)
cv2.imwrite('color_spaces_hsv.jpg', hsv_img)
cv2.imwrite('color_spaces_red_mask.jpg', mask_red)
cv2.imwrite('color_spaces_green_mask.jpg', mask_green)
cv2.imwrite('color_spaces_red_extracted.jpg', red_result)
cv2.imwrite('color_spaces_green_extracted.jpg', green_result)

print("모든 변환 결과를 이미지 파일로 저장했습니다.")

# ========== 미션 ==========
print("\n" + "="*50)
print("미션: 색 공간 변환 실습")
print("1. 파란색 물체를 검출하는 마스크를 만들어보세요.")
print("2. 노란색과 파란색을 동시에 검출해보세요.")
print("3. HSV 채널을 분리하여 각 채널을 확인해보세요.")
print("4. 그레이스케일 이미지를 다시 BGR로 변환해보세요.")

print("\n정답:")
print("""
import cv2
import numpy as np

# 샘플 이미지 생성 (이전 코드와 동일)

# 1. 파란색 물체 검출
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])
mask_blue = cv2.inRange(hsv_img, lower_blue, upper_blue)
blue_result = cv2.bitwise_and(sample_img, sample_img, mask=mask_blue)

# 2. 노란색과 파란색 동시에 검출
lower_yellow = np.array([20, 50, 50])
upper_yellow = np.array([40, 255, 255])
mask_yellow = cv2.inRange(hsv_img, lower_yellow, upper_yellow)
mask_both = cv2.bitwise_or(mask_blue, mask_yellow)
both_result = cv2.bitwise_and(sample_img, sample_img, mask=mask_both)

# 3. HSV 채널 분리 및 표시
h, s, v = cv2.split(hsv_img)
cv2.imshow('Hue', h)
cv2.imshow('Saturation', s)
cv2.imshow('Value', v)

# 4. 그레이스케일에서 BGR로 변환
gray_to_bgr = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)

# 결과 표시
cv2.imshow('Blue Extracted', blue_result)
cv2.imshow('Yellow and Blue', both_result)
cv2.imshow('Gray to BGR', gray_to_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
""")

print("\n다음 강의: 05_Edge_Detection.py")