# 07_Authentication.py
# 사용자 인증 기능
# 로그인, 로그아웃을 구현합니다.
# 설치: pip install flask
# 실행: python 07_Authentication.py

from flask import Flask, render_template, request, redirect, url_for, session  # 인증 관련 모듈
import sqlite3  # 데이터베이스

app = Flask(__name__)
app.config['SECRET_KEY'] = 'simple-secret-key'  # 세션 키

# 데이터베이스 파일 경로
DATABASE = 'auth_demo.db'

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
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            is_active BOOLEAN DEFAULT 1,
            role TEXT DEFAULT 'user'
        )
    ''')
    
    conn.commit()
    conn.close()

# 테이블 생성 실행
init_db()

# ========== 데코레이터 ==========

def login_required(f):
    """로그인이 필요한 페이지를 보호하는 데코레이터"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:  # 세션에 user_id가 없으면
            return redirect(url_for('login', next=request.url))  # 로그인 페이지로 리다이렉트
        return f(*args, **kwargs)
    return decorated_function

# ========== 라우팅 ==========

@app.route('/')
def index():
    """메인 페이지"""
    username = session.get('username')
    return '''
    <h1>Flask 사용자 인증 예제</h1>
    <ul>
    ''' + (
        f'<li>환영합니다, {username}님!</li>'
        '<li><a href="/dashboard">대시보드</a></li>'
        '<li><a href="/logout">로그아웃</a></li>'
    if username else
        '<li><a href="/login">로그인</a></li>'
        '<li><a href="/register">회원가입</a></li>'
    ) + '''
    </ul>
    '''

@app.route('/register', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def register():
    """회원가입"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # 검증
        if not all([username, email, password, confirm_password]):
            error = '모든 필드를 입력하세요!'
        elif password != confirm_password:
            error = '비밀번호가 일치하지 않습니다!'
        else:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM user WHERE username = ? OR email = ?", (username, email))
            if cursor.fetchone():
                error = '사용자명 또는 이메일이 이미 존재합니다!'
            else:
                cursor.execute("INSERT INTO user (username, email, password) VALUES (?, ?, ?)",
                               (username, email, password))
                conn.commit()
                error = None
            conn.close()
        
        if error is None:
            return redirect(url_for('login'))
        
        return render_template('register.html', error=error, username=username, email=email)
    
    return render_template('register.html')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """로그인"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        error = None
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        
        if user is None:
            error = '사용자명이 잘못되었습니다!'
        elif user['password'] != password:
            error = '비밀번호가 잘못되었습니다!'
        
        if error is None:
            session.clear()
            session['username'] = user['username']
            
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            return redirect(url_for('dashboard'))
        
        return render_template('login.html', error=error, username=username)
    
    return render_template('login.html')
        
        return render_template('login.html', error=error, username=username)
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """로그아웃"""
    session.clear()
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    """사용자 대시보드"""
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    
    return f'''
    <h1>{user['username']}님의 대시보드</h1>
    <p>이메일: {user['email']}</p>
    <ul>
        <li><a href="/logout">로그아웃</a></li>
    </ul>
    '''

if __name__ == '__main__':
    app.run(debug=True)
            return '비밀번호가 변경되었습니다! <a href="/dashboard">대시보드로</a>'
        
        return render_template('change_password.html', error=error)
    
    return render_template('change_password.html')

@app.route('/admin')
@admin_required
def admin_panel():
    """관리자 패널"""
    users = User.query.all()
    return render_template('admin_panel.html', users=users)

# 샘플 데이터
def init_sample_users():
    """샘플 사용자 추가"""
    with app.app_context():
        if User.query.count() == 0:
            # 일반 사용자
            user1 = User(username='alice', email='alice@example.com')
            user1.set_password('password123')
            
            # 관리자
            admin = User(username='admin', email='admin@example.com', role='admin')
            admin.set_password('admin123')
            
            db.session.add(user1)
            db.session.add(admin)
            db.session.commit()
            print("샘플 사용자 추가 완료!")

if __name__ == '__main__':
    init_sample_users()
    app.run(debug=True, port=5000)

# 미션:
# 1. 사용자가 비활성화되는 기능을 추가하세요.
# 2. 관리자가 사용자를 비활성화할 수 있는 기능을 추가하세요.
# 정답:
# @app.route('/admin/user/<int:user_id>/deactivate', methods=['POST'])
# @admin_required
# def deactivate_user(user_id):
#     user = User.query.get_or_404(user_id)
#     user.is_active = False
#     db.session.commit()
#     return '사용자가 비활성화되었습니다!'