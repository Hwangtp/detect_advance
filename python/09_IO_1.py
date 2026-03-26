# 09_입출력_2.py
# 수업 설명: 이 파일에서는 사용자 입출력과 파일 읽기/쓰기를 배웁니다.
# 대상: 자바 등 기초프로그래밍 활용자, 초급 수준
# 파이썬 버전: 3.12, IDE: PyCharm 최신 버전

import csv  # CSV 파일을 읽고 쓰기 위한 모듈을 임포트합니다.

# 실습 예제 1: 사용자 입력
name = input("이름을 입력하세요: ")  # input 함수로 사용자 입력을 문자열로 받습니다.
print(f"안녕하세요, {name}!")  # 입력된 이름을 포함한 인사말을 출력합니다.

# 실습 예제 2: 숫자 입력
age = int(input("나이를 입력하세요: "))  # input으로 받은 문자열을 int로 변환하여 정수로 저장합니다.
print(f"당신의 나이는 {age}살입니다.")  # 나이를 포함한 메시지를 출력합니다.

# 실습 예제 3: print 자세히
print("Hello", "World", sep="-")  # sep 파라미터로 구분자를 "-"로 설정하여 출력합니다.
print("End", end=" ")  # end 파라미터로 끝에 공백을 추가합니다.
print("Line")  # "Line"을 출력합니다.

# 실습 예제 4: 파일 쓰기 (with 사용)
with open("example.txt", "w") as f:  # with 문으로 파일을 열어 쓰기 모드로 엽니다. 자동으로 닫힙니다.
    f.write("Hello, File!")  # 파일에 "Hello, File!"을 씁니다.

# 실습 예제 5: 파일 쓰기 (without with)
f = open("example2.txt", "w")  # open 함수로 파일을 쓰기 모드로 엽니다.
f.write("Hello without with!")  # 파일에 "Hello without with!"을 씁니다.
f.close()  # 파일을 명시적으로 닫습니다.

# 실습 예제 6: 파일 읽기 (with 사용)
with open("example.txt", "r") as f:  # with 문으로 파일을 읽기 모드로 엽니다.
    content = f.read()  # 파일의 전체 내용을 읽어 content에 저장합니다.
    print(content)  # 읽은 내용을 출력합니다.

# 실습 예제 7: 파일 읽기 (without with)
f = open("example2.txt", "r")  # open 함수로 파일을 읽기 모드로 엽니다.
content2 = f.read()  # 파일의 전체 내용을 읽어 content2에 저장합니다.
print(content2)  # 읽은 내용을 출력합니다.
f.close()  # 파일을 닫습니다.

# 실습 예제 8: 파일에 추가
with open("example.txt", "a") as f:  # 추가 모드로 파일을 엽니다.
    f.write("\nNew line")  # 파일 끝에 새 줄을 추가합니다.

# 실습 예제 9: 여러 줄 읽기
with open("example.txt", "r") as f:  # 읽기 모드로 파일을 엽니다.
    lines = f.readlines()  # 파일의 모든 줄을 리스트로 읽습니다.
    for line in lines:  # 각 줄에 대해 반복합니다.
        print(line.strip())  # 줄바꿈 문자를 제거하고 출력합니다.

# 실습 예제 10: CSV 파일 쓰기
with open("data.csv", "w", newline="") as csvfile:  # CSV 파일을 쓰기 모드로 엽니다. newline=""로 줄바꿈 처리.
    writer = csv.writer(csvfile)  # csv.writer 객체를 생성합니다.
    writer.writerow(["Name", "Age", "City"])  # 헤더 행을 씁니다.
    writer.writerow(["Alice", 25, "Seoul"])  # 데이터 행을 씁니다.
    writer.writerow(["Bob", 30, "Busan"])  # 또 다른 데이터 행을 씁니다.

# 실습 예제 11: CSV 파일 읽기
with open("data.csv", "r") as csvfile:  # CSV 파일을 읽기 모드로 엽니다.
    reader = csv.reader(csvfile)  # csv.reader 객체를 생성합니다.
    for row in reader:  # 각 행에 대해 반복합니다.
        print(row)  # 행을 리스트로 출력합니다.

# 미션: CSV 파일에 학생 정보를 쓰고 읽어 출력하세요. (힌트: csv 모듈 사용)
# 정답:
# import csv  # csv 모듈 임포트
# with open("students.csv", "w", newline="") as f:  # 쓰기 모드로 열기
#     writer = csv.writer(f)
#     writer.writerow(["이름", "나이", "성적"])  # 헤더
#     writer.writerow(["김철수", 20, "A"])  # 데이터
#     writer.writerow(["이영희", 22, "B"])  # 데이터
# with open("students.csv", "r") as f:  # 읽기 모드로 열기
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)  # 각 행 출력
