# 08_입출력_1.py
# 수업 설명: 이 파일에서는 함수의 기본 개념과 사용법을 배웁니다.
# 대상: 자바 등 기초프로그래밍 활용자, 초급 수준
# 파이썬 버전: 3.12, IDE: PyCharm 최신 버전

# 실습 예제 1: 함수 정의
def greet():  # greet 함수를 정의합니다. 매개변수가 없습니다.
    print("Hello!")  # "Hello!"를 출력합니다.

greet()  # greet 함수를 호출합니다.

# 실습 예제 2: 매개변수와 인수
def add(a, b):  # add 함수를 정의합니다. a와 b는 매개변수입니다.
    return a + b  # a와 b의 합을 반환합니다.

result = add(5, 3)  # add 함수를 호출하며 5와 3을 인수로 전달합니다.
print(result)  # 반환된 결과 8을 출력합니다.

# 실습 예제 3: 입력값과 리턴값에 따른 함수 형태
def func1():  # 입력 없음, 리턴 없음: 단순 실행 함수
    print("No input, no return")  # 메시지를 출력합니다.

def func2(x):  # 입력 있음, 리턴 없음: 입력을 받아 처리하지만 반환하지 않음
    print(f"Input: {x}")  # 입력된 x를 출력합니다.

def func3():  # 입력 없음, 리턴 있음: 값을 생성하여 반환
    return "Return value"  # 문자열을 반환합니다.

def func4(x):  # 입력 있음, 리턴 있음: 입력을 받아 계산 후 반환
    return x * 2  # x의 2배를 반환합니다.

# 실습 예제 4: 매개변수를 지정하여 호출
def introduce(name, age):  # name과 age 매개변수를 받는 함수
    print(f"이름: {name}, 나이: {age}")  # 이름과 나이를 출력합니다.

introduce(age=25, name="Alice")  # 키워드 인수를 사용하여 호출합니다.

# 실습 예제 5: 입력값이 몇 개가 될지 모를 때
def sum_all(*args):  # *args를 사용하여 가변 인수를 받습니다.
    total = 0  # 합계를 저장할 변수
    for num in args:  # args의 각 요소를 반복
        total += num  # total에 더합니다.
    return total  # 총합을 반환합니다.

print(sum_all(1, 2, 3, 4))  # sum_all()의 인자를 튜플형태로 넘김(왜곡방지). 1+2+3+4=10을 출력합니다.

# 실습 예제 6: 키워드 매개변수 kwargs
def print_info(**kwargs):  # **kwargs를 사용하여 키워드 가변 인수를 받습니다.
    for key, value in kwargs.items():  # kwargs의 키-값 쌍을 반복
        print(f"{key}: {value}")  # 각 키와 값을 출력합니다.

print_info(name="Bob", age=30, city="Seoul")  # 여러 키워드 인수를 전달합니다.

# 실습 예제 7: 함수의 리턴값은 언제나 하나
def return_multiple():  # 여러 값을 반환하는 함수
    return 1, 2, 3  # 튜플 (1, 2, 3)을 반환합니다.

a, b, c = return_multiple()  # 반환된 튜플을 언패킹하여 a, b, c에 할당합니다.
print(a, b, c)  # 1 2 3을 출력합니다.

# 실습 예제 8: 매개변수에 초깃값 미리 설정
def greet_person(name, greeting="Hello"):  # greeting에 기본값 "Hello" 설정
    print(f"{greeting}, {name}!")  # 인사말과 이름을 출력합니다.

greet_person("Charlie")  # 기본값 사용: "Hello, Charlie!"
greet_person("David", "Hi")  # "Hi" 지정: "Hi, David!"

# 실습 예제 9: 함수 안에서 선언한 변수의 효력 범위
def test_scope():  # 함수 정의
    local_var = "local"  # 지역 변수 선언
    print(local_var)  # 지역 변수 출력

test_scope()  # 함수 호출
# print(local_var)  # 오류: 지역 변수는 함수 밖에서 접근 불가

# 실습 예제 10: 함수 안에서 함수 밖의 변수를 변경
global_var = "global"  # 전역 변수 선언

def change_global():  # 함수 정의
    global global_var  # 전역 변수임을 선언
    global_var = "changed"  # 전역 변수 변경

change_global()  # 함수 호출
print(global_var)  # 변경된 값 "changed" 출력

# 실습 예제 11: lambda 예약어 기본
square = lambda x: x ** 2  # lambda를 사용하여 x의 제곱값을 반환하는 익명 함수를 만듭니다.
print(square(5))  # 5를 전달해 25가 출력되는지 확인합니다.

# 실습 예제 12: lambda를 정렬 기준으로 사용
students = [("Kim", 90), ("Lee", 75), ("Park", 88)]  # 이름과 점수를 튜플로 저장한 리스트입니다.
sorted_students = sorted(students, key=lambda student: student[1])  # 각 튜플의 두 번째 값인 점수를 기준으로 오름차순 정렬합니다.
print(sorted_students)  # 점수 기준으로 정렬된 결과를 출력합니다.

# 실습 예제 13: lambda와 map 함수
numbers = [1, 2, 3, 4, 5]  # 숫자 리스트를 준비합니다.
doubled = list(map(lambda x: x * 2, numbers))  # 각 숫자에 2를 곱한 결과를 새 리스트로 만듭니다. // map(함수, 리스트)
print(doubled)  # [2, 4, 6, 8, 10]을 출력합니다.

# 실습 예제 14: lambda와 filter 함수
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # 짝수인 값만 골라 새 리스트로 만듭니다.
print(even_numbers)  # [2, 4]를 출력합니다.

# 미션: 여러 숫자를 입력받아 평균을 계산하는 함수를 작성하세요. (힌트: *args 사용)
# 정답:
# def average(*args):  # 가변 인수 받음
#     if len(args) == 0:  # 인수가 없으면
#         return 0  # 0 반환
#     return sum(args) / len(args)  # 합을 개수로 나누어 평균 반환
# print(average(1, 2, 3, 4, 5))  # 3.0 출력
