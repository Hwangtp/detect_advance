# 13_DB_CRUD.py
# 수업 설명: 이 파일에서는 MySQL 데이터베이스와의 연결 및 CRUD 연산을 배웁니다.
# 대상: 자바 등 기초프로그래밍 활용자, 초급 수준
# 파이썬 버전: 3.12, IDE: PyCharm 최신 버전
# pip install pymysql  # MySQL 연결 라이브러리 설치 명령어

import pymysql  # pymysql: MySQL 데이터베이스와의 연결 및 쿼리 실행을 위한 라이브러리. ORM 없이 직접 SQL 쿼리를 사용할 수 있게 해줍니다.

# 데이터베이스 연결 정보 (실제 환경에 맞게 수정)
DB_HOST = 'localhost'  # 데이터베이스 호스트 주소
DB_USER = 'root'  # 데이터베이스 사용자 이름
DB_PASSWORD = 'password'  # 데이터베이스 비밀번호
DB_NAME = 'test_db'  # 데이터베이스 이름

# 실습 예제 1: 데이터베이스 연결
def connect_db():  # 데이터베이스 연결 함수 정의
    return pymysql.connect(  # pymysql.connect를 사용하여 연결 객체 반환
        host=DB_HOST,  # 호스트 설정
        user=DB_USER,  # 사용자 설정
        password=DB_PASSWORD,  # 비밀번호 설정
        database=DB_NAME,  # 데이터베이스 설정
        charset='utf8mb4',  # 문자셋 설정 (유니코드 지원)
        cursorclass=pymysql.cursors.DictCursor  # 커서 클래스를 DictCursor로 설정하여 결과를 딕셔너리로 반환
    )

# 실습 예제 2: 테이블 생성 (Create)
def create_table():  # 테이블 생성 함수
    connection = connect_db()  # 데이터베이스 연결
    try:  # 예외 처리 시작
        with connection.cursor() as cursor:  # 커서 생성 (with문으로 자동 닫힘)
            sql = """  # SQL 쿼리 문자열
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INT,
                grade VARCHAR(10)
            )
            """
            cursor.execute(sql)  # 쿼리 실행
        connection.commit()  # 변경사항 커밋
        print("Table created successfully")  # 성공 메시지
    finally:  # 항상 실행
        connection.close()  # 연결 닫기

# 실습 예제 3: 데이터 삽입 (Insert)
def insert_student(name, age, grade):  # 학생 데이터 삽입 함수
    connection = connect_db()  # 연결
    try:  # 예외 처리
        with connection.cursor() as cursor:  # 커서
            sql = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"  # 삽입 쿼리 (%s는 플레이스홀더)
            cursor.execute(sql, (name, age, grade))  # 쿼리 실행, 튜플로 값 전달
        connection.commit()  # 커밋
        print("Student inserted successfully")  # 성공 메시지
    finally:  # 연결 닫기
        connection.close()

# 실습 예제 4: 데이터 조회 (Select)
def get_students():  # 학생 데이터 조회 함수
    connection = connect_db()  # 연결
    try:  # 예외 처리
        with connection.cursor() as cursor:  # 커서
            sql = "SELECT * FROM students"  # 모든 학생 조회 쿼리
            cursor.execute(sql)  # 쿼리 실행
            result = cursor.fetchall()  # 모든 결과 가져오기 (딕셔너리 리스트)
            for row in result:  # 각 행 출력
                print(row)
    finally:  # 연결 닫기
        connection.close()

# 실습 예제 5: 데이터 업데이트 (Update)
def update_student(student_id, new_age):  # 학생 나이 업데이트 함수
    connection = connect_db()  # 연결
    try:  # 예외 처리
        with connection.cursor() as cursor:  # 커서
            sql = "UPDATE students SET age = %s WHERE id = %s"  # 업데이트 쿼리
            cursor.execute(sql, (new_age, student_id))  # 쿼리 실행
        connection.commit()  # 커밋
        print("Student updated successfully")  # 성공 메시지
    finally:  # 연결 닫기
        connection.close()

# 실습 예제 6: 데이터 삭제 (Delete)
def delete_student(student_id):  # 학생 삭제 함수
    connection = connect_db()  # 연결
    try:  # 예외 처리
        with connection.cursor() as cursor:  # 커서
            sql = "DELETE FROM students WHERE id = %s"  # 삭제 쿼리
            cursor.execute(sql, (student_id,))  # 쿼리 실행 (튜플로 ID 전달)
        connection.commit()  # 커밋
        print("Student deleted successfully")  # 성공 메시지
    finally:  # 연결 닫기
        connection.close()

# 실습 예제 7: CRUD 실행 예제
if __name__ == "__main__":  # 스크립트 직접 실행 시
    # 테이블 생성
    create_table()

    # 데이터 삽입
    insert_student("Alice", 20, "A")
    insert_student("Bob", 22, "B")

    # 데이터 조회
    print("All students:")
    get_students()

    # 데이터 업데이트
    update_student(1, 21)

    # 다시 조회
    print("After update:")
    get_students()

    # 데이터 삭제
    delete_student(2)

    # 최종 조회
    print("After delete:")
    get_students()

# 미션: 학생 정보를 삽입하고 조회하는 함수를 작성하세요. (힌트: insert와 select 함수)
# 정답:
# def insert_and_get_student(name, age, grade):  # 삽입 후 조회 함수
#     insert_student(name, age, grade)  # 삽입 함수 호출
#     print(f"Inserted student: {name}")  # 삽입 메시지
#     print("Current students:")  # 조회 전 메시지
#     get_students()  # 조회 함수 호출
# 
# # 사용 예:
# insert_and_get_student("Charlie", 19, "A+")  # 함수 호출