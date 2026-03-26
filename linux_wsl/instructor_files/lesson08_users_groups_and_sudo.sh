#!/bin/bash
# WSL Ubuntu 기준 강사용 실습 파일
# 이 파일은 한 줄씩 직접 입력하며 설명하는 수업 노트다.
# 자동 실행용이라기보다 강사용 실습 가이드로 사용한다.
# 모든 실습은 WSL Ubuntu 터미널에서 진행하는 것을 기준으로 한다.

# 수업 제목: 사용자 그룹 sudo 이해
# 수업 목표: 사용자와 그룹, sudo의 의미를 이해하고 안전하게 시스템 명령을 실행한다.
# 수업 개요: whoami, id, groups, sudo를 중심으로 시스템 권한 구조를 이해한다.

# 핵심 개념
# - 사용자와 그룹은 권한 관리의 기본 단위다.
# - sudo는 관리자 권한이 필요한 명령을 일시적으로 실행하게 해준다.
# - WSL Ubuntu에서도 계정 구조와 시스템 계정 파일은 일반 리눅스와 거의 같은 방식으로 보인다.

# 핵심 실습 명령어

# 현재 로그인한 사용자 이름을 다시 확인한다.
whoami

# id는 uid, gid, 소속 그룹을 보여준다.
id

# groups는 현재 사용자가 속한 그룹 목록을 간단히 보여준다.
groups

# 현재 계정 홈 디렉터리를 확인해 계정과 홈의 연결을 다시 확인한다.
echo $HOME

# /etc/passwd 는 계정 정보 파일이다. 현재 계정 한 줄을 찾아 홈 경로와 기본 셸을 읽어 본다.
grep "^$USER:" /etc/passwd

# /etc/group 은 그룹 정보 파일이다. sudo 그룹 줄을 직접 읽으며 그룹 구조를 이해한다.
grep '^sudo' /etc/group

# sudo -l 은 현재 사용자가 어떤 sudo 권한을 갖는지 조회한다.
sudo -l

# apt update 는 패키지 목록을 갱신한다. sudo가 필요한 대표 명령이다.
sudo apt update

# apt install 은 패키지를 설치한다. -y 옵션은 yes를 자동 승인한다.
sudo apt install -y tree

# 설치한 tree 명령으로 실습 폴더 구조를 보기 좋게 출력한다.
tree ~/linux_lab

# adduser는 새 사용자를 만든다. 실습 환경에서는 필요시만 사용한다.
sudo adduser linuxstudent

# usermod -aG 는 기존 그룹을 유지한 채 새 그룹을 추가한다. sudo 그룹에 넣는 예시다.
sudo usermod -aG sudo linuxstudent

# 실습용 새 계정이 만들어졌는지 passwd 파일에서 확인한다.
grep '^linuxstudent:' /etc/passwd

# 생성한 실습용 사용자를 삭제하는 예시다.
sudo deluser linuxstudent

# 개인 실습 문제

# 문제 1. 현재 사용자가 어떤 그룹에 속해 있는지 확인하고 그 의미를 설명해 보자.
# 문제 2. tree가 없다면 sudo apt install로 설치한 뒤 다시 실행해 보자.
# 문제 3. sudo가 왜 필요한지 apt update 예시를 기준으로 설명해 보자.
# 문제 4. /etc/passwd 에서 현재 계정 줄을 찾아 홈 디렉터리와 기본 셸이 어디인지 읽어 보자.

# 정답 예시

# 정답 1. groups 또는 id로 확인할 수 있으며 그룹은 권한 묶음 단위다.
# 정답 2. sudo apt install -y tree 후 tree ~/linux_lab 를 실행하면 된다.
# 정답 3. 시스템 전역 패키지 정보와 설정은 일반 사용자 권한으로 바꾸기 어려워서 sudo가 필요하다.
# 정답 4. grep "^$USER:" /etc/passwd 결과에서 보통 /home/계정명 과 /bin/bash 또는 /bin/sh 같은 셸 정보를 볼 수 있다.
