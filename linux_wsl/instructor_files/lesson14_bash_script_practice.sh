#!/bin/bash
# WSL Ubuntu 기준 강사용 실습 파일
# 이 파일은 한 줄씩 직접 입력하며 설명하는 수업 노트다.
# 자동 실행용이라기보다 강사용 실습 가이드로 사용한다.
# 모든 실습은 WSL Ubuntu 터미널에서 진행하는 것을 기준으로 한다.

# 수업 제목: 배시 스크립트 실전 자동화
# 수업 목표: 반복문과 파일 작업을 활용해 작은 자동화 도구를 만든다.
# 수업 개요: 백업 스크립트, 반복 출력, 조건 검사, 로그 남기기 예제를 통해 실전 감각을 익힌다.

# 핵심 개념
# - 스크립트는 여러 리눅스 명령어를 묶어 자동화하는 도구다.
# - 운영자는 반복적인 작업을 스크립트로 줄여 시간을 절약한다.

# 핵심 실습 명령어

# 백업 대상 폴더를 만든다.
mkdir -p ~/linux_lab/day14/source

# 실습 위치로 이동한다.
cd ~/linux_lab/day14

# 백업 대상 파일을 만든다.
printf 'alpha\nbeta\n' > source/list.txt

# 백업 스크립트를 만든다.
nano backup_script.sh

# 실행 권한을 부여한다.
chmod +x backup_script.sh

# 백업 스크립트를 실행한다.
./backup_script.sh

# 생성된 backup 폴더를 확인한다.
ls -R

# 실행 기록 파일을 읽는다.
cat backup.log

# 보충 코드 예시

# 파일 예시: backup_script.sh
# #!/bin/bash
# DATE=$(date +%Y%m%d_%H%M%S)
# BACKUP_DIR="backup_$DATE"
# mkdir -p "$BACKUP_DIR"
# cp -r source "$BACKUP_DIR"
# echo "[$DATE] backup completed" >> backup.log
# echo "백업이 완료되었습니다: $BACKUP_DIR"

# 개인 실습 문제

# 문제 1. for 문을 사용해 student1, student2, student3 폴더를 자동 생성해 보자.
# 문제 2. 백업 스크립트에 백업 후 tree 출력 줄을 추가해 보자.
# 문제 3. if 문을 사용해 source 폴더가 없으면 경고 후 종료하는 기능을 넣어 보자.

# 정답 예시

# 정답 1. for i in 1 2 3; do mkdir -p student$i; done 형태를 사용할 수 있다.
# 정답 2. tree "$BACKUP_DIR" 또는 find "$BACKUP_DIR" 를 추가하면 된다.
# 정답 3. if [ ! -d source ]; then echo 'source 폴더 없음'; exit 1; fi 를 넣으면 된다.
