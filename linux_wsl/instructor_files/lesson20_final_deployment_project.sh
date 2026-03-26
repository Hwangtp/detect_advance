#!/bin/bash
# WSL Ubuntu 기준 강사용 실습 파일
# 이 파일은 한 줄씩 직접 입력하며 설명하는 수업 노트다.
# 자동 실행용이라기보다 강사용 실습 가이드로 사용한다.
# 모든 실습은 WSL Ubuntu 터미널에서 진행하는 것을 기준으로 한다.

# 수업 제목: 최종 배포 프로젝트
# 수업 목표: WSL Ubuntu에서 Flask 앱을 Docker Compose로 실행하고 배포 흐름을 정리한다.
# 수업 개요: 리눅스 명령어, 네트워크, Python, Flask, Docker를 하나로 묶어 실제 배포형 예제를 완성한다.

# 핵심 개념
# - 배포는 앱을 다른 사람도 접속 가능한 상태로 만드는 과정이다.
# - 개발과 운영 사이의 핵심 차이는 실행 방식, 로그, 포트, 재현 가능성이다.

# 핵심 실습 명령어

# 최종 프로젝트 폴더를 만든다.
mkdir -p ~/linux_lab/day20/final_project

# 최종 프로젝트 폴더로 이동한다.
cd ~/linux_lab/day20/final_project

# 이전 차시 예제를 복사해 출발점을 만든다.
cp -r ~/linux_lab/day19/flask_docker/* .

# compose 설정 파일을 작성한다.
nano docker-compose.yml

# compose up은 정의된 서비스를 실행한다. -d 는 백그라운드 실행이다.
docker compose up -d

# compose ps는 서비스 컨테이너 상태를 확인한다.
docker compose ps

# 최종 배포 앱 응답을 다시 확인한다.
curl http://127.0.0.1:5050

# 전체 서비스 로그를 본다.
docker compose logs

# compose down은 관련 컨테이너와 네트워크를 정리한다.
docker compose down

# 보충 코드 예시

# 파일 예시: docker-compose.yml
# services:
#   web:
#     build: .
#     container_name: linux_final_web
#     ports:
#       - "5050:5000"

# 개인 실습 문제

# 문제 1. 서비스 이름을 webapp으로 바꾸고 compose up이 어떻게 반영되는지 확인해 보자.
# 문제 2. docker compose logs 로 앱 로그를 읽고 어떤 서버가 실행 중인지 말해 보자.
# 문제 3. 최종적으로 리눅스와 Docker가 왜 배포에 연결되는지 설명해 보자.

# 정답 예시

# 정답 1. docker-compose.yml 의 service 키 이름을 webapp으로 바꾸고 다시 up 하면 된다.
# 정답 2. Gunicorn 또는 Flask 앱 로그가 보이며 포트 바인딩 정보도 확인할 수 있다.
# 정답 3. 리눅스는 실행 환경, Docker는 동일한 환경을 재현해 배포를 쉽게 만드는 도구이기 때문이다.
