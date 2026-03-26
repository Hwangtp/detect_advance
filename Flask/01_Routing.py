# 01_Routing.py
# 고급 라우팅 기능
# 이 파일에서는 URL 매개변수, 쿼리 문자열, HTTP 메서드 등을 배웁니다.
# 실행: python 01_Routing.py

from flask import Flask, request, redirect, url_for  # Flask 및 요청 처리 클래스 임포트

app = Flask(__name__)  # Flask 앱 생성

# 라우팅 예제 1: 기본 라우팅
@app.route('/')
def index():
    """홈 페이지"""
    return '''
    <h1>Flask 라우팅 예제</h1>
    <ul>
        <li><a href="/products">상품 목록</a></li>
        <li><a href="/product/1">상품 1</a></li>
        <li><a href="/product/2">상품 2</a></li>
        <li><a href="/user/john/posts">John의 게시글</a></li>
        <li><a href="/search?keyword=python">Python 검색</a></li>
        <li><a href="/redirect-example">리다이렉트 예제</a></li>
    </ul>
    '''

# 라우팅 예제 2: 정수형 매개변수
@app.route('/product/<int:product_id>')  # <int:product_id>: 정수만 받음
def product_detail(product_id):
    """
    상품 상세 페이지입니다.
    product_id는 정수로만 변환됩니다.
    예: /product/1 (O), /product/abc (X - 자동으로 404 오류)
    """
    products = {  # 상품 정보 딕셔너리
        1: {'name': 'Laptop', 'price': 1500},
        2: {'name': 'Phone', 'price': 800},
        3: {'name': 'Tablet', 'price': 400},
    }
    
    if product_id in products:  # 상품이 존재하면
        product = products[product_id]
        return f'''
        <h1>{product['name']}</h1>
        <p>가격: ${product['price']}</p>
        <a href="/products">상품 목록으로</a>
        '''
    else:  # 상품이 없으면
        return '<h1>상품을 찾을 수 없습니다.</h1>', 404

# 라우팅 예제 3: 여러 경로 매개변수
@app.route('/user/<username>/posts/<int:post_id>')  # 문자열과 정수 모두 사용
def user_post(username, post_id):
    """
    사용자의 특정 게시글을 표시합니다.
    예: /user/john/posts/5 -> username='john', post_id=5
    """
    return f'''
    <h1>{username}님의 게시글 #{post_id}</h1>
    <p>이것은 {username}님이 작성한 게시글입니다.</p>
    <a href="/user/{username}/posts">모든 게시글 보기</a>
    '''

# 라우팅 예제 4: 정보만 보기 (고정 경로도 가변 경로도 가능)
@app.route('/products')  # 고정 경로
def products_list():
    """상품 목록 페이지"""
    return '''
    <h1>상품 목록</h1>
    <ul>
        <li><a href="/product/1">상품 1: Laptop</a></li>
        <li><a href="/product/2">상품 2: Phone</a></li>
        <li><a href="/product/3">상품 3: Tablet</a></li>
    </ul>
    <a href="/">홈으로</a>
    '''

# 라우팅 예제 5: 쿼리 문자열 (Query String)
@app.route('/search')  # 쿼리 문자열: ?keyword=python&page=2
def search():
    """
    검색 기능입니다.
    쿼리 문자열을 사용하여 검색어와 페이지를 받습니다.
    예: /search?keyword=python&page=2
    """
    keyword = request.args.get('keyword', 'default')  # 기본값: 'default'
    page = request.args.get('page', 1, type=int)  # 기본값: 1, 정수로 변환
    
    return f'''
    <h1>검색 결과</h1>
    <p>검색어: {keyword}</p>
    <p>페이지: {page}</p>
    <form>
        <input type="text" name="keyword" placeholder="검색어 입력">
        <input type="number" name="page" placeholder="페이지" value="1">
        <button type="submit">검색</button>
    </form>
    <a href="/">홈으로</a>
    '''

# 라우팅 예제 6: 여러 경로가 같은 함수로 연결
@app.route('/main')  # 첫 번째 경로
@app.route('/index')  # 두 번째 경로
@app.route('/home')  # 세 번째 경로
def home():
    """
    여러 경로가 같은 함수로 연결됩니다.
    /main, /index, /home 모두 이 함수를 실행합니다.
    """
    return '<h1>홈 페이지</h1><a href="/">돌아가기</a>'

# 라우팅 예제 7: 리다이렉트 (Redirect)
@app.route('/redirect-example')
def redirect_example():
    """
    다른 페이지로 자동 이동합니다.
    redirect(url_for('함수명')): 함수명의 URL로 이동
    """
    return redirect(url_for('index'))  # 홈 페이지로 리다이렉트

# 라우팅 예제 8: url_for 함수
@app.route('/url-example')
def url_example():
    """
    url_for 함수를 사용하여 URL을 동적으로 생성합니다.
    함수명을 문자열로 전달하면 해당 함수의 URL이 생성됩니다.
    """
    product_url = url_for('product_detail', product_id=1)  # /product/1
    user_url = url_for('user_post', username='john', post_id=5)  # /user/john/posts/5
    
    return f'''
    <h1>URL 생성 예제</h1>
    <p>상품 URL: <a href="{product_url}">{product_url}</a></p>
    <p>사용자 게시글 URL: <a href="{user_url}">{user_url}</a></p>
    <a href="/">홈으로</a>
    '''

# 라우팅 예제 9: HTTP 메서드 분리 (GET, POST, PUT, DELETE)
@app.route('/api/comments', methods=['GET', 'POST'])  # GET과 POST 모두 처리
def comments():
    """
    댓글 API입니다.
    GET: 댓글 목록 반환
    POST: 새로운 댓글 추가
    """
    if request.method == 'GET':  # GET 요청
        comments_list = [
            {'id': 1, 'text': 'Great!'},
            {'id': 2, 'text': 'Awesome!'},
        ]
        return f'<h1>댓글 목록</h1><p>{comments_list}</p>'
    
    elif request.method == 'POST':  # POST 요청
        comment_text = request.form.get('text', 'No text')
        return f'<h1>댓글 저장됨</h1><p>내용: {comment_text}</p>'

# 라우팅 예제 10: 와일드카드 경로
@app.route('/files/<path:filename>')  # <path:filename>: 슬래시를 포함한 경로 허용
def serve_file(filename):
    """
    파일 서빙 예제입니다.
    /files/css/style.css -> filename='css/style.css'
    """
    return f'<h1>파일 요청</h1><p>파일 경로: {filename}</p>'

# 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True, port=5000)

# 미션:
# 1. /blog/<int:year>/<int:month> 라우트를 추가하세요. 연도와 월을 받아서 표시하세요.
# 2. /api/posts 라우트를 만들어 GET (목록)과 POST (생성)를 다르게 처리하세요.
# 정답:
# @app.route('/blog/<int:year>/<int:month>')
# def blog_archive(year, month):
#     return f'<h1>{year}년 {month}월 블로그</h1>'
#
# @app.route('/api/posts', methods=['GET', 'POST'])
# def api_posts():
#     if request.method == 'GET':
#         return '<h1>게시글 목록</h1>'
#     elif request.method == 'POST':
#         return '<h1>게시글 생성됨</h1>'