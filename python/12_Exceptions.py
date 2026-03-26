# 12_날개달기_2.py
# 수업 설명: 이 파일에서는 패키지와 예외 처리의 사용법을 배웁니다.
# 대상: 자바 등 기초프로그래밍 활용자, 초급 수준
# 파이썬 버전: 3.12, IDE: PyCharm 최신 버전

# 실습 예제 1: 패키지 만들기 (주석으로 설명)
# 디렉터리에 __init__.py 파일을 생성하여 패키지를 만듭니다. 그 후 모듈을 추가합니다.
# 예: my_package/__init__.py (빈 파일 또는 초기화 코드), my_package/module1.py (모듈 파일)

# 실습 예제 2: 패키지 임포트
# from my_package import my_module  # my_package 패키지에서 my_module 모듈을 임포트합니다.
# my_module.function()  # 임포트된 모듈의 함수를 호출합니다.

# 실습 예제 3: __init__.py 의 용도
# 패키지 초기화, __all__ 리스트 정의 (from package import * 시 임포트할 항목 지정), 패키지 수준 변수/함수 정의 등

# 실습 예제 4: relative 패키지
# from . import module1  # 같은 패키지 내의 module1을 임포트합니다.
# from .. import parent_module  # 부모 패키지의 parent_module을 임포트합니다.

# 실습 예제 5: 예외 처리
try:  # 예외가 발생할 수 있는 코드를 시도합니다.
    x = 10 / 0  # 0으로 나누기 오류가 발생합니다.
except ZeroDivisionError:  # ZeroDivisionError 예외를 잡습니다.
    print("0으로 나눌 수 없습니다.")  # 오류 메시지를 출력합니다.

# 실습 예제 6: 여러 예외 처리
try:  # 예외가 발생할 수 있는 코드를 시도합니다.
    num = int("abc")  # 문자열을 정수로 변환 시 ValueError 발생
except (ValueError, TypeError) as e:  # ValueError 또는 TypeError를 잡습니다.
    print(f"Error: {e}")  # 오류 메시지를 출력합니다.

# 실습 예제 7: else와 finally
try:  # 예외가 발생할 수 있는 코드를 시도합니다.
    result = 10 / 2  # 정상적인 나눗셈
except ZeroDivisionError:  # ZeroDivisionError를 잡습니다.
    print("Division by zero")  # 오류 시 출력
else:  # 예외가 발생하지 않았을 때 실행됩니다.
    print(f"Result: {result}")  # 결과 출력
finally:  # 예외 발생 여부와 관계없이 항상 실행됩니다.
    print("Always executed")  # 항상 실행되는 메시지

# 실습 예제 8: 오류 회피
try:  # 파일 열기를 시도합니다.
    file = open("nonexistent.txt", "r")  # 존재하지 않는 파일 열기
except FileNotFoundError:  # FileNotFoundError를 잡습니다.
    print("파일이 없습니다.")  # 오류 메시지 출력

# 실습 예제 9: 오류 일부러 발생시키기
def check_age(age):  # 나이를 체크하는 함수 정의
    if age < 0:  # 나이가 음수이면
        raise ValueError("Age cannot be negative")  # ValueError를 발생시킵니다.
    return age  # 나이를 반환합니다.

try:  # 함수 호출을 시도합니다.
    check_age(-5)  # 음수 나이로 호출
except ValueError as e:  # ValueError를 잡습니다.
    print(e)  # 오류 메시지 출력

# 실습 예제 10: 예외 만들기
class CustomError(Exception):  # Exception을 상속받는 사용자 정의 예외 클래스
    pass  # 기본 구현

try:  # 사용자 정의 예외 발생을 시도합니다.
    raise CustomError("This is a custom error")  # CustomError 발생
except CustomError as e:  # CustomError를 잡습니다.
    print(e)  # 오류 메시지 출력

# 실습 예제 11: 오류는 언제 발생하는가?
# - 파일이 없을 때 (FileNotFoundError): open() 함수로 존재하지 않는 파일을 열 때
# - 0으로 나눌 때 (ZeroDivisionError): 숫자를 0으로 나눌 때
# - 잘못된 타입 연산 (TypeError): 호환되지 않는 타입 간 연산 시
# - 인덱스 범위 초과 (IndexError): 리스트나 문자열의 유효하지 않은 인덱스 접근 시

# 미션: 파일을 열고 내용을 읽는 함수를 만들고, 예외 처리를 추가하세요. (힌트: try-except-finally)
# 정답:
# def read_file(filename):  # 파일을 읽는 함수 정의
#     try:  # 파일 열기를 시도합니다.
#         with open(filename, 'r') as file:  # 파일을 읽기 모드로 엽니다.
#             content = file.read()  # 파일 내용을 읽습니다.
#             return content  # 내용을 반환합니다.
#     except FileNotFoundError:  # 파일이 없을 때
#         print(f"파일 '{filename}'을 찾을 수 없습니다.")  # 오류 메시지
#         return None  # None 반환
#     except IOError as e:  # 기타 I/O 오류
#         print(f"I/O 오류: {e}")  # 오류 메시지
#         return None  # None 반환
#     finally:  # 항상 실행
#         print("파일 읽기 시도 완료.")  # 완료 메시지
# 
# result = read_file("example.txt")  # 함수 호출
# if result:  # 내용이 있으면
#     print(result)  # 출력