# 13_DB_CRUD.py

<div style="background: linear-gradient(135deg, #f59e0b, #f97316); color: #ffffff; padding: 18px 22px; border-radius: 16px; margin: 18px 0;">
  <h2 style="margin: 0 0 8px 0;">DB CRUD</h2>
  <p style="margin: 0; line-height: 1.7;">MySQL과 연결해 CRUD 작업을 수행하는 실전 예제 파일입니다.</p>
</div>

<table>
  <tr>
    <td style="background-color:#fff7ed; border:1px solid #fdba74; border-radius:14px; padding:16px;">
      <strong style="color:#c2410c;">왜 중요한가</strong><br><br>
      Python 코드가 데이터베이스와 실제로 연결되는 흐름을 경험하게 합니다.
    </td>
  </tr>
</table>

## 핵심 학습 포인트

<div style="background-color:#f8fafc; border:1px solid #cbd5e1; border-radius:14px; padding:16px; margin:12px 0;">
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li style="margin: 8px 0;"><strong style="color:#0f766e;">1.</strong> DB 연결</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">2.</strong> INSERT</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">3.</strong> SELECT</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">4.</strong> UPDATE</li>
<li style="margin: 8px 0;"><strong style="color:#0f766e;">5.</strong> DELETE</li>
  </ul>
</div>

## 추천 학습 방법

<div style="background-color:#ecfeff; border-left:8px solid #06b6d4; padding:16px 18px; border-radius:12px; margin:12px 0;">
  <ol style="margin:0; padding-left:20px; line-height:1.9;">
    <li><code>.py</code> 파일을 직접 실행해 예제 결과를 확인합니다.</li>
    <li>주석과 출력 결과를 함께 보며 코드 흐름을 따라갑니다.</li>
    <li>예제 값을 조금씩 바꿔 보며 어떤 점이 달라지는지 관찰합니다.</li>
    <li>마지막에는 비슷한 문제를 스스로 다시 작성해 봅니다.</li>
  </ol>
</div>

## 같이 보면 좋은 파일

<div style="background-color:#f5f3ff; border:1px solid #c4b5fd; border-radius:14px; padding:16px; margin:12px 0;">
  <ul style="margin:0; padding-left:20px; line-height:1.8;">
    <li><code>Overview.md</code></li>
    <li>이전 번호 파일과 다음 번호 파일</li>
    <li>같은 주제가 이어지는 후속 실습 파일</li>
  </ul>
</div>

## 코드

```python
import pymysql

DB_HOST = 'localhost'

DB_USER = 'root'

DB_PASSWORD = 'password'

DB_NAME = 'test_db'

def connect_db():

    return pymysql.connect(

        host=DB_HOST,

        user=DB_USER,

        password=DB_PASSWORD,

        database=DB_NAME,

        charset='utf8mb4',

        cursorclass=pymysql.cursors.DictCursor

    )

def create_table():

    connection = connect_db()

    try:

        with connection.cursor() as cursor:

            sql = """  # SQL 쿼리 문자열
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INT,
                grade VARCHAR(10)
            )
            """

            cursor.execute(sql)

        connection.commit()

        print("Table created successfully")

    finally:

        connection.close()

def insert_student(name, age, grade):

    connection = connect_db()

    try:

        with connection.cursor() as cursor:

            sql = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"

            cursor.execute(sql, (name, age, grade))

        connection.commit()

        print("Student inserted successfully")

    finally:

        connection.close()

def get_students():

    connection = connect_db()

    try:

        with connection.cursor() as cursor:

            sql = "SELECT * FROM students"

            cursor.execute(sql)

            result = cursor.fetchall()

            for row in result:

                print(row)

    finally:

        connection.close()

def update_student(student_id, new_age):

    connection = connect_db()

    try:

        with connection.cursor() as cursor:

            sql = "UPDATE students SET age = %s WHERE id = %s"

            cursor.execute(sql, (new_age, student_id))

        connection.commit()

        print("Student updated successfully")

    finally:

        connection.close()

def delete_student(student_id):

    connection = connect_db()

    try:

        with connection.cursor() as cursor:

            sql = "DELETE FROM students WHERE id = %s"

            cursor.execute(sql, (student_id,))

        connection.commit()

        print("Student deleted successfully")

    finally:

        connection.close()

if __name__ == "__main__":

    create_table()

    insert_student("Alice", 20, "A")

    insert_student("Bob", 22, "B")

    print("All students:")

    get_students()

    update_student(1, 21)

    print("After update:")

    get_students()

    delete_student(2)

    print("After delete:")

    get_students()
```
