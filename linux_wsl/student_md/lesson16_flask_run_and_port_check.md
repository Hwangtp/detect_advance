<div align="center">

# Flask 실행과 포트 확인

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> 간단한 Flask 앱을 실행하고 localhost와 포트 개념을 확인한다.

> **오늘 배우는 내용**  
> WSL Ubuntu에서 Flask 앱을 만들고 브라우저와 curl로 접속 확인까지 해 본다.

## 핵심 개념

- 웹 앱은 특정 포트에서 요청을 기다리는 프로세스다.
- localhost와 127.0.0.1은 현재 내 컴퓨터 자신을 가리킨다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
mkdir -p ~/linux_lab/day16/flask_app
cd ~/linux_lab/day16/flask_app
python3 -m venv .venv
source .venv/bin/activate
pip install flask
nano app.py
python app.py
curl http://127.0.0.1:5000
ss -tulnp | grep 5000
```

### 실습 파일 예시: `app.py`

```bash
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from WSL Flask'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

## 개인 실습 문제

1. /hello 경로를 추가해 다른 문장을 반환하도록 만들어 보자.
2. port 값을 5001로 바꾸고 curl 주소도 맞춰 다시 접속해 보자.
3. ss 명령에서 LISTEN 상태가 왜 보이는지 설명해 보자.

## 정답 예시

1. @app.route('/hello') 함수를 하나 더 만들면 된다.
2. app.run(..., port=5001) 로 바꾸고 curl http://127.0.0.1:5001 로 테스트하면 된다.
3. Flask 서버가 외부 요청을 기다리며 포트를 열고 있기 때문이다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
