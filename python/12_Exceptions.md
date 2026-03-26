# 12_Exceptions.py

<div style="background: linear-gradient(135deg, #f59e0b, #f97316); color: #ffffff; padding: 18px 22px; border-radius: 16px; margin: 18px 0;">
  <h2 style="margin: 0 0 8px 0;">예외 처리</h2>
  <p style="margin: 0; line-height: 1.7;">오류 상황을 다루는 try, except와 예외 개념을 설명하는 파일입니다.</p>
</div>

<table>
  <tr>
    <td style="background-color:#fff7ed; border:1px solid #fdba74; border-radius:14px; padding:16px;">
      <strong style="color:#c2410c;">왜 중요한가</strong><br><br>
      프로그램이 예상치 못한 상황에서도 멈추지 않도록 만드는 기본기를 길러 줍니다.
    </td>
  </tr>
</table>

## 핵심 학습 포인트

<div style="background-color:#f8fafc; border:1px solid #cbd5e1; border-radius:14px; padding:16px; margin:12px 0;">
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li style="margin: 8px 0;"><strong style="color:#0f766e;">1.</strong> 예외</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">2.</strong> try/except</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">3.</strong> 에러 유형</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">4.</strong> 안전한 코드</li>
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
try:

    x = 10 / 0

except ZeroDivisionError:

    print("0으로 나눌 수 없습니다.")

try:

    num = int("abc")

except (ValueError, TypeError) as e:

    print(f"Error: {e}")

try:

    result = 10 / 2

except ZeroDivisionError:

    print("Division by zero")

else:

    print(f"Result: {result}")

finally:

    print("Always executed")

try:

    file = open("nonexistent.txt", "r")

except FileNotFoundError:

    print("파일이 없습니다.")

def check_age(age):

    if age < 0:

        raise ValueError("Age cannot be negative")

    return age

try:

    check_age(-5)

except ValueError as e:

    print(e)

class CustomError(Exception):

    pass

try:

    raise CustomError("This is a custom error")

except CustomError as e:

    print(e)
```
