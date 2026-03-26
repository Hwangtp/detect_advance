# 08_File_Upload.py
# 파일 업로드 처리
# 사용자로부터 파일을 받아 저장하고 목록을 표시합니다.
# 설치: pip install flask
# 실행: python 08_File_Upload.py

from flask import Flask, render_template, request, redirect, url_for, send_file  # 파일 처리 모듈
import sqlite3  # 데이터베이스
import os  # 파일 시스템
from datetime import datetime  # 날짜/시간

app = Flask(__name__)

# 파일 업로드 설정
UPLOAD_FOLDER = 'uploads'  # 업로드 폴더

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# uploads 폴더가 없으면 생성
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 데이터베이스 파일 경로
DATABASE = 'upload_demo.db'

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
        CREATE TABLE IF NOT EXISTS file_upload (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_filename TEXT NOT NULL,
            saved_filename TEXT NOT NULL,
            file_size INTEGER,
            file_type TEXT,
            description TEXT,
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
    <h1>Flask 파일 업로드 예제</h1>
    <ul>
        <li><a href="/upload">파일 업로드</a></li>
        <li><a href="/files">업로드된 파일 목록</a></li>
        <li><a href="/statistics">업로드 통계</a></li>
    </ul>
    '''

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """파일 업로드 페이지"""
    if request.method == 'POST':
        # 폼 데이터 추출
        description = request.form.get('description', '')
        
        # 파일이 없으면
        if 'file' not in request.files:
            error = '파일을 선택하세요!'
            return render_template('upload.html', error=error)
        
        file = request.files['file']
        
        # 파일명이 비어있으면
        if file.filename == '':
            error = '파일을 선택하세요!'
            return render_template('upload.html', error=error)
        
        # 파일 저장
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # 데이터베이스에 저장
        file_size = os.path.getsize(file_path)
        file_type = filename.split('.')[-1] if '.' in filename else ''
        
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO file_upload (original_filename, saved_filename, file_size, file_type, description)
            VALUES (?, ?, ?, ?, ?)
        ''', (filename, filename, file_size, file_type, description))
        conn.commit()
        conn.close()
        
        return redirect(url_for('files_list'))
    
    return render_template('upload.html')

@app.route('/files')
def files_list():
    """업로드된 파일 목록"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM file_upload ORDER BY uploaded_at DESC")
    files = cursor.fetchall()
    conn.close()
    
    return render_template('files_list.html', files=files)

@app.route('/file/<int:file_id>')
def file_detail(file_id):
    """파일 상세 정보"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM file_upload WHERE id = ?", (file_id,))
    file = cursor.fetchone()
    conn.close()
    
    if not file:
        return "파일을 찾을 수 없습니다.", 404
    
    return render_template('file_detail.html', file=file)

@app.route('/download/<int:file_id>')
def download_file(file_id):
    """파일 다운로드"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM file_upload WHERE id = ?", (file_id,))
    file = cursor.fetchone()
    conn.close()
    
    if not file:
        return "파일을 찾을 수 없습니다.", 404
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file['saved_filename'])
    return send_file(file_path, as_attachment=True, download_name=file['original_filename'])

@app.route('/delete/<int:file_id>', methods=['POST'])
def delete_file(file_id):
    """파일 삭제"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM file_upload WHERE id = ?", (file_id,))
    file = cursor.fetchone()
    
    if file:
        # 파일 시스템에서 삭제
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file['saved_filename'])
        if os.path.exists(file_path):
            os.remove(file_path)
        
        # 데이터베이스에서 삭제
        cursor.execute("DELETE FROM file_upload WHERE id = ?", (file_id,))
        conn.commit()
    
    conn.close()
    return redirect(url_for('files_list'))

@app.route('/statistics')
def statistics():
    """업로드 통계"""
    conn = get_db()
    cursor = conn.cursor()
    
    # 총 파일 수
    cursor.execute("SELECT COUNT(*) FROM file_upload")
    total_files = cursor.fetchone()[0]
    
    # 총 파일 크기
    cursor.execute("SELECT SUM(file_size) FROM file_upload")
    total_size = cursor.fetchone()[0] or 0
    
    # 파일 타입별 수
    cursor.execute("SELECT file_type, COUNT(*) FROM file_upload GROUP BY file_type")
    type_stats = cursor.fetchall()
    
    conn.close()
    
    return render_template('statistics.html',
                         total_files=total_files,
                         total_size=total_size,
                         type_stats=type_stats)

if __name__ == '__main__':
    app.run(debug=True)