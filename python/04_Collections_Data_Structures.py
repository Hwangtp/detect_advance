# 04_Collections_Data_Structures_Combined.py
# 수업 설명: 이 파일에서는 컬렉션 자료구조(리스트, 튜플, 딕셔너리, 집합)의 개념과 실제 사용법을 배웁니다.
# 대상: 자바 등 기초프로그래밍 활용자, 초급 수준
# 파이썬 버전: 3.12, IDE: PyCharm 최신 버전

# 컬렉션 자료구조 설명: 개념과 선택 기준
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

# 설명문 전체를 먼저 출력해 수업 도입부로 사용합니다.
print(guide_text)

# =========================== 리스트 실습 예제 ===========================
print("=" * 60)
print("리스트 실습 예제")
print("=" * 60)

# 리스트 생성: 문자열 여러 개를 저장한 리스트를 생성합니다.
fruits = ["apple", "banana", "cherry"]
print("초기 리스트:", fruits)

# 리스트 인덱싱 및 슬라이싱
print("첫 번째 요소:", fruits[0])
print("슬라이싱 [1:3]:", fruits[1:3])
print("마지막 요소:", fruits[-1])

# 리스트 연산
list1 = [1, 2, 3]
list2 = [4, 5]
print("list1 + list2:", list1 + list2)
print("list1 * 2:", list1 * 2)

# 리스트 추가 및 수정
fruits.append("orange")
print("append 후:", fruits)

fruits[1] = "grape"
print("인덱스 1 수정 후:", fruits)

# 리스트 삭제
del fruits[2]
print("del fruits[2] 후:", fruits)

fruits.remove("apple")
print("remove('apple') 후:", fruits)

# 리스트 정렬 및 역순
numbers = [3, 1, 4, 1, 5]
numbers.append(9)
print("append(9) 후:", numbers)

numbers.sort()
print("sort() 후:", numbers)

numbers.reverse()
print("reverse() 후:", numbers)

# =========================== 튜플 실습 예제 ===========================
print("\n" + "=" * 60)
print("튜플 실습 예제")
print("=" * 60)

# 튜플 생성 및 기본 접근
tup = (1, 2, 3)
print("튜플:", tup)
print("첫 번째 요소:", tup[0])
print("튜플 길이:", len(tup))

# 튜플 언패킹
position = (10, 20)
print("좌표 튜플:", position)
print("x 좌표:", position[0])
print("y 좌표:", position[1])

x, y = position
print("언패킹 결과: x =", x, ", y =", y)

# =========================== 딕셔너리 실습 예제 ===========================
print("\n" + "=" * 60)
print("딕셔너리 실습 예제")
print("=" * 60)

# 딕셔너리 생성
person = {"name": "John", "age": 30}
print("초기 딕셔너리:", person)

# 딕셔너리 접근
print("name 값:", person["name"])

# 딕셔너리 항목 추가
person["city"] = "Seoul"
print("city 추가 후:", person)

# 딕셔너리 항목 삭제
del person["age"]
print("age 삭제 후:", person)

# 딕셔너리 메서드
print("모든 key:", person.keys())
print("모든 value:", person.values())
print("모든 key-value 쌍:", person.items())

# =========================== 집합 실습 예제 ===========================
print("\n" + "=" * 60)
print("집합 실습 예제")
print("=" * 60)

# 집합으로 중복 제거
numbers_with_dup = [1, 2, 2, 3, 3, 4, 5]
print("중복이 있는 리스트:", numbers_with_dup)

number_set = set(numbers_with_dup)
print("중복 제거 후 집합:", number_set)

# 집합 연산
other_set = {3, 4, 5, 6}
print("비교 집합:", other_set)
print("교집합 (number_set & other_set):", number_set & other_set)
print("합집합 (number_set | other_set):", number_set | other_set)

# =========================== 심화 예제 ===========================
print("\n" + "=" * 60)
print("심화 예제: 학생 정보 관리")
print("=" * 60)

# 학생 정보를 딕셔너리로 만들기
students = [
    {"name": "김철수", "age": 20, "scores": [85, 90, 95]},
    {"name": "이영희", "age": 21, "scores": [92, 88, 91]},
    {"name": "박민준", "age": 20, "scores": [78, 82, 85]}
]

# 학생 정보 출력
for student in students:
    print(f"이름: {student['name']}, 나이: {student['age']}, 점수: {student['scores']}")

print("\n미션: 학생 정보를 딕셔너리로 만들고, 이름과 점수를 출력하세요.")
print("정답:")
student = {"name": "김철수", "score": 95}
print("이름:", student["name"])
print("점수:", student["score"])
