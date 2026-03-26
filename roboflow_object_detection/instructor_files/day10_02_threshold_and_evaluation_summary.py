# pip install pandas

"""Day 10-2. 임계값과 평가 요약.

이 파일은 confidence threshold를 바꾸면 정밀도와 재현율이 어떻게 달라지는지
고정된 예측 예제로 계산해 보는 마무리 수업이다.
"""

# pandas는 CSV 표 데이터를 읽고, 열 이름 기준으로 선택하고, 통계를 확인할 때 가장 많이 사용하는 라이브러리다.
import pandas as pd

# 예상 출력 핵심:
# - threshold 0.9에서는 precision 1.0, recall 0.3333으로 출력된다.
# - threshold 0.6에서는 precision 0.6667, recall 0.6667로 균형이 맞는다.
# - 마지막 해석 문장은 오탐을 줄이려면 threshold를 높이고, 놓침을 줄이려면 낮춘다고 정리한다.

print("=== Day 10-2: 임계값과 평가 요약 ===")

# 아래 표는 예측 하나마다 confidence와 실제 정답 여부를 정리한 고정 예시다.
predictions = pd.DataFrame([
    {'confidence': 0.95, 'is_true_positive': True},
    {'confidence': 0.91, 'is_true_positive': True},
    {'confidence': 0.88, 'is_true_positive': False},
    {'confidence': 0.83, 'is_true_positive': True},
    {'confidence': 0.72, 'is_true_positive': False},
    {'confidence': 0.67, 'is_true_positive': True},
    {'confidence': 0.55, 'is_true_positive': False},
    {'confidence': 0.49, 'is_true_positive': True},
])

# 전체 정답 객체 수를 고정해 두면 threshold에 따라 놓친 개수도 계산할 수 있다.
total_ground_truth = 6
print("\n[실습 1] 예측 표")
print(predictions.to_string(index=False))


def evaluate_at_threshold(threshold: float) -> dict:
    # threshold 이상만 남기는 이유는 confidence가 낮은 예측을 버리기 위해서다.
    kept = predictions[predictions['confidence'] >= threshold]
    tp = int(kept['is_true_positive'].sum())
    fp = int(len(kept) - tp)
    fn = int(total_ground_truth - tp)
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / total_ground_truth if total_ground_truth else 0.0
    return {
        'threshold': threshold,
        'kept_predictions': int(len(kept)),
        'tp': tp,
        'fp': fp,
        'fn': fn,
        'precision': round(precision, 4),
        'recall': round(recall, 4),
    }

# 여러 threshold를 비교하면 값 하나를 바꿨을 때 평가 지표가 어떻게 움직이는지 확인할 수 있다.
results = pd.DataFrame([
    evaluate_at_threshold(0.9),
    evaluate_at_threshold(0.8),
    evaluate_at_threshold(0.6),
    evaluate_at_threshold(0.5),
])

print("\n[실습 2] threshold별 평가 요약")
print(results.to_string(index=False))

# 높은 threshold는 fp를 줄이지만 tp까지 줄일 수 있으므로 정밀도와 재현율 균형이 중요하다.
best_precision_row = results.sort_values(['precision', 'recall'], ascending=False).iloc[0]
best_recall_row = results.sort_values(['recall', 'precision'], ascending=False).iloc[0]
print("\n[실습 3] 가장 높은 precision 구간")
print(best_precision_row.to_dict())
print("\n[실습 4] 가장 높은 recall 구간")
print(best_recall_row.to_dict())

# 마지막으로 threshold 선택은 목표에 따라 달라진다는 문장을 출력해 수업을 정리한다.
print("\n[실습 5] 해석 문장")
print('오탐을 줄이고 싶으면 threshold를 높이고, 놓침을 줄이고 싶으면 threshold를 낮추는 쪽을 검토한다.')
