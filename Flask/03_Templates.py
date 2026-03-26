# 03_Templates.py
# Jinja2 템플릿 사용
# 이 파일에서는 HTML 템플릿 파일을 사용하여 동적 페이지를 생성합니다.
# 반드시 Jinja_Template_Guide.txt 파일을 읽고 학습하세요!
# 디렉토리 구조:
# - 03_Templates.py
# - templates/
#   - index.html
#   - user.html
#   - products.html
#   - base.html

from flask import Flask, render_template  # render_template: 템플릿 파일을 렌더링

app = Flask(__name__)  # Flask 앱 생성

# 라우팅 1: 간단한 템플릿 렌더링
@app.route('/')
def index():
    """메인 페이지"""
    # render_template('파일명', 변수=값)
    # 템플릿 파일에 변수를 전달하여 템플릿이 동적으로 생성됩니다.
    return render_template(
        'index.html',
        title='Flask 템플릿 예제',
        welcome_message='Flask에 오신 것을 환영합니다!',
        items=['라우팅', '템플릿', '데이터베이스', '인증']
    )

# 라우팅 2: 사용자 정보 표시
@app.route('/user/<int:user_id>')
def user(user_id):
    """사용자 정보 페이지"""
    # 사용자 데이터 (실제로는 데이터베이스에서 조회)
    users = {
        1: {'name': 'Alice', 'email': 'alice@example.com', 'age': 25},
        2: {'name': 'Bob', 'email': 'bob@example.com', 'age': 30},
        3: {'name': 'Charlie', 'email': 'charlie@example.com', 'age': 28},
    }
    
    user_data = users.get(user_id)
    
    if user_data:  # 사용자가 존재하면
        return render_template(
            'user.html',
            user=user_data,  # 딕셔너리를 템플릿으로 전달
            user_id=user_id
        )
    else:
        return '<h1>사용자를 찾을 수 없습니다.</h1>', 404

# 라우팅 3: 상품 목록
@app.route('/products')
def products():
    """상품 목록 페이지"""
    # 상품 리스트 (실제로는 데이터베이스에서 조회)
    products_list = [
        {'id': 1, 'name': 'Laptop', 'price': 1500, 'in_stock': True},
        {'id': 2, 'name': 'Phone', 'price': 800, 'in_stock': True},
        {'id': 3, 'name': 'Tablet', 'price': 400, 'in_stock': False},
        {'id': 4, 'name': 'Monitor', 'price': 300, 'in_stock': True},
    ]
    
    return render_template(
        'products.html',
        products=products_list,
        total_products=len(products_list)
    )

# 라우팅 4: 전역 변수와 필터
@app.route('/demo')
def demo():
    """템플릿 필터 예제"""
    text = 'hello world'
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    
    return render_template(
        'demo.html',  # 별도로 만들어야 함
        text=text,
        numbers=numbers,
        length=len(numbers)
    )

# 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True, port=5000)

"""
필요한 템플릿 파일들:

1. templates/index.html
   (아래 내용 참고)

2. templates/user.html
   (아래 내용 참고)

3. templates/products.html
   (아래 내용 참고)

4. templates/base.html
   (기본 템플릿, 상속 용도)
"""

# 미션:
# 1. /posts 라우트를 만들고 post 목록을 템플릿으로 표시하세요.
# 2. templates/posts.html 파일을 만들어 for 루프로 게시글을 표시하세요.
# 정답:
# @app.route('/posts')
# def posts():
#     posts_list = [
#         {'id': 1, 'title': 'Flask 배우기', 'author': 'Alice'},
#         {'id': 2, 'title': 'Python 팁', 'author': 'Bob'},
#     ]
#     return render_template('posts.html', posts=posts_list)