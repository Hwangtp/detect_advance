# 04_Forms.py
# HTML 폼 처리
# 이 파일에서는 사용자로부터 데이터를 입력받고 처리하는 방법을 배웁니다.
# 실행: python 04_Forms.py

from flask import Flask, render_template, request, redirect, url_for  # 폼 처리용 모듈 임포트

app = Flask(__name__)  # Flask 앱 생성

# 메모리에 데이터 저장 (실제로는 데이터베이스 사용)
users_list = []  # 사용자 정보 저장소
contact_messages = []  # 문의 메시지 저장소

# 라우팅 1: 간단한 폼
@app.route('/register', methods=['GET', 'POST'])  # GET (폼 표시), POST (데이터 처리)
def register():
    """사용자 회원가입"""
    if request.method == 'POST':  # POST 요청 (폼 제출)
        # 폼 데이터 추출
        username = request.form.get('username')  # 'username' 필드 값
        email = request.form.get('email')  # 'email' 필드 값
        password = request.form.get('password')  # 'password' 필드 값
        
        # 기본 검증
        if not username or not email or not password:
            error = '모든 필드를 입력하세요!'
            return render_template('register.html', error=error)
        
        # 사용자 정보 저장
        user = {
            'username': username,
            'email': email,
            'password': password  # 실제로는 암호화 필요!
        }
        users_list.append(user)
        
        # 성공 메시지와 함께 리다이렉트
        return render_template('register_success.html', user=user)
    
    else:  # GET 요청 (폼 표시)
        return render_template('register.html')

# 라우팅 2: 여러 필드의 폼
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """문의 폼"""
    if request.method == 'POST':
        # 폼 데이터 추출
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        subject = request.form.get('subject')
        message = request.form.get('message')
        category = request.form.get('category')  # 선택 박스
        
        # 검증
        if not all([name, email, message]):
            return render_template(
                'contact.html',
                error='필수 필드를 입력하세요!'
            )
        
        # 메시지 저장
        contact = {
            'name': name,
            'email': email,
            'phone': phone,
            'subject': subject or '제목 없음',
            'message': message,
            'category': category or '기타'
        }
        contact_messages.append(contact)
        
        # 확인 페이지로 리다이렉트
        return redirect(url_for('contact_success'))
    
    else:
        return render_template('contact.html')

# 라우팅 3: 폼 성공 페이지
@app.route('/contact-success')
def contact_success():
    """문의 성공 페이지"""
    return '''
    <h1>감사합니다!</h1>
    <p>문의가 접수되었습니다.</p>
    <a href="/contact">다시 보내기</a> | 
    <a href="/">홈으로</a>
    '''

# 라우팅 4: 폼 데이터 확인
@app.route('/users')
def users():
    """등록된 사용자 목록"""
    return render_template('users_list.html', users=users_list)

# 라우팅 5: 검색 폼
@app.route('/search', methods=['GET', 'POST'])
def search():
    """검색 기능"""
    if request.method == 'POST':
        query = request.form.get('query', '')
        results = []
        
        # 사용자 목록에서 검색
        for user in users_list:
            if query.lower() in user['username'].lower() or \
               query.lower() in user['email'].lower():
                results.append(user)
        
        return render_template('search_results.html', results=results, query=query)
    
    else:
        return render_template('search.html')

# 라우팅 6: 체크박스와 라디오 버튼
@app.route('/survey', methods=['GET', 'POST'])
def survey():
    """설문조사 폼"""
    if request.method == 'POST':
        # 라디오 버튼 (하나만 선택)
        rating = request.form.get('rating')  # rating: 1~5
        
        # 체크박스 (여러 개 선택 가능)
        features = request.form.getlist('features')  # 여러 값 받기
        
        # 텍스트 영역
        feedback = request.form.get('feedback')
        
        result = {
            'rating': rating,
            'features': features,
            'feedback': feedback
        }
        
        return render_template('survey_result.html', result=result)
    
    else:
        return render_template('survey.html')

# 라우팅 7: HTML 폼 직접 표시
@app.route('/')
def index():
    """메인 페이지"""
    return '''
    <h1>Flask 폼 처리 예제</h1>
    <ul>
        <li><a href="/register">회원가입</a></li>
        <li><a href="/contact">문의하기</a></li>
        <li><a href="/search">검색</a></li>
        <li><a href="/survey">설문조사</a></li>
        <li><a href="/users">등록된 사용자</a></li>
    </ul>
    '''

# 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True, port=5000)

"""
필요한 템플릿 파일들:

1. templates/register.html
   회원가입 폼

2. templates/register_success.html
   회원가입 성공 페이지

3. templates/contact.html
   문의 폼

4. templates/users_list.html
   사용자 목록

5. templates/search.html
   검색 폼

6. templates/search_results.html
   검색 결과

7. templates/survey.html
   설문조사 폼

8. templates/survey_result.html
   설문조사 결과
"""

# 미션:
# 1. /product-info 라우트를 만들고, 상품 정보를 입력받는 폼을 만드세요.
# 2. 이름, 가격, 설명, 카테고리를 입력받으세요.
# 정답:
# @app.route('/product-info', methods=['GET', 'POST'])
# def product_info():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         price = request.form.get('price')
#         description = request.form.get('description')
#         category = request.form.get('category')
#         return f'<h1>상품: {name}</h1><p>가격: {price}</p>'
#     else:
#         return '''
#         <form method="post">
#             <input name="name" placeholder="상품명"><br>
#             <input name="price" placeholder="가격"><br>
#             <textarea name="description"></textarea><br>
#             <select name="category">
#                 <option>전자제품</option>
#                 <option>의류</option>
#             </select><br>
#             <button>제출</button>
#         </form>
#         '''