# Day 10-1. IoU와 confidence 이해

<div style="background: linear-gradient(135deg, #0f766e, #14b8a6); color:#ffffff; padding:20px 24px; border-radius:18px; margin:18px 0;">
  <h2 style="margin:0 0 10px 0;">수업 개요</h2>
  <p style="margin:0; line-height:1.8;">정답 박스와 예측 박스를 직접 숫자로 비교하면서 IoU와 confidence가 각각 무엇을 뜻하는지 분리해서 이해합니다.</p>
</div>

<div style="background-color:#eff6ff; border:1px solid #93c5fd; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#1d4ed8;">오늘 실습 구성</h3>
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
<li>정답 박스와 예측 박스 좌표 읽기</li>
<li>IoU 직접 계산하기</li>
<li>좋은 예측과 나쁜 예측의 IoU 비교</li>
<li>confidence와 위치 정확도의 차이 설명</li>
  </ul>
</div>

<div style="background-color:#f0fdf4; border:1px solid #86efac; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#15803d;">수업 체크포인트</h3>
  <ol style="margin:0; padding-left:20px; line-height:1.8;">
<li>IoU가 겹친 정도를 나타내는 비율이라는 점을 설명할 수 있다.</li>
<li>confidence가 높아도 박스 위치가 틀릴 수 있다는 점을 이해한다.</li>
<li>탐지 평가는 IoU와 confidence를 함께 봐야 한다는 점을 말할 수 있다.</li>
  </ol>
</div>

<div style="background-color:#fff7ed; border:1px solid #fdba74; border-radius:16px; padding:16px 18px; margin:14px 0;">
  <h3 style="margin:0 0 10px 0; color:#c2410c;">학습 가이드</h3>
  <p style="margin:0; line-height:1.9;">탐지 모델을 해석할 때 가장 많이 헷갈리는 두 값이 IoU와 confidence입니다. 하나는 위치 정확도, 다른 하나는 확신 정도라는 점을 분리해서 이해하면 결과 화면을 훨씬 정확하게 읽을 수 있습니다.</p>
</div>

## 실습 코드

학생용 복습 자료이므로 아래 코드는 주석을 뺀 실행용 코드입니다. 수업 시간에는 그대로 복사해 실행하면서 결과를 확인하면 됩니다.

```python
def compute_iou(box_a, box_b):

    ax1, ay1, ax2, ay2 = box_a
    bx1, by1, bx2, by2 = box_b


    inter_x1 = max(ax1, bx1)
    inter_y1 = max(ay1, by1)
    inter_x2 = min(ax2, bx2)
    inter_y2 = min(ay2, by2)


    inter_w = max(0, inter_x2 - inter_x1)
    inter_h = max(0, inter_y2 - inter_y1)
    inter_area = inter_w * inter_h


    area_a = (ax2 - ax1) * (ay2 - ay1)
    area_b = (bx2 - bx1) * (by2 - by1)
    union_area = area_a + area_b - inter_area

    return inter_area / union_area if union_area else 0.0

print("=== Day 10-1: IoU와 confidence 이해 ===")


ground_truth = [40, 30, 140, 150]
prediction_good = [50, 40, 150, 160]
prediction_bad = [120, 110, 220, 230]

print("\n[실습 1] 정답 박스와 예측 박스")
print({'정답': ground_truth, '좋은예측': prediction_good, '나쁜예측': prediction_bad})


iou_good = compute_iou(ground_truth, prediction_good)
iou_bad = compute_iou(ground_truth, prediction_bad)
print("\n[실습 2] IoU 비교")
print({'좋은예측 IoU': round(iou_good, 4), '나쁜예측 IoU': round(iou_bad, 4)})


confidence_good = 0.93
confidence_bad = 0.97
print("\n[실습 3] confidence 비교")
print({'좋은예측 confidence': confidence_good, '나쁜예측 confidence': confidence_bad})


print("\n[실습 4] IoU 0.5 기준 통과 여부")
print({
    '좋은예측 통과': iou_good >= 0.5,
    '나쁜예측 통과': iou_bad >= 0.5,
})


print("\n[실습 5] 해석 문장")
print('confidence가 0.97로 더 높아도 IoU가 낮으면 좋은 탐지라고 할 수 없다.')
```
