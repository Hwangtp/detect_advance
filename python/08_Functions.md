# 08_Functions.py

<div style="background: linear-gradient(135deg, #f59e0b, #f97316); color: #ffffff; padding: 18px 22px; border-radius: 16px; margin: 18px 0;">
  <h2 style="margin: 0 0 8px 0;">함수</h2>
  <p style="margin: 0; line-height: 1.7;">함수 정의, 매개변수, 반환값을 익히는 핵심 파일입니다.</p>
</div>

<table>
  <tr>
    <td style="background-color:#fff7ed; border:1px solid #fdba74; border-radius:14px; padding:16px;">
      <strong style="color:#c2410c;">왜 중요한가</strong><br><br>
      코드를 재사용 가능하고 읽기 좋게 나누는 능력을 길러 줍니다.
    </td>
  </tr>
</table>

## 핵심 학습 포인트

<div style="background-color:#f8fafc; border:1px solid #cbd5e1; border-radius:14px; padding:16px; margin:12px 0;">
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li style="margin: 8px 0;"><strong style="color:#0f766e;">1.</strong> 함수 정의</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">2.</strong> 매개변수</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">3.</strong> 반환값</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">4.</strong> 여러 값 반환</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">5.</strong> 재사용</li>
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
def greet():

    print("Hello!")

greet()

def add(a, b):

    return a + b

result = add(5, 3)

print(result)

def func1():

    print("No input, no return")

def func2(x):

    print(f"Input: {x}")

def func3():

    return "Return value"

def func4(x):

    return x * 2

def introduce(name, age):

    print(f"이름: {name}, 나이: {age}")

introduce(age=25, name="Alice")

def sum_all(*args):

    total = 0

    for num in args:

        total += num

    return total

print(sum_all(1, 2, 3, 4))

def print_info(**kwargs):

    for key, value in kwargs.items():

        print(f"{key}: {value}")

print_info(name="Bob", age=30, city="Seoul")

def return_multiple():

    return 1, 2, 3

a, b, c = return_multiple()

print(a, b, c)

def greet_person(name, greeting="Hello"):

    print(f"{greeting}, {name}!")

greet_person("Charlie")

greet_person("David", "Hi")

def test_scope():

    local_var = "local"

    print(local_var)

test_scope()

global_var = "global"

def change_global():

    global global_var

    global_var = "changed"

change_global()

print(global_var)

square = lambda x: x ** 2

print(square(5))

students = [("Kim", 90), ("Lee", 75), ("Park", 88)]

sorted_students = sorted(students, key=lambda student: student[1])

print(sorted_students)

numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))

print(doubled)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
```
