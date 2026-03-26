<div align="center">

# 파일과 디렉터리 기본 조작

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> 파일 생성, 폴더 생성, 복사 전 준비 작업을 익힌다.

> **오늘 배우는 내용**  
> touch, mkdir, echo, tree 대체 명령을 활용해 폴더 구조를 직접 설계해 본다.

## 핵심 개념

- 리눅스에서는 파일과 폴더를 명령어 한 줄로 빠르게 만들 수 있다.
- 실습 폴더 구조를 잘 만드는 습관이 나중에 배포에도 큰 도움이 된다.
- 경로를 이해하지 못하면 파일이 어디에 생성됐는지 잃어버리기 쉽다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
pwd
cd ~
mkdir -p ~/linux_lab/day03/classroom/students
mkdir -p ~/linux_lab/day03/classroom/teachers
cd ~/linux_lab/day03/classroom
pwd
touch plan.txt
touch students/student01.txt students/student02.txt
echo 'Linux practice list' > plan.txt
echo 'student01' > students/student01.txt
echo 'student02' > students/student02.txt
ls -R
find . -maxdepth 2
find . -maxdepth 2 -type d
find . -maxdepth 2 -type f
mkdir -p backup/2026/03
touch backup/2026/03/readme.txt
realpath backup/2026/03/readme.txt
```

## 옵션 포인트

- `ls -R` : ls -R의 -R 옵션은 recursive이며 하위 폴더까지 재귀적으로 목록을 보여준다.
- `find . -maxdepth 2 -type d` : -type d 옵션은 디렉터리만 찾는다. 폴더 구조만 따로 읽고 싶을 때 쓴다.
- `find . -maxdepth 2 -type f` : -type f 옵션은 파일만 찾는다. 파일과 폴더를 구분해 이해하게 도와준다.

## 개인 실습 문제

1. 강의실 폴더, 과제 폴더, 제출 폴더를 직접 원하는 구조로 만들어 보자.
2. find 명령으로 현재 폴더 아래 파일만 찾고 폴더도 함께 찾는 결과를 비교해 보자.
3. 한 줄 명령으로 3명의 학생 파일을 만들어 내용을 각각 다르게 저장해 보자.
4. realpath 로 students/student01.txt 의 절대경로를 확인하고 왜 이 위치에 생겼는지 설명해 보자.

## 정답 예시

1. mkdir -p classroom homework submit 처럼 기본 폴더를 만든 뒤 필요시 하위 폴더를 추가하면 된다.
2. find . -maxdepth 2 와 find . -type f 의 결과 차이를 보면 파일만 찾는 옵션을 이해할 수 있다.
3. touch students/student03.txt 후 echo 명령으로 내용을 넣거나 한 줄로 세 파일을 만들 수 있다.
4. 현재 위치가 ~/linux_lab/day03/classroom 이기 때문에 상대경로 students/student01.txt 는 그 하위 위치에 생성된다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
