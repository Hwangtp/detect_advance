#!/bin/bash
# WSL Ubuntu 기준 강사용 실습 파일
# 이 파일은 한 줄씩 직접 입력하며 설명하는 수업 노트다.
# 자동 실행용이라기보다 강사용 실습 가이드로 사용한다.
# 모든 실습은 WSL Ubuntu 터미널에서 진행하는 것을 기준으로 한다.

# 수업 제목: 파일과 디렉터리 기본 조작
# 수업 목표: 파일 생성, 폴더 생성, 복사 전 준비 작업을 익힌다.
# 수업 개요: touch, mkdir, echo, tree 대체 명령을 활용해 폴더 구조를 직접 설계해 본다.

# 핵심 개념
# - 리눅스에서는 파일과 폴더를 명령어 한 줄로 빠르게 만들 수 있다.
# - 실습 폴더 구조를 잘 만드는 습관이 나중에 배포에도 큰 도움이 된다.
# - 경로를 이해하지 못하면 파일이 어디에 생성됐는지 잃어버리기 쉽다.

# 핵심 실습 명령어

# 실습 시작 위치를 먼저 확인한다. 어느 위치에서 만들었는지가 매우 중요하다.
pwd

# 현재 계정 홈으로 이동해 개인 작업 공간을 기준점으로 삼는다.
cd ~

# 수업용 디렉터리 구조를 만든다.
mkdir -p ~/linux_lab/day03/classroom/students

# 교사용 폴더도 함께 만든다.
mkdir -p ~/linux_lab/day03/classroom/teachers

# 실습 위치로 들어간다.
cd ~/linux_lab/day03/classroom

# 현재 위치가 classroom 인지 다시 확인한다.
pwd

# 수업 계획을 적을 빈 파일을 만든다.
touch plan.txt

# 한 번에 여러 파일을 만들 수 있다.
touch students/student01.txt students/student02.txt

# > 는 파일 내용을 새로 쓴다.
echo 'Linux practice list' > plan.txt

# 학생 정보 파일 예시를 만든다.
echo 'student01' > students/student01.txt

# 두 번째 학생 파일 예시다.
echo 'student02' > students/student02.txt

# ls -R의 -R 옵션은 recursive이며 하위 폴더까지 재귀적으로 목록을 보여준다.
ls -R

# find는 파일을 찾는다. -maxdepth 2는 두 단계까지만 내려가게 제한한다.
find . -maxdepth 2

# -type d 옵션은 디렉터리만 찾는다. 폴더 구조만 따로 읽고 싶을 때 쓴다.
find . -maxdepth 2 -type d

# -type f 옵션은 파일만 찾는다. 파일과 폴더를 구분해 이해하게 도와준다.
find . -maxdepth 2 -type f

# 연월 구조 폴더를 한 번에 만드는 예시다.
mkdir -p backup/2026/03

# 깊은 경로에 파일을 생성한다.
touch backup/2026/03/readme.txt

# 상대경로로 만든 파일이 실제 어디에 있는지 절대경로로 확인한다.
realpath backup/2026/03/readme.txt

# 개인 실습 문제

# 문제 1. 강의실 폴더, 과제 폴더, 제출 폴더를 직접 원하는 구조로 만들어 보자.
# 문제 2. find 명령으로 현재 폴더 아래 파일만 찾고 폴더도 함께 찾는 결과를 비교해 보자.
# 문제 3. 한 줄 명령으로 3명의 학생 파일을 만들어 내용을 각각 다르게 저장해 보자.
# 문제 4. realpath 로 students/student01.txt 의 절대경로를 확인하고 왜 이 위치에 생겼는지 설명해 보자.

# 정답 예시

# 정답 1. mkdir -p classroom homework submit 처럼 기본 폴더를 만든 뒤 필요시 하위 폴더를 추가하면 된다.
# 정답 2. find . -maxdepth 2 와 find . -type f 의 결과 차이를 보면 파일만 찾는 옵션을 이해할 수 있다.
# 정답 3. touch students/student03.txt 후 echo 명령으로 내용을 넣거나 한 줄로 세 파일을 만들 수 있다.
# 정답 4. 현재 위치가 ~/linux_lab/day03/classroom 이기 때문에 상대경로 students/student01.txt 는 그 하위 위치에 생성된다.
