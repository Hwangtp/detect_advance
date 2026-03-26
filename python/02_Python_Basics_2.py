# 02_파이썬이란_무엇인가_2.py
# 수업 설명: 이 파일에서는 파이썬 설치 방법과 기본 사용법, 에디터 사용법을 배웁니다.
# 대상: 자바 등 기초프로그래밍 활용자, 초급 수준
# 파이썬 버전: 3.12, IDE: PyCharm 최신 버전

# 실습 예제 1: 파이썬 설치 (주석으로 설명)
# 윈도우: python.org에서 3.12 다운로드 후 설치, PATH 추가하여 명령 프롬프트에서 python 명령어 사용 가능
# 맥: Homebrew 설치 후 brew install python@3.12 명령어로 설치

# 실습 예제 2: 파이썬 기초 실습 준비
# PyCharm을 열고 새 프로젝트 생성, Python 인터프리터를 3.12로 설정하여 환경 준비

# 실습 예제 3: 간단한 계산
a = 10  # 정수 10을 변수 a에 할당합니다.
b = 20  # 정수 20을 변수 b에 할당합니다.
print(a + b)  # a와 b의 합을 계산하여 출력합니다. 결과: 30

# 실습 예제 4: 문자열 연결
greeting = "Hello"  # 문자열 "Hello"를 변수 greeting에 저장합니다.
name = "World"  # 문자열 "World"를 변수 name에 저장합니다.
message = greeting + " " + name + "!"  # 문자열을 + 연산자로 연결합니다.
print(message)  # 연결된 문자열 "Hello World!"을 출력합니다.

# 실습 예제 5: 리스트 생성과 반복
numbers = [1, 2, 3, 4, 5]  # 정수 리스트를 생성합니다.
for num in numbers:  # 리스트의 각 요소를 num에 순차적으로 할당하며 반복합니다.
    print("Number:", num)  # 각 숫자를 "Number: "와 함께 출력합니다.

# 실습 예제 6: 함수 정의와 호출
def square(x):  # square 함수를 정의합니다. 매개변수 x를 받아 x의 제곱을 반환합니다.
    return x * x  # x * x를 계산하여 반환합니다.

result = square(4)  # square 함수를 호출하여 4의 제곱을 계산하고 result에 저장합니다.
print("4의 제곱:", result)  # 결과 16을 출력합니다.

# 실습 예제 7: IDLE 에디터 사용 (주석으로)
# IDLE에서 print("Hello") 입력 후 F5로 실행하여 대화형 모드에서 코드 실행

# 실습 예제 8: 명령 프롬프트에서 실행 (주석으로)
# cmd에서 python 파일명.py 실행, 또는 python -c "print('Hi')"로 한 줄 명령 실행

# 실습 예제 9: 추천 에디터 (주석으로)
# PyCharm (전문 IDE, 디버깅 기능 강력), VS Code (가벼운 에디터, 확장 가능), Sublime Text (빠른 편집, 가벼움)

# 실습 예제 10: 주석 사용
# 이 줄은 주석입니다. 코드 실행에 영향을 주지 않습니다.
print("수고하셨습니다.")  # 인라인 주석: 코드 옆에 설명을 추가합니다.

# 미션: 두 숫자를 입력받아 합을 출력하는 코드를 작성하세요. (힌트: input 함수 사용)
# 정답:
# num1 = int(input("첫 번째 숫자를 입력하세요: "))  # input으로 문자열 입력받아 int로 변환
# num2 = int(input("두 번째 숫자를 입력하세요: "))  # 두 번째 숫자 입력
# print("합:", num1 + num2)  # 두 숫자의 합 출력