#!/bin/bash
# WSL Ubuntu 기준 강사용 실습 파일
# 이 파일은 한 줄씩 직접 입력하며 설명하는 수업 노트다.
# 자동 실행용이라기보다 강사용 실습 가이드로 사용한다.
# 모든 실습은 WSL Ubuntu 터미널에서 진행하는 것을 기준으로 한다.

# 수업 제목: 패키지 관리와 환경 정보
# 수업 목표: apt로 프로그램을 설치하고 환경 관련 명령을 이해한다.
# 수업 개요: 업데이트, 설치, 제거, 환경변수, which, whereis를 통해 개발 환경을 준비한다.

# 핵심 개념
# - 패키지 관리자는 리눅스에서 프로그램을 설치하는 표준 방법이다.
# - 어떤 명령이 어디에 설치됐는지 아는 습관이 중요하다.

# 핵심 실습 명령어

# 패키지 목록을 최신 상태로 갱신한다.
sudo apt update

# upgrade는 설치된 패키지를 최신 버전으로 업데이트한다. -y는 자동 승인이다.
sudo apt upgrade -y

# which는 명령어 실행 파일 경로를 찾는다.
which python3

# whereis는 바이너리, 소스, 매뉴얼 위치를 함께 보여준다.
whereis python3

# --version 옵션은 설치된 버전을 확인할 때 자주 사용한다.
python3 --version

# $PATH는 명령어를 찾는 경로 목록이다. 콜론으로 구분된다.
echo $PATH

# curl은 HTTP 요청 테스트에 자주 쓰이는 도구다.
sudo apt install -y curl

# 설치가 잘 됐는지 버전으로 확인한다.
curl --version

# remove는 패키지를 삭제한다. 설정 일부는 남을 수 있다.
sudo apt remove -y tree

# 수업용 도구를 다시 설치한다.
sudo apt install -y tree

# -L 2 는 tree 깊이를 2단계로 제한한다.
tree -L 2 ~/linux_lab

# 개인 실습 문제

# 문제 1. which, whereis, --version 세 가지로 python3 정보를 각각 확인해 보자.
# 문제 2. curl과 tree를 설치하거나 재설치해 보고 버전을 확인해 보자.
# 문제 3. $PATH를 보고 왜 명령어를 폴더명 없이 실행할 수 있는지 설명해 보자.

# 정답 예시

# 정답 1. which python3, whereis python3, python3 --version 을 순서대로 실행하면 된다.
# 정답 2. sudo apt install -y curl tree 후 curl --version, tree --version 또는 tree 실행으로 확인한다.
# 정답 3. PATH에 등록된 폴더를 셸이 탐색해 실행 파일을 찾기 때문이다.
