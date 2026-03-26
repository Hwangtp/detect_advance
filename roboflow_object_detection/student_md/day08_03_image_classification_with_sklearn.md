# Day 08-3. sklearn으로 이미지 분류하기

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 개요</h2>
  <p style="margin:0; line-height:1.8;">이미지를 64개의 숫자 특징으로 펼쳐서 sklearn 분류기로 학습시키며, 이미지 분류도 결국 표 데이터 분류 흐름과 이어진다는 점을 확인합니다.</p>
</div>

<div style="background-color:#eff6ff; border:1px solid #93c5fd; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#1d4ed8;">오늘 실습 구성</h3>
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li>digits.data shape와 train/test 분리 확인</li>
    <li>StandardScaler로 픽셀 스케일 맞추기</li>
    <li>LogisticRegression으로 숫자 분류 학습</li>
    <li>정확도와 혼동행렬 해석</li>
    <li>predict_proba로 클래스 확률 읽기</li>
  </ul>
</div>

<div style="background-color:#f0fdf4; border:1px solid #86efac; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#15803d;">수업 체크포인트</h3>
  <ol style="margin:0; padding-left:20px; line-height:1.8;">
    <li>이미지를 펼친 벡터도 sklearn 입력값이 될 수 있다.</li>
    <li>정확도와 혼동행렬을 함께 보며 분류 결과를 해석할 수 있다.</li>
    <li>확률 출력이 예측 신뢰도 설명에 도움이 된다는 점을 이해한다.</li>
  </ol>
</div>

<div style="background-color:#fff7ed; border:1px solid #fdba74; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#c2410c;">학습 가이드</h3>
  <p style="margin:0; line-height:1.9;">CNN을 배우기 전 단계로, 이미지도 결국 숫자 배열이라는 감각을 먼저 익히는 수업입니다. 표 데이터 분류와 같은 흐름으로 학습하고 평가할 수 있다는 점을 잡아 두면 이후 딥러닝 단계가 훨씬 덜 낯설어집니다.</p>
</div>

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
import numpy as np


from sklearn.datasets import load_digits


from sklearn.linear_model import LogisticRegression


from sklearn.metrics import accuracy_score, confusion_matrix


from sklearn.model_selection import train_test_split


from sklearn.preprocessing import StandardScaler

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
```
