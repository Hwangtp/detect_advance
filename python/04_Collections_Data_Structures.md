# 04_Collections_Data_Structures.py

<div style="background: linear-gradient(135deg, #f59e0b, #f97316); color: #ffffff; padding: 18px 22px; border-radius: 16px; margin: 18px 0;">
  <h2 style="margin: 0 0 8px 0;">컬렉션 자료구조</h2>
  <p style="margin: 0; line-height: 1.7;">리스트, 튜플, 딕셔너리, 집합의 개념과 실제 사용법을 함께 배우는 파일입니다.</p>
</div>

<table>
  <tr>
    <td style="background-color:#fff7ed; border:1px solid #fdba74; border-radius:14px; padding:16px;">
      <strong style="color:#c2410c;">왜 중요한가</strong><br><br>
      컬렉션 자료구조의 선택 기준을 이해하고, 실제로 코드에서 사용하는 감각을 익히는 단계입니다.
    </td>
  </tr>
</table>

## 핵심 학습 포인트

<div style="background-color:#f8fafc; border:1px solid #cbd5e1; border-radius:14px; padding:16px; margin:12px 0;">
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li style="margin: 8px 0;"><strong style="color:#0f766e;">1.</strong> 자료구조 개념과 선택 이유</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">2.</strong> 리스트 생성과 수정</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">3.</strong> 튜플 사용법</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">4.</strong> 딕셔너리 다루기</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">5.</strong> 집합과 중복 제거</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">6.</strong> 컬렉션 메서드 기초</li>
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
guide_text = """
Python 컬렉션 자료구조 설명문

1. 컬렉션이란?
컬렉션은 여러 개의 데이터를 하나로 묶어서 관리하는 자료형입니다.
파이썬에서는 리스트, 튜플, 딕셔너리, 집합이 대표적인 컬렉션입니다.

2. 왜 컬렉션을 사용할까?
프로그램은 보통 하나의 값보다 여러 값을 함께 다루는 일이 더 많습니다.
학생 이름 목록, 상품 정보, 좌표 값, 중복 없는 태그 목록처럼
여러 데이터를 체계적으로 저장하고 관리해야 할 때 컬렉션이 필요합니다.

3. 리스트(list)
- 순서가 있는 자료형
- 값의 추가, 수정, 삭제가 가능함
- 반복 처리에 많이 사용됨
- 예: 학생 목록, 점수 목록, 할 일 목록

4. 튜플(tuple)
- 순서가 있는 자료형
- 한 번 만들면 값을 바꿀 수 없음
- 고정된 데이터를 안전하게 보관할 때 적합함
- 예: 좌표, 날짜, RGB 색상값

5. 딕셔너리(dictionary)
- key와 value의 쌍으로 구성됨
- 이름표를 붙여 데이터를 관리하기 좋음
- 구조화된 데이터를 다룰 때 매우 자주 사용됨
- 예: 학생 1명의 이름, 나이, 전공 정보

6. 집합(set)
- 중복을 허용하지 않음
- 순서가 없음
- 중복 제거와 포함 여부 검사에 강함
- 예: 태그 모음, 중복 제거한 번호 목록

7. 선택 기준
- 순서대로 여러 값을 저장하면 리스트
- 값이 바뀌면 안 되면 튜플
- 항목 이름으로 관리하면 딕셔너리
- 중복 제거가 중요하면 집합

8. 핵심 메시지
자료구조는 문법 암기보다 선택이 중요합니다.
어떤 데이터를 어떤 방식으로 저장할지 판단하는 능력이
좋은 프로그램을 만드는 기본이 됩니다.
"""

print(guide_text)

print("=" * 60)

print("리스트 실습 예제")

print("=" * 60)

fruits = ["apple", "banana", "cherry"]

print("초기 리스트:", fruits)

print("첫 번째 요소:", fruits[0])

print("슬라이싱 [1:3]:", fruits[1:3])

print("마지막 요소:", fruits[-1])

list1 = [1, 2, 3]

list2 = [4, 5]

print("list1 + list2:", list1 + list2)

print("list1 * 2:", list1 * 2)

fruits.append("orange")

print("append 후:", fruits)

fruits[1] = "grape"

print("인덱스 1 수정 후:", fruits)

del fruits[2]

print("del fruits[2] 후:", fruits)

fruits.remove("apple")

print("remove('apple') 후:", fruits)

numbers = [3, 1, 4, 1, 5]

numbers.append(9)

print("append(9) 후:", numbers)

numbers.sort()

print("sort() 후:", numbers)

numbers.reverse()

print("reverse() 후:", numbers)

print("\n" + "=" * 60)

print("튜플 실습 예제")

print("=" * 60)

tup = (1, 2, 3)

print("튜플:", tup)

print("첫 번째 요소:", tup[0])

print("튜플 길이:", len(tup))

position = (10, 20)

print("좌표 튜플:", position)

print("x 좌표:", position[0])

print("y 좌표:", position[1])

x, y = position

print("언패킹 결과: x =", x, ", y =", y)

print("\n" + "=" * 60)

print("딕셔너리 실습 예제")

print("=" * 60)

person = {"name": "John", "age": 30}

print("초기 딕셔너리:", person)

print("name 값:", person["name"])

person["city"] = "Seoul"

print("city 추가 후:", person)

del person["age"]

print("age 삭제 후:", person)

print("모든 key:", person.keys())

print("모든 value:", person.values())

print("모든 key-value 쌍:", person.items())

print("\n" + "=" * 60)

print("집합 실습 예제")

print("=" * 60)

numbers_with_dup = [1, 2, 2, 3, 3, 4, 5]

print("중복이 있는 리스트:", numbers_with_dup)

number_set = set(numbers_with_dup)

print("중복 제거 후 집합:", number_set)

other_set = {3, 4, 5, 6}

print("비교 집합:", other_set)

print("교집합 (number_set & other_set):", number_set & other_set)

print("합집합 (number_set | other_set):", number_set | other_set)

print("\n" + "=" * 60)

print("심화 예제: 학생 정보 관리")

print("=" * 60)

students = [

    {"name": "김철수", "age": 20, "scores": [85, 90, 95]},

    {"name": "이영희", "age": 21, "scores": [92, 88, 91]},

    {"name": "박민준", "age": 20, "scores": [78, 82, 85]}

]

for student in students:

    print(f"이름: {student['name']}, 나이: {student['age']}, 점수: {student['scores']}")

print("\n미션: 학생 정보를 딕셔너리로 만들고, 이름과 점수를 출력하세요.")

print("정답:")

student = {"name": "김철수", "score": 95}

print("이름:", student["name"])

print("점수:", student["score"])
```
