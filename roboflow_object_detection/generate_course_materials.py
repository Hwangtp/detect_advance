from __future__ import annotations

import csv
from pathlib import Path
from textwrap import dedent


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
INSTRUCTOR_DIR = BASE_DIR / "instructor_files"
STUDENT_DIR = BASE_DIR / "student_md"


def ensure_dirs() -> None:
    for directory in [DATA_DIR, INSTRUCTOR_DIR, STUDENT_DIR]:
        directory.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str) -> None:
    path.write_text(content.strip() + "\n", encoding="utf-8")


def write_csv(path: Path, header: list[str], rows: list[list[object]]) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)


def build_market_fish_rows() -> list[list[object]]:
    rows: list[list[object]] = []
    for i in range(1200):
        if i % 3 == 0:
            species = "bream"
            length = round(24 + (i % 11) * 0.8 + (i % 5) * 0.1, 2)
            weight = round(220 + (i % 17) * 11 + (i % 7) * 2.5, 2)
            tail = round(8.2 + (i % 6) * 0.25, 2)
        elif i % 3 == 1:
            species = "smelt"
            length = round(10 + (i % 9) * 0.45 + (i % 4) * 0.08, 2)
            weight = round(8 + (i % 13) * 1.6 + (i % 5) * 0.3, 2)
            tail = round(3.4 + (i % 6) * 0.12, 2)
        else:
            species = "perch"
            length = round(16 + (i % 12) * 0.65 + (i % 5) * 0.14, 2)
            weight = round(55 + (i % 19) * 5.8 + (i % 7) * 1.7, 2)
            tail = round(5.1 + (i % 7) * 0.19, 2)
        rows.append([species, length, weight, tail])
    return rows


def build_student_rows() -> list[list[object]]:
    rows: list[list[object]] = []
    for i in range(1500):
        hours = round(1.5 + (i % 10) * 0.7 + (i % 3) * 0.15, 2)
        practice = round(0.5 + (i % 8) * 0.55 + (i % 4) * 0.1, 2)
        sleep = round(5.5 + (i % 7) * 0.4, 2)
        score = round(35 + hours * 6.8 + practice * 4.9 + sleep * 1.8 + (i % 6) * 0.9, 2)
        passed = 1 if score >= 75 else 0
        rows.append([hours, practice, sleep, score, passed])
    return rows


def build_fruit_rows() -> list[list[object]]:
    rows: list[list[object]] = []
    for i in range(1350):
        group = i % 3
        if group == 0:
            fruit = "apple"
            sweetness = round(62 + (i % 12) * 1.1, 2)
            crunch = round(74 + (i % 10) * 0.9, 2)
            moisture = round(54 + (i % 8) * 0.8, 2)
        elif group == 1:
            fruit = "banana"
            sweetness = round(79 + (i % 9) * 0.8, 2)
            crunch = round(24 + (i % 7) * 0.7, 2)
            moisture = round(68 + (i % 9) * 0.9, 2)
        else:
            fruit = "orange"
            sweetness = round(70 + (i % 10) * 0.9, 2)
            crunch = round(38 + (i % 8) * 0.8, 2)
            moisture = round(81 + (i % 10) * 0.7, 2)
        rows.append([fruit, sweetness, crunch, moisture])
    return rows


def build_detection_rows() -> list[list[object]]:
    rows: list[list[object]] = []
    for i in range(1200):
        image_id = f"img_{i + 1:04d}.jpg"
        label = ["helmet", "vest", "person"][i % 3]
        width = 640
        height = 640
        x_center = round(0.15 + (i % 17) * 0.04, 3)
        y_center = round(0.2 + (i % 13) * 0.045, 3)
        box_w = round(0.14 + (i % 7) * 0.02, 3)
        box_h = round(0.18 + (i % 6) * 0.025, 3)
        split = "train" if i < 900 else "valid" if i < 1050 else "test"
        rows.append([image_id, label, width, height, x_center, y_center, box_w, box_h, split])
    return rows


def lesson_py(day: int, title: str, objective: str, code: str) -> str:
    return dedent(
        f"""
        # Day {day:02d} - {title}
        # ?? ??: {objective}
        # ?? ??: Python 3.12, Google Colab
        # ??: ?? ???? ???? ???? ??? ?? ??? ?? ??? ???? ?????.

        from pathlib import Path

        # ?? ?? ??? ?? ??? ?? ??? ?? ??? ?? ?? ?? ??? ?? ?? ??? ???????.
        if "__file__" in globals():
            COURSE_ROOT = Path(__file__).resolve().parents[1]
        else:
            COURSE_ROOT = Path(".").resolve()

        DATA_DIR = COURSE_ROOT / "data"
        if not DATA_DIR.exists():
            DATA_DIR = Path("data")

        {code.strip()}
        """
    ).strip()

