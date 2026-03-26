# 07_제어문_2.py
# 수업 설명: 이 파일에서는 while 문과 for 문의 사용법을 배웁니다.
# 대상: 자바 등 기초프로그래밍 활용자, 초급 수준
# 파이썬 버전: 3.12, IDE: PyCharm 최신 버전

# 실습 예제 1: while 문 기본
count = 0  # count 변수를 0으로 초기화합니다.
while count < 3:  # count가 3보다 작은 동안 반복합니다.
    print(count)  # 현재 count 값을 출력합니다.
    count += 1  # count를 1 증가시킵니다.

# 실습 예제 2: while 문 break
while True:  # 무한 루프를 시작합니다.
    print("무한 루프")  # "무한 루프"를 출력합니다.
    break  # 루프를 강제 종료합니다.

# 실습 예제 3: while 문 continue
num = 0  # num 변수를 0으로 초기화합니다.
while num < 5:  # num이 5보다 작은 동안 반복합니다.
    num += 1  # num을 1 증가시킵니다.
    if num == 3:  # num이 3이면
        continue  # 아래 코드를 건너뛰고 다음 반복으로 갑니다.
    print(num)  # num이 3이 아닐 때만 출력합니다.

# 실습 예제 4: while 문의 맨 처음으로 돌아가기
i = 0  # i 변수를 0으로 초기화합니다.
while i < 10:  # i가 10보다 작은 동안 반복합니다.
    i += 1  # i를 1 증가시킵니다.
    if i % 2 == 0:  # i가 짝수이면
        continue  # 아래 코드를 건너뛰고 다음 반복으로 갑니다.
    print(i)  # 홀수일 때만 i를 출력합니다.

# 실습 예제 5: 무한 루프 예제 (주의: 실제 실행 시 Ctrl+C로 중단)
# while True:  # 무한 루프 (실행하지 마세요)
#     print("Infinite loop")  # 계속 출력됩니다.

# 실습 예제 6: for 문 기본
fruits = ["apple", "banana", "cherry"]  # 리스트를 생성합니다.
for fruit in fruits:  # fruits 리스트의 각 요소를 fruit에 순차적으로 할당하며 반복합니다.
    print(fruit)  # 각 fruit를 출력합니다.

# 실습 예제 7: range 함수
for i in range(3):  # range(3)은 0, 1, 2를 생성합니다.
    print(i)  # i를 출력합니다.

# 실습 예제 8: range with start, end
for i in range(1, 6):  # range(1, 6)은 1, 2, 3, 4, 5를 생성합니다.
    print(i)  # i를 출력합니다.

# 실습 예제 9: range with step
for i in range(0, 10, 2):  # range(0, 10, 2)은 0, 2, 4, 6, 8을 생성합니다.
    print(i)  # i를 출력합니다.

# 실습 예제 10: for 문과 continue
for i in range(5):  # 0부터 4까지 반복합니다.
    if i == 2:  # i가 2이면
        continue  # 아래 코드를 건너뛰고 다음 반복으로 갑니다.
    print(i)  # i가 2가 아닐 때만 출력합니다.

# 실습 예제 11: for 문으로 리스트 만들기
squares_for = []  # 제곱값을 저장할 빈 리스트를 준비합니다.
for x in range(5):  # 0부터 4까지 반복합니다.
    squares_for.append(x**2)  # x의 제곱값을 리스트에 추가합니다.
print(squares_for)  # [0, 1, 4, 9, 16]을 출력합니다.

# 실습 예제 12: 리스트 컴프리헨션
squares = [x**2 for x in range(5)]  # 반복문과 append를 한 줄로 줄여 제곱값 리스트를 만듭니다.
print(squares)  # [0, 1, 4, 9, 16]을 출력합니다.

# 실습 예제 13: 조건이 있는 리스트 컴프리헨션
even_numbers = [x for x in range(10) if x % 2 == 0]  # 0부터 9까지 중 짝수만 골라 리스트를 만듭니다.
print(even_numbers)  # [0, 2, 4, 6, 8]을 출력합니다.

# 실습 예제 14: 딕셔너리 컴프리헨션
squares_dict = {x: x**2 for x in range(5)}  # 숫자와 그 제곱값을 key-value 형태의 딕셔너리로 만듭니다.
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}을 출력합니다.

# 실습 예제 15: 중첩 루프
for i in range(3):  # i가 0, 1, 2일 때
    for j in range(2):  # j가 0, 1일 때
        print(f"i={i}, j={j}")  # i와 j의 값을 출력합니다.

# 되새김 문제: 제어문 연습
# 1. 1부터 5까지 출력하세요.
for i in range(1, 6):  # 1부터 5까지 반복
    print(i)  # i 출력
# 2. while 문으로 1부터 10까지 합 계산
total = 0  # 합계를 저장할 변수 초기화
i = 1  # 시작 값
while i <= 10:  # i가 10 이하일 때 반복
    total += i  # total에 i를 더함
    i += 1  # i 증가
print("합:", total)  # 합 출력

# 미션: 1부터 100까지의 짝수 합을 계산하는 코드를 작성하세요. (힌트: for 문과 if 문)
# 정답:
# total = 0  # 합계 초기화
# for i in range(1, 101):  # 1부터 100까지 반복
#     if i % 2 == 0:  # 짝수인지 검사
#         total += i  # 짝수면 합계에 더함
# print("짝수 합:", total)  # 결과 출력
