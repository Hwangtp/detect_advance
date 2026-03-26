#!/bin/bash
# WSL Ubuntu 기준 강사용 실습 파일
# 이 파일은 한 줄씩 직접 입력하며 설명하는 수업 노트다.
# 자동 실행용이라기보다 강사용 실습 가이드로 사용한다.
# 모든 실습은 WSL Ubuntu 터미널에서 진행하는 것을 기준으로 한다.

# 수업 제목: 리다이렉션과 파이프
# 수업 목표: 출력 방향을 바꾸고 여러 명령어를 연결하는 법을 익힌다.
# 수업 개요: >, >>, | 를 중심으로 텍스트를 가공하고 결과를 파일로 저장하는 패턴을 연습한다.

# 핵심 개념
# - 리눅스의 강점은 작은 명령어를 파이프로 연결해 큰 작업을 만드는 데 있다.
# - 리다이렉션은 출력을 화면이 아니라 파일로 보내는 기술이다.

# 핵심 실습 명령어

# 실습 폴더를 만든다.
mkdir -p ~/linux_lab/day06

# 실습 위치로 이동한다.
cd ~/linux_lab/day06

# 중복 데이터가 있는 예시 파일을 만든다.
printf 'apple\nbanana\napple\norange\nbanana\nbanana\n' > fruits.txt

# 원본 데이터를 확인한다.
cat fruits.txt

# sort는 줄 단위 정렬을 한다. 기본은 오름차순이다.
sort fruits.txt

# > 로 정렬 결과를 새 파일에 저장한다.
sort fruits.txt > fruits_sorted.txt

# uniq는 연속 중복 줄을 하나로 줄인다. 보통 sort와 함께 쓴다.
sort fruits.txt | uniq

# uniq -c 의 -c 옵션은 중복 횟수를 함께 보여준다.
sort fruits.txt | uniq -c

# 파이프 결과도 파일에 저장할 수 있다.
sort fruits.txt | uniq -c > count.txt

# >> 는 append이며 기존 파일 끝에 내용을 추가한다.
echo 'grape' >> fruits.txt

# wc -l 의 -l 옵션은 줄 수를 센다.
cat fruits.txt | wc -l

# grep 결과를 바로 다음 명령어에 넘겨 특정 단어 개수를 센다.
grep 'banana' fruits.txt | wc -l

# 개인 실습 문제

# 문제 1. student 목록 파일을 만들어 정렬 후 count.txt 같은 결과 파일을 직접 만들어 보자.
# 문제 2. 중복된 과일 파일에서 가장 많이 나온 단어를 눈으로 찾아보자.
# 문제 3. 원본 파일을 덮어쓸 때와 이어 쓸 때의 차이를 > 와 >> 로 실험해 보자.

# 정답 예시

# 정답 1. sort students.txt | uniq -c > students_count.txt 패턴을 그대로 응용하면 된다.
# 정답 2. sort 후 uniq -c 결과를 보면 banana가 가장 많다는 것을 확인할 수 있다.
# 정답 3. > 는 덮어쓰기, >> 는 이어쓰기다.
