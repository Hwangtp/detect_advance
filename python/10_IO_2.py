# 10_입출력_2.py
# 수업 설명: 파일 경로, JSON 파일, 예외처리를 포함한 실용적인 입출력을 다룹니다.
# 대상: 파이썬 기초를 익힌 학습자
# 파이썬 버전: 3.12

import json
from pathlib import Path

# 실습 예제 1: pathlib로 경로 만들기
base_path = Path(".")
text_file = base_path / "notes.txt"
json_file = base_path / "student.json"
print("텍스트 파일 경로:", text_file)
print("JSON 파일 경로:", json_file)

# 실습 예제 2: 텍스트 파일 쓰기 (UTF-8)
with open(text_file, "w", encoding="utf-8") as file:
    file.write("파이썬 파일 입출력\n")
    file.write("두 번째 줄입니다.\n")
    file.write("세 번째 줄입니다.\n")

# 실습 예제 3: 텍스트 파일 읽기
with open(text_file, "r", encoding="utf-8") as file:
    content = file.read()
    print("\n파일 전체 내용:")
    print(content)

# 실습 예제 4: 줄 단위로 읽기
with open(text_file, "r", encoding="utf-8") as file:
    print("줄 단위 읽기:")
    for line in file:
        print(line.strip())

# 실습 예제 5: 파일 존재 여부 확인
print("\nnotes.txt 존재 여부:", text_file.exists())
print("sample.txt 존재 여부:", Path("sample.txt").exists())

# 실습 예제 6: JSON 데이터 만들기
student = {
    "name": "Kim",
    "age": 20,
    "major": "Computer Science",
    "skills": ["Python", "SQL", "HTML"],
}

# 실습 예제 7: JSON 파일로 저장하기
with open(json_file, "w", encoding="utf-8") as file:
    json.dump(student, file, ensure_ascii=False, indent=2)

# 실습 예제 8: JSON 파일 읽기
with open(json_file, "r", encoding="utf-8") as file:
    loaded_student = json.load(file)
    print("\nJSON 파일에서 읽은 데이터:")
    print(loaded_student)

# 실습 예제 9: JSON 데이터에서 값 꺼내기
print("이름:", loaded_student["name"])
print("기술 목록:", loaded_student["skills"])

# 실습 예제 10: 예외처리와 함께 파일 읽기
try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("\nmissing.txt 파일을 찾을 수 없습니다.")

# 실습 예제 11: 폴더 안의 txt 파일 찾기
print("\n현재 폴더의 txt 파일:")
for path in base_path.glob("*.txt"):
    print(path.name)

# 실습 예제 12: 파일 정보 확인
if text_file.exists():
    print("\n파일 이름:", text_file.name)
    print("확장자:", text_file.suffix)
    print("절대 경로:", text_file.resolve())

# 실습 예제 13: 여러 줄을 리스트로 저장한 뒤 파일로 쓰기
todo_list = ["자료구조 복습", "반복문 연습", "파일 입출력 정리"]
todo_file = Path("todo.txt")

with open(todo_file, "w", encoding="utf-8") as file:
    for item in todo_list:
        file.write(item + "\n")

with open(todo_file, "r", encoding="utf-8") as file:
    todos = [line.strip() for line in file]
    print("\n할 일 목록:", todos)

# 실습 예제 14: JSON에 데이터 추가 후 다시 저장하기
loaded_student["grade"] = 3

with open(json_file, "w", encoding="utf-8") as file:
    json.dump(loaded_student, file, ensure_ascii=False, indent=2)

print("\n수정된 JSON 데이터 저장 완료")

# 실습 문제: 파일 입출력 연습
# 1. diary.txt 파일을 만들고 오늘 한 일을 3줄 이상 저장해 보세요.
# 2. diary.txt 파일을 다시 읽어서 한 줄씩 출력해 보세요.
# 3. 자신의 정보를 딕셔너리로 만든 뒤 profile.json 파일로 저장해 보세요.

# 미션: scores.txt 파일에 점수 여러 개를 저장하고, 다시 읽어서 평균을 구해 보세요.
# 힌트:
# with open("scores.txt", "w", encoding="utf-8") as file:
#     file.write("80\n90\n100\n")
#
# with open("scores.txt", "r", encoding="utf-8") as file:
#     scores = [int(line.strip()) for line in file]
#     print(sum(scores) / len(scores))
