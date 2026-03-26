# 03_자료형_1.py
# 수업 설명: 이 파일에서는 숫자형과 문자열 자료형의 기본 사용법을 배웁니다.
# 대상: 자바 등 기초프로그래밍 활용자, 초급 수준
# 파이썬 버전: 3.12, IDE: PyCharm 최신 버전

# 실습 예제 1: 숫자형 만들기
num1 = 10  # 정수형 숫자 10을 변수 num1에 할당합니다.
num2 = 3.14  # 실수형 숫자 3.14를 변수 num2에 할당합니다.
print(num1)  # num1의 값 10을 출력합니다.
print(num2)  # num2의 값 3.14를 출력합니다.

# 실습 예제 2: 숫자형 연산자
a = 5  # 정수 5를 변수 a에 저장합니다.
b = 2  # 정수 2를 변수 b에 저장합니다.
print(a + b)  # a와 b의 덧셈 결과를 출력합니다: 7
print(a - b)  # a에서 b를 뺀 결과를 출력합니다: 3
print(a * b)  # a와 b의 곱셈 결과를 출력합니다: 10
print(a / b)  # a를 b로 나눈 실수 결과를 출력합니다: 2.5
print(a // b)  # a를 b로 나눈 몫을 출력합니다: 2
print(a % b)  # a를 b로 나눈 나머지를 출력합니다: 1
print(a ** b)  # a의 b 거듭제곱을 출력합니다: 25

# 실습 예제 3: 문자열 만들기
str1 = "Hello"  # 큰따옴표를 사용하여 문자열 "Hello"를 str1에 할당합니다.
str2 = 'World'  # 작은따옴표를 사용하여 문자열 "World"를 str2에 할당합니다.
print(str1)  # str1의 값 "Hello"를 출력합니다.
print(str2)  # str2의 값 "World"를 출력합니다.

# 실습 예제 4: 문자열에 따옴표 포함
str3 = "He said, 'Hello'"  # 큰따옴표 안에 작은따옴표를 포함하여 문자열을 만듭니다.
print(str3)  # "He said, 'Hello'"를 출력합니다.

# 실습 예제 5: 여러 줄 문자열
str4 = """This is
a multi-line
string"""  # 세 개의 따옴표를 사용하여 여러 줄 문자열을 만듭니다.
print(str4)  # 여러 줄로 된 문자열을 출력합니다.

# 실습 예제 6: 문자열 연산
str5 = "Python"  # 문자열 "Python"을 str5에 할당합니다.
str6 = " is fun"  # 문자열 " is fun"을 str6에 할당합니다.
print(str5 + str6)  # str5와 str6을 연결하여 "Python is fun"을 출력합니다.
print(str5 * 3)  # str5를 3번 반복하여 "PythonPythonPython"을 출력합니다.

# 실습 예제 7: 문자열 인덱싱
print(str5[0])  # str5의 첫 번째 문자 'P'를 출력합니다 (인덱스 0).
print(str5[-1])  # str5의 마지막 문자 'n'을 출력합니다 (인덱스 -1).

# 실습 예제 8: 문자열 슬라이싱
print(str5[0:3])  # str5의 0부터 2까지 슬라이싱하여 "Pyt"를 출력합니다.
print(str5[2:])  # str5의 2부터 끝까지 슬라이싱하여 "thon"을 출력합니다.
print(str5[:4])  # str5의 처음부터 3까지 슬라이싱하여 "Pyth"를 출력합니다.

# 실습 예제 9: 문자열 포매팅
name = "Alice"  # 문자열 "Alice"를 name에 할당합니다.
age = 30  # 정수 30을 age에 할당합니다.
print("이름: %s, 나이: %d" % (name, age))  # % 포매팅을 사용하여 출력합니다.
print("이름: {}, 나이: {}".format(name, age))  # format 함수를 사용하여 출력합니다.
print(f"이름: {name}, 나이: {age}")  # f-string을 사용하여 출력합니다.

# 실습 예제 10: 문자열 관련 함수
text = "hello world"  # 문자열 "hello world"를 text에 할당합니다.
print(text.upper())  # text를 대문자로 변환하여 "HELLO WORLD"를 출력합니다.
print(text.lower())  # text를 소문자로 변환하여 "hello world"를 출력합니다.
print(text.title())  # 각 단어의 첫 글자를 대문자로 하여 "Hello World"를 출력합니다.
print(text.replace("world", "Python"))  # "world"를 "Python"으로 교체하여 "hello Python"을 출력합니다.

# 미션: 자신의 이름과 나이를 문자열로 연결하여 출력하세요. (힌트: 문자열 연결과 포매팅)
# 정답:
# name = "홍길동"  # 자신의 이름을 문자열로 저장
# age = 25  # 자신의 나이를 정수로 저장
# print(name + "의 나이는 " + str(age) + "살입니다.")  # 문자열 연결 사용
# 또는 print(f"{name}의 나이는 {age}살입니다.")  # f-string 사용