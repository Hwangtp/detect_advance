#!/bin/bash
# WSL Ubuntu 기준 강사용 실습 파일
# 이 파일은 한 줄씩 직접 입력하며 설명하는 수업 노트다.
# 자동 실행용이라기보다 강사용 실습 가이드로 사용한다.
# 모든 실습은 WSL Ubuntu 터미널에서 진행하는 것을 기준으로 한다.

# 수업 제목: 도커 입문과 기본 명령어
# 수업 목표: Docker가 무엇인지 이해하고 이미지와 컨테이너를 직접 실행한다.
# 수업 개요: 리눅스 위에서 Docker가 어떤 역할을 하는지 배우고 hello-world와 nginx 컨테이너를 실습한다.

# 핵심 개념
# - 이미지는 실행 준비가 끝난 프로그램 묶음이고 컨테이너는 실제 실행 중인 인스턴스다.
# - Docker는 환경 차이를 줄여 배포를 쉽게 만드는 도구다.

# 핵심 실습 명령어

# 도커가 설치됐는지 버전을 확인한다.
docker --version

# pull은 이미지를 다운로드한다.
docker pull hello-world

# images는 로컬에 저장된 이미지 목록을 보여준다.
docker images

# run은 이미지를 기반으로 컨테이너를 생성하고 실행한다.
docker run hello-world

# 웹서버 예시 이미지인 nginx를 내려받는다.
docker pull nginx

# -d 는 detached 백그라운드 실행, -p 8080:80 은 호스트 포트와 컨테이너 포트를 연결, --name 은 이름 지정이다.
docker run -d -p 8080:80 --name mynginx nginx

# 현재 실행 중인 컨테이너 목록을 본다.
docker ps

# nginx 컨테이너가 잘 응답하는지 확인한다.
curl http://127.0.0.1:8080

# logs는 컨테이너 로그를 출력한다.
docker logs mynginx

# stop은 실행 중인 컨테이너를 정상 종료한다.
docker stop mynginx

# rm은 종료된 컨테이너를 삭제한다.
docker rm mynginx

# 개인 실습 문제

# 문제 1. hello-world와 nginx 이미지의 차이를 설명해 보자.
# 문제 2. 8081:80 포트 매핑으로 nginx를 다시 실행해 보자.
# 문제 3. docker ps 와 docker images 의 차이를 설명해 보자.

# 정답 예시

# 정답 1. hello-world는 테스트용, nginx는 실제 웹서버 예시 이미지다.
# 정답 2. docker run -d -p 8081:80 --name mynginx2 nginx 로 실습할 수 있다.
# 정답 3. ps는 실행 중인 컨테이너, images는 저장된 이미지 목록을 보여준다.
