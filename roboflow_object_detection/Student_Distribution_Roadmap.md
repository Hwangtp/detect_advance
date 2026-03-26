# Student Distribution Roadmap

<div style="background: linear-gradient(135deg, #1e3a8a 0%, #0f766e 45%, #ea580c 100%); color:#ffffff; padding:28px 30px; border-radius:24px; margin:18px 0 22px 0; box-shadow:0 18px 40px rgba(15, 23, 42, 0.18);">
  <h1 style="margin:0 0 12px 0; font-size:2rem;">학생 배포용 전체 학습 로드맵</h1>
  <p style="margin:0; line-height:1.9; font-size:1.05rem;">이 과정은 <strong>파이썬 기초</strong>에서 출발해 <strong>DB</strong>, <strong>Flask</strong>, <strong>OpenCV</strong>, <strong>머신러닝</strong>, <strong>딥러닝</strong>을 거쳐, 마지막에는 <strong>Roboflow + YOLO 기반 객체탐지 프로젝트</strong>를 완성하는 흐름으로 진행됩니다.</p>
</div>

<div style="display:grid; grid-template-columns:repeat(2, minmax(0, 1fr)); gap:14px; margin:18px 0;">
  <div style="background:linear-gradient(135deg, #eff6ff, #dbeafe); border:1px solid #93c5fd; border-radius:18px; padding:18px 20px;">
    <h3 style="margin:0 0 10px 0; color:#1d4ed8;">과정의 시작</h3>
    <p style="margin:0; line-height:1.8; color:#1e293b;">Python 문법과 코딩 기초 체력을 먼저 만들고, DB와 Flask로 데이터와 웹의 구조를 이해합니다.</p>
  </div>
  <div style="background:linear-gradient(135deg, #ecfeff, #cffafe); border:1px solid #67e8f9; border-radius:18px; padding:18px 20px;">
    <h3 style="margin:0 0 10px 0; color:#0f766e;">과정의 도착점</h3>
    <p style="margin:0; line-height:1.8; color:#1e293b;">학습된 <code>best.pt</code>를 이용해 웹캠과 영상에서 원하는 물체를 실제로 탐지하는 프로젝트를 완성합니다.</p>
  </div>
</div>

## 이 과정의 최종 목적

<div style="background:linear-gradient(135deg, #fff7ed, #ffedd5); border:1px solid #fdba74; border-radius:20px; padding:20px 22px; margin:14px 0 18px 0; box-shadow:0 8px 20px rgba(251, 146, 60, 0.12);">
  <h2 style="margin:0 0 12px 0; color:#c2410c;">우리가 마지막에 만들 결과물</h2>
  <ul style="margin:0; padding-left:20px; line-height:1.95; color:#431407;">
    <li>웹캠에서 물체를 실시간으로 탐지할 수 있다.</li>
    <li>영상 파일에서도 같은 모델로 물체를 탐지할 수 있다.</li>
    <li>Roboflow로 직접 만든 데이터셋으로 사용자 정의 객체를 탐지할 수 있다.</li>
    <li>YOLO를 이용해 실제 객체탐지 프로젝트를 완성할 수 있다.</li>
  </ul>
</div>

## 전체 학습 순서

<div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:22px; padding:18px 22px; margin:12px 0 18px 0;">
  <ol style="margin:0; padding-left:22px; line-height:2; color:#0f172a;">
    <li><strong>Python</strong> : 코딩의 가장 기본이 되는 문법과 사고방식을 익힙니다.</li>
    <li><strong>DB</strong> : 데이터를 저장하고 조회하는 구조를 배웁니다.</li>
    <li><strong>Flask</strong> : 웹 서비스의 기본 구조와 흐름을 이해합니다.</li>
    <li><strong>OpenCV</strong> : 이미지, 영상, 웹캠을 다루는 방법을 익힙니다.</li>
    <li><strong>머신러닝</strong> : 데이터로 규칙을 학습하는 기본 모델을 배웁니다.</li>
    <li><strong>딥러닝</strong> : MLP와 CNN을 통해 이미지 이해의 기반을 다집니다.</li>
    <li><strong>Roboflow + YOLO</strong> : 직접 만든 데이터셋으로 객체탐지 프로젝트를 완성합니다.</li>
  </ol>
</div>

### 1. Python

