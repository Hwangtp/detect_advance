# 01_Python_Basics_1.py

<div style="background: linear-gradient(135deg, #f59e0b, #f97316); color: #ffffff; padding: 18px 22px; border-radius: 16px; margin: 18px 0;">
  <h2 style="margin: 0 0 8px 0;">Python 기초 1</h2>
  <p style="margin: 0; line-height: 1.7;">Python의 첫 인상, 출력, 변수, 간단한 계산과 문자열 사용을 익히는 입문 파일입니다.</p>
</div>

<table>
  <tr>
    <td style="background-color:#fff7ed; border:1px solid #fdba74; border-radius:14px; padding:16px;">
      <strong style="color:#c2410c;">왜 중요한가</strong><br><br>
      프로그래밍을 처음 배우는 학습자가 Python 문법의 분위기에 익숙해지기 좋습니다.
    </td>
  </tr>
</table>

## 핵심 학습 포인트

<div style="background-color:#f8fafc; border:1px solid #cbd5e1; border-radius:14px; padding:16px; margin:12px 0;">
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li style="margin: 8px 0;"><strong style="color:#0f766e;">1.</strong> print 함수</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">2.</strong> 변수 선언</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">3.</strong> 기본 연산</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">4.</strong> 문자열 기초</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">5.</strong> Python의 특징</li>
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
print("Hello, Python!")

name = "Python"

print("Welcome to", name)

a = 10

b = 5

print("덧셈:", a + b)

print("뺄셈:", a - b)

print("곱셈:", a * b)

print("나눗셈:", a / b)

fruits = ["apple", "banana", "cherry"]

print("과일 목록:", fruits)

print("첫 번째 과일:", fruits[0])

age = 25

if age >= 20:

    print("성인입니다.")

else:

    print("미성년자입니다.")
```
