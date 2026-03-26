# 05_Edge_Detection.py
# 엣지 검출
# Canny, Sobel, Laplacian 등 다양한 엣지 검출 알고리즘을 학습합니다.
# 설치: pip install opencv-python numpy
# 실행: python 05_Edge_Detection.py

import cv2  # OpenCV 라이브러리
import numpy as np  # NumPy 라이브러리

print("OpenCV 엣지 검출")
print("=" * 50)

# ========== 샘플 이미지 생성 ==========

print("\n1. 샘플 이미지 생성")

# 엣지 검출을 위한 샘플 이미지 생성
sample_img = np.zeros((400, 600, 3), dtype=np.uint8)

# 흰색 배경
sample_img[:, :] = [255, 255, 255]

# 검은색 도형들 추가
cv2.rectangle(sample_img, (50, 50), (150, 150), (0, 0, 0), -1)    # 사각형
cv2.circle(sample_img, (300, 100), 50, (0, 0, 0), -1)             # 원
cv2.line(sample_img, (450, 50), (550, 150), (0, 0, 0), 3)         # 대각선
cv2.ellipse(sample_img, (150, 300), (80, 40), 45, 0, 360, (0, 0, 0), -1)  # 타원

# 텍스트 추가
cv2.putText(sample_img, 'EDGE DETECTION', (200, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

print("엣지 검출용 샘플 이미지를 생성했습니다.")

# 그레이스케일 변환
gray_img = cv2.cvtColor(sample_img, cv2.COLOR_BGR2GRAY)
print("그레이스케일로 변환했습니다.")

# ========== Sobel 엣지 검출 ==========

print("\n2. Sobel 엣지 검출")

# Sobel X 방향
sobelx = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=3)
sobelx_abs = cv2.convertScaleAbs(sobelx)

# Sobel Y 방향
sobely = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3)
sobely_abs = cv2.convertScaleAbs(sobely)

# Sobel X와 Y 결합
sobel_combined = cv2.addWeighted(sobelx_abs, 0.5, sobely_abs, 0.5, 0)

print("Sobel 필터로 엣지를 검출했습니다.")

# ========== Laplacian 엣지 검출 ==========

print("\n3. Laplacian 엣지 검출")

# Laplacian
laplacian = cv2.Laplacian(gray_img, cv2.CV_64F)
laplacian_abs = cv2.convertScaleAbs(laplacian)

print("Laplacian 필터로 엣지를 검출했습니다.")

# ========== Canny 엣지 검출 ==========

print("\n4. Canny 엣지 검출")

# Canny 엣지 검출
canny = cv2.Canny(gray_img, 100, 200)

print("Canny 알고리즘으로 엣지를 검출했습니다.")

# ========== Prewitt 필터 (커스텀) ==========

print("\n5. Prewitt 필터")

# Prewitt 커널 정의
kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=np.float32)
kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)

# Prewitt 필터 적용
prewittx = cv2.filter2D(gray_img, -1, kernelx)
prewitty = cv2.filter2D(gray_img, -1, kernely)
prewitt = cv2.addWeighted(prewittx, 0.5, prewitty, 0.5, 0)

print("Prewitt 필터로 엣지를 검출했습니다.")

# ========== 노이즈가 있는 이미지로 테스트 ==========

print("\n6. 노이즈가 있는 이미지 테스트")

# 가우시안 노이즈 추가
noise = np.random.normal(0, 25, gray_img.shape).astype(np.uint8)
noisy_img = cv2.add(gray_img, noise)

# 노이즈가 있는 이미지의 Canny 엣지 검출
canny_noisy = cv2.Canny(noisy_img, 100, 200)

# 블러 적용 후 엣지 검출
blurred = cv2.GaussianBlur(noisy_img, (5, 5), 0)
canny_blurred = cv2.Canny(blurred, 100, 200)

print("노이즈가 있는 이미지에서도 엣지 검출을 테스트했습니다.")

# ========== 결과 표시 ==========

print("\n7. 결과 표시")

