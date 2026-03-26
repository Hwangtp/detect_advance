# pip install pandas scikit-learn

"""Day 02-1. train/test 분리의 기초.

이 파일은 데이터를 왜 나눠야 하는지, 그리고 KNN에서 n_neighbors 값이 무엇을 뜻하는지를
초심자 눈높이에서 한 번에 보여주기 위한 강사용 실습 파일이다.
모든 결과는 random_state=42로 고정해 항상 같은 출력이 나오도록 맞췄다.
"""

# pandas는 CSV 파일을 표 형태로 읽고, 필요한 열만 선택하고, 표를 보기 좋게 출력할 때 사용한다.
import pandas as pd

# train_test_split은 데이터를 학습용과 시험용으로 나눠서 공정하게 평가할 때 사용하는 함수다.
from sklearn.model_selection import train_test_split

# KNeighborsClassifier는 가까운 이웃 k개의 의견을 모아 클래스를 정하는 대표적인 입문용 분류 모델이다.
from sklearn.neighbors import KNeighborsClassifier

# 예상 출력 핵심:
# - 전체 데이터를 바로 평가한 정확도는 1.0으로 출력된다.
# - 분리 후 데이터 크기는 X_train (960, 3), X_test (240, 3)으로 출력된다.
# - k=5 모델의 학습용/시험용 정확도는 모두 1.0으로 출력된다.
# - k를 너무 크게 잡으면 0.9792, 0.9208, 0.6667처럼 성능이 떨어지는 예시가 출력된다.

# 수업 시작 제목을 먼저 출력해 지금 어떤 실습을 하는지 학생이 바로 알 수 있게 한다.
print("=== Day 02-1: train/test 분리의 기초 ===")

# CSV 파일에서 생선 데이터를 읽는다.
# 이 데이터는 길이, 무게, 꼬리 길이로 생선 종류를 맞히는 분류 문제다.
df = pd.read_csv("data/market_fish_extended.csv")

# X는 모델이 보고 배울 입력값(feature)이다.
# 여기서는 길이, 무게, 꼬리 길이 3개 숫자를 사용한다.
X = df[["length_cm", "weight_g", "tail_cm"]]

# y는 모델이 맞혀야 하는 정답(label)이다.
# 여기서는 생선 종류(species)가 정답 역할을 한다.
y = df["species"]

# KNN에서 n_neighbors는 "가까운 이웃을 몇 개 참고할 것인가"를 뜻한다.
# 예를 들어 5라면 가장 가까운 5개의 데이터가 어떤 생선인지 보고 다수결로 예측한다.
# 처음 배우는 단계에서는 5처럼 너무 작지도 너무 크지도 않은 홀수 값을 자주 사용한다.
full_model = KNeighborsClassifier(n_neighbors=5)

# fit은 모델에게 X와 y를 보여 주며 패턴을 학습시키는 단계다.
full_model.fit(X, y)

# 일부러 공정하지 않은 평가를 먼저 보여 준다.
# 전체 데이터를 학습하고 바로 같은 데이터로 점수를 재면 점수가 지나치게 좋아 보일 수 있다.
print("\n[실습 1] 전체 데이터를 한 번에 학습하고 평가")
print("정확도:", round(full_model.score(X, y), 4))

# 데이터를 학습용과 시험용으로 나눈다.
# test_size=0.2는 전체의 20%를 시험용으로 쓰겠다는 뜻이다.
# random_state=42는 항상 같은 방식으로 나누기 위한 고정값이다.
# stratify=y는 생선 종류 비율이 train/test에 비슷하게 유지되도록 맞춰 준다.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

# 나뉜 데이터 크기를 보여 주면 학생이 train/test split 결과를 눈으로 확인할 수 있다.
print("\n[실습 2] 분리된 데이터 크기")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)

# 학습용 데이터 안에 각 생선 종류가 몇 개씩 들어 있는지 확인한다.
# 이렇게 해야 데이터가 한쪽 종류로 치우치지 않았는지 설명할 수 있다.
print("\n[실습 3] 학습용 클래스 분포")
print(y_train.value_counts().sort_index().to_string())

# 시험용 데이터도 같은 방식으로 확인한다.
# stratify를 썼기 때문에 학습용과 시험용의 비율이 비슷하게 유지된다.
print("\n[실습 4] 시험용 클래스 분포")
print(y_test.value_counts().sort_index().to_string())

# 이번에는 공정하게 나눈 학습용 데이터만 사용해 모델을 다시 학습한다.
# 수업에서는 전체 데이터 점수보다 이 점수가 더 믿을 만하다고 강조하면 된다.
split_model = KNeighborsClassifier(n_neighbors=5)
split_model.fit(X_train, y_train)

# 학습용 점수와 시험용 점수를 나눠서 출력한다.
# 지금 데이터는 쉬운 편이라 둘 다 1.0이지만, 핵심은 둘을 구분해서 본다는 점이다.
print("\n[실습 5] 분리 후 학습용/시험용 점수")
print("학습용 정확도:", round(split_model.score(X_train, y_train), 4))
print("시험용 정확도:", round(split_model.score(X_test, y_test), 4))

# 새 생선 하나를 만들어 예측해 본다.
# 이 값은 실제 수업에서 "새 입력을 넣으면 모델이 어떤 답을 내는가"를 보여 주는 예시다.
sample_df = pd.DataFrame([
    {"length_cm": 25.2, "weight_g": 240.0, "tail_cm": 8.3}
])
print("\n[실습 6] 새 샘플 예측")
print(split_model.predict(sample_df).tolist())

# 이제 n_neighbors 값을 바꾸면 어떻게 되는지 비교 실습을 추가로 보여 준다.
# k가 너무 작으면 가까운 몇 개만 보고, k가 너무 크면 너무 많은 데이터를 섞어 보게 된다.
# 따라서 적당한 k를 찾는 것이 하이퍼파라미터 조정의 시작이라고 설명할 수 있다.
print("\n[실습 7] n_neighbors 값 비교")
for k in [1, 5, 241, 481, 959]:
    # 같은 데이터라도 k 값이 달라지면 모델의 판단 기준이 달라진다.
    compare_model = KNeighborsClassifier(n_neighbors=k)
    compare_model.fit(X_train, y_train)

    # 학습용/시험용 점수를 함께 출력하면 k가 너무 큰 경우 성능이 떨어지는 모습을 볼 수 있다.
    print(
        f"k={k}: 학습용={round(compare_model.score(X_train, y_train), 4)}, "
        f"시험용={round(compare_model.score(X_test, y_test), 4)}"
    )

# 마지막으로 왜 수업에서 k=5를 먼저 쓰는지 설명하는 문장을 출력한다.
# 홀수 값을 쓰면 동점이 줄고, 너무 작은 값과 너무 큰 값의 극단도 피하기 쉽다.
print("\n[실습 8] 왜 n_neighbors=5를 먼저 쓰는가")
print("k는 참고할 이웃 수를 뜻하며, 5는 너무 작지도 너무 크지도 않은 입문용 기준값이다.")
print("k를 지나치게 크게 잡으면 멀리 있는 데이터까지 섞여서 오히려 분류가 둔해질 수 있다.")