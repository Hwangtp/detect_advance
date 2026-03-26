# 15_Video.py

<div style="background: linear-gradient(135deg, #f59e0b, #f97316); color: #ffffff; padding: 18px 22px; border-radius: 16px; margin: 18px 0;">
  <h2 style="margin: 0 0 8px 0;">Video 실습</h2>
  <p style="margin: 0; line-height: 1.7;">동영상 파일을 읽고 처리하는 OpenCV 실습 파일입니다.</p>
</div>

<table>
  <tr>
    <td style="background-color:#fff7ed; border:1px solid #fdba74; border-radius:14px; padding:16px;">
      <strong style="color:#c2410c;">왜 중요한가</strong><br><br>
      이미지 처리보다 한 단계 확장된 영상 처리 흐름을 익히는 데 적합합니다.
    </td>
  </tr>
</table>

## 핵심 학습 포인트

<div style="background-color:#f8fafc; border:1px solid #cbd5e1; border-radius:14px; padding:16px; margin:12px 0;">
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li style="margin: 8px 0;"><strong style="color:#0f766e;">1.</strong> 동영상 파일 읽기</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">2.</strong> 프레임 처리</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">3.</strong> 영상 반복 처리</li>
  </ul>
</div>

## 추천 학습 방법

<div style="background-color:#ecfeff; border-left:8px solid #06b6d4; padding:16px 18px; border-radius:12px; margin:12px 0;">
  <ol style="margin:0; padding-left:20px; line-height:1.9;">
    <li><code>.py</code> 파일을 직접 실행해 예제 결과를 확인합니다.</li>
    <li>주석과 출력 결과를 함께 보며 코드 흐름을 따라갑니다.</li>
    <li>예제 값을 조금씩 바꿔 보며 어떤 점이 달라지는지 관찰합니다.</li>
    <li>마지막에는 비슷한 문제를 스스로 다시 작성해 봅니다.</li>
  </ol>
</div>

## 같이 보면 좋은 파일

<div style="background-color:#f5f3ff; border:1px solid #c4b5fd; border-radius:14px; padding:16px; margin:12px 0;">
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li><code>Overview.md</code></li>
    <li>이전 번호 파일과 다음 번호 파일</li>
    <li>같은 주제가 이어지는 후속 실습 파일</li>
  </ul>
</div>

## 코드

```python
import cv2

video_path = 'sample.mp4'

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():

    print(f"동영상 파일 '{video_path}'을 열 수 없습니다.")

    exit()

print("동영상 파일이 열렸습니다. 'q' 키를 눌러 종료하세요.")

while True:

    ret, frame = cap.read()

    if not ret:

        print("동영상 재생이 끝났습니다.")

        break

    cv2.imshow('Video', frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):

        break

cap.release()

cv2.destroyAllWindows()

print("동영상 실습이 종료되었습니다.")
```
