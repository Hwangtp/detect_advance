# Day 10-2. 임계값과 평가 요약

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 개요</h2>
  <p style="margin:0; line-height:1.8;">confidence threshold를 바꿨을 때 정밀도와 재현율이 어떻게 달라지는지 고정 예측 표로 계산하며 객체 탐지 평가를 정리합니다.</p>
</div>

<div style="background-color:#eff6ff; border:1px solid #93c5fd; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#1d4ed8;">오늘 실습 구성</h3>
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
<li>confidence와 정답 여부 표 읽기</li>
<li>threshold별 남는 예측 개수 계산</li>
<li>precision, recall, false negative 비교</li>
<li>상황에 따른 threshold 선택 해석</li>
  </ul>
</div>

<div style="background-color:#f0fdf4; border:1px solid #86efac; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#15803d;">수업 체크포인트</h3>
  <ol style="margin:0; padding-left:20px; line-height:1.8;">
<li>threshold가 올라가면 어떤 예측이 제거되는지 설명할 수 있다.</li>
<li>precision과 recall의 trade-off를 말할 수 있다.</li>
<li>탐지 평가를 실제 운영 목표와 연결해 해석할 수 있다.</li>
  </ol>
</div>

<div style="background-color:#fff7ed; border:1px solid #fdba74; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#c2410c;">학습 가이드</h3>
  <p style="margin:0; line-height:1.9;">수업 마지막 파일은 수치 계산보다 해석이 더 중요합니다. threshold를 하나로 외우기보다, 어떤 상황에서 오탐을 더 싫어하고 어떤 상황에서 놓침을 더 싫어하는지 연결해서 생각해 보는 것이 핵심입니다.</p>
</div>

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
import pandas as pd

print("=== Day 10-2: 임계값과 평가 요약 ===")


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


total_ground_truth = 6
print("\n[실습 1] 예측 표")
print(predictions.to_string(index=False))

def evaluate_at_threshold(threshold: float) -> dict:

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


results = pd.DataFrame([
    evaluate_at_threshold(0.9),
    evaluate_at_threshold(0.8),
    evaluate_at_threshold(0.6),
    evaluate_at_threshold(0.5),
])

print("\n[실습 2] threshold별 평가 요약")
print(results.to_string(index=False))


best_precision_row = results.sort_values(['precision', 'recall'], ascending=False).iloc[0]
best_recall_row = results.sort_values(['recall', 'precision'], ascending=False).iloc[0]
print("\n[실습 3] 가장 높은 precision 구간")
print(best_precision_row.to_dict())
print("\n[실습 4] 가장 높은 recall 구간")
print(best_recall_row.to_dict())


print("\n[실습 5] 해석 문장")
print('오탐을 줄이고 싶으면 threshold를 높이고, 놓침을 줄이고 싶으면 threshold를 낮추는 쪽을 검토한다.')
```
