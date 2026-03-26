<div align="center">

# 리눅스와 WSL 첫걸음

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> 리눅스가 무엇인지 이해하고 WSL Ubuntu 터미널에 익숙해진다.

> **오늘 배우는 내용**  
> 리눅스의 역할, WSL Ubuntu의 의미, 터미널 프롬프트, 현재 사용자와 운영체제 정보를 읽는 실습을 진행한다.

## 핵심 개념

- 리눅스는 서버, 개발, 배포 환경에서 많이 사용하는 운영체제이다.
- WSL은 Windows 안에서 Linux 환경을 사용할 수 있게 해주는 기능이다.
- 터미널은 마우스보다 명령어로 시스템을 다루는 화면이다.
- 루트 디렉터리 / 는 리눅스 전체의 시작점이고 홈 디렉터리 ~ 는 현재 계정의 개인 작업 공간이다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
pwd
whoami
echo $USER
uname -a
cat /etc/os-release
hostname
date
ls /
ls /home
echo $HOME
echo /home/$USER
ls -ld / /home ~
cd ~
pwd
cd /
pwd
mkdir -p ~/linux_lab/day01
cd ~/linux_lab/day01
touch welcome.txt
echo 'Linux class starts here.' > welcome.txt
cat welcome.txt
```

## 옵션 포인트

- `pwd` : pwd는 print working directory의 약자이며 현재 작업 위치를 출력한다. 옵션 없이 자주 사용한다.
- `uname -a` : uname은 시스템 정보를 보여준다. -a 옵션은 커널, 아키텍처 등 가능한 많은 정보를 함께 출력한다.
- `ls -ld / /home ~` : ls -ld 의 -d 옵션은 디렉터리 자체 정보를 보여준다. 루트, home, 현재 계정 홈을 한 번에 비교한다.
- `cd ~` : cd는 디렉터리를 이동한다. ~는 홈 디렉터리를 의미한다.
- `mkdir -p ~/linux_lab/day01` : mkdir은 폴더를 만든다. -p 옵션은 중간 폴더가 없어도 한 번에 생성한다.

## 개인 실습 문제

1. 현재 사용자 이름, 운영체제 이름, 홈 디렉터리 경로를 각각 확인해 보고 세 값을 노트에 적어보자.
2. ~/linux_lab/day01 안에 intro.txt 파일을 만들고 자기소개 한 줄을 저장해 보자.
3. 루트 디렉터리와 홈 디렉터리의 차이를 직접 이동해 보며 설명해 보자.
4. /, /home, ~ 세 위치를 ls -ld 로 비교하고 어떤 곳이 개인 작업 공간인지 말해 보자.

## 정답 예시

1. whoami, cat /etc/os-release, echo $HOME 순서로 확인할 수 있다.
2. touch intro.txt 후 echo '안녕하세요 리눅스 수업을 시작합니다.' > intro.txt 를 입력하면 된다.
3. cd / 는 시스템 최상위 위치로 이동하고 cd ~ 는 현재 사용자 홈으로 이동한다.
4. ls -ld / /home ~ 를 보면 / 는 전체 시작점, /home 은 사용자 홈 모음, ~ 는 내 계정 전용 작업 공간임을 확인할 수 있다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
