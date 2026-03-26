# 06_Control_Structures_1.py

<div style="background: linear-gradient(135deg, #f59e0b, #f97316); color: #ffffff; padding: 18px 22px; border-radius: 16px; margin: 18px 0;">
  <h2 style="margin: 0 0 8px 0;">제어문 1</h2>
  <p style="margin: 0; line-height: 1.7;">if, elif, else를 이용한 조건문을 학습하는 파일입니다.</p>
</div>

<table>
  <tr>
    <td style="background-color:#fff7ed; border:1px solid #fdba74; border-radius:14px; padding:16px;">
      <strong style="color:#c2410c;">왜 중요한가</strong><br><br>
      프로그램 흐름을 상황에 따라 바꾸는 사고방식을 처음 익히는 단계입니다.
    </td>
  </tr>
</table>

## 핵심 학습 포인트

<div style="background-color:#f8fafc; border:1px solid #cbd5e1; border-radius:14px; padding:16px; margin:12px 0;">
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li style="margin: 8px 0;"><strong style="color:#0f766e;">1.</strong> 조건문</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">2.</strong> 비교 연산</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">3.</strong> 분기 처리</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">4.</strong> 논리 연산</li>
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
age = 20

if age >= 18:

    print("성인입니다.")

if age < 18:

    print("미성년자입니다.")

else:

    print("성인입니다.")

score = 85

if score >= 90:

    print("A")

elif score >= 80:

    print("B")

else:

    print("C")

num = 10

if num > 0:

    if num % 2 == 0:

        print("양수이고 짝수입니다.")

    else:

        print("양수이고 홀수입니다.")

else:

    print("음수입니다.")

fruits = ["apple", "banana"]

if "apple" in fruits:

    print("사과가 있습니다.")

result = "성인" if age >= 18 else "미성년자"

print(result)

x = 5

if x > 0 and x < 10:

    print("x는 1부터 9 사이입니다.")

is_adult = True if age >= 18 else False

print("성인인가?", is_adult)
```
