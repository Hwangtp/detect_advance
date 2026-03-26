#!/bin/bash
# WSL Ubuntu 기준 강사용 실습 파일
# 이 파일은 한 줄씩 직접 입력하며 설명하는 수업 노트다.
# 자동 실행용이라기보다 강사용 실습 가이드로 사용한다.
# 모든 실습은 WSL Ubuntu 터미널에서 진행하는 것을 기준으로 한다.

# 수업 제목: WSL에서 파이썬과 가상환경
# 수업 목표: python3, pip, venv를 이용해 개발 환경을 분리한다.
# 수업 개요: WSL Ubuntu에서 파이썬 개발 준비를 하고 가상환경을 사용해 본다.

# 핵심 개념
# - 가상환경은 프로젝트별 패키지 충돌을 막아 준다.
# - 배포 전 개발 환경을 분리하는 습관이 중요하다.

# 핵심 실습 명령어

# 설치된 파이썬 버전을 확인한다.
python3 --version

# pip는 파이썬 패키지 관리자다.
pip3 --version

# 프로젝트 폴더를 만든다.
mkdir -p ~/linux_lab/day15/flask_project

# 프로젝트 폴더로 이동한다.
cd ~/linux_lab/day15/flask_project

# -m venv 는 venv 모듈을 실행해 가상환경 폴더를 만든다.
python3 -m venv .venv

# source는 현재 셸에서 스크립트를 실행한다. activate로 가상환경을 활성화한다.
source .venv/bin/activate

# 가상환경 활성화 후 python 경로가 .venv 안으로 바뀌는지 확인한다.
which python

# 가상환경 안에서도 버전을 확인한다.
python --version

# pip install은 파이썬 패키지를 설치한다.
pip install flask

# 현재 설치된 패키지 목록을 requirements 형태로 출력한다.
pip freeze

# 패키지 목록을 파일로 저장한다.
pip freeze > requirements.txt

# 가상환경을 종료하고 시스템 기본 셸 상태로 돌아간다.
deactivate

# 개인 실습 문제

# 문제 1. 새 가상환경을 만들고 requests 패키지를 설치한 뒤 pip freeze 결과를 확인해 보자.
# 문제 2. 가상환경 활성화 전후 which python 결과가 왜 다른지 설명해 보자.
# 문제 3. requirements.txt를 만드는 이유를 말해 보자.

# 정답 예시

# 정답 1. python3 -m venv .venv 후 source .venv/bin/activate, pip install requests 순서로 진행하면 된다.
# 정답 2. 활성화 후에는 셸이 .venv/bin/python 을 우선 사용하기 때문이다.
# 정답 3. 다른 환경에서도 동일한 패키지 버전을 다시 설치하기 위해서다.
