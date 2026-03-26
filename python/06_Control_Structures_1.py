# 06_제어문_1.py
# 수업 설명: 이 파일에서는 if 문의 기본 구조와 사용법을 배웁니다.
# 대상: 자바 등 기초프로그래밍 활용자, 초급 수준
# 파이썬 버전: 3.12, IDE: PyCharm 최신 버전

# 실습 예제 1: if 문 기본
age = 20  # 정수 20을 age 변수에 할당합니다.
if age >= 18:  # age가 18 이상인지 조건을 검사합니다.
    print("성인입니다.")  # 조건이 참이면 "성인입니다."를 출력합니다.

# 실습 예제 2: if-else
if age < 18:  # age가 18 미만인지 검사합니다.
    print("미성년자입니다.")  # 참이면 "미성년자입니다." 출력
else:  # 그렇지 않으면
    print("성인입니다.")  # "성인입니다." 출력

# 실습 예제 3: elif 사용
score = 85  # 정수 85를 score에 할당합니다.
if score >= 90:  # score가 90 이상이면
    print("A")  # "A" 출력
elif score >= 80:  # score가 80 이상이면 (90 미만)
    print("B")  # "B" 출력
else:  # 그 외
    print("C")  # "C" 출력

# 실습 예제 4: 중첩 if
num = 10  # 정수 10을 num에 할당합니다.
if num > 0:  # num이 0보다 크면
    if num % 2 == 0:  # num을 2로 나눈 나머지가 0이면 (짝수)
        print("양수이고 짝수입니다.")  # "양수이고 짝수입니다." 출력
    else:  # 그렇지 않으면 (홀수)
        print("양수이고 홀수입니다.")  # "양수이고 홀수입니다." 출력
else:  # num이 0 이하이면
    print("음수입니다.")  # "음수입니다." 출력

# 실습 예제 5: 들여쓰기 방법 알아보기 (주석으로)
# 파이썬에서는 들여쓰기(4칸 스페이스)를 사용하여 코드 블록을 구분합니다. 잘못된 들여쓰기는 IndentationError를 발생시킵니다.

# 실습 예제 6: 조건문에 리스트 사용
fruits = ["apple", "banana"]  # 리스트를 생성합니다.
if "apple" in fruits:  # "apple"이 fruits 리스트에 있는지 검사합니다.
    print("사과가 있습니다.")  # 있으면 "사과가 있습니다." 출력

# 실습 예제 7: 조건부 표현식
result = "성인" if age >= 18 else "미성년자"  # 조건부 표현식: 참이면 "성인", 거짓이면 "미성년자"
print(result)  # result를 출력합니다.

# 실습 예제 8: 여러 조건
x = 5  # 정수 5를 x에 할당합니다.
if x > 0 and x < 10:  # x가 0보다 크고 10보다 작은지 and 연산으로 검사합니다.
    print("x는 1부터 9 사이입니다.")  # 참이면 "x는 1부터 9 사이입니다." 출력

# 실습 예제 9: if 문과 변수
is_adult = True if age >= 18 else False  # 조건부 표현식으로 is_adult에 True 또는 False 할당
print("성인인가?", is_adult)  # "성인인가?"와 is_adult 값을 출력합니다.

# 미션: 점수를 입력받아 등급(A, B, C, F)을 출력하는 코드를 작성하세요. (힌트: if-elif-else)
# 정답:
# score = int(input("점수를 입력하세요: "))  # input으로 점수 입력받아 정수로 변환
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# else:
#     print("F")