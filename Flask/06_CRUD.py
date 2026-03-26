# 06_CRUD.py
# CRUD 연산 (Create, Read, Update, Delete)
# 데이터베이스의 기본 연산을 구현합니다.
# 설치: pip install flask
# 실행: python 06_CRUD.py

from flask import Flask, render_template, request, redirect, url_for  # Flask 및 관련 모듈
import sqlite3  # 데이터베이스 직접 사용
from datetime import datetime  # 날짜/시간

app = Flask(__name__)  # Flask 앱 생성

# 데이터베이스 파일 경로
DATABASE = 'crud_demo.db'

# 데이터베이스 연결 함수
def get_db():
    """데이터베이스 연결 반환"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # 딕셔너리처럼 접근 가능
    return conn

# 테이블 생성
def init_db():
    """데이터베이스 테이블 생성"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS article (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

# 테이블 생성 실행
init_db()

# ========== CREATE (생성) ==========

@app.route('/')
def index():
    """메인 페이지"""
    return '''
    <h1>Flask CRUD 예제</h1>
    <ul>
        <li><a href="/articles">게시글 목록</a></li>
        <li><a href="/article/new">새 게시글 작성</a></li>
    </ul>
    '''

@app.route('/article/new', methods=['GET', 'POST'])
def create_article():
    """새로운 게시글 생성"""
    if request.method == 'POST':  # 폼 제출
        # 폼 데이터 추출
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author')
        
        # 검증
        if not all([title, content, author]):
            error = '모든 필드를 입력하세요!'
            return render_template('article_form.html', error=error)
        
        # 데이터베이스에 저장
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO article (title, content, author)
            VALUES (?, ?, ?)
        ''', (title, content, author))
        article_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        # 상세 페이지로 리다이렉트
        return redirect(url_for('read_article', article_id=article_id))
    
    else:  # GET: 폼 표시
        return render_template('article_form.html')

# ========== READ (읽기) ==========

@app.route('/articles')
def articles_list():
    """모든 게시글 목록 (페이징 포함)"""
    page = request.args.get('page', 1, type=int)  # 페이지 번호 (기본값: 1)
    per_page = 5  # 페이지당 게시글 수
    
    # 게시글을 페이징하여 조회
    offset = (page - 1) * per_page
    conn = get_db()
    cursor = conn.cursor()
    
    # 전체 게시글 수
    cursor.execute("SELECT COUNT(*) FROM article")
    total_count = cursor.fetchone()[0]
    total_pages = (total_count + per_page - 1) // per_page  # 올림 계산
    
    # 현재 페이지의 게시글
    cursor.execute('''
        SELECT * FROM article
        ORDER BY created_at DESC
        LIMIT ? OFFSET ?
    ''', (per_page, offset))
    articles = cursor.fetchall()
    conn.close()
    
    return render_template(
        'articles_list.html',
        articles=articles,
        page=page,
        total_pages=total_pages,
        total_count=total_count
    )

@app.route('/article/<int:article_id>')
def read_article(article_id):
    """특정 게시글 상세 조회"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM article WHERE id = ?", (article_id,))
    article = cursor.fetchone()
    conn.close()
    
    if not article:
        return "게시글을 찾을 수 없습니다.", 404
    
    return render_template('article_detail.html', article=article)

@app.route('/articles/search')
def search_articles():
    """게시글 검색"""
    keyword = request.args.get('q', '')  # 검색어
    
    conn = get_db()
    cursor = conn.cursor()
    
    if keyword:
        # 제목과 내용에서 검색
        cursor.execute('''
            SELECT * FROM article
            WHERE title LIKE ? OR content LIKE ?
        ''', (f'%{keyword}%', f'%{keyword}%'))
        articles = cursor.fetchall()
        message = f"'{keyword}' 검색 결과"
    else:
        articles = []
        message = "검색어를 입력하세요."
    
    conn.close()
    
    return render_template(
        'search_results.html',
        articles=articles,
        keyword=keyword,
        message=message
    )

# ========== UPDATE (수정) ==========

@app.route('/article/<int:article_id>/edit', methods=['GET', 'POST'])
def update_article(article_id):
    """게시글 수정"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM article WHERE id = ?", (article_id,))
    article = cursor.fetchone()
    conn.close()
    
    if not article:
        return "게시글을 찾을 수 없습니다.", 404
    
    if request.method == 'POST':  # 폼 제출
        # 폼 데이터로 업데이트
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author')
        
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE article
            SET title = ?, content = ?, author = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (title, content, author, article_id))
        conn.commit()
        conn.close()
        
        # 상세 페이지로 리다이렉트
        return redirect(url_for('read_article', article_id=article_id))
    
    else:  # GET: 수정 폼 표시
        return render_template('article_form.html', article=article)

# ========== DELETE (삭제) ==========

@app.route('/article/<int:article_id>/delete', methods=['POST'])
def delete_article(article_id):
    """게시글 삭제"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM article WHERE id = ?", (article_id,))
    conn.commit()
    conn.close()
    
    # 목록으로 리다이렉트
    return redirect(url_for('articles_list'))

# ========== 추가 기능 ==========

@app.route('/article/<int:article_id>/duplicate', methods=['POST'])
def duplicate_article(article_id):
    """게시글 복제"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM article WHERE id = ?", (article_id,))
    original = cursor.fetchone()
    
    if not original:
        conn.close()
        return "게시글을 찾을 수 없습니다.", 404
    
    # 새로운 게시글 생성 (기존 내용 복사)
    cursor.execute('''
        INSERT INTO article (title, content, author)
        VALUES (?, ?, ?)
    ''', (f"{original['title']} (복사)", original['content'], original['author']))
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return redirect(url_for('read_article', article_id=new_id))

@app.route('/articles/stats')
def statistics():
    """통계 정보"""
    conn = get_db()
    cursor = conn.cursor()
    
    # 전체 게시글 수
    cursor.execute("SELECT COUNT(*) FROM article")
    total_articles = cursor.fetchone()[0]
    
    # 작성자 수
    cursor.execute("SELECT COUNT(DISTINCT author) FROM article")
    authors_count = cursor.fetchone()[0]
    
    # 작성자별 게시글 수
    cursor.execute('''
        SELECT author, COUNT(*) as count
        FROM article
        GROUP BY author
        ORDER BY count DESC
    ''')
    author_stats = cursor.fetchall()
    
    conn.close()
    
    return render_template(
        'statistics.html',
        total_articles=total_articles,
        authors_count=authors_count,
        author_stats=author_stats
    )

# 샘플 데이터 초기화
def init_sample_data():
    """샘플 데이터 추가"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM article")
    if cursor.fetchone()[0] == 0:
        articles = [
            ('Flask 시작하기', 'Flask는 가볍고 유연한 웹 프레임워크입니다.', 'Alice'),
            ('데이터베이스 연동', '직접 SQL을 사용하여 데이터베이스를 관리할 수 있습니다.', 'Bob'),
            ('Jinja 템플릿', 'Jinja는 강력한 템플릿 엔진입니다.', 'Alice'),
        ]
        
        cursor.executemany('''
            INSERT INTO article (title, content, author)
            VALUES (?, ?, ?)
        ''', articles)
        
        conn.commit()
        print("샘플 데이터 추가 완료!")
    
    conn.close()

if __name__ == '__main__':
    init_sample_data()  # 샘플 데이터 추가
    app.run(debug=True)
    init_sample_data()
    app.run(debug=True, port=5000)

# 미션:
# 1. 조회수 기능을 추가하세요. (views 컬럼 추가, 조회할 때마다 증가)
# 2. 게시글을 최신순 외에 인기순(조회수)으로도 정렬할 수 있게 하세요.
# 정답:
# Article 모델에 추가:
# views = db.Column(db.Integer, default=0)
#
# read_article 함수에서 조회수 증가:
# article.views += 1
# db.session.commit()