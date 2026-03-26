<div align="center">

# 터미널 이동과 경로 이해

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> 절대경로와 상대경로를 구분하고 원하는 폴더로 정확히 이동한다.

> **오늘 배우는 내용**  
> pwd, ls, cd를 반복해 쓰며 경로 감각을 익히고 탭 자동완성도 함께 연습한다.

## 핵심 개념

- 절대경로는 /로 시작하는 전체 주소다.
- 상대경로는 현재 위치를 기준으로 계산하는 주소다.
- .. 는 상위 폴더, . 는 현재 폴더를 의미한다.
- WSL Ubuntu에서는 보통 /home/계정명 아래에서 개인 작업을 진행한다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
pwd
realpath .
echo $HOME
cd /home
ls -l /home
cd ~
mkdir -p ~/linux_lab/day02/projects/app
mkdir -p ~/linux_lab/day02/projects/data
cd ~/linux_lab/day02
pwd
ls
ls -l
ls -a
cd projects
cd app
pwd
cd ..
cd ../data
cd ~/linux_lab/day02/projects/app
cd -
ls -ld . .. ~ /
```

## 옵션 포인트

- `realpath .` : realpath 는 현재 위치의 실제 절대경로를 보여준다. . 은 현재 폴더를 의미한다.
- `ls -l /home` : ls -l 로 /home 아래 계정 폴더 구조를 본다. -l 옵션은 상세 목록이다.
- `mkdir -p ~/linux_lab/day02/projects/app` : 여러 단계 폴더를 한 번에 만들며 경로 구조를 연습한다. -p 옵션은 중복 생성에도 안전하다.
- `ls -l` : ls -l의 -l 옵션은 long format이며 권한, 소유자, 크기, 날짜를 자세히 보여준다.
- `ls -a` : ls -a의 -a 옵션은 숨김 파일까지 함께 보여준다.
- `ls -ld . .. ~ /` : 현재 폴더, 상위 폴더, 홈, 루트의 차이를 한 화면에서 비교한다. -d 옵션은 폴더 자체를 보여준다.

## 개인 실습 문제

1. day02 폴더 아래에 notes, images, backup 세 폴더를 만들고 각각 들어가 본다.
2. 절대경로로 app 폴더에 들어간 뒤 상대경로만 써서 data 폴더로 이동해 본다.
3. cd -, .., ~ 를 각각 써 보며 어떤 이동이 일어나는지 설명해 보자.
4. 현재 위치가 /home/계정명/projects/app 일 때 ../data 와 ~/linux_lab/day02/projects/data 의 차이를 말로 설명해 보자.

## 정답 예시

1. mkdir -p ~/linux_lab/day02/notes ~/linux_lab/day02/images ~/linux_lab/day02/backup 처럼 만들 수 있다.
2. cd ~/linux_lab/day02/projects/app 후 cd ../data 로 이동하면 된다.
3. cd - 는 이전 폴더, cd .. 는 상위 폴더, cd ~ 는 홈 디렉터리다.
4. ../data 는 현재 위치 기준 상대경로이고 ~/linux_lab/day02/projects/data 는 홈 기준 절대경로다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
