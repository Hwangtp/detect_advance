#!/bin/bash
# WSL Ubuntu 기준 강사용 실습 파일
# 이 파일은 한 줄씩 직접 입력하며 설명하는 수업 노트다.
# 자동 실행용이라기보다 강사용 실습 가이드로 사용한다.
# 모든 실습은 WSL Ubuntu 터미널에서 진행하는 것을 기준으로 한다.

# 수업 제목: 네트워크 기초와 다운로드
# 수업 목표: IP, 포트, localhost를 이해하고 curl과 wget을 사용한다.
# 수업 개요: 네트워크 기초 개념을 배우고 웹 요청 및 포트 확인 명령을 실습한다.

# 핵심 개념
# - localhost는 현재 내 컴퓨터 자신을 의미한다.
# - 포트는 하나의 컴퓨터 안에서 서비스를 구분하는 번호다.

# 핵심 실습 명령어

# -I 옵션은 네트워크 인터페이스의 IP 주소를 간단히 출력한다.
hostname -I

# ping은 네트워크 연결을 확인한다. -c 4 는 4번만 보내고 종료한다.
ping -c 4 8.8.8.8

# 도메인 이름이 IP로 해석되는지 함께 확인한다.
ping -c 2 google.com

# curl은 URL에 요청을 보내고 응답을 받아온다.
curl https://example.com

# -I 옵션은 본문 없이 헤더만 가져온다.
curl -I https://example.com

# wget은 파일 다운로드에 특화돼 있다. -O 옵션은 저장 파일명을 지정한다.
wget -O sample.html https://example.com

# 다운로드한 파일 앞부분을 확인한다.
head sample.html

# ss는 소켓 상태를 본다. -t TCP, -u UDP, -l listening, -n 숫자형, -p 프로세스 정보다.
ss -tulnp | head

# 간단한 웹서버를 8000번 포트에서 실행한다. 브라우저 테스트용이다.
python3 -m http.server 8000

# 로컬 웹서버에 직접 접속해 응답을 확인한다.
curl http://localhost:8000

# 개인 실습 문제

# 문제 1. python3 -m http.server 9000 을 띄운 뒤 curl http://localhost:9000 으로 확인해 보자.
# 문제 2. curl -I 와 curl 본문의 차이를 직접 비교해 보자.
# 문제 3. ss -tulnp 결과에서 LISTEN 상태의 의미를 설명해 보자.

# 정답 예시

# 정답 1. 다른 터미널에서 서버를 띄우거나 실행 후 curl로 확인하면 된다.
# 정답 2. -I 는 헤더만, 일반 curl 은 본문까지 가져온다.
# 정답 3. LISTEN은 외부 연결을 기다리는 서버 포트 상태다.
