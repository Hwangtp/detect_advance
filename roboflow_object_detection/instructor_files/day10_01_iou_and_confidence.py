# 추가 설치 없음

"""Day 10-1. IoU와 confidence 이해.

이 파일은 예측 박스와 정답 박스를 직접 숫자로 놓고 IoU를 계산해 보며,
confidence 점수가 왜 함께 해석되어야 하는지 설명한다.
"""

# 예상 출력 핵심:
# - 좋은 예측 IoU는 0.7021, 나쁜 예측 IoU는 0.0345로 출력된다.
# - confidence는 나쁜 예측 쪽이 0.97로 더 높지만 IoU 기준은 통과하지 못한다.
# - 즉 IoU와 confidence를 함께 봐야 한다는 메시지가 핵심이다.

def compute_iou(box_a, box_b):
    # 박스는 [x1, y1, x2, y2] 형식이라고 가정한다.
    ax1, ay1, ax2, ay2 = box_a
    bx1, by1, bx2, by2 = box_b

    # 겹치는 영역의 왼쪽 위와 오른쪽 아래 좌표를 구한다.
    inter_x1 = max(ax1, bx1)
    inter_y1 = max(ay1, by1)
    inter_x2 = min(ax2, bx2)
    inter_y2 = min(ay2, by2)

    # 겹치지 않으면 너비나 높이가 음수가 되므로 0으로 보정한다.
    inter_w = max(0, inter_x2 - inter_x1)
    inter_h = max(0, inter_y2 - inter_y1)
    inter_area = inter_w * inter_h

    # 두 박스 전체 면적에서 겹친 부분을 한 번 빼면 합집합 면적이 된다.
    area_a = (ax2 - ax1) * (ay2 - ay1)
    area_b = (bx2 - bx1) * (by2 - by1)
    union_area = area_a + area_b - inter_area

    return inter_area / union_area if union_area else 0.0


print("=== Day 10-1: IoU와 confidence 이해 ===")

# 정답 박스와 예측 박스를 직접 정해 두면 계산 과정을 수업에서 손으로 따라가기 쉽다.
ground_truth = [40, 30, 140, 150]
prediction_good = [50, 40, 150, 160]
prediction_bad = [120, 110, 220, 230]

print("\n[실습 1] 정답 박스와 예측 박스")
print({'정답': ground_truth, '좋은예측': prediction_good, '나쁜예측': prediction_bad})

# IoU가 높을수록 위치가 잘 맞았다는 뜻이다.
iou_good = compute_iou(ground_truth, prediction_good)
iou_bad = compute_iou(ground_truth, prediction_bad)
print("\n[실습 2] IoU 비교")
print({'좋은예측 IoU': round(iou_good, 4), '나쁜예측 IoU': round(iou_bad, 4)})

# confidence는 모델이 스스로 얼마나 확신하는지를 뜻하지만, 위치 정확도와는 다른 값이다.
confidence_good = 0.93
confidence_bad = 0.97
print("\n[실습 3] confidence 비교")
print({'좋은예측 confidence': confidence_good, '나쁜예측 confidence': confidence_bad})

# confidence가 더 높아도 IoU가 낮으면 탐지 품질은 좋지 않을 수 있다는 점을 강조한다.
print("\n[실습 4] IoU 0.5 기준 통과 여부")
print({
    '좋은예측 통과': iou_good >= 0.5,
    '나쁜예측 통과': iou_bad >= 0.5,
})

# 실제 수업에서는 confidence와 IoU를 함께 봐야 한다는 문장을 결과와 연결해 보여 준다.
print("\n[실습 5] 해석 문장")
print('confidence가 0.97로 더 높아도 IoU가 낮으면 좋은 탐지라고 할 수 없다.')
