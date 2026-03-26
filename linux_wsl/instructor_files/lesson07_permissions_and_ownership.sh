#!/bin/bash
# WSL Ubuntu 기준 강사용 실습 파일
# 이 파일은 한 줄씩 직접 입력하며 설명하는 수업 노트다.
# 자동 실행용이라기보다 강사용 실습 가이드로 사용한다.
# 모든 실습은 WSL Ubuntu 터미널에서 진행하는 것을 기준으로 한다.

# 수업 제목: 권한과 소유자
# 수업 목표: ls -l 결과를 읽고 chmod로 권한을 바꿀 수 있다.
# 수업 개요: 권한 표기, 읽기 쓰기 실행 권한, chmod 숫자 표기와 문자 표기를 함께 익힌다.

# 핵심 개념
# - 리눅스에서는 파일마다 권한과 소유자가 존재한다.
# - 권한 문제를 이해해야 서버 실행 오류를 해결할 수 있다.

# 핵심 실습 명령어

# 실습 폴더를 만든다.
mkdir -p ~/linux_lab/day07

# 실습 위치로 이동한다.
cd ~/linux_lab/day07

# 실행 스크립트 예시 파일을 만든다.
echo '#!/bin/bash
echo hello linux' > hello.sh

# ls -l 은 권한과 소유자를 자세히 보여준다.
ls -l hello.sh

# chmod는 권한을 변경한다. u+x 는 user에게 execute 권한을 추가한다.
chmod u+x hello.sh

# 변경된 권한을 다시 확인한다.
ls -l hello.sh

# ./ 는 현재 폴더를 의미한다. 실행 권한이 있는 스크립트를 직접 실행한다.
./hello.sh

# 숫자 권한 표기 예시다. 6은 rw, 4는 r, 4는 r 을 의미한다.
chmod 644 hello.sh

# 숫자 권한 변경 결과를 확인한다.
ls -l hello.sh

# 755는 소유자 rwx, 그룹 r-x, 기타 r-x 를 의미한다.
chmod 755 hello.sh

# 실행 가능한 일반 스크립트 권한 형태를 확인한다.
ls -l hello.sh

# id는 현재 사용자의 uid, gid, 그룹 정보를 보여준다.
id

# 개인 실습 문제

# 문제 1. readme.txt 파일을 만들고 600, 644, 666 권한으로 각각 바꿔보자.
# 문제 2. hello.sh의 실행 권한을 뺀 뒤 다시 주는 과정을 반복해 보자.
# 문제 3. 숫자 권한 700, 744, 755의 차이를 말로 설명해 보자.

# 정답 예시

# 정답 1. chmod 600 readme.txt, chmod 644 readme.txt, chmod 666 readme.txt 순으로 실습할 수 있다.
# 정답 2. chmod u-x hello.sh 로 제거하고 chmod u+x hello.sh 로 다시 추가할 수 있다.
# 정답 3. 700은 소유자만 모두 가능, 744는 소유자만 쓰기 가능, 755는 소유자 전체와 타인 읽기 실행 가능이다.
