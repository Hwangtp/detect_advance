#!/bin/bash
# WSL Ubuntu 기준 강사용 실습 파일
# 이 파일은 한 줄씩 직접 입력하며 설명하는 수업 노트다.
# 자동 실행용이라기보다 강사용 실습 가이드로 사용한다.
# 모든 실습은 WSL Ubuntu 터미널에서 진행하는 것을 기준으로 한다.

# 수업 제목: Gunicorn과 백그라운드 실행
# 수업 목표: 개발 서버와 운영 서버의 차이를 알고 Gunicorn으로 앱을 실행한다.
# 수업 개요: Flask 개발 서버와 Gunicorn의 차이, nohup, 백그라운드 실행, 로그 확인을 경험한다.

# 핵심 개념
# - 개발 서버는 학습용, 운영 서버는 실제 서비스용에 가깝다.
# - Gunicorn은 Python 웹 앱을 더 안정적으로 실행하는 WSGI 서버다.

# 핵심 실습 명령어

# 앞에서 만든 Flask 앱 폴더로 이동한다.
cd ~/linux_lab/day16/flask_app

# 가상환경을 활성화한다.
source .venv/bin/activate

# 운영형 실행 예시를 위해 gunicorn을 설치한다.
pip install gunicorn

# --bind 는 주소와 포트를 지정한다. app:app 은 app.py 안의 Flask 객체 app을 뜻한다.
gunicorn --bind 0.0.0.0:8000 app:app

# Gunicorn 서버 응답을 확인한다.
curl http://127.0.0.1:8000

# nohup은 터미널 종료 후에도 프로세스를 유지한다. > 와 2>&1 은 표준출력과 에러를 로그 파일에 모은다. & 는 백그라운드 실행이다.
nohup gunicorn --bind 0.0.0.0:8000 app:app > gunicorn.log 2>&1 &

# 현재 셸의 백그라운드 작업을 확인한다.
jobs

# 실제 실행 중인 gunicorn 프로세스를 찾는다.
ps -ef | grep gunicorn

# 로그 파일 마지막 20줄을 확인한다.
tail -n 20 gunicorn.log

# pkill -f 는 명령행 패턴으로 프로세스를 종료한다.
pkill -f gunicorn

# 개인 실습 문제

# 문제 1. Flask 개발 서버와 Gunicorn의 차이를 말로 정리해 보자.
# 문제 2. nohup으로 실행 후 로그 파일이 생기는지 확인해 보자.
# 문제 3. 8000 대신 9000 포트로 Gunicorn을 띄우고 curl로 테스트해 보자.

# 정답 예시

# 정답 1. Flask 개발 서버는 개발용, Gunicorn은 더 운영 환경에 가까운 WSGI 서버다.
# 정답 2. nohup 명령 뒤에 > gunicorn.log 2>&1 & 를 붙이면 된다.
# 정답 3. gunicorn --bind 0.0.0.0:9000 app:app 후 curl http://127.0.0.1:9000 로 확인한다.
