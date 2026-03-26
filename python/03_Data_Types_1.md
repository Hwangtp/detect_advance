# 03_Data_Types_1.py

<div style="background: linear-gradient(135deg, #f59e0b, #f97316); color: #ffffff; padding: 18px 22px; border-radius: 16px; margin: 18px 0;">
  <h2 style="margin: 0 0 8px 0;">데이터 타입 1</h2>
  <p style="margin: 0; line-height: 1.7;">숫자형과 문자열의 기본 사용법을 다루는 파일입니다.</p>
</div>

<table>
  <tr>
    <td style="background-color:#fff7ed; border:1px solid #fdba74; border-radius:14px; padding:16px;">
      <strong style="color:#c2410c;">왜 중요한가</strong><br><br>
      자료형의 가장 기초인 숫자와 문자열을 다루는 감각을 익히는 단계입니다.
    </td>
  </tr>
</table>

## 핵심 학습 포인트

<div style="background-color:#f8fafc; border:1px solid #cbd5e1; border-radius:14px; padding:16px; margin:12px 0;">
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li style="margin: 8px 0;"><strong style="color:#0f766e;">1.</strong> 정수</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">2.</strong> 실수</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">3.</strong> 문자열</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">4.</strong> 슬라이싱</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">5.</strong> 문자열 포맷팅</li>
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
num1 = 10

num2 = 3.14

print(num1)

print(num2)

a = 5

b = 2

print(a + b)

print(a - b)

print(a * b)

print(a / b)

print(a // b)

print(a % b)

print(a ** b)

str1 = "Hello"

str2 = 'World'

print(str1)

print(str2)

str3 = "He said, 'Hello'"

print(str3)

str4 = """This is
a multi-line
string"""

print(str4)

str5 = "Python"

str6 = " is fun"

print(str5 + str6)

print(str5 * 3)

print(str5[0])

print(str5[-1])

print(str5[0:3])

print(str5[2:])

print(str5[:4])

name = "Alice"

age = 30

print("이름: %s, 나이: %d" % (name, age))

print("이름: {}, 나이: {}".format(name, age))

print(f"이름: {name}, 나이: {age}")

text = "hello world"

print(text.upper())

print(text.lower())

print(text.title())

print(text.replace("world", "Python"))
```
