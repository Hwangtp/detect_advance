# 05_Database.py
# Flask에서 데이터베이스 연결
# SQLite 데이터베이스를 직접 사용하여 데이터를 관리합니다.
# 설치: pip install flask
# 실행: python 05_Database.py

from flask import Flask  # Flask 임포트
import sqlite3  # SQLite 직접 사용
from datetime import datetime  # 날짜/시간

# Flask 앱 설정
app = Flask(__name__)  # Flask 앱 생성

# 데이터베이스 파일 경로
DATABASE = 'app.db'

# 데이터베이스 연결 함수
def get_db():
    """데이터베이스 연결 반환"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # 딕셔너리처럼 접근 가능
    return conn

# 데이터베이스 초기화 및 테이블 생성
def init_db():
    """데이터베이스와 테이블 생성"""
    conn = get_db()
    cursor = conn.cursor()
    
    # 사용자 테이블 생성
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            age INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 게시글 테이블 생성
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS post (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT,
            user_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES user (id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("데이터베이스 생성 완료!")

# 데이터 추가 함수
def add_sample_data():
    """샘플 데이터 추가"""
    conn = get_db()
    cursor = conn.cursor()
    
    # 이미 데이터가 있는지 확인
    cursor.execute("SELECT COUNT(*) FROM user")
    if cursor.fetchone()[0] > 0:
        print("이미 데이터가 있습니다.")
        conn.close()
        return
    
    # 사용자 추가
    cursor.execute("INSERT INTO user (username, email, password, age) VALUES (?, ?, ?, ?)",
                   ('alice', 'alice@example.com', 'password123', 25))
    cursor.execute("INSERT INTO user (username, email, password, age) VALUES (?, ?, ?, ?)",
                   ('bob', 'bob@example.com', 'password456', 30))
    
    # 게시글 추가
    cursor.execute("INSERT INTO post (title, content, user_id) VALUES (?, ?, ?)",
                   ('Flask 배우기', 'Flask는 가벼운 웹 프레임워크입니다.', 1))
    cursor.execute("INSERT INTO post (title, content, user_id) VALUES (?, ?, ?)",
                   ('데이터베이스 활용', '직접 SQL을 사용하면 쉽게 관리할 수 있습니다.', 1))
    cursor.execute("INSERT INTO post (title, content, user_id) VALUES (?, ?, ?)",
                   ('Python 팁', 'Python은 배우기 쉬운 언어입니다.', 2))
    
    conn.commit()
    conn.close()
    print("샘플 데이터 추가 완료!")

# 데이터 조회 함수
def query_examples():
    """데이터 조회 예제"""
    conn = get_db()
    cursor = conn.cursor()
    
    # 예제 1: 모든 사용자 조회
    print("\n=== 모든 사용자 ===")
    cursor.execute("SELECT username, email FROM user")
    users = cursor.fetchall()
    for user in users:
        print(f"- {user['username']}: {user['email']}")
    
    # 예제 2: 특정 사용자 조회
    print("\n=== 특정 사용자 ===")
    cursor.execute("SELECT username, age FROM user WHERE username = ?", ('alice',))
    user = cursor.fetchone()
    if user:
        print(f"사용자: {user['username']}, 나이: {user['age']}")
    
    # 예제 3: 조건부 조회
    print("\n=== 조건부 조회 ===")
    cursor.execute("SELECT username, age FROM user WHERE age >= ?", (25,))
    users_over_25 = cursor.fetchall()
    for user in users_over_25:
        print(f"- {user['username']}: {user['age']}세")
    
    # 예제 4: 관계를 통한 조회 (사용자의 게시글)
    print("\n=== Alice의 게시글 ===")
    cursor.execute("SELECT id FROM user WHERE username = ?", ('alice',))
    alice_id = cursor.fetchone()
    if alice_id:
        cursor.execute("SELECT title FROM post WHERE user_id = ?", (alice_id['id'],))
        posts = cursor.fetchall()
        for post in posts:
            print(f"- {post['title']}")
    
    conn.close()

# 데이터 수정 및 삭제
def update_delete_examples():
    """데이터 수정 및 삭제 예제"""
    conn = get_db()
    cursor = conn.cursor()
    
    # 수정 예제
    print("\n=== 데이터 수정 ===")
    cursor.execute("UPDATE user SET age = ? WHERE username = ?", (26, 'alice'))
    conn.commit()
    print("Alice의 나이를 26으로 업데이트했습니다.")
    
    # 삭제 예제 (주석 처리)
    print("\n=== 데이터 삭제 ===")
    # cursor.execute("DELETE FROM user WHERE username = ?", ('bob',))
    # conn.commit()
    # print("Bob을 삭제했습니다.")
    
    conn.close()

# 고급 쿼리
def advanced_queries():
    """고급 쿼리 예제"""
    conn = get_db()
    cursor = conn.cursor()
    
    print("\n=== 고급 쿼리 ===")
    
    # 개수 세기
    cursor.execute("SELECT COUNT(*) FROM user")
    user_count = cursor.fetchone()[0]
    print(f"전체 사용자 수: {user_count}")
    
    # 정렬
    print("\nAlphabetical order:")
    cursor.execute("SELECT username FROM user ORDER BY username")
    sorted_users = cursor.fetchall()
    for user in sorted_users:
        print(f"- {user['username']}")
    
    # 역순 정렬
    print("\nReverse order:")
    cursor.execute("SELECT username FROM user ORDER BY username DESC")
    reverse_users = cursor.fetchall()
    for user in reverse_users:
        print(f"- {user['username']}")
    
    # 제한 (LIMIT)
    print("\nFirst 2 users:")
    cursor.execute("SELECT username FROM user LIMIT 2")
    limited = cursor.fetchall()
    for user in limited:
        print(f"- {user['username']}")
    
    conn.close()

# 메인 실행
if __name__ == '__main__':
    print("1. 데이터베이스 초기화...")
    init_db()
    
    print("\n2. 샘플 데이터 추가...")
    add_sample_data()
    
    print("\n3. 데이터 조회...")
    query_examples()
    
    print("\n4. 데이터 수정...")
    update_delete_examples()
    
    print("\n5. 고급 쿼리...")
    advanced_queries()
    
    print("\n완료!")

# 미션:
# 1. Comment 테이블을 추가하세요. (id, content, post_id, user_id, created_at)
# 2. Post와 Comment의 관계를 설정하세요.
# 정답:
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS comment (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         content TEXT NOT NULL,
#         post_id INTEGER NOT NULL,
#         user_id INTEGER NOT NULL,
#         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#         FOREIGN KEY (post_id) REFERENCES post (id),
#         FOREIGN KEY (user_id) REFERENCES user (id)
#     )
# ''')