def lesson_md(day: int, title: str, summary: str, keywords: list[str], practice: list[str]) -> str:
    keyword_text = "\n".join([f"- {item}" for item in keywords])
    practice_text = "\n".join([f"1. {item}" if idx == 0 else f"{idx + 1}. {item}" for idx, item in enumerate(practice)])
    return dedent(
        f"""
        # Day {day:02d}. {title}

        ## 수업 목표
        {summary}

        ## 오늘의 핵심 용어
        {keyword_text}

        ## 학습 흐름
        1. 개념 이해
        2. 데이터 확인
        3. 코드 타이핑 실습
        4. 결과 해석
        5. 짧은 응용 활동

        ## 실습 체크포인트
        {practice_text}
        """
    ).strip()


def build_lessons() -> tuple[dict[str, str], dict[str, str]]:
    lessons_py: dict[str, str] = {}
    lessons_md: dict[str, str] = {}

    lessons_py["day01_ai_colab_and_easy_ml.py"] = lesson_py(
        1,
        "인공지능 입문과 코랩, 첫 분류",
        "인공지능, 머신러닝, 딥러닝 차이를 이해하고 코랩에서 가장 쉬운 분류 예제를 실행한다.",
        """
        # 인공지능(AI): 사람의 판단처럼 보이는 일을 컴퓨터가 하도록 만드는 큰 분야입니다.
        # 머신러닝(ML): 사람이 규칙을 모두 직접 쓰지 않고, 데이터로 규칙을 배우게 하는 방법입니다.
        # 딥러닝(DL): 머신러닝의 한 종류이며, 신경망을 여러 층으로 깊게 쌓아 학습합니다.

        print("안녕하세요. 로보플로우 객체탐지 수업에 오신 것을 환영합니다.")
        # 위 출력은 파이썬 코드가 정상 실행되었음을 보여줍니다.
        # 초심자는 먼저 '실행이 되는 경험'을 하는 것이 중요합니다.

        import pandas as pd
        from sklearn.neighbors import KNeighborsClassifier

        # 데이터셋(dataset): 학습에 사용하는 표 형태의 자료입니다.
        # 여기서는 강사용 폴더 안의 CSV 파일을 읽어와 사용합니다.
        fish_df = pd.read_csv(DATA_DIR / "market_fish_extended.csv")

        # head(): 데이터의 앞부분 5행을 보여 주는 함수입니다.
        print(fish_df.head())
        # 이 결과는 생선 종류(species)와 길이(length_cm), 무게(weight_g), 꼬리 길이(tail_cm)가 들어 있음을 의미합니다.

        # 특성(feature): 모델이 보고 배우는 입력값입니다.
        # 정답(label): 모델이 맞혀야 하는 값입니다.
        X = fish_df[["length_cm", "weight_g", "tail_cm"]]
        y = fish_df["species"]

        model = KNeighborsClassifier(n_neighbors=5)
        # k-최근접 이웃: 가장 가까운 이웃 k개를 보고 다수결로 분류하는 매우 쉬운 알고리즘입니다.
        model.fit(X, y)
        # fit(): 모델이 데이터에서 패턴을 학습하는 단계입니다.

        sample = [[26.5, 280, 8.8]]
        prediction = model.predict(sample)
        print("예측 결과:", prediction[0])
        # 예측 결과가 bream이라면, 입력한 생선이 도미 패턴과 가장 가깝다는 뜻입니다.

        score = model.score(X, y)
        print("훈련 데이터 정확도:", round(score, 4))
        # 정확도(accuracy): 전체 예측 중에서 맞춘 비율입니다.
        # 훈련 데이터 정확도가 높다는 것은 현재 학습에 사용한 자료는 잘 구분했다는 뜻입니다.

        # 코랩 사용 팁
        # 1. Shift + Enter: 현재 셀 실행
        # 2. + 코드: 새 코드 셀 추가
        # 3. + 텍스트: 설명용 텍스트 셀 추가
        # 4. 런타임 초기화 후 다시 실행하면 처음부터 흐름을 확인할 수 있습니다.
        """,
    )
    lessons_md["day01_ai_colab_and_easy_ml.md"] = lesson_md(
        1,
        "인공지능 입문과 코랩, 첫 분류",
        "인공지능, 머신러닝, 딥러닝의 관계를 이해하고 코랩에서 첫 분류 모델을 실행한다.",
        ["인공지능", "머신러닝", "딥러닝", "데이터셋", "특성", "정답", "정확도", "코랩 셀"],
        ["CSV 데이터를 읽을 수 있다.", "특성과 정답을 구분할 수 있다.", "k-최근접 이웃 분류를 실행할 수 있다.", "예측 결과와 정확도의 의미를 설명할 수 있다."],
    )

    lessons_py["day02_training_test_and_preprocessing.py"] = lesson_py(
        2,
        "훈련 세트, 테스트 세트, 전처리",
        "데이터를 나누는 이유를 이해하고 스케일 차이를 맞추는 전처리를 실습한다.",
        """
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import StandardScaler
        from sklearn.neighbors import KNeighborsClassifier

        df = pd.read_csv(DATA_DIR / "market_fish_extended.csv")

        X = df[["length_cm", "weight_g", "tail_cm"]]
        y = df["species"]

        # 훈련 세트(training set): 모델을 학습시키는 데이터입니다.
        # 테스트 세트(test set): 학습이 끝난 뒤 성능을 확인하는 데이터입니다.
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        print("훈련 세트 크기:", X_train.shape)
        print("테스트 세트 크기:", X_test.shape)
        # 이 결과는 전체 데이터 중 80%는 학습용, 20%는 평가용으로 나뉘었다는 뜻입니다.

        raw_model = KNeighborsClassifier(n_neighbors=5)
        raw_model.fit(X_train, y_train)
        raw_score = raw_model.score(X_test, y_test)
        print("전처리 전 테스트 정확도:", round(raw_score, 4))
        # 여기서의 정확도는 아직 특성의 크기 차이를 그대로 둔 상태의 성능입니다.

        scaler = StandardScaler()
        # 전처리(preprocessing): 모델이 더 잘 배우도록 데이터를 정리하는 과정입니다.
        # StandardScaler: 평균 0, 표준편차 1 기준으로 값을 맞춰 줍니다.
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        scaled_model = KNeighborsClassifier(n_neighbors=5)
        scaled_model.fit(X_train_scaled, y_train)
        scaled_score = scaled_model.score(X_test_scaled, y_test)
        print("전처리 후 테스트 정확도:", round(scaled_score, 4))
        # 전처리 후 정확도가 좋아졌다면, 서로 단위가 다른 길이와 무게를 비슷한 기준으로 맞춘 효과가 있다는 뜻입니다.

        suspicious_fish = [[25, 150, 8.1]]
        suspicious_fish_scaled = scaler.transform(suspicious_fish)
        print("새 샘플 예측:", scaled_model.predict(suspicious_fish_scaled)[0])
        # 새 샘플 예측은 실제 현장에서 처음 보는 입력이 어느 클래스와 가까운지 보여 줍니다.

        # 샘플링 편향(sampling bias): 데이터가 한쪽으로 치우쳐 모델이 공정하게 배우지 못하는 문제입니다.
        # stratify=y 옵션은 클래스 비율을 비슷하게 유지하도록 도와줍니다.
        """,
    )
    lessons_md["day02_training_test_and_preprocessing.md"] = lesson_md(
        2,
        "훈련 세트, 테스트 세트, 전처리",
        "모델을 제대로 평가하기 위해 데이터를 나누고, 특성의 단위를 맞추는 전처리를 이해한다.",
        ["훈련 세트", "테스트 세트", "전처리", "표준화", "샘플링 편향", "평가"],
        ["train_test_split의 역할을 설명할 수 있다.", "전처리 전후의 성능 차이를 확인할 수 있다.", "새 샘플에 대해 예측을 수행할 수 있다."],
    )

    lessons_py["day03_regression_for_prediction.py"] = lesson_py(
        3,
        "회귀로 숫자 예측하기",
        "공부 시간과 연습 시간이 점수에 어떤 영향을 주는지 회귀 모델로 예측한다.",
        """
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LinearRegression
        from sklearn.metrics import r2_score, mean_absolute_error

        df = pd.read_csv(DATA_DIR / "student_learning_extended.csv")

        # 회귀(regression): 정답이 숫자인 문제를 푸는 방법입니다.
        X = df[["study_hours", "practice_hours", "sleep_hours"]]
        y = df["exam_score"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = LinearRegression()
        # 선형 회귀(linear regression): 입력과 결과가 직선 관계라고 보고 예측하는 가장 쉬운 회귀 모델입니다.
        model.fit(X_train, y_train)

        pred = model.predict(X_test)
        r2 = r2_score(y_test, pred)
        mae = mean_absolute_error(y_test, pred)

        print("R^2 점수:", round(r2, 4))
        # R^2는 모델이 점수의 변화를 얼마나 잘 설명하는지 나타냅니다.
        # 1에 가까울수록 설명력이 좋다는 뜻입니다.

        print("평균 절대 오차:", round(mae, 4))
        # 평균 절대 오차(MAE)는 평균적으로 몇 점 정도 틀리는지 보여 줍니다.
        # 값이 작을수록 예측이 실제 점수와 가깝다는 뜻입니다.

        new_student = [[5.5, 2.5, 7.0]]
        predicted_score = model.predict(new_student)[0]
        print("새 학생의 예상 점수:", round(predicted_score, 2))
        # 이 값은 공부 시간, 실습 시간, 수면 시간이 주어졌을 때 예상 시험 점수를 의미합니다.

        print("기울기:", model.coef_)
        print("절편:", model.intercept_)
        # 기울기(coef_)는 각 특성이 결과에 얼마나 영향을 주는지 보여 줍니다.
        # 절편(intercept_)은 입력이 모두 0일 때 출발 기준값 역할을 합니다.

        # 과대적합(overfitting): 학습 데이터는 잘 맞지만 새 데이터에서 성능이 떨어지는 현상입니다.
        # 과소적합(underfitting): 모델이 너무 단순해서 학습 데이터조차 충분히 설명하지 못하는 현상입니다.
        """,
    )
    lessons_md["day03_regression_for_prediction.md"] = lesson_md(
        3,
        "회귀로 숫자 예측하기",
        "분류와 회귀의 차이를 이해하고 숫자 예측 모델을 실습한다.",
        ["회귀", "선형 회귀", "R^2", "평균 절대 오차", "기울기", "절편", "과대적합", "과소적합"],
        ["분류와 회귀를 구분할 수 있다.", "시험 점수 예측 모델을 만들 수 있다.", "R^2와 MAE를 해석할 수 있다."],
    )

    lessons_py["day04_classification_and_probability.py"] = lesson_py(
        4,
        "분류와 확률 이해하기",
        "합격 여부를 분류하고 확률 출력이 무엇을 뜻하는지 익힌다.",
        """
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import confusion_matrix, classification_report

        df = pd.read_csv(DATA_DIR / "student_learning_extended.csv")

        X = df[["study_hours", "practice_hours", "sleep_hours"]]
        y = df["passed"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        model = LogisticRegression(max_iter=1000)
        # 로지스틱 회귀(logistic regression): 이름은 회귀지만 분류 문제에 많이 쓰는 대표 알고리즘입니다.
        model.fit(X_train, y_train)

        score = model.score(X_test, y_test)
        print("테스트 정확도:", round(score, 4))
        # 정확도는 합격/불합격을 얼마나 잘 맞췄는지 보여 줍니다.

        sample = [[3.5, 1.0, 6.0]]
        prob = model.predict_proba(sample)[0]
        pred = model.predict(sample)[0]

        print("불합격 확률:", round(prob[0], 4))
        print("합격 확률:", round(prob[1], 4))
        print("최종 예측:", pred)
        # 확률은 모델이 얼마나 자신 있게 판단했는지 보여 줍니다.
        # 예를 들어 합격 확률이 0.82라면 82% 정도의 확신으로 합격으로 본다는 뜻입니다.

        test_pred = model.predict(X_test)
        print("혼동 행렬:")
        print(confusion_matrix(y_test, test_pred))
        # 혼동 행렬(confusion matrix)은 무엇을 맞췄고 무엇을 틀렸는지 표로 보여 줍니다.

        print("분류 리포트:")
        print(classification_report(y_test, test_pred))
        # precision, recall, f1-score는 분류 성능을 더 자세히 보여 주는 지표입니다.
        # 초심자는 우선 accuracy와 함께 '틀리는 방식'을 확인하는 용도로 보면 좋습니다.
        """,
    )
    lessons_md["day04_classification_and_probability.md"] = lesson_md(
        4,
        "분류와 확률 이해하기",
        "합격 여부 분류 문제를 통해 확률 출력과 성능 지표를 이해한다.",
        ["로지스틱 회귀", "확률", "정확도", "혼동 행렬", "정밀도", "재현율", "F1-score"],
        ["합격/불합격 분류 모델을 만들 수 있다.", "predict와 predict_proba의 차이를 설명할 수 있다.", "혼동 행렬을 읽을 수 있다."],
    )

    lessons_py["day05_unsupervised_learning_and_clustering.py"] = lesson_py(
        5,
        "비지도 학습과 군집",
        "정답 없이 비슷한 것끼리 묶는 군집 알고리즘을 쉬운 과일 데이터로 배운다.",
        """
        import pandas as pd
        from sklearn.cluster import KMeans
        from sklearn.preprocessing import StandardScaler

        df = pd.read_csv(DATA_DIR / "fruit_traits_extended.csv")

        X = df[["sweetness", "crunch", "moisture"]]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        # 비지도 학습(unsupervised learning): 정답 없이 데이터의 구조를 찾는 학습입니다.

        model = KMeans(n_clusters=3, random_state=42, n_init=10)
        # 군집(clustering): 비슷한 데이터끼리 묶는 작업입니다.
        # k-평균(KMeans): 중심점과의 거리를 기준으로 묶는 대표 알고리즘입니다.
        clusters = model.fit_predict(X_scaled)

        df["cluster"] = clusters
        print(df.head())
        # cluster 열이 추가되었다면 각 과일 데이터가 어느 묶음에 들어갔는지 표시된 것입니다.

        print("군집별 개수:")
        print(df["cluster"].value_counts().sort_index())
        # 군집별 개수는 비슷한 패턴이 몇 개씩 모였는지 의미합니다.

        centers = scaler.inverse_transform(model.cluster_centers_)
        center_df = pd.DataFrame(centers, columns=["sweetness", "crunch", "moisture"])
        print("군집 중심:")
        print(center_df)
        # 군집 중심(center)은 각 묶음의 대표적인 평균 성격이라고 보면 됩니다.

        # 실제 과일 이름은 정답이 아니라 참고용입니다.
        # 군집 번호 0, 1, 2는 알고리즘이 임의로 붙인 이름일 뿐이며 우열이나 순서를 뜻하지 않습니다.
        """,
    )
    lessons_md["day05_unsupervised_learning_and_clustering.md"] = lesson_md(
        5,
        "비지도 학습과 군집",
        "정답이 없는 데이터에서 비슷한 패턴을 묶는 방법을 이해한다.",
        ["비지도 학습", "군집", "KMeans", "군집 중심", "표준화"],
        ["정답이 없는 문제를 설명할 수 있다.", "KMeans를 실행할 수 있다.", "군집 결과와 군집 중심을 해석할 수 있다."],
    )

    lessons_py["day06_neural_network_intro.py"] = lesson_py(
        6,
        "딥러닝 첫걸음",
        "신경망이 무엇인지 이해하고 텐서플로로 가장 단순한 분류 모델을 만든다.",
        """
        import numpy as np
        import tensorflow as tf
        from sklearn.model_selection import train_test_split
        import pandas as pd

        df = pd.read_csv(DATA_DIR / "student_learning_extended.csv")
        X = df[["study_hours", "practice_hours", "sleep_hours"]].values
        y = df["passed"].values

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        model = tf.keras.Sequential([
            tf.keras.layers.Dense(8, activation="relu", input_shape=(3,)),
            tf.keras.layers.Dense(1, activation="sigmoid"),
        ])
        # Dense 층: 앞층의 모든 노드와 연결되는 기본 신경망 층입니다.
        # relu: 음수는 0으로, 양수는 그대로 보내는 대표 활성화 함수입니다.
        # sigmoid: 0과 1 사이 확률처럼 보이는 값을 출력할 때 자주 사용합니다.

        model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
        # optimizer: 가중치를 어떻게 업데이트할지 정하는 방법입니다.
        # loss: 모델이 얼마나 틀렸는지를 숫자로 표현한 값입니다.

        history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2, verbose=0)
        # epoch: 전체 훈련 데이터를 한 바퀴 학습한 횟수입니다.
        # validation_split: 훈련 데이터의 일부를 검증용으로 따로 떼어 확인합니다.

        test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
        print("테스트 손실:", round(float(test_loss), 4))
        print("테스트 정확도:", round(float(test_acc), 4))
        # 정확도가 높아지면 신경망이 합격/불합격 패턴을 어느 정도 배웠다는 뜻입니다.

        sample = np.array([[4.0, 1.5, 6.5]])
        prob = model.predict(sample, verbose=0)[0][0]
        print("합격 확률:", round(float(prob), 4))
        # 출력값이 0.5보다 크면 보통 합격 쪽으로 해석합니다.

        print("마지막 검증 정확도:", round(float(history.history["val_accuracy"][-1]), 4))
        # 학습 과정의 마지막 검증 정확도는 모델이 새로운 데이터에도 어느 정도 일반화되는지 보여 줍니다.
        """,
    )
    lessons_md["day06_neural_network_intro.md"] = lesson_md(
        6,
        "딥러닝 첫걸음",
        "신경망의 기본 구성 요소와 텐서플로 학습 흐름을 익힌다.",
        ["인공 신경망", "Dense", "활성화 함수", "손실", "옵티마이저", "에포크", "검증 데이터"],
        ["Sequential 모델을 만들 수 있다.", "compile, fit, evaluate의 흐름을 설명할 수 있다.", "확률 출력의 의미를 이해할 수 있다."],
    )

    lessons_py["day07_deep_neural_network_training.py"] = lesson_py(
        7,
        "심층 신경망과 훈련 모범 사례",
        "층을 더 쌓고 드롭아웃, 저장, 조기 종료 개념을 이해한다.",
        """
        import tensorflow as tf
        from sklearn.model_selection import train_test_split
        import pandas as pd

        df = pd.read_csv(DATA_DIR / "student_learning_extended.csv")
        X = df[["study_hours", "practice_hours", "sleep_hours"]].values
        y = df["passed"].values

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(3,)),
            tf.keras.layers.Dense(32, activation="relu"),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(16, activation="relu"),
            tf.keras.layers.Dense(1, activation="sigmoid"),
        ])
        # 드롭아웃(dropout): 일부 연결을 훈련 중 잠시 꺼서 과대적합을 줄이려는 기법입니다.

        model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

        early_stop = tf.keras.callbacks.EarlyStopping(
            monitor="val_loss", patience=5, restore_best_weights=True
        )
        # EarlyStopping: 검증 손실이 좋아지지 않으면 훈련을 멈추는 장치입니다.
        # restore_best_weights=True는 가장 좋았던 시점의 가중치를 되돌려 줍니다.

        history = model.fit(
            X_train,
            y_train,
            validation_split=0.2,
            epochs=50,
            batch_size=32,
            callbacks=[early_stop],
            verbose=0,
        )

        model.save(COURSE_ROOT / "day07_student_pass_model.keras")
        # 모델 저장은 다음 수업이나 배포 단계에서 재사용하기 위해 중요합니다.

        loaded_model = tf.keras.models.load_model(COURSE_ROOT / "day07_student_pass_model.keras")
        test_loss, test_acc = loaded_model.evaluate(X_test, y_test, verbose=0)

        print("실제 학습 에포크 수:", len(history.history["loss"]))
        print("불러온 모델의 테스트 정확도:", round(float(test_acc), 4))
        # 조기 종료가 동작했다면 설정한 최대 epoch보다 적은 횟수에서 멈췄을 수 있습니다.

        print("최저 검증 손실:", round(float(min(history.history["val_loss"])), 4))
        # 검증 손실이 낮을수록 보지 못한 데이터에 대한 예측이 더 안정적일 가능성이 큽니다.
        """,
    )
    lessons_md["day07_deep_neural_network_training.md"] = lesson_md(
        7,
        "심층 신경망과 훈련 모범 사례",
        "심층 신경망 구조와 과대적합을 줄이는 기본 전략을 익힌다.",
        ["심층 신경망", "드롭아웃", "검증 손실", "조기 종료", "모델 저장", "모델 복원"],
        ["층이 깊어질 때의 의미를 설명할 수 있다.", "드롭아웃과 EarlyStopping의 목적을 설명할 수 있다.", "모델 저장과 복원을 수행할 수 있다."],
    )

    lessons_py["day08_cnn_image_basics.py"] = lesson_py(
        8,
        "합성곱 신경망과 이미지 분류",
        "이미지에서 CNN이 왜 강한지 이해하고 가장 쉬운 CNN 분류 예제를 실행한다.",
        """
        import tensorflow as tf

        (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()

        # 이미지 데이터는 보통 0~255 범위의 픽셀값으로 이루어집니다.
        train_images = train_images / 255.0
        test_images = test_images / 255.0
        # 정규화(normalization): 값을 0~1 사이로 줄여 학습을 안정적으로 돕는 과정입니다.

        model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(28, 28)),
            tf.keras.layers.Reshape((28, 28, 1)),
            tf.keras.layers.Conv2D(16, (3, 3), activation="relu"),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(10, activation="softmax"),
        ])
        # Conv2D: 작은 필터로 이미지를 훑으며 특징을 찾는 층입니다.
        # MaxPooling2D: 중요한 특징만 남기고 크기를 줄여 계산량을 줄이는 층입니다.
        # softmax: 여러 클래스 중 각 클래스일 확률처럼 해석되는 값을 만듭니다.

        model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
        model.fit(train_images, train_labels, epochs=3, validation_split=0.1, verbose=0)

        test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=0)
        print("CNN 테스트 정확도:", round(float(test_acc), 4))
        # CNN 정확도가 비교적 높게 나오면, 이미지의 모양 정보를 잘 학습했다는 뜻입니다.

        sample_probs = model.predict(test_images[:1], verbose=0)[0]
        print("첫 이미지의 예측 확률 분포:", sample_probs.round(4))
        print("가장 높은 확률의 클래스:", int(sample_probs.argmax()))
        # 가장 높은 확률의 클래스 번호가 모델이 최종 선택한 예측값입니다.
        """,
    )
    lessons_md["day08_cnn_image_basics.md"] = lesson_md(
        8,
        "합성곱 신경망과 이미지 분류",
        "CNN의 핵심 구성 요소와 이미지 분류 흐름을 이해한다.",
        ["CNN", "합성곱", "필터", "풀링", "정규화", "소프트맥스"],
        ["이미지 데이터의 형태를 설명할 수 있다.", "Conv2D와 MaxPooling2D의 역할을 구분할 수 있다.", "CNN 분류 결과를 읽을 수 있다."],
    )

    lessons_py["day09_roboflow_and_object_detection_workflow.py"] = lesson_py(
        9,
        "로보플로우와 객체탐지 워크플로우",
        "분류와 객체탐지의 차이를 이해하고 로보플로우 프로젝트 흐름을 익힌다.",
        """
        import pandas as pd

        df = pd.read_csv(DATA_DIR / "detection_annotations_extended.csv")

        print(df.head())
        # 이 표는 이미지 하나마다 어떤 객체가 어디에 있는지 박스 정보가 들어 있음을 의미합니다.

        print("데이터 분할 개수:")
        print(df["split"].value_counts())
        # train, valid, test는 각각 학습, 검증, 최종 평가 단계에 사용됩니다.

        print("클래스 개수:")
        print(df["label"].value_counts())
        # 클래스 불균형이 심하면 특정 객체만 잘 찾는 문제가 생길 수 있습니다.

        # 객체탐지(object detection): 이미지 안에 '무엇이 있는지'와 '어디에 있는지'를 함께 찾는 작업입니다.
        # 바운딩 박스(bounding box): 객체를 감싸는 사각형 좌표입니다.
        # 로보플로우(Roboflow): 데이터 업로드, 라벨링, 증강, 버전 관리, 학습 연결을 도와주는 플랫폼입니다.

        # 로보플로우 수업 실전 흐름
        # 1. 새 프로젝트 생성
        # 2. 이미지 업로드
        # 3. 클래스 정의
        # 4. 박스 라벨링
        # 5. 전처리와 증강 설정
        # 6. 버전 생성
        # 7. 모델 학습
        # 8. 추론 결과 확인

        # YOLO 형식에서 자주 보는 값
        # x_center, y_center: 박스 중심 좌표를 이미지 크기로 나눈 상대값입니다.
        # box_width, box_height: 박스 크기를 이미지 크기로 나눈 상대값입니다.

        sample_row = df.iloc[0]
        print("예시 이미지:", sample_row["image_id"])
        print("예시 클래스:", sample_row["label"])
        print("예시 중심 좌표:", (sample_row["x_center"], sample_row["y_center"]))
        print("예시 박스 크기:", (sample_row["box_width"], sample_row["box_height"]))
        # 상대 좌표를 쓰는 이유는 이미지 크기가 달라도 같은 형식으로 학습시키기 쉽기 때문입니다.
        """,
    )
    lessons_md["day09_roboflow_and_object_detection_workflow.md"] = lesson_md(
        9,
        "로보플로우와 객체탐지 워크플로우",
        "객체탐지의 개념과 로보플로우 기반 데이터 준비 흐름을 이해한다.",
        ["객체탐지", "바운딩 박스", "라벨링", "증강", "버전", "YOLO 형식", "train/valid/test"],
        ["분류와 객체탐지의 차이를 설명할 수 있다.", "객체탐지 데이터셋의 기본 구조를 설명할 수 있다.", "로보플로우 작업 순서를 말할 수 있다."],
    )

    lessons_py["day10_roboflow_inference_and_evaluation.py"] = lesson_py(
        10,
        "객체탐지 추론과 평가",
        "객체탐지 결과를 읽는 법과 confidence, IoU, mAP 개념을 쉬운 예제로 이해한다.",
        """
        # confidence score: 모델이 이 박스가 맞다고 생각하는 자신감 점수입니다.
        # IoU(Intersection over Union): 예측 박스와 정답 박스가 얼마나 겹치는지 나타내는 값입니다.
        # mAP(mean Average Precision): 객체탐지 모델 성능을 종합적으로 보는 대표 지표입니다.

        predicted_box = {"x1": 100, "y1": 120, "x2": 260, "y2": 320}
        ground_truth_box = {"x1": 120, "y1": 140, "x2": 280, "y2": 330}

        # 아래 함수는 두 박스의 IoU를 직접 계산하는 쉬운 예제입니다.
        def calculate_iou(box_a, box_b):
            # 교집합 좌표를 구합니다.
            inter_x1 = max(box_a["x1"], box_b["x1"])
            inter_y1 = max(box_a["y1"], box_b["y1"])
            inter_x2 = min(box_a["x2"], box_b["x2"])
            inter_y2 = min(box_a["y2"], box_b["y2"])

            # 겹치는 너비와 높이를 구합니다.
            inter_width = max(0, inter_x2 - inter_x1)
            inter_height = max(0, inter_y2 - inter_y1)
            inter_area = inter_width * inter_height

            # 각 박스의 넓이를 구합니다.
            area_a = (box_a["x2"] - box_a["x1"]) * (box_a["y2"] - box_a["y1"])
            area_b = (box_b["x2"] - box_b["x1"]) * (box_b["y2"] - box_b["y1"])

            union_area = area_a + area_b - inter_area
            return inter_area / union_area

        iou = calculate_iou(predicted_box, ground_truth_box)
        print("IoU:", round(iou, 4))
        # IoU가 1에 가까울수록 예측 박스와 정답 박스가 잘 겹친다는 뜻입니다.

        detections = [
            {"label": "helmet", "confidence": 0.93},
            {"label": "vest", "confidence": 0.88},
            {"label": "person", "confidence": 0.41},
        ]

        # threshold(임계값): 이 값보다 confidence가 낮으면 결과를 버리는 기준입니다.
        threshold = 0.5
        filtered = [d for d in detections if d["confidence"] >= threshold]

        print("임계값 적용 후 남은 탐지 결과:", filtered)
        # confidence가 낮은 박스를 제거하면 화면이 덜 복잡해지고 오탐을 줄일 수 있습니다.

        # 로보플로우 배포 아이디어
        # 1. 웹캠 안전모 탐지
        # 2. 공장 안전조끼 탐지
        # 3. 교실 물품 자동 카운팅
        # 4. 창고 박스 개수 세기
        # 5. 불량품 위치 찾기

        print("수업 마무리: 이제 학생들은 분류, 회귀, 군집, 딥러닝, CNN, 객체탐지의 큰 흐름을 연결해 볼 수 있습니다.")
        """,
    )
    lessons_md["day10_roboflow_inference_and_evaluation.md"] = lesson_md(
        10,
        "객체탐지 추론과 평가",
        "객체탐지 결과를 읽고 성능 지표를 이해하며 간단한 배포 아이디어까지 연결한다.",
        ["confidence", "IoU", "mAP", "threshold", "오탐", "미탐", "추론", "배포"],
        ["객체탐지 결과 화면을 읽을 수 있다.", "confidence와 threshold의 관계를 설명할 수 있다.", "IoU와 mAP의 의미를 말할 수 있다."],
    )

    return lessons_py, lessons_md


