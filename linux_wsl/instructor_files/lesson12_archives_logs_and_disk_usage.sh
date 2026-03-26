#!/bin/bash
# WSL Ubuntu 기준 강사용 실습 파일
# 이 파일은 한 줄씩 직접 입력하며 설명하는 수업 노트다.
# 자동 실행용이라기보다 강사용 실습 가이드로 사용한다.
# 모든 실습은 WSL Ubuntu 터미널에서 진행하는 것을 기준으로 한다.

# 수업 제목: 압축 로그 디스크 사용량
# 수업 목표: tar, zip, du, df, tail을 이용해 로그와 파일 묶음을 다룬다.
# 수업 개요: 백업과 로그 관리의 핵심 명령어를 배우고 운영 습관을 만든다.

# 핵심 개념
# - 배포와 운영에서는 압축과 로그 확인이 자주 등장한다.
# - 디스크 사용량을 읽는 능력은 서버 관리의 기본이다.

# 핵심 실습 명령어

# 압축 대상 폴더를 만든다.
mkdir -p ~/linux_lab/day12/project

# 프로젝트 폴더로 이동한다.
cd ~/linux_lab/day12/project

# 로그 파일 예시를 만든다.
printf 'log1\nlog2\nlog3\n' > app.log

# 설정 파일 예시를 만든다.
printf 'config=true\nport=5000\n' > config.ini

# 상위 폴더에서 압축 실습을 진행한다.
cd ..

# tar -cvf 는 create, verbose, file 옵션이다. 폴더를 tar 묶음으로 만든다.
tar -cvf project.tar project

# -t 옵션은 압축 내부 목록을 본다.
tar -tvf project.tar

# 압축 해제 대상 폴더를 미리 만든다.
mkdir -p extracted

# -x 는 extract, -C 는 특정 폴더에 푸는 옵션이다.
tar -xvf project.tar -C extracted

# du는 디스크 사용량을 본다. -s 요약, -h 보기 쉬운 단위다.
du -sh project

# df는 파일시스템 전체 용량과 사용량을 본다.
df -h

# -f 옵션은 파일 끝을 계속 따라가며 본다. 실시간 로그 확인용이다.
tail -f project/app.log

# 개인 실습 문제

# 문제 1. practice 폴더를 만들고 tar로 묶었다가 다른 폴더에 풀어보자.
# 문제 2. du -sh 와 df -h 의 차이를 설명해 보자.
# 문제 3. tail -f 로 로그를 보는 이유를 말해 보자.

# 정답 예시

# 정답 1. tar -cvf practice.tar practice 후 mkdir extracted && tar -xvf practice.tar -C extracted 로 실습할 수 있다.
# 정답 2. du는 특정 폴더 사용량, df는 파일시스템 전체 용량을 본다.
# 정답 3. 실시간으로 새로운 로그 줄을 확인하며 서버 상태를 보기 위해 쓴다.
