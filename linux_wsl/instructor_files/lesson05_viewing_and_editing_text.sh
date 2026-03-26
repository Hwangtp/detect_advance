#!/bin/bash
# WSL Ubuntu 기준 강사용 실습 파일
# 이 파일은 한 줄씩 직접 입력하며 설명하는 수업 노트다.
# 자동 실행용이라기보다 강사용 실습 가이드로 사용한다.
# 모든 실습은 WSL Ubuntu 터미널에서 진행하는 것을 기준으로 한다.

# 수업 제목: 텍스트 읽기와 편집
# 수업 목표: cat, less, head, tail, nano로 텍스트 파일을 읽고 수정한다.
# 수업 개요: 긴 로그 파일과 설정 파일을 읽는 기본 패턴을 익히고 nano 편집을 처음 경험한다.

# 핵심 개념
# - 서버 운영에서 텍스트 파일을 읽는 능력은 매우 중요하다.
# - 설정 파일, 로그 파일, 코드 파일을 모두 텍스트로 다룬다.

# 핵심 실습 명령어

# day05 실습 폴더를 만든다.
mkdir -p ~/linux_lab/day05

# 실습 폴더로 이동한다.
cd ~/linux_lab/day05

# printf는 줄바꿈이 포함된 여러 줄 문자열을 만들기 좋다.
printf 'line1\nline2\nline3\nline4\nline5\nline6\n' > log.txt

# cat은 짧은 파일을 한 번에 볼 때 좋다.
cat log.txt

# head는 기본적으로 앞 10줄을 보여준다. 짧은 파일에서도 확인용으로 쓴다.
head log.txt

# head -n 3 의 -n 옵션은 줄 수를 지정한다.
head -n 3 log.txt

# tail은 뒤 10줄을 보여준다.
tail log.txt

# tail -n 2 는 마지막 두 줄만 확인한다.
tail -n 2 log.txt

# less는 긴 파일을 페이지 단위로 읽는다. q 키로 종료한다.
less log.txt

# nano는 초보자가 쓰기 쉬운 텍스트 편집기다. 수정 후 Ctrl+O 저장, Ctrl+X 종료를 사용한다.
nano notes.txt

# 편집 내용을 다시 확인한다.
cat notes.txt

# nl은 line number를 붙여 출력한다. 줄 번호로 설명할 때 유용하다.
nl log.txt

# 개인 실습 문제

# 문제 1. 10줄 이상의 practice.txt 파일을 만든 뒤 head와 tail로 앞뒤를 각각 확인해 보자.
# 문제 2. nano로 자기소개 파일을 만들고 두 줄 이상 입력해 보자.
# 문제 3. less에서 /line4 검색을 해 보고 q로 종료해 보자.

# 정답 예시

# 정답 1. printf를 활용해 여러 줄을 쉽게 만들 수 있고 head -n, tail -n 으로 앞뒤를 잘라 볼 수 있다.
# 정답 2. nano intro.txt 로 열고 저장 후 cat intro.txt 로 확인하면 된다.
# 정답 3. less 안에서 /line4 입력 후 Enter 로 검색하고 q 로 종료한다.