def build_overview() -> str:
    return dedent(
        """
        # 로보플로우를 활용한 객체탐지 수업 자료

        ## 구성
        - `instructor_files`: 강사용 파이썬 실습 파일 10개
        - `student_md`: 학생 배포용 마크다운 10개
        - `data`: 수업용 CSV 데이터셋

        ## 수업 설계 방향
        - 교재의 Chapter 01, 02, 03, 04, 06, 07, 08 내용을 초심자 수준으로 다시 재구성했습니다.
        - 마지막 2일은 로보플로우 객체탐지 워크플로우와 추론/평가 개념을 연결하도록 설계했습니다.
        - 강사용 파이썬 파일에는 모든 예제, 용어 설명, 실행 결과 해석을 주석으로 넣었습니다.
        - 학생용 마크다운에는 주석과 예시 코드를 넣지 않고 핵심 개념과 학습 체크포인트만 정리했습니다.

        ## 데이터셋
        - `market_fish_extended.csv`: 생선 분류용 1200행
        - `student_learning_extended.csv`: 점수 예측/합격 분류용 1500행
        - `fruit_traits_extended.csv`: 군집 실습용 1350행
        - `detection_annotations_extended.csv`: 객체탐지 좌표 이해용 1200행
        """
    ).strip()


def generate() -> None:
    ensure_dirs()

    write_csv(
        DATA_DIR / "market_fish_extended.csv",
        ["species", "length_cm", "weight_g", "tail_cm"],
        build_market_fish_rows(),
    )
    write_csv(
        DATA_DIR / "student_learning_extended.csv",
        ["study_hours", "practice_hours", "sleep_hours", "exam_score", "passed"],
        build_student_rows(),
    )
    write_csv(
        DATA_DIR / "fruit_traits_extended.csv",
        ["fruit", "sweetness", "crunch", "moisture"],
        build_fruit_rows(),
    )
    write_csv(
        DATA_DIR / "detection_annotations_extended.csv",
        ["image_id", "label", "image_width", "image_height", "x_center", "y_center", "box_width", "box_height", "split"],
        build_detection_rows(),
    )

    lessons_py, lessons_md = build_lessons()
    for file_name, content in lessons_py.items():
        write_text(INSTRUCTOR_DIR / file_name, content)
    for file_name, content in lessons_md.items():
        write_text(STUDENT_DIR / file_name, content)

    write_text(BASE_DIR / "README.md", build_overview())


if __name__ == "__main__":
    generate()
    import runpy
    runpy.run_path(str(BASE_DIR / "refresh_materials.py"), run_name="__main__")
