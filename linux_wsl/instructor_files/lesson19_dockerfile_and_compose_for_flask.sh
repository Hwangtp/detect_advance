#!/bin/bash
# WSL Ubuntu 기준 강사용 실습 파일
# 이 파일은 한 줄씩 직접 입력하며 설명하는 수업 노트다.
# 자동 실행용이라기보다 강사용 실습 가이드로 사용한다.
# 모든 실습은 WSL Ubuntu 터미널에서 진행하는 것을 기준으로 한다.

# 수업 제목: Dockerfile과 Compose로 Flask 묶기
# 수업 목표: Flask 앱을 Docker 이미지로 만들고 compose로 실행한다.
# 수업 개요: 직접 만든 앱을 컨테이너화하면서 Docker의 진짜 가치를 체감한다.

# 핵심 개념
# - Dockerfile은 이미지를 만드는 조리법이다.
# - compose는 여러 설정을 파일로 적어 실행을 단순하게 만든다.

# 핵심 실습 명령어

# Docker 예제 폴더를 만든다.
mkdir -p ~/linux_lab/day19/flask_docker

# 예제 폴더로 이동한다.
cd ~/linux_lab/day19/flask_docker

# Flask 앱 파일을 작성한다.
nano app.py

# 필요 패키지 목록 파일을 작성한다.
nano requirements.txt

# 이미지 빌드용 Dockerfile을 작성한다.
nano Dockerfile

# build는 Dockerfile을 읽어 이미지를 만든다. -t 는 태그 이름 지정이다.
docker build -t flask-demo:1.0 .

# 방금 만든 이미지가 목록에 생겼는지 확인한다.
docker images

# 호스트 5050 포트를 컨테이너 5000 포트와 연결해 실행한다.
docker run -d -p 5050:5000 --name flask-demo-app flask-demo:1.0

# 컨테이너로 실행된 Flask 앱 응답을 확인한다.
curl http://127.0.0.1:5050

# 실행 중인 컨테이너를 종료한다.
docker stop flask-demo-app

# 컨테이너를 제거한다.
docker rm flask-demo-app

# 보충 코드 예시

# 파일 예시: app.py
# from flask import Flask
# 
# app = Flask(__name__)
# 
# @app.route('/')
# def home():
#     return 'Dockerized Flask on Linux'
# 
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

# 파일 예시: requirements.txt
# flask==3.1.0
# gunicorn==23.0.0

# 파일 예시: Dockerfile
# FROM python:3.11-slim
# 
# WORKDIR /app
# 
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# 
# COPY app.py .
# 
# EXPOSE 5000
# 
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

# 개인 실습 문제

# 문제 1. /health 경로를 추가하고 다시 이미지를 빌드해 보자.
# 문제 2. 컨테이너 이름과 포트를 바꿔 두 번째 실행을 해 보자.
# 문제 3. Dockerfile의 EXPOSE와 docker run -p 의 차이를 설명해 보자.

# 정답 예시

# 정답 1. app.py 수정 후 docker build -t flask-demo:1.1 . 로 새 이미지를 만들면 된다.
# 정답 2. docker run -d -p 5051:5000 --name flask-demo-app2 flask-demo:1.1 형태로 실행할 수 있다.
# 정답 3. EXPOSE는 문서적 선언이고 실제 포트 연결은 -p 옵션이 수행한다.
