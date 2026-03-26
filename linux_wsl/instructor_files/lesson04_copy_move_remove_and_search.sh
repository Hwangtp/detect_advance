#!/bin/bash
# WSL Ubuntu 기준 강사용 실습 파일
# 이 파일은 한 줄씩 직접 입력하며 설명하는 수업 노트다.
# 자동 실행용이라기보다 강사용 실습 가이드로 사용한다.
# 모든 실습은 WSL Ubuntu 터미널에서 진행하는 것을 기준으로 한다.

# 수업 제목: 복사 이동 삭제와 파일 찾기
# 수업 목표: cp, mv, rm, find를 이해하고 안전하게 파일을 관리한다.
# 수업 개요: 복사와 이동, 이름 변경, 삭제, 검색 작업을 실습 폴더 안에서 반복적으로 수행한다.

# 핵심 개념
# - cp는 복사, mv는 이동 또는 이름 변경, rm은 삭제다.
# - 삭제는 되돌리기 어렵기 때문에 항상 대상 경로를 먼저 확인해야 한다.

# 핵심 실습 명령어

# 원본과 결과 폴더를 분리해 안전하게 실습한다.
mkdir -p ~/linux_lab/day04/source ~/linux_lab/day04/target

# 실습 위치로 이동한다.
cd ~/linux_lab/day04

# 원본 파일을 만든다.
echo 'report v1' > source/report.txt

# cp는 파일을 복사한다. 대상 이름을 바꿔 저장할 수도 있다.
cp source/report.txt target/report_copy.txt

# cp -r 의 -r 옵션은 디렉터리를 재귀적으로 복사한다.
cp -r source target/source_backup

# mv는 파일 위치를 바꾸거나 이름을 바꿀 수 있다.
mv target/report_copy.txt target/report_final.txt

# 같은 폴더 안에서 이름 변경 예시다.
mv source/report.txt source/report_old.txt

# -name 옵션은 파일 이름 패턴으로 검색한다. 작은따옴표로 패턴을 감싼다.
find . -name '*.txt'

# -type d 는 디렉터리만 찾는다. -type f 는 파일만 찾는다.
find . -type d

# rm은 파일을 삭제한다. 경로를 반드시 확인한 뒤 사용한다.
rm target/report_final.txt

# rm -r 의 -r 옵션은 디렉터리와 그 안 내용을 재귀적으로 삭제한다.
rm -r target/source_backup

# 실습 후 남아 있는 파일 구조를 확인한다.
ls -R

# 개인 실습 문제

# 문제 1. source 안에 notes.txt와 todo.txt를 만들고 target으로 각각 다른 이름으로 복사해 보자.
# 문제 2. find 명령으로 report가 포함된 파일만 찾아보자.
# 문제 3. 삭제 전에 ls와 pwd를 먼저 실행하는 습관을 직접 실습해 보자.

# 정답 예시

# 정답 1. cp source/notes.txt target/notes_copy.txt 와 cp source/todo.txt target/todo_copy.txt 를 사용할 수 있다.
# 정답 2. find . -name '*report*' 로 찾을 수 있다.
# 정답 3. pwd 로 현재 위치를 확인하고 ls 로 대상을 다시 본 뒤 rm 을 실행하는 흐름이 안전하다.