<div style="background:linear-gradient(135deg, #eff6ff, #f8fafc); border-left:8px solid #2563eb; border-radius:16px; padding:18px 20px; margin:12px 0;">
  <p style="margin:0; line-height:1.9;">변수, 조건문, 반복문, 함수, 클래스, 파일 입출력 같은 내용을 익히며 이후 모든 과목을 읽을 수 있는 기본 문해력을 만듭니다. 나중에 OpenCV 코드, Flask 코드, 머신러닝 코드를 읽는 힘도 여기서 시작됩니다.</p>
</div>

### 2. DB

<div style="background:linear-gradient(135deg, #f0fdf4, #f8fafc); border-left:8px solid #16a34a; border-radius:16px; padding:18px 20px; margin:12px 0;">
  <p style="margin:0; line-height:1.9;">SQL, 테이블 생성, 데이터 삽입과 조회, 수정과 삭제, JOIN, 서브쿼리 같은 내용을 배우며 데이터를 구조적으로 보는 힘을 기릅니다. 이 힘은 이후 Flask와 프로젝트 확장에도 연결됩니다.</p>
</div>

### 3. Flask

<div style="background:linear-gradient(135deg, #faf5ff, #f8fafc); border-left:8px solid #9333ea; border-radius:16px; padding:18px 20px; margin:12px 0;">
  <p style="margin:0; line-height:1.9;">라우팅, 템플릿, 폼 처리, DB 연결, CRUD, 파일 업로드를 배우며 웹 애플리케이션의 기본 구조를 익힙니다. 나중에는 객체탐지 결과를 웹 서비스처럼 보여주는 확장으로도 이어질 수 있습니다.</p>
</div>

### 4. OpenCV

<div style="background:linear-gradient(135deg, #ecfeff, #f8fafc); border-left:8px solid #0891b2; border-radius:16px; padding:18px 20px; margin:12px 0;">
  <p style="margin:0; line-height:1.9;">이미지 읽기, 영상 읽기, 웹캠 연결, 도형 그리기, 색공간 변환, 엣지 검출, 얼굴 인식 등을 배우며 카메라와 영상 입력을 실제로 다루는 감각을 익힙니다. 객체탐지 프로젝트에서 매우 중요한 준비 단계입니다.</p>
</div>

### 5. 머신러닝

<div style="background:linear-gradient(135deg, #fff7ed, #f8fafc); border-left:8px solid #ea580c; border-radius:16px; padding:18px 20px; margin:12px 0;">
  <p style="margin:0; line-height:1.9;">분류, 회귀, train/test split, 스케일링, 로지스틱 분류, KMeans 등을 배우며 모델이 데이터를 보고 규칙을 학습한다는 감각을 익힙니다. 이것은 객체탐지 모델을 이해하는 기초 체력입니다.</p>
</div>

### 6. 딥러닝

<div style="background:linear-gradient(135deg, #fefce8, #f8fafc); border-left:8px solid #ca8a04; border-radius:16px; padding:18px 20px; margin:12px 0;">
  <p style="margin:0; line-height:1.9;">MLP, 하이퍼파라미터, CNN을 배우며 이미지에서 특징을 어떻게 찾는지 이해합니다. 특히 CNN은 뒤에서 YOLO 객체탐지를 이해하는 가장 중요한 다리 역할을 합니다.</p>
</div>

### 7. Roboflow + YOLO 객체탐지

<div style="background:linear-gradient(135deg, #fee2e2, #fff7ed); border-left:8px solid #dc2626; border-radius:16px; padding:18px 20px; margin:12px 0; box-shadow:0 10px 24px rgba(220, 38, 38, 0.10);">
  <p style="margin:0 0 10px 0; line-height:1.9;"><strong>가장 중요한 최종 단계입니다.</strong> 객체탐지 데이터셋 구조, YOLO 형식, Roboflow 라벨링, <code>data.yaml</code>, YOLO 학습, <code>best.pt</code> 생성, 웹캠 탐지, 영상 탐지까지 실제 프로젝트 흐름을 다룹니다.</p>
  <p style="margin:0; line-height:1.9;">즉 후반부는 단순 이론이 아니라 최종 결과물을 완성하는 프로젝트 구간입니다.</p>
</div>

## 객체탐지에서 특히 중요한 구간

