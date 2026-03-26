# 02_Static_Files.py
# 정적 파일 (CSS, JavaScript, 이미지) 처리
# 이 파일에서는 CSS와 JavaScript를 사용하는 방법을 배웁니다.
# 실행: python 02_Static_Files.py
# 디렉토리 구조:
# - 02_Static_Files.py
# - static/
#   - css/
#     - style.css
#   - js/
#     - script.js
#   - images/
#     - logo.png

from flask import Flask, url_for  # url_for: 정적 파일의 경로를 생성

app = Flask(__name__)  # Flask 앱 생성

# 라우팅: 메인 페이지
@app.route('/')
def index():
    """
    메인 페이지입니다.
    CSS와 JavaScript를 로드합니다.
    """
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>정적 파일 예제</title>
        <!-- CSS 파일 링크: url_for('static', filename='css/style.css')는 /static/css/style.css를 생성 -->
        <link rel="stylesheet" href="/static/css/style.css">
        <style>
            /* 인라인 스타일: 간단한 스타일 정의 */
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            h1 { color: #333; }
            .button-group {
                margin: 20px 0;
            }
            button {
                padding: 10px 20px;
                margin-right: 10px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 14px;
            }
            button:hover {
                background-color: #0056b3;
            }
            .result {
                margin-top: 20px;
                padding: 10px;
                background-color: #e7f3ff;
                border-left: 4px solid #007bff;
                display: none;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Flask 정적 파일 예제</h1>
            
            <h2>1. 이미지 표시</h2>
            <p>다음은 정적 이미지입니다:</p>
            <img src="/static/images/logo.png" alt="로고" style="max-width: 200px;">
            
            <h2>2. 버튼 클릭 이벤트</h2>
            <div class="button-group">
                <button onclick="showMessage()">메시지 표시</button>
                <button onclick="changeColor()">배경색 변경</button>
                <button onclick="showTime()">현재 시간</button>
                <button onclick="resetPage()">초기화</button>
            </div>
            
            <h2>3. 결과 표시</h2>
            <div class="result" id="result"></div>
            
            <h2>4. 입력 폼</h2>
            <input type="text" id="nameInput" placeholder="이름을 입력하세요">
            <button onclick="greet()">인사하기</button>
            
            <h2>5. 리스트 추가</h2>
            <input type="text" id="itemInput" placeholder="항목을 입력하세요">
            <button onclick="addItem()">추가</button>
            <ul id="itemList"></ul>
        </div>
        
        <!-- JavaScript 파일 링크: /static/js/script.js -->
        <script src="/static/js/script.js"></script>
        
        <!-- 인라인 JavaScript: 간단한 함수 정의 -->
        <script>
            // JavaScript 함수 예제들
            
            // 1. 메시지 표시
            function showMessage() {
                const result = document.getElementById('result');
                result.textContent = '안녕하세요! Flask 정적 파일이 작동합니다.';
                result.style.display = 'block';
            }
            
            // 2. 배경색 변경
            function changeColor() {
                const colors = ['#fff', '#ffe7e7', '#e7ffe7', '#e7e7ff', '#ffffe7'];
                const randomColor = colors[Math.floor(Math.random() * colors.length)];
                document.body.style.backgroundColor = randomColor;
            }
            
            // 3. 현재 시간 표시
            function showTime() {
                const result = document.getElementById('result');
                const now = new Date();
                result.textContent = '현재 시간: ' + now.toLocaleString();
                result.style.display = 'block';
            }
            
            // 4. 페이지 초기화
            function resetPage() {
                document.body.style.backgroundColor = '#f5f5f5';
                document.getElementById('result').style.display = 'none';
                document.getElementById('itemList').innerHTML = '';
                document.getElementById('nameInput').value = '';
                document.getElementById('itemInput').value = '';
            }
            
            // 5. 인사하기
            function greet() {
                const name = document.getElementById('nameInput').value;
                if (name) {
                    const result = document.getElementById('result');
                    result.textContent = name + '님, 안녕하세요!';
                    result.style.display = 'block';
                } else {
                    alert('이름을 입력하세요!');
                }
            }
            
            // 6. 리스트 항목 추가
            function addItem() {
                const input = document.getElementById('itemInput');
                const list = document.getElementById('itemList');
                
                if (input.value) {
                    const li = document.createElement('li');
                    li.textContent = input.value;
                    list.appendChild(li);
                    input.value = '';
                } else {
                    alert('항목을 입력하세요!');
                }
            }
        </script>
    </body>
    </html>
    '''

# 라우팅: 정적 파일 경로 정보
@app.route('/about')
def about():
    """정적 파일에 대한 정보"""
    return '''
    <h1>정적 파일 관리</h1>
    <h2>디렉토리 구조</h2>
    <pre>
project/
├── app.py
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       └── logo.png
└── templates/
    └── index.html
    </pre>
    <h2>url_for 사용법</h2>
    <p>url_for('static', filename='css/style.css') → /static/css/style.css</p>
    <p>url_for('static', filename='js/script.js') → /static/js/script.js</p>
    <p>url_for('static', filename='images/logo.png') → /static/images/logo.png</p>
    <a href="/">홈으로</a>
    '''

# 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True, port=5000)

"""
정적 파일 설정을 위해 필요한 파일들:

1. static/css/style.css 생성:
   body { font-family: Arial; }
   h1 { color: #007bff; }

2. static/js/script.js 생성:
   console.log('JavaScript 로드됨');

3. static/images/logo.png:
   (이미지 파일을 다운로드하거나 생성하세요)

또는 주어진 샘플로 빈 파일 생성 가능:
   touch static/css/style.css
   touch static/js/script.js
"""

# 미션:
# 1. static/css/style.css 파일을 만들고 h1 색상을 빨간색으로 설정하세요.
# 2. static/js/script.js에 alert 함수를 하나 추가하세요.
# 정답:
# CSS:
# h1 { color: red; }
#
# JavaScript:
# alert('JavaScript 파일이 로드되었습니다!');