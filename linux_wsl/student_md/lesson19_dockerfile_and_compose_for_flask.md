<div align="center">

# Dockerfile과 Compose로 Flask 묶기

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> Flask 앱을 Docker 이미지로 만들고 compose로 실행한다.

> **오늘 배우는 내용**  
> 직접 만든 앱을 컨테이너화하면서 Docker의 진짜 가치를 체감한다.

## 핵심 개념

- Dockerfile은 이미지를 만드는 조리법이다.
- compose는 여러 설정을 파일로 적어 실행을 단순하게 만든다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
mkdir -p ~/linux_lab/day19/flask_docker
cd ~/linux_lab/day19/flask_docker
nano app.py
nano requirements.txt
nano Dockerfile
docker build -t flask-demo:1.0 .
docker images
docker run -d -p 5050:5000 --name flask-demo-app flask-demo:1.0
curl http://127.0.0.1:5050
docker stop flask-demo-app
docker rm flask-demo-app
```

### 실습 파일 예시: `app.py`

```bash
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Dockerized Flask on Linux'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### 실습 파일 예시: `requirements.txt`

```bash
flask==3.1.0
gunicorn==23.0.0
```

### 실습 파일 예시: `Dockerfile`

```bash
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

## 개인 실습 문제

1. /health 경로를 추가하고 다시 이미지를 빌드해 보자.
2. 컨테이너 이름과 포트를 바꿔 두 번째 실행을 해 보자.
3. Dockerfile의 EXPOSE와 docker run -p 의 차이를 설명해 보자.

## 정답 예시

1. app.py 수정 후 docker build -t flask-demo:1.1 . 로 새 이미지를 만들면 된다.
2. docker run -d -p 5051:5000 --name flask-demo-app2 flask-demo:1.1 형태로 실행할 수 있다.
3. EXPOSE는 문서적 선언이고 실제 포트 연결은 -p 옵션이 수행한다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
