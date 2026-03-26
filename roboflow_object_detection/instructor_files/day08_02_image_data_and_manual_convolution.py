# pip install numpy scikit-learn

"""Day 08-2. 이미지 데이터와 수동 합성곱.

이 파일은 숫자 이미지가 어떤 행렬로 표현되는지 확인하고,
작은 커널을 직접 적용해 합성곱이 어떤 계산인지 눈으로 이해하도록 만든다.
"""

# numpy는 행렬, 벡터, 픽셀 배열처럼 숫자 묶음을 빠르게 계산하고 보기 좋게 정리할 때 사용한다.
import numpy as np

# load_digits는 8x8 손글씨 숫자 이미지 예제를 바로 불러와 이미지 분류와 합성곱 설명에 사용한다.
from sklearn.datasets import load_digits

# 예상 출력 핵심:
# - 이미지 묶음 shape는 (1797, 8, 8)로 출력된다.
# - 첫 번째 이미지 정답 숫자는 0이고, 3x3 패치와 커널 계산 결과는 14.0으로 출력된다.
# - 2x2 평균 풀링 값은 7.25, 정규화된 첫 행도 고정된 숫자 배열로 출력된다.

print("=== Day 08-2: 이미지 데이터와 수동 합성곱 ===")

# digits 데이터셋은 8x8 흑백 이미지 1797장을 담고 있으므로 이미지 기초 수업에 적합하다.
digits = load_digits()
images = digits.images
labels = digits.target

# 이미지 묶음의 모양을 확인하면 (샘플 수, 높이, 너비) 구조를 이해할 수 있다.
print("\n[실습 1] 이미지 묶음의 shape 확인")
print(images.shape)

# 첫 번째 이미지를 꺼내면 한 장의 숫자 이미지가 8x8 행렬이라는 점을 볼 수 있다.
first_image = images[0]
first_label = int(labels[0])
print("\n[실습 2] 첫 번째 이미지의 정답 숫자")
print(first_label)
print("\n[실습 3] 첫 번째 이미지의 픽셀 행렬")
print(first_image.astype(int))

# 한 행의 합을 보면 어느 줄에 밝은 픽셀이 많이 모였는지 빠르게 파악할 수 있다.
print("\n[실습 4] 행별 밝기 합")
print(first_image.sum(axis=1).astype(int))

# 가운데가 밝고 주변은 어둡게 보이는 영역을 잡아 합성곱 예제를 만든다.
patch = first_image[2:5, 2:5]
print("\n[실습 5] 3x3 패치")
print(patch.astype(int))

# 아래 커널은 가운데와 세로 줄을 강조하는 간단한 특징 추출 필터다.
kernel = np.array([
    [0, 1, 0],
    [1, 2, 1],
    [0, 1, 0],
], dtype=float)
print("\n[실습 6] 합성곱 커널")
print(kernel.astype(int))

# 패치와 커널을 같은 위치끼리 곱한 뒤 모두 더하면 합성곱의 출력값 한 칸이 계산된다.
convolution_value = float(np.sum(patch * kernel))
print("\n[실습 7] 패치와 커널의 원소별 곱 합")
print(round(convolution_value, 2))

# 실제 합성곱은 이미지를 여러 위치로 이동하며 반복하므로, 첫 줄에서 몇 칸 계산해 본다.
first_row_outputs = []
for start_col in range(6):
    # 3x3 창을 한 칸씩 오른쪽으로 이동시키며 같은 커널을 적용한다.
    window = first_image[0:3, start_col:start_col + 3]
    first_row_outputs.append(round(float(np.sum(window * kernel)), 2))

print("\n[실습 8] 첫 번째 행 위치별 합성곱 출력")
print(first_row_outputs)

# 평균 풀링처럼 2x2 평균을 구하면 세부 정보는 줄지만 전체 패턴은 유지된다는 점을 보여줄 수 있다.
pooling_window = first_image[2:4, 2:4]
pooled_value = float(pooling_window.mean())
print("\n[실습 9] 2x2 평균 풀링 값")
print(round(pooled_value, 2))

# 픽셀을 0~1 범위로 나누면 모델이 다루기 쉬운 입력값으로 바꾸는 정규화의 감각을 익힐 수 있다.
normalized_image = first_image / 16.0
print("\n[실습 10] 정규화된 첫 행")
print(np.round(normalized_image[0], 3))
