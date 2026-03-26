# 05_Data_Type_2.py

<div style="background: linear-gradient(135deg, #f59e0b, #f97316); color: #ffffff; padding: 18px 22px; border-radius: 16px; margin: 18px 0;">
  <h2 style="margin: 0 0 8px 0;">데이터 타입 2</h2>
  <p style="margin: 0; line-height: 1.7;">집합, 불 자료형, 복사, 언패킹 등 자료형 확장 내용을 다룹니다.</p>
</div>

<table>
  <tr>
    <td style="background-color:#fff7ed; border:1px solid #fdba74; border-radius:14px; padding:16px;">
      <strong style="color:#c2410c;">왜 중요한가</strong><br><br>
      기초 자료형을 실제 문제 해결에 더 자연스럽게 연결하는 데 도움을 줍니다.
    </td>
  </tr>
</table>

## 핵심 학습 포인트

<div style="background-color:#f8fafc; border:1px solid #cbd5e1; border-radius:14px; padding:16px; margin:12px 0;">
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li style="margin: 8px 0;"><strong style="color:#0f766e;">1.</strong> set</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">2.</strong> bool</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">3.</strong> 복사</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">4.</strong> 언패킹</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">5.</strong> truthy/falsy</li>
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
set1 = {1, 2, 3}

print(set1)

set2 = {2, 3, 4}

print(set1 & set2)

print(set1 | set2)

print(set1 - set2)

print(set1 ^ set2)

set1.add(4)

print(set1)

set1.remove(2)

print(set1)

print(len(set1))

is_true = True

is_false = False

print(is_true)

print(is_false)

print(1 == 1)

print(1 != 2)

print(5 > 3 and 2 < 4)

print(5 > 3 or 2 > 4)

print(not True)

print(bool(0))

print(bool(1))

print(bool(""))

print(bool("hello"))

print(bool([]))

print(bool([1, 2]))

x = 10

y = "Hello"

print(x, y)

original = [1, 2, 3]

copy_list = original[:]

print(copy_list)

a, b, c = 1, 2, 3

print(a, b, c)

print(5 + 3)

print("Hi")

my_list = [1, 2, 3]

print(len(my_list))
```
