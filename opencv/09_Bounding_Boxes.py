# 09_Bounding_Boxes.py
# 바운딩 박스
# 객체 검출 결과를 바운딩 박스로 표시하고 관리하는 방법을 학습합니다.
# 설치: pip install opencv-python numpy
# 실행: python 09_Bounding_Boxes.py

import cv2  # OpenCV 라이브러리
import numpy as np  # NumPy 라이브러리

print("OpenCV 바운딩 박스")
print("=" * 50)

# ========== 샘플 이미지 생성 ==========

print("\n1. 샘플 이미지 생성")

# 바운딩 박스 데모를 위한 샘플 이미지
sample_img = np.ones((500, 700, 3), dtype=np.uint8) * 255

# 여러 객체 배치
objects = [
    {"name": "person", "bbox": (50, 100, 80, 150), "color": (255, 200, 150)},
    {"name": "car", "bbox": (200, 150, 120, 80), "color": (0, 0, 255)},
    {"name": "dog", "bbox": (400, 200, 60, 40), "color": (139, 69, 19)},
    {"name": "chair", "bbox": (550, 250, 80, 100), "color": (139, 69, 19)},
    {"name": "bottle", "bbox": (150, 300, 20, 60), "color": (0, 255, 0)},
]

# 객체들을 이미지에 그리기
for obj in objects:
    x, y, w, h = obj["bbox"]
    cv2.rectangle(sample_img, (x, y), (x + w, y + h), obj["color"], -1)

    # 객체 이름 표시
    cv2.putText(sample_img, obj["name"], (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

print("샘플 이미지에 여러 객체를 배치했습니다.")

# ========== 바운딩 박스 클래스 정의 ==========

print("\n2. 바운딩 박스 클래스 정의")

class BoundingBox:
    """바운딩 박스를 관리하는 클래스"""

    def __init__(self, x, y, width, height, class_name="", confidence=1.0, color=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.class_name = class_name
        self.confidence = confidence
        self.color = color if color is not None else (255, 0, 0)

    def get_center(self):
        """바운딩 박스의 중심 좌표 반환"""
        return (self.x + self.width // 2, self.y + self.height // 2)

    def get_area(self):
        """바운딩 박스의 면적 계산"""
        return self.width * self.height

    def get_bbox(self):
        """바운딩 박스 좌표 반환 (x, y, w, h)"""
        return (self.x, self.y, self.width, self.height)

    def draw(self, image, thickness=2, show_label=True, show_confidence=True):
        """이미지에 바운딩 박스 그리기"""
        # 바운딩 박스 그리기
        cv2.rectangle(image, (self.x, self.y), (self.x + self.width, self.y + self.height), self.color, thickness)

        if show_label:
            # 라벨 텍스트 생성
            label = self.class_name
            if show_confidence and self.confidence < 1.0:
                label += ".2f"

            # 텍스트 크기 계산
            (text_width, text_height), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)

            # 텍스트 배경 그리기
            cv2.rectangle(image, (self.x, self.y - text_height - 10),
                         (self.x + text_width, self.y), self.color, -1)

            # 텍스트 그리기
            cv2.putText(image, label, (self.x, self.y - 5),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    def contains_point(self, point):
        """점이 바운딩 박스 안에 있는지 확인"""
        px, py = point
        return (self.x <= px <= self.x + self.width and
                self.y <= py <= self.y + self.height)

    def iou(self, other):
        """다른 바운딩 박스와의 IoU 계산"""
        # 좌표 변환
        x1_min, y1_min = self.x, self.y
        x1_max, y1_max = self.x + self.width, self.y + self.height
        x2_min, y2_min = other.x, other.y
        x2_max, y2_max = other.x + other.width, other.y + other.height

        # 교집합 영역 계산
        inter_x_min = max(x1_min, x2_min)
        inter_y_min = max(y1_min, y2_min)
        inter_x_max = min(x1_max, x2_max)
        inter_y_max = min(y1_max, y2_max)

        inter_area = max(0, inter_x_max - inter_x_min) * max(0, inter_y_max - inter_y_min)

        # 합집합 영역 계산
        union_area = self.get_area() + other.get_area() - inter_area

        if union_area == 0:
            return 0

        return inter_area / union_area

    def expand(self, margin):
        """바운딩 박스를 확장"""
        self.x -= margin
        self.y -= margin
        self.width += 2 * margin
        self.height += 2 * margin

    def shrink(self, margin):
        """바운딩 박스를 축소"""
        self.x += margin
        self.y += margin
        self.width -= 2 * margin
        self.height -= 2 * margin

# ========== 바운딩 박스 객체 생성 ==========

print("\n3. 바운딩 박스 객체 생성")

bboxes = []
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]

for i, obj in enumerate(objects):
    bbox = BoundingBox(
        obj["bbox"][0], obj["bbox"][1], obj["bbox"][2], obj["bbox"][3],
        obj["name"], 0.85 + i * 0.03, colors[i % len(colors)]
    )
    bboxes.append(bbox)
    print(f"바운딩 박스 생성: {bbox.class_name} at {bbox.get_bbox()}")

# ========== 바운딩 박스 조작 ==========

print("\n4. 바운딩 박스 조작")

# 바운딩 박스 정보 출력
for bbox in bboxes:
    center = bbox.get_center()
    area = bbox.get_area()
    print(f"{bbox.class_name}: 중심=({center[0]}, {center[1]}), 면적={area}")

# 바운딩 박스 확장/축소
expanded_bboxes = []
for bbox in bboxes:
    expanded = BoundingBox(bbox.x, bbox.y, bbox.width, bbox.height, bbox.class_name, bbox.confidence, bbox.color)
    expanded.expand(10)  # 10픽셀 확장
    expanded_bboxes.append(expanded)
    print(f"{bbox.class_name} 확장: {expanded.get_bbox()}")

# ========== 바운딩 박스 시각화 ==========

print("\n5. 바운딩 박스 시각화")

# 원본 바운딩 박스 표시
original_display = sample_img.copy()
for bbox in bboxes:
    bbox.draw(original_display)

# 확장된 바운딩 박스 표시
expanded_display = sample_img.copy()
for bbox in expanded_bboxes:
    bbox.draw(expanded_display, thickness=1)

# ========== IoU 계산 및 표시 ==========

print("\n6. IoU 계산")

# 모든 바운딩 박스 쌍에 대한 IoU 계산
iou_matrix = np.zeros((len(bboxes), len(bboxes)))

for i in range(len(bboxes)):
    for j in range(len(bboxes)):
        if i != j:
            iou_matrix[i, j] = bboxes[i].iou(bboxes[j])

print("IoU 행렬:")
print(iou_matrix)

# 높은 IoU를 가진 박스 쌍 찾기
high_iou_pairs = []
for i in range(len(bboxes)):
    for j in range(i + 1, len(bboxes)):
        iou = iou_matrix[i, j]
        if iou > 0.1:  # 10% 이상 겹치는 경우
            high_iou_pairs.append((i, j, iou))

print(f"높은 IoU를 가진 박스 쌍: {len(high_iou_pairs)}개")
for i, j, iou in high_iou_pairs:
    print(".3f")

# ========== 바운딩 박스 그룹화 ==========

print("\n7. 바운딩 박스 그룹화")

def group_bboxes_by_class(bboxes):
    """클래스별로 바운딩 박스 그룹화"""
    groups = {}
    for bbox in bboxes:
        class_name = bbox.class_name
        if class_name not in groups:
            groups[class_name] = []
        groups[class_name].append(bbox)
    return groups

def find_overlapping_groups(bboxes, iou_threshold=0.3):
    """겹치는 바운딩 박스 그룹 찾기"""
    groups = []
    used = [False] * len(bboxes)

    for i in range(len(bboxes)):
        if used[i]:
            continue

        group = [i]
        used[i] = True

        for j in range(i + 1, len(bboxes)):
            if not used[j] and bboxes[i].iou(bboxes[j]) > iou_threshold:
                group.append(j)
                used[j] = True

        if len(group) > 1:
            groups.append(group)

    return groups

# 클래스별 그룹화
class_groups = group_bboxes_by_class(bboxes)
print("클래스별 그룹:")
for class_name, group_bboxes in class_groups.items():
    print(f"  {class_name}: {len(group_bboxes)}개")

# 겹치는 그룹 찾기
overlapping_groups = find_overlapping_groups(bboxes, 0.1)
print(f"겹치는 그룹 수: {len(overlapping_groups)}")

# ========== 바운딩 박스 필터링 ==========

print("\n8. 바운딩 박스 필터링")

def filter_bboxes_by_area(bboxes, min_area=None, max_area=None):
    """면적 기준으로 바운딩 박스 필터링"""
    filtered = []
    for bbox in bboxes:
        area = bbox.get_area()
        if ((min_area is None or area >= min_area) and
            (max_area is None or area <= max_area)):
            filtered.append(bbox)
    return filtered

def filter_bboxes_by_confidence(bboxes, min_confidence=0.5):
    """신뢰도 기준으로 바운딩 박스 필터링"""
    return [bbox for bbox in bboxes if bbox.confidence >= min_confidence]

# 면적 필터링
small_bboxes = filter_bboxes_by_area(bboxes, max_area=5000)
large_bboxes = filter_bboxes_by_area(bboxes, min_area=5000)

print(f"작은 객체: {len(small_bboxes)}개")
print(f"큰 객체: {len(large_bboxes)}개")

# 신뢰도 필터링
high_conf_bboxes = filter_bboxes_by_confidence(bboxes, 0.9)
print(f"높은 신뢰도 객체: {len(high_conf_bboxes)}개")

# ========== 결과 표시 ==========

print("\n9. 결과 표시")

# 필터링 결과 표시
filtered_display = sample_img.copy()
for bbox in small_bboxes:
    bbox.draw(filtered_display, color=(0, 255, 0))  # 초록색으로 작은 객체

for bbox in large_bboxes:
    bbox.draw(filtered_display, color=(255, 0, 0))  # 빨강색으로 큰 객체

# 모든 결과 표시
cv2.imshow('Original BBoxes', original_display)
cv2.imshow('Expanded BBoxes', expanded_display)
cv2.imshow('Filtered BBoxes', filtered_display)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ========== 이미지 저장 ==========

print("\n10. 이미지 저장")

cv2.imwrite('bboxes_original.jpg', original_display)
cv2.imwrite('bboxes_expanded.jpg', expanded_display)
cv2.imwrite('bboxes_filtered.jpg', filtered_display)

print("바운딩 박스 결과를 이미지 파일로 저장했습니다.")

# ========== 미션 ==========
print("\n" + "="*50)
print("미션: 바운딩 박스 실습")
print("1. 바운딩 박스의 면적을 기준으로 정렬하는 함수를 만들어보세요.")
print("2. 두 바운딩 박스의 교집합 영역을 계산하는 함수를 추가하세요.")
print("3. 바운딩 박스를 JSON 형식으로 저장하고 불러오는 기능을 구현하세요.")
print("4. 바운딩 박스의 종횡비(aspect ratio)를 계산하는 메서드를 추가하세요.")

print("\n정답:")
print("""
import json

# 1. 면적 기준 정렬
def sort_bboxes_by_area(bboxes, descending=True):
    return sorted(bboxes, key=lambda bbox: bbox.get_area(), reverse=descending)

sorted_bboxes = sort_bboxes_by_area(bboxes)
for bbox in sorted_bboxes:
    print(f"{bbox.class_name}: {bbox.get_area()}")

# 2. 교집합 영역 계산
def get_intersection_area(bbox1, bbox2):
    x1, y1 = max(bbox1.x, bbox2.x), max(bbox1.y, bbox2.y)
    x2, y2 = min(bbox1.x + bbox1.width, bbox2.x + bbox2.width), min(bbox1.y + bbox1.height, bbox2.y + bbox2.height)

    width = max(0, x2 - x1)
    height = max(0, y2 - y1)

    return width * height

# 3. JSON 저장/불러오기
def save_bboxes_to_json(bboxes, filename):
    data = []
    for bbox in bboxes:
        data.append({
            'x': bbox.x, 'y': bbox.y, 'width': bbox.width, 'height': bbox.height,
            'class_name': bbox.class_name, 'confidence': bbox.confidence,
            'color': bbox.color
        })

    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def load_bboxes_from_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    bboxes = []
    for item in data:
        bbox = BoundingBox(
            item['x'], item['y'], item['width'], item['height'],
            item['class_name'], item['confidence'], tuple(item['color'])
        )
        bboxes.append(bbox)

    return bboxes

# 저장 및 불러오기 테스트
save_bboxes_to_json(bboxes, 'bboxes.json')
loaded_bboxes = load_bboxes_from_json('bboxes.json')
print(f"저장된 바운딩 박스 수: {len(loaded_bboxes)}")

# 4. 종횡비 계산 메서드 추가 (BoundingBox 클래스에 추가)
def get_aspect_ratio(self):
    if self.height == 0:
        return 0
    return self.width / self.height

# BoundingBox 클래스에 메서드 추가 후 사용
for bbox in bboxes:
    ratio = bbox.get_aspect_ratio()
    print(f"{bbox.class_name} 종횡비: {ratio:.2f}")
""")

print("\n축하합니다! OpenCV 객체 검출 강의를 모두 완료했습니다!")
print("이제 실제 이미지와 비디오에서 객체를 검출할 수 있습니다.")