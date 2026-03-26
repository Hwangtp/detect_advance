# 03_Drawing_Shapes.py
# 도형 그리기
# OpenCV로 선, 사각형, 원, 타원, 다각형 등 다양한 도형을 그리는 방법을 학습합니다.
# 설치: pip install opencv-python numpy
# 실행: python 03_Drawing_Shapes.py

import cv2  # OpenCV 라이브러리
import numpy as np  # NumPy 라이브러리

print("OpenCV 도형 그리기")
print("=" * 50)

# ========== 캔버스 생성 ==========

print("\n1. 캔버스 생성")

# 흰색 배경의 캔버스 생성
canvas = np.ones((500, 700, 3), dtype=np.uint8) * 255
print("700x500 크기의 흰색 캔버스를 생성했습니다.")

# ========== 선 그리기 ==========

print("\n2. 선 그리기")

# 기본 선 그리기
cv2.line(canvas, (50, 50), (200, 50), (255, 0, 0), 2)  # 파란색 선
cv2.line(canvas, (50, 80), (200, 80), (0, 255, 0), 4)  # 초록색 선 (두껍게)
cv2.line(canvas, (50, 110), (200, 110), (0, 0, 255), 1)  # 빨간색 선 (얇게)

# 대각선 그리기
cv2.line(canvas, (50, 140), (200, 190), (0, 0, 0), 2)  # 검은색 대각선

print("여러 종류의 선을 그렸습니다.")

# ========== 사각형 그리기 ==========

print("\n3. 사각형 그리기")

# 채워진 사각형
cv2.rectangle(canvas, (250, 50), (350, 100), (255, 0, 0), -1)  # 파란색 채움

# 빈 사각형
cv2.rectangle(canvas, (250, 120), (350, 170), (0, 255, 0), 3)  # 초록색 테두리

# 둥근 모서리 사각형 (사실은 그냥 사각형)
cv2.rectangle(canvas, (250, 190), (350, 240), (0, 0, 255), 2)  # 빨간색 테두리

print("여러 종류의 사각형을 그렸습니다.")

# ========== 원 그리기 ==========

print("\n4. 원 그리기")

# 채워진 원
cv2.circle(canvas, (450, 75), 25, (255, 0, 0), -1)  # 파란색 채움

# 빈 원
cv2.circle(canvas, (450, 150), 25, (0, 255, 0), 3)  # 초록색 테두리

# 두꺼운 테두리의 원
cv2.circle(canvas, (450, 225), 25, (0, 0, 255), 5)  # 빨간색 두꺼운 테두리

print("여러 종류의 원을 그렸습니다.")

# ========== 타원 그리기 ==========

print("\n5. 타원 그리기")

# 기본 타원
cv2.ellipse(canvas, (100, 300), (60, 30), 0, 0, 360, (255, 0, 0), 2)  # 파란색

# 회전된 타원
cv2.ellipse(canvas, (250, 300), (60, 30), 45, 0, 360, (0, 255, 0), 2)  # 초록색, 45도 회전

# 부분 타원 (반원)
cv2.ellipse(canvas, (400, 300), (60, 30), 0, 0, 180, (0, 0, 255), 2)  # 빨간색, 반원

print("여러 종류의 타원을 그렸습니다.")

# ========== 다각형 그리기 ==========

print("\n6. 다각형 그리기")

# 삼각형
triangle_pts = np.array([[550, 270], [600, 320], [500, 320]], np.int32)
cv2.fillPoly(canvas, [triangle_pts], (255, 0, 0))  # 파란색 채움

# 오각형
pentagon_pts = np.array([[100, 400], [130, 370], [160, 370], [170, 400], [140, 420]], np.int32)
cv2.polylines(canvas, [pentagon_pts], True, (0, 255, 0), 2)  # 초록색 테두리

# 육각형
hexagon_pts = np.array([[250, 380], [280, 370], [310, 380], [310, 410], [280, 420], [250, 410]], np.int32)
cv2.fillPoly(canvas, [hexagon_pts], (0, 0, 255))  # 빨간색 채움

print("여러 종류의 다각형을 그렸습니다.")

# ========== 텍스트 쓰기 ==========

print("\n7. 텍스트 쓰기")

# 텍스트 추가
cv2.putText(canvas, 'OpenCV Drawing', (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv2.putText(canvas, 'Shapes Demo', (400, 450), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 0), 2)

print("텍스트를 추가했습니다.")

# ========== 결과 표시 및 저장 ==========

print("\n8. 결과 표시")

# 결과 이미지 표시
cv2.imshow('Drawing Shapes', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 이미지 저장
cv2.imwrite('drawing_shapes.jpg', canvas)
print("drawing_shapes.jpg 파일로 저장되었습니다.")

# ========== 미션 ==========
print("\n" + "="*50)
print("미션: 도형 그리기 실습")
print("1. 빨간색으로 큰 원을 그리고 그 안에 노란색 작은 원을 그려보세요.")
print("2. 파란색으로 삼각형을 그리고 그 안에 'Hi!' 텍스트를 쓰세요.")
print("3. 초록색으로 별 모양을 그려보세요.")
print("4. 그린 도형들을 포함한 이미지를 저장하세요.")

print("\n정답:")
print("""
import cv2
import numpy as np

# 캔버스 생성
canvas = np.ones((400, 600, 3), dtype=np.uint8) * 255

# 1. 빨간색 큰 원과 노란색 작은 원
cv2.circle(canvas, (150, 200), 80, (0, 0, 255), -1)  # 빨간색 큰 원
cv2.circle(canvas, (150, 200), 40, (0, 255, 255), -1)  # 노란색 작은 원

# 2. 파란색 삼각형과 텍스트
pts = np.array([[350, 120], [450, 120], [400, 200]], np.int32)
cv2.fillPoly(canvas, [pts], (255, 0, 0))  # 파란색 삼각형
cv2.putText(canvas, 'Hi!', (385, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

# 3. 초록색 별 모양 (단순화된 별)
star_pts = np.array([[500, 50], [510, 80], [540, 80], [520, 100], [530, 130],
                     [500, 110], [470, 130], [480, 100], [460, 80], [490, 80]], np.int32)
cv2.fillPoly(canvas, [star_pts], (0, 255, 0))

# 4. 이미지 저장
cv2.imwrite('my_shapes.jpg', canvas)
cv2.imshow('My Shapes', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
""")

print("\n다음 강의: 04_Color_Spaces.py")