# 모든 엣지 검출 결과를 표시
cv2.imshow('Original', sample_img)
cv2.imshow('Grayscale', gray_img)
cv2.imshow('Sobel X', sobelx_abs)
cv2.imshow('Sobel Y', sobely_abs)
cv2.imshow('Sobel Combined', sobel_combined)
cv2.imshow('Laplacian', laplacian_abs)
cv2.imshow('Canny', canny)
cv2.imshow('Prewitt', prewitt)
cv2.imshow('Noisy Image', noisy_img)
cv2.imshow('Canny on Noisy', canny_noisy)
cv2.imshow('Canny on Blurred', canny_blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ========== 이미지 저장 ==========

print("\n8. 이미지 저장")

cv2.imwrite('edge_original.jpg', sample_img)
cv2.imwrite('edge_grayscale.jpg', gray_img)
cv2.imwrite('edge_sobel_x.jpg', sobelx_abs)
cv2.imwrite('edge_sobel_y.jpg', sobely_abs)
cv2.imwrite('edge_sobel_combined.jpg', sobel_combined)
cv2.imwrite('edge_laplacian.jpg', laplacian_abs)
cv2.imwrite('edge_canny.jpg', canny)
cv2.imwrite('edge_prewitt.jpg', prewitt)
cv2.imwrite('edge_noisy.jpg', noisy_img)
cv2.imwrite('edge_canny_noisy.jpg', canny_noisy)
cv2.imwrite('edge_canny_blurred.jpg', canny_blurred)

print("모든 엣지 검출 결과를 이미지 파일로 저장했습니다.")

# ========== 미션 ==========
print("\n" + "="*50)
print("미션: 엣지 검출 실습")
print("1. Canny 엣지 검출의 임계값을 조절하여 결과를 비교해보세요.")
print("2. Sobel과 Laplacian의 결과를 비교해보세요.")
print("3. 노이즈가 있는 이미지에서 더 좋은 결과를 얻기 위한 방법을 찾아보세요.")
print("4. 자신만의 엣지 검출 필터를 만들어보세요.")

print("\n정답:")
print("""
import cv2
import numpy as np

# 샘플 이미지 로드 (이전 코드와 동일)

# 1. Canny 임계값 조절 비교
canny_low = cv2.Canny(gray_img, 50, 150)    # 낮은 임계값
canny_high = cv2.Canny(gray_img, 150, 250)  # 높은 임계값
canny_wide = cv2.Canny(gray_img, 50, 250)   # 넓은 범위

# 2. Sobel vs Laplacian 비교
# Sobel은 그라디언트 방향을 고려, Laplacian은 2차 미분
# Sobel이 더 부드럽고 Laplacian이 더 날카로운 엣지를 검출

# 3. 노이즈 처리 방법
# - 가우시안 블러 적용
# - 미디언 블러 적용
# - 양방향 필터 적용
blurred_gaussian = cv2.GaussianBlur(noisy_img, (3, 3), 0)
blurred_median = cv2.medianBlur(noisy_img, 3)
blurred_bilateral = cv2.bilateralFilter(noisy_img, 9, 75, 75)

canny_gaussian = cv2.Canny(blurred_gaussian, 100, 200)
canny_median = cv2.Canny(blurred_median, 100, 200)
canny_bilateral = cv2.Canny(blurred_bilateral, 100, 200)

# 4. 커스텀 엣지 검출 필터 (Roberts Cross)
roberts_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
roberts_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)

robertsx = cv2.filter2D(gray_img, -1, roberts_x)
robertsy = cv2.filter2D(gray_img, -1, roberts_y)
roberts = cv2.addWeighted(cv2.convertScaleAbs(robertsx), 0.5, cv2.convertScaleAbs(robertsy), 0.5, 0)

# 결과 표시
cv2.imshow('Canny Low', canny_low)
cv2.imshow('Canny High', canny_high)
cv2.imshow('Canny Wide', canny_wide)
cv2.imshow('Roberts Edge', roberts)
cv2.waitKey(0)
cv2.destroyAllWindows()
""")

print("\n다음 강의: 06_Face_Detection.py")