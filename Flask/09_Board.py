# 09_Board.py
# Flask 통합 프로젝트: 커뮤니티 게시판
# 게시글 작성, 조회, 댓글 등 포함
# 설치: pip install flask
# 실행: python 09_Board.py

from flask import Flask, render_template, request, redirect, url_for, session  # Flask 핵심
import sqlite3  # 데이터베이스
from datetime import datetime  # 날짜/시간

app = Flask(__name__)
app.config['SECRET_KEY'] = 'board-secret-key'  # 세션 키

# 데이터베이스 파일 경로
DATABASE = 'community_board.db'

# 데이터베이스 연결 함수
def get_db():
    """데이터베이스 연결 반환"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# 테이블 생성
def init_db():
    """데이터베이스 테이블 생성"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS post (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            post_id INTEGER NOT NULL,
            author TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (post_id) REFERENCES post (id)
        )
    ''')
    
    conn.commit()
    conn.close()

# 테이블 생성 실행
init_db()

# ========== 라우팅 ==========

@app.route('/')
def index():
    """메인 페이지"""
    return '''
    <h1>커뮤니티 게시판</h1>
    <ul>
        <li><a href="/posts">게시글 목록</a></li>
        <li><a href="/post/new">새 게시글 작성</a></li>
    </ul>
    '''

@app.route('/posts')
def posts_list():
    """게시글 목록"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM post ORDER BY created_at DESC")
    posts = cursor.fetchall()
    conn.close()
    
    return render_template('posts_list.html', posts=posts)

@app.route('/post/new', methods=['GET', 'POST'])
def create_post():
    """새 게시글 작성"""
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author', '익명')
        
        if not title or not content:
            error = '제목과 내용을 입력하세요!'
            return render_template('post_form.html', error=error)
        
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO post (title, content, author)
            VALUES (?, ?, ?)
        ''', (title, content, author))
        post_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return redirect(url_for('view_post', post_id=post_id))
    
    return render_template('post_form.html')

@app.route('/post/<int:post_id>')
def view_post(post_id):
    """게시글 상세 보기"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM post WHERE id = ?", (post_id,))
    post = cursor.fetchone()
    
    if not post:
        conn.close()
        return "게시글을 찾을 수 없습니다.", 404
    
    # 댓글 조회
    cursor.execute("SELECT * FROM comment WHERE post_id = ? ORDER BY created_at", (post_id,))
    comments = cursor.fetchall()
    conn.close()
    
    return render_template('post_detail.html', post=post, comments=comments)

@app.route('/post/<int:post_id>/comment', methods=['POST'])
def add_comment(post_id):
    """댓글 추가"""
    content = request.form.get('content')
    author = request.form.get('author', '익명')
    
    if not content:
        return redirect(url_for('view_post', post_id=post_id))
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO comment (content, post_id, author)
        VALUES (?, ?, ?)
    ''', (content, post_id, author))
    conn.commit()
    conn.close()
    
    return redirect(url_for('view_post', post_id=post_id))

if __name__ == '__main__':
    app.run(debug=True)