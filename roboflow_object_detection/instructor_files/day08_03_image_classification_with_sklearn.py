# pip install numpy scikit-learn

"""Day 08-3. sklearn으로 이미지 분류하기.

이 파일은 손글씨 숫자 이미지 데이터를 sklearn 분류기로 학습시키고,
이미지 분류가 표 형태 데이터 분류와 같은 구조로 진행된다는 점을 보여 준다.
"""

# numpy는 행렬, 벡터, 픽셀 배열처럼 숫자 묶음을 빠르게 계산하고 보기 좋게 정리할 때 사용한다.
import numpy as np

# load_digits는 8x8 손글씨 숫자 이미지 예제를 바로 불러와 이미지 분류와 합성곱 설명에 사용한다.
from sklearn.datasets import load_digits

# LogisticRegression은 분류 확률과 최종 클래스를 함께 설명하기 좋은 기본 분류 모델이라 사용한다.
from sklearn.linear_model import LogisticRegression

# accuracy_score와 confusion_matrix는 분류 결과를 숫자 하나와 표 형태로 함께 해석할 때 사용한다.
from sklearn.metrics import accuracy_score, confusion_matrix

# train_test_split은 데이터를 학습용과 시험용으로 공정하게 나누어 일반화 성능을 확인할 때 사용한다.
from sklearn.model_selection import train_test_split

# StandardScaler는 특징값의 평균과 스케일을 맞춰 거리 기반 모델과 신경망 학습을 더 안정적으로 만든다.
from sklearn.preprocessing import StandardScaler

# 예상 출력 핵심:
# - 입력 데이터 shape는 (1797, 64), 학습/테스트 크기는 (1347, 64), (450, 64)로 출력된다.
# - 테스트 정확도는 0.9778로 출력된다.
# - 첫 3개 테스트 이미지 예측은 [8, 0, 9]로 고정되며, 첫 번째 샘플은 정답 1을 8로 잘못 예측한다.

print("=== Day 08-3: sklearn으로 이미지 분류하기 ===")

digits = load_digits()
X = digits.data
y = digits.target

print("\n[실습 1] 입력 데이터 shape")
print(X.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
print("\n[실습 2] 학습/테스트 데이터 개수")
print(X_train.shape, X_test.shape)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=2000, random_state=42)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred)
print("\n[실습 3] 테스트 정확도")
print(round(acc, 4))

cm = confusion_matrix(y_test, y_pred)
print("\n[실습 4] 혼동행렬 일부")
print(cm[:5, :5])

proba = model.predict_proba(X_test_scaled[:3])
print("\n[실습 5] 첫 3개 테스트 이미지의 예측 숫자")
print(y_pred[:3].tolist())
print("\n[실습 6] 첫 번째 테스트 이미지의 클래스별 확률")
print(np.round(proba[0], 4))

print("\n[실습 7] 정답과 예측 비교")
for idx in range(3):
    print({
        '정답': int(y_test[idx]),
        '예측': int(y_pred[idx]),
        '최고확률': round(float(np.max(proba[idx])), 4),
    })
