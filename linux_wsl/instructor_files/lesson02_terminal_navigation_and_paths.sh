#!/bin/bash
# WSL Ubuntu 기준 강사용 실습 파일
# 이 파일은 한 줄씩 직접 입력하며 설명하는 수업 노트다.
# 자동 실행용이라기보다 강사용 실습 가이드로 사용한다.
# 모든 실습은 WSL Ubuntu 터미널에서 진행하는 것을 기준으로 한다.

# 수업 제목: 터미널 이동과 경로 이해
# 수업 목표: 절대경로와 상대경로를 구분하고 원하는 폴더로 정확히 이동한다.
# 수업 개요: pwd, ls, cd를 반복해 쓰며 경로 감각을 익히고 탭 자동완성도 함께 연습한다.

# 핵심 개념
# - 절대경로는 /로 시작하는 전체 주소다.
# - 상대경로는 현재 위치를 기준으로 계산하는 주소다.
# - .. 는 상위 폴더, . 는 현재 폴더를 의미한다.
# - WSL Ubuntu에서는 보통 /home/계정명 아래에서 개인 작업을 진행한다.

# 핵심 실습 명령어

# 실습 시작 전 현재 위치를 먼저 확인한다. 경로 학습은 항상 현재 위치 인식부터 시작한다.
pwd

# realpath 는 현재 위치의 실제 절대경로를 보여준다. . 은 현재 폴더를 의미한다.
realpath .

# 현재 계정의 홈 디렉터리 절대경로를 다시 확인한다.
echo $HOME

# /home 은 일반 계정 폴더들이 모이는 위치다.
cd /home

# ls -l 로 /home 아래 계정 폴더 구조를 본다. -l 옵션은 상세 목록이다.
ls -l /home

# ~ 로 다시 현재 계정 홈으로 돌아온다.
cd ~

# 여러 단계 폴더를 한 번에 만들며 경로 구조를 연습한다. -p 옵션은 중복 생성에도 안전하다.
mkdir -p ~/linux_lab/day02/projects/app

# 프로젝트 폴더와 데이터 폴더를 따로 만든다.
mkdir -p ~/linux_lab/day02/projects/data

# 홈 기준 절대경로 이동 예시다.
cd ~/linux_lab/day02

# 현재 위치를 눈으로 확인해 경로 감각을 만든다.
pwd

# 현재 폴더의 기본 목록을 본다.
ls

# ls -l의 -l 옵션은 long format이며 권한, 소유자, 크기, 날짜를 자세히 보여준다.
ls -l

# ls -a의 -a 옵션은 숨김 파일까지 함께 보여준다.
ls -a

# 현재 위치 기준 상대경로 이동 예시다.
cd projects

# 하위 폴더로 더 이동한다.
cd app

# 현재 위치가 ~/linux_lab/day02/projects/app 인지 확인한다.
pwd

# 상위 폴더 한 단계로 이동한다. .. 는 parent directory를 뜻한다.
cd ..

# 상위 폴더로 이동한 뒤 다른 형제 폴더로 바로 들어가는 상대경로 예시다.
cd ../data

# 절대경로로 다시 특정 위치를 지정한다.
cd ~/linux_lab/day02/projects/app

# cd - 는 직전에 있던 디렉터리로 되돌아간다. 작업 위치를 빠르게 오갈 때 유용하다.
cd -

# 현재 폴더, 상위 폴더, 홈, 루트의 차이를 한 화면에서 비교한다. -d 옵션은 폴더 자체를 보여준다.
ls -ld . .. ~ /

# 개인 실습 문제

# 문제 1. day02 폴더 아래에 notes, images, backup 세 폴더를 만들고 각각 들어가 본다.
# 문제 2. 절대경로로 app 폴더에 들어간 뒤 상대경로만 써서 data 폴더로 이동해 본다.
# 문제 3. cd -, .., ~ 를 각각 써 보며 어떤 이동이 일어나는지 설명해 보자.
# 문제 4. 현재 위치가 /home/계정명/projects/app 일 때 ../data 와 ~/linux_lab/day02/projects/data 의 차이를 말로 설명해 보자.

# 정답 예시

# 정답 1. mkdir -p ~/linux_lab/day02/notes ~/linux_lab/day02/images ~/linux_lab/day02/backup 처럼 만들 수 있다.
# 정답 2. cd ~/linux_lab/day02/projects/app 후 cd ../data 로 이동하면 된다.
# 정답 3. cd - 는 이전 폴더, cd .. 는 상위 폴더, cd ~ 는 홈 디렉터리다.
# 정답 4. ../data 는 현재 위치 기준 상대경로이고 ~/linux_lab/day02/projects/data 는 홈 기준 절대경로다.
