# 00_Hello_Flask.py
# ===== Flask란 무엇인가? =====
# Flask는 Python로 웹 애플리케이션을 만드는 가벼운 웹 프레임워크입니다.
# - Micro Framework: 필수 기능만 포함 (가볍고 빠움)
# - 유연함: 필요한 기능을 직접 추가할 수 있음
# - 쉬운 학습: 초보자도 쉽게 배울 수 있음
# - 강력함: 대규모 프로젝트에도 사용 가능

# ===== Flask를 왜 사용하는가? =====
# 1. 간단함: 몇 줄의 코드로도 웹 서버를 만들 수 있음
# 2. 유연함: 자유롭게 프로젝트 구조를 설계할 수 있음
# 3. 학습 용이: Python 기초 알면 바로 배울 수 있음
# 4. 확장성: 필요에 따라 라이브러리 추가 가능 (DB, 인증, 파일처리 등)
# 5. 커뮤니티: 많은 자료와 라이브러리 지원

# ===== Flask의 동작 원리 =====
# 1. Flask 앱을 만든다
# 2. URL과 함수를 연결한다 (@app.route 데코레이터)
# 3. 웹 브라우저가 URL을 요청한다
# 4. Flask가 URL을 분석하고 해당 함수를 실행한다
# 5. 함수의 반환값(HTML)을 브라우저에 보낸다

# ===== 이 파일에서 배우는 것 =====
# 1. Flask 앱 생성하기
# 2. 라우팅 (URL 매핑) 방법
# 3. 뷰 함수 작성하기
# 4. HTML 응답 반환하기
# 5. 여러 라우트 만드는 방법

# 설치: pip install flask
# 실행: python 00_Hello_Flask.py
# 접속: http://localhost:5000 (웹 브라우저에서 접속)

from flask import Flask  # Flask 클래스를 임포트합니다.
# Flask: 웹 애플리케이션의 핵심 클래스
# 모든 Flask 웹앱은 Flask 인스턴스 하나를 기반으로 동작합니다.

# Flask 애플리케이션 생성
app = Flask(__name__)  # Flask 인스턴스를 생성합니다.
# __name__: 현재 모듈의 이름 (Flask가 리소스 위치를 파악할 때 사용)

# 라우팅 (Routing): URL과 함수를 연결합니다.
@app.route('/')  # 데코레이터: / 경로로 접속하면 아래 함수를 실행
def hello():  # 뷰 함수: URL에 매핑된 함수
    """
    홈 페이지를 표시하는 함수입니다.
    http://localhost:5000/ 에 접속하면 이 함수가 실행됩니다.
    반환값: HTML 문자열
    """
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask 시작</title>
        <style>
            body { font-family: Arial; text-align: center; margin-top: 50px; }
            h1 { color: blue; }
        </style>
    </head>
    <body>
        <h1>Flask에 오신 것을 환영합니다!</h1>
        <p>첫 번째 Flask 애플리케이션입니다.</p>
        <ul>
            <li><a href="/user/Alice">Alice 프로필</a></li>
            <li><a href="/user/Bob">Bob 프로필</a></li>
            <li><a href="/about">소개</a></li>
            <li><a href="/contact">문의</a></li>
        </ul>
    </body>
    </html>
    '''  # HTML 코드를 문자열로 반환합니다.

# 라우팅 예제 2: 다른 경로
@app.route('/about')  # /about 경로로 접속하면 이 함수 실행
def about():
    """소개 페이지"""
    return '<h1>소개 페이지</h1><p>이것은 Flask 웹 애플리케이션입니다.</p>'

# 라우팅 예제 3: URL 매개변수
@app.route('/user/<name>')  # <name>은 변수 (동적 URL)
def user_profile(name):
    """
    사용자 프로필 페이지입니다.
    URL에서 사용자 이름을 받아서 표시합니다.
    예: /user/Alice -> name = 'Alice'
    """
    return f'''
    <h1>{name}님의 프로필</h1>
    <p>환영합니다, {name}!</p>
    <a href="/">홈으로</a>
    '''  # f-string을 사용하여 변수를 HTML에 삽입합니다.

# 라우팅 예제 4: 여러 HTTP 메서드 처리
from flask import request  # 요청 정보를 처리하기 위해 임포트

@app.route('/contact', methods=['GET', 'POST'])  # GET과 POST 모두 지원
def contact():
    """
    문의 페이지입니다.
    GET 요청: 폼 표시
    POST 요청: 데이터 처리
    """
    if request.method == 'POST':  # POST 요청이면
        name = request.form.get('name')  # 폼 데이터에서 'name' 필드 추출
        email = request.form.get('email')  # 폼 데이터에서 'email' 필드 추출
        return f'<h1>감사합니다!</h1><p>{name}님({email})으로부터 받았습니다.</p><a href="/">홈으로</a>'
    else:  # GET 요청이면 폼을 표시
        return '''
        <h1>문의하기</h1>
        <form method="post">
            <input type="text" name="name" placeholder="이름" required><br>
            <input type="email" name="email" placeholder="이메일" required><br>
            <textarea name="message" placeholder="메시지" required></textarea><br>
            <button type="submit">전송</button>
        </form>
        <a href="/">홈으로</a>
        '''

# 오류 처리: 페이지를 찾을 수 없을 때
@app.errorhandler(404)  # 404 오류 (페이지 없음) 처리
def page_not_found(error):
    """
    존재하지 않는 페이지에 접속했을 때 처리합니다.
    """
    return '<h1>404 오류</h1><p>페이지를 찾을 수 없습니다.</p><a href="/">홈으로</a>', 404

# 애플리케이션 실행
if __name__ == '__main__':  # 이 파일이 직접 실행될 때
    # Flask 개발 서버를 시작합니다.
    app.run(
        host='localhost',  # 호스트: localhost (로컬 컴퓨터)
        port=5000,  # 포트: 5000 (변경 가능: 8000, 3000 등)
        debug=True  # 디버그 모드: 코드 변경 시 자동 재시작
    )

# 미션:
# 1. 새로운 라우트 '/hello/<name>'을 추가하여 인사말을 표시하세요.
# 2. 모든 라우트의 HTML을 더 예쁘게 꾸미세요.
# 정답:
# @app.route('/hello/<name>')
# def hello_user(name):
#     return f'<h1>안녕하세요, {name}님!</h1>'
#
# 실행 후 http://localhost:5000/hello/Alice 에 접속해보세요.