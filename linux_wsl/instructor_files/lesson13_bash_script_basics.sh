#!/bin/bash
# WSL Ubuntu 기준 강사용 실습 파일
# 이 파일은 한 줄씩 직접 입력하며 설명하는 수업 노트다.
# 자동 실행용이라기보다 강사용 실습 가이드로 사용한다.
# 모든 실습은 WSL Ubuntu 터미널에서 진행하는 것을 기준으로 한다.

# 수업 제목: 배시 스크립트 기초
# 수업 목표: 셸 스크립트 구조와 변수, 입력, 조건문의 기본을 익힌다.
# 수업 개요: 처음으로 .sh 파일을 직접 만들고 실행하며 자동화 감각을 잡는다.

# 핵심 개념
# - 반복 작업을 줄이기 위해 스크립트를 만든다.
# - 스크립트는 명령어를 순서대로 묶은 자동화 문서다.

# 핵심 실습 명령어

# 스크립트 실습 폴더를 만든다.
mkdir -p ~/linux_lab/day13

# 실습 폴더로 이동한다.
cd ~/linux_lab/day13

# nano로 새 스크립트 파일을 만든다.
nano hello_script.sh

# +x 는 실행 권한을 추가한다.
chmod +x hello_script.sh

# 현재 폴더의 스크립트를 직접 실행한다.
./hello_script.sh

# 입력을 받는 스크립트도 만든다.
nano input_script.sh

# 실행 권한을 부여한다.
chmod +x input_script.sh

# 사용자 입력을 받아 결과를 출력해 본다.
./input_script.sh

# 보충 코드 예시

# 파일 예시: hello_script.sh
# #!/bin/bash
# echo "안녕하세요 리눅스 스크립트 수업입니다."
# echo "현재 사용자는 $(whoami) 입니다."
# echo "현재 위치는 $(pwd) 입니다."

# 파일 예시: input_script.sh
# #!/bin/bash
# read -p "이름을 입력하세요: " USER_NAME
# if [ -z "$USER_NAME" ]; then
#   echo "이름이 비어 있습니다."
# else
#   echo "반갑습니다, $USER_NAME 님."
# fi

# 개인 실습 문제

# 문제 1. 오늘 날짜와 사용자 이름을 출력하는 스크립트를 직접 만들어 보자.
# 문제 2. read -p 를 사용해 좋아하는 과일을 입력받고 출력해 보자.
# 문제 3. 입력이 비어 있으면 경고 문장을 출력하는 if 문을 다시 작성해 보자.

# 정답 예시

# 정답 1. date 와 whoami 명령을 echo와 함께 조합하면 된다.
# 정답 2. read -p '좋아하는 과일: ' FRUIT 후 echo "$FRUIT" 를 사용하면 된다.
# 정답 3. if [ -z "$VALUE" ]; then ... fi 형태를 그대로 응용하면 된다.
