# Day 08-2. 이미지 데이터와 수동 합성곱

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 개요</h2>
  <p style="margin:0; line-height:1.8;">숫자 이미지가 8x8 행렬로 저장된다는 사실을 확인하고, 커널을 직접 곱해 합성곱이 어떤 계산인지 이해합니다.</p>
</div>

<div style="background-color:#eff6ff; border:1px solid #93c5fd; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#1d4ed8;">오늘 실습 구성</h3>
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li>digits 이미지 데이터셋 shape 확인</li>
    <li>첫 번째 이미지와 정답 숫자 읽기</li>
    <li>3x3 패치와 커널 직접 계산</li>
    <li>위치별 합성곱 출력과 평균 풀링 비교</li>
    <li>정규화된 픽셀 값 확인</li>
  </ul>
</div>

<div style="background-color:#f0fdf4; border:1px solid #86efac; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#15803d;">수업 체크포인트</h3>
  <ol style="margin:0; padding-left:20px; line-height:1.8;">
    <li>이미지 한 장이 숫자 행렬이라는 점을 설명할 수 있다.</li>
    <li>커널을 곱하고 더하는 과정이 합성곱이라는 점을 이해한다.</li>
    <li>정규화와 풀링이 왜 필요한지 말할 수 있다.</li>
  </ol>
</div>

<div style="background-color:#fff7ed; border:1px solid #fdba74; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#c2410c;">학습 가이드</h3>
  <p style="margin:0; line-height:1.9;">행렬 출력이 많아 보여도 각 숫자는 픽셀 밝기라는 점만 먼저 잡으면 훨씬 편해집니다. 패치와 커널을 같은 위치끼리 곱하고 더하는 계산을 손으로 한 번 따라가면 CNN의 첫 관문이 훨씬 쉬워집니다.</p>
</div>

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
import numpy as np


from sklearn.datasets import load_digits

print("=== Day 08-2: 이미지 데이터와 수동 합성곱 ===")


digits = load_digits()
images = digits.images
labels = digits.target


print("\n[실습 1] 이미지 묶음의 shape 확인")
print(images.shape)


first_image = images[0]
first_label = int(labels[0])
print("\n[실습 2] 첫 번째 이미지의 정답 숫자")
print(first_label)
print("\n[실습 3] 첫 번째 이미지의 픽셀 행렬")
print(first_image.astype(int))


print("\n[실습 4] 행별 밝기 합")
print(first_image.sum(axis=1).astype(int))


patch = first_image[2:5, 2:5]
print("\n[실습 5] 3x3 패치")
print(patch.astype(int))


kernel = np.array([
    [0, 1, 0],
    [1, 2, 1],
    [0, 1, 0],
], dtype=float)
print("\n[실습 6] 합성곱 커널")
print(kernel.astype(int))


convolution_value = float(np.sum(patch * kernel))
print("\n[실습 7] 패치와 커널의 원소별 곱 합")
print(round(convolution_value, 2))


first_row_outputs = []
for start_col in range(6):

    window = first_image[0:3, start_col:start_col + 3]
    first_row_outputs.append(round(float(np.sum(window * kernel)), 2))

print("\n[실습 8] 첫 번째 행 위치별 합성곱 출력")
print(first_row_outputs)


pooling_window = first_image[2:4, 2:4]
pooled_value = float(pooling_window.mean())
print("\n[실습 9] 2x2 평균 풀링 값")
print(round(pooled_value, 2))


normalized_image = first_image / 16.0
print("\n[실습 10] 정규화된 첫 행")
print(np.round(normalized_image[0], 3))
```
