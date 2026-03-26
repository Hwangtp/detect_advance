# 07_Control_Structures_2.py

<div style="background: linear-gradient(135deg, #f59e0b, #f97316); color: #ffffff; padding: 18px 22px; border-radius: 16px; margin: 18px 0;">
  <h2 style="margin: 0 0 8px 0;">제어문 2</h2>
  <p style="margin: 0; line-height: 1.7;">for, while 반복문과 컴프리헨션을 다루는 파일입니다.</p>
</div>

<table>
  <tr>
    <td style="background-color:#fff7ed; border:1px solid #fdba74; border-radius:14px; padding:16px;">
      <strong style="color:#c2410c;">왜 중요한가?</strong><br><br>
      반복문은 여러 데이터를 한 번에 처리하는 핵심 도구이며, 컴프리헨션은 그 반복 처리를 더 간결하게 표현하는 방법입니다.
    </td>
  </tr>
</table>

## 학습 포인트

<div style="background-color:#f8fafc; border:1px solid #cbd5e1; border-radius:14px; padding:16px; margin:12px 0;">
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li style="margin: 8px 0;"><strong style="color:#0f766e;">1.</strong> for 반복문</li>
    <li style="margin: 8px 0;"><strong style="color:#0f766e;">2.</strong> while 반복문</li>
    <li style="margin: 8px 0;"><strong style="color:#0f766e;">3.</strong> 리스트 컴프리헨션</li>
    <li style="margin: 8px 0;"><strong style="color:#0f766e;">4.</strong> 딕셔너리 컴프리헨션</li>
  </ul>
</div>

## 추천 학습 방법

<div style="background-color:#ecfeff; border-left:8px solid #06b6d4; padding:16px 18px; border-radius:12px; margin:12px 0;">
  <ol style="margin:0; padding-left:20px; line-height:1.9;">
    <li><code>.py</code> 파일을 직접 실행해 예제 결과를 확인합니다.</li>
    <li>먼저 일반 반복문을 이해한 뒤, 같은 작업이 컴프리헨션에서 어떻게 표현되는지 비교합니다.</li>
    <li>반복, 조건, 자료 생성이 각각 어디에 들어가는지 문법 구조를 확인합니다.</li>
    <li>짧고 단순한 경우에는 컴프리헨션을, 복잡한 경우에는 일반 반복문을 사용하는 기준을 익힙니다.</li>
  </ol>
</div>

## 같이 보면 좋은 파일

<div style="background-color:#f5f3ff; border:1px solid #c4b5fd; border-radius:14px; padding:16px; margin:12px 0;">
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li><code>Overview.md</code></li>
    <li><code>06_Control_Structures_1.md</code></li>
    <li><code>04_Collections_Data_Structures.md</code></li>
  </ul>
</div>

## 반복문과 컴프리헨션

반복문은 같은 작업을 여러 번 수행할 때 사용하는 문법입니다.  
예를 들어 여러 이름을 출력하거나, 여러 숫자의 합을 구하거나, 리스트의 각 값을 변형할 때 반복문이 필요합니다.

이 파일에서는 `while`문과 `for`문을 다루고, 그 다음 단계로 컴프리헨션을 소개합니다.  
컴프리헨션은 반복문과 다른 별개의 개념이 아니라, **반복문으로 자료를 만들어 내는 작업을 더 간단하게 표현한 문법**입니다.

---

## 컴프리헨션이란?

컴프리헨션(comprehension)은 반복문을 사용해 새로운 컬렉션 자료를 만드는 간결한 표현입니다.

예를 들어 0부터 4까지의 제곱값을 리스트로 만들려면 일반적으로는 아래처럼 작성할 수 있습니다.

```python
squares = []

for x in range(5):
    squares.append(x**2)
```

이 코드는 반복하면서 값을 계산하고, 그 결과를 리스트에 넣는 과정을 분명하게 보여 줍니다.

같은 작업은 파이썬에서 더 짧게 표현할 수도 있습니다.

```python
squares = [x**2 for x in range(5)]
```

이처럼 **반복하면서 값을 만들어 리스트나 딕셔너리 같은 자료구조에 담는 문법**이 컴프리헨션입니다.

---

## 왜 컴프리헨션을 배우는가

컴프리헨션은 단지 코드를 줄이기 위한 기술이 아닙니다.

- 반복문으로 새 자료를 만드는 패턴이 자주 등장한다
- `for`문과 `append()`의 관계를 더 잘 이해하게 된다
- 코드를 짧고 읽기 좋게 표현할 수 있다
- 파이썬에서 자주 보이는 문법에 익숙해질 수 있다

즉, 컴프리헨션은 새로운 어려운 문법이라기보다  
**이미 알고 있는 반복문을 더 압축해서 표현한 방식**으로 볼 수 있습니다.

---

## 리스트 컴프리헨션의 기본 문법

리스트 컴프리헨션의 기본 형태는 다음과 같습니다.

```python
[표현식 for 변수 in 반복가능한값]
```

예를 들어

```python
[x**2 for x in range(5)]
```

이 코드는 다음 의미를 가집니다.