<div style="background:linear-gradient(135deg, #111827, #1f2937); color:#ffffff; border-radius:22px; padding:22px 24px; margin:18px 0;">
  <h2 style="margin:0 0 14px 0; color:#fbbf24;">객체탐지 핵심 구간</h2>
  <ol style="margin:0; padding-left:22px; line-height:2;">
    <li><strong>개념 연결 단계</strong> : CNN과 객체탐지의 연결을 이해합니다.</li>
    <li><strong>학습 준비 단계</strong> : 객체탐지 데이터셋 구조와 YOLO 학습 준비를 익힙니다.</li>
    <li><strong>실행 단계</strong> : IoU, confidence, threshold, webcam / video inference 실행까지 연결합니다.</li>
  </ol>
</div>

<div style="display:grid; grid-template-columns:repeat(3, minmax(0, 1fr)); gap:12px; margin:16px 0;">
  <div style="background:#eff6ff; border:1px solid #93c5fd; border-radius:16px; padding:16px;">
    <h4 style="margin:0 0 8px 0; color:#1d4ed8;">전체 목표 이해</h4>
    <p style="margin:0; line-height:1.8; color:#1e293b;"><code>object_detection_goal_map</code><br>과정의 최종 목적을 객체탐지 프로젝트로 선명하게 잡아 줍니다.</p>
  </div>
  <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:16px; padding:16px;">
    <h4 style="margin:0 0 8px 0; color:#15803d;">데이터셋과 학습</h4>
    <p style="margin:0; line-height:1.8; color:#1e293b;"><code>roboflow_custom_dataset_and_training</code><br>Roboflow 라벨링과 YOLO 학습 흐름을 연결합니다.</p>
  </div>
  <div style="background:#fff7ed; border:1px solid #fdba74; border-radius:16px; padding:16px;">
    <h4 style="margin:0 0 8px 0; color:#c2410c;">실행과 적용</h4>
    <p style="margin:0; line-height:1.8; color:#1e293b;"><code>webcam_and_video_detection_with_yolov8</code><br><code>best.pt</code>를 웹캠과 영상에 실제로 적용합니다.</p>
  </div>
</div>

## 학생이 마지막에 할 수 있어야 하는 것

<div style="background:linear-gradient(135deg, #f8fafc, #eef2ff); border:1px solid #c7d2fe; border-radius:20px; padding:20px 22px; margin:16px 0;">
  <ul style="margin:0; padding-left:20px; line-height:2; color:#1e293b;">
    <li>나는 Python으로 기본 코드를 읽고 작성할 수 있다.</li>
    <li>나는 데이터베이스와 웹의 기본 구조를 이해한다.</li>
    <li>나는 OpenCV로 이미지, 영상, 웹캠을 다룰 수 있다.</li>
    <li>나는 머신러닝과 딥러닝의 기본 흐름을 이해한다.</li>
    <li>나는 Roboflow로 데이터셋을 만들 수 있다.</li>
    <li>나는 YOLO로 객체탐지 모델을 학습시킬 수 있다.</li>
    <li>나는 학습된 <code>best.pt</code>를 이용해 웹캠과 영상에서 물체를 탐지할 수 있다.</li>
  </ul>
</div>

## 권장 학습 태도

<div style="background:linear-gradient(135deg, #fafaf9, #fef3c7); border:1px solid #fcd34d; border-radius:18px; padding:18px 20px; margin:16px 0;">
  <ul style="margin:0; padding-left:20px; line-height:1.95; color:#3f3f46;">
    <li>앞 단계가 완벽하지 않아도 다음 단계로 넘어가되, 흐름은 끊기지 않게 따라옵니다.</li>
    <li>코드를 외우기보다 "이 코드가 왜 필요한가"를 계속 연결해서 이해합니다.</li>
    <li>후반부 객체탐지 파트에서는 데이터 준비, 라벨링, 학습, 추론이 하나의 프로젝트라는 점을 항상 기억합니다.</li>
  </ul>
</div>

## 한 문장 정리

<div style="background: linear-gradient(135deg, #0f172a, #1e293b); color:#ffffff; border-radius:20px; padding:20px 24px; margin:18px 0; box-shadow:0 14px 30px rgba(15, 23, 42, 0.18);">
  <p style="margin:0; line-height:1.9; font-size:1.02rem;"><strong>이 전체 수업 과정은</strong> <code>Python -> DB -> Flask -> OpenCV -> 머신러닝 -> 딥러닝 -> Roboflow + YOLO 객체탐지</code><strong>로 이어지며, 최종 목적은 사용자가 정의한 물체를 웹캠과 영상에서 탐지하는 실제 프로젝트를 완성하는 것입니다.</strong></p>
</div>