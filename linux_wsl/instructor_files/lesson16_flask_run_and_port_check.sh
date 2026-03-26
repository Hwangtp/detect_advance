#!/bin/bash
# WSL Ubuntu 기준 강사용 실습 파일
# 이 파일은 한 줄씩 직접 입력하며 설명하는 수업 노트다.
# 자동 실행용이라기보다 강사용 실습 가이드로 사용한다.
# 모든 실습은 WSL Ubuntu 터미널에서 진행하는 것을 기준으로 한다.

# 수업 제목: Flask 실행과 포트 확인
# 수업 목표: 간단한 Flask 앱을 실행하고 localhost와 포트 개념을 확인한다.
# 수업 개요: WSL Ubuntu에서 Flask 앱을 만들고 브라우저와 curl로 접속 확인까지 해 본다.

# 핵심 개념
# - 웹 앱은 특정 포트에서 요청을 기다리는 프로세스다.
# - localhost와 127.0.0.1은 현재 내 컴퓨터 자신을 가리킨다.

# 핵심 실습 명령어

# Flask 앱 폴더를 만든다.
mkdir -p ~/linux_lab/day16/flask_app

# 앱 폴더로 이동한다.
cd ~/linux_lab/day16/flask_app

# 가상환경을 만든다.
python3 -m venv .venv

# 가상환경을 활성화한다.
source .venv/bin/activate

# Flask 패키지를 설치한다.
pip install flask

# Flask 앱 파일을 작성한다.
nano app.py

# 파이썬으로 앱을 직접 실행한다.
python app.py

# curl로 로컬 서버 응답을 확인한다.
curl http://127.0.0.1:5000

# 5000번 포트에서 어떤 프로세스가 대기 중인지 확인한다.
ss -tulnp | grep 5000

# 보충 코드 예시

# 파일 예시: app.py
# from flask import Flask
# 
# app = Flask(__name__)
# 
# @app.route('/')
# def home():
#     return 'Hello from WSL Flask'
# 
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)

# 개인 실습 문제

# 문제 1. /hello 경로를 추가해 다른 문장을 반환하도록 만들어 보자.
# 문제 2. port 값을 5001로 바꾸고 curl 주소도 맞춰 다시 접속해 보자.
# 문제 3. ss 명령에서 LISTEN 상태가 왜 보이는지 설명해 보자.

# 정답 예시

# 정답 1. @app.route('/hello') 함수를 하나 더 만들면 된다.
# 정답 2. app.run(..., port=5001) 로 바꾸고 curl http://127.0.0.1:5001 로 테스트하면 된다.
# 정답 3. Flask 서버가 외부 요청을 기다리며 포트를 열고 있기 때문이다.