- `range(5)`에서 값을 하나씩 꺼낸다
- 꺼낸 값을 `x`에 넣는다
- `x**2`를 계산한다
- 계산 결과들을 리스트로 모은다

여기서 핵심은 **맨 앞의 표현식이 리스트에 실제로 들어갈 값**이라는 점입니다.

---

## 일반 반복문과 리스트 컴프리헨션의 관계

아래 두 코드는 같은 일을 합니다.

```python
result = []

for x in range(5):
    result.append(x + 1)
```

```python
result = [x + 1 for x in range(5)]
```

즉, 리스트 컴프리헨션은 다음 과정을 한 줄로 줄인 것입니다.

1. 빈 리스트를 만든다
2. 반복문을 돈다
3. 값을 계산한다
4. 리스트에 추가한다

따라서 리스트 컴프리헨션을 이해하려면 먼저 일반 `for`문을 정확히 이해하는 것이 중요합니다.

---

## 조건이 있는 리스트 컴프리헨션

리스트 컴프리헨션에는 조건도 붙일 수 있습니다.

기본 형태는 다음과 같습니다.

```python
[표현식 for 변수 in 반복가능한값 if 조건식]
```

예를 들어 짝수만 리스트로 만들고 싶다면

```python
[x for x in range(10) if x % 2 == 0]
```

이 코드는 다음처럼 해석할 수 있습니다.

- 0부터 9까지 반복하면서
- 짝수인 경우만 통과시키고
- 통과한 값을 리스트에 넣는다

즉, 조건이 있는 리스트 컴프리헨션은 **반복하면서 필요한 값만 골라 새 리스트를 만드는 문법**입니다.

---

## 리스트 컴프리헨션은 언제 유용한가

리스트 컴프리헨션은 다음과 같은 상황에서 특히 잘 어울립니다.

- 기존 값을 변형해서 새 리스트를 만들 때
- 특정 조건을 만족하는 값만 걸러낼 때
- 짧고 규칙적인 반복 작업을 할 때
- 결과가 새 리스트 생성이라는 점이 분명할 때

```python
names = ["kim", "lee", "park"]
upper_names = [name.upper() for name in names]
```

위 코드는 문자열 목록을 모두 대문자로 바꾼 새 리스트를 만드는 예입니다.

---

## 리스트 컴프리헨션의 장점

리스트 컴프리헨션의 대표적인 장점은 다음과 같습니다.

- 코드가 짧아진다
- 새 리스트를 만든다는 목적이 바로 보인다
- 반복과 결과 생성이 한 줄에 드러난다
- 파이썬다운 코드 스타일에 익숙해질 수 있다

특히 단순한 변환과 필터링 작업에서는 일반 반복문보다 더 읽기 쉬운 경우가 많습니다.

---

## 리스트 컴프리헨션의 주의점

컴프리헨션은 편리하지만 항상 더 좋은 것은 아닙니다.

아래와 같은 경우에는 일반 반복문이 더 적합할 수 있습니다.

- 조건이 너무 많을 때
- 중첩이 복잡할 때
- 한 줄이 지나치게 길어질 때
- 중간 과정이 많아 한 번에 읽기 어려울 때

중요한 기준은 "짧은가"보다 "읽기 쉬운가"입니다.

---

## 딕셔너리 컴프리헨션

컴프리헨션은 리스트뿐 아니라 딕셔너리에도 사용할 수 있습니다.

기본 형태는 다음과 같습니다.

```python
{key표현식: value표현식 for 변수 in 반복가능한값}
```

예를 들면

```python
{x: x**2 for x in range(5)}
```

이 코드는 다음 딕셔너리를 만듭니다.

```python
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

딕셔너리 컴프리헨션은 반복을 통해 일정한 규칙의 `key-value` 쌍을 만들 때 유용합니다.

---

## 핵심 정리

리스트 컴프리헨션은 **반복문으로 값을 하나씩 만들어 리스트에 넣는 과정을 짧고 명확하게 표현하는 파이썬 문법**입니다.

컴프리헨션은 반복문을 없애는 문법이 아니라, 반복문으로 하는 단순한 자료 생성 작업을 간결하게 표현하는 방법입니다.

## 코드

```python
count = 0

while count < 3:

    print(count)

    count += 1

while True:

    print("무한 루프")

    break

num = 0

while num < 5:

    num += 1

    if num == 3:

        continue

    print(num)

i = 0

while i < 10:

    i += 1

    if i % 2 == 0:

        continue

    print(i)

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:

    print(fruit)

for i in range(3):

    print(i)

for i in range(1, 6):

    print(i)

for i in range(0, 10, 2):

    print(i)

for i in range(5):

    if i == 2:

        continue

    print(i)

squares_for = []

for x in range(5):

    squares_for.append(x**2)

print(squares_for)

squares = [x**2 for x in range(5)]

print(squares)

even_numbers = [x for x in range(10) if x % 2 == 0]

print(even_numbers)

squares_dict = {x: x**2 for x in range(5)}

print(squares_dict)

for i in range(3):

    for j in range(2):

        print(f"i={i}, j={j}")

for i in range(1, 6):

    print(i)

total = 0

i = 1

while i <= 10:

    total += i

    i += 1

print("합", total)
```
