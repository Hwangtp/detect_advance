<div align="center">

# 사용자 그룹 sudo 이해

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> 사용자와 그룹, sudo의 의미를 이해하고 안전하게 시스템 명령을 실행한다.

> **오늘 배우는 내용**  
> whoami, id, groups, sudo를 중심으로 시스템 권한 구조를 이해한다.

## 핵심 개념

- 사용자와 그룹은 권한 관리의 기본 단위다.
- sudo는 관리자 권한이 필요한 명령을 일시적으로 실행하게 해준다.
- WSL Ubuntu에서도 계정 구조와 시스템 계정 파일은 일반 리눅스와 거의 같은 방식으로 보인다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
whoami
id
groups
echo $HOME
grep "^$USER:" /etc/passwd
grep '^sudo' /etc/group
sudo -l
sudo apt update
sudo apt install -y tree
tree ~/linux_lab
sudo adduser linuxstudent
sudo usermod -aG sudo linuxstudent
grep '^linuxstudent:' /etc/passwd
sudo deluser linuxstudent
```

## 옵션 포인트

- `sudo apt install -y tree` : apt install 은 패키지를 설치한다. -y 옵션은 yes를 자동 승인한다.

## 개인 실습 문제

1. 현재 사용자가 어떤 그룹에 속해 있는지 확인하고 그 의미를 설명해 보자.
2. tree가 없다면 sudo apt install로 설치한 뒤 다시 실행해 보자.
3. sudo가 왜 필요한지 apt update 예시를 기준으로 설명해 보자.
4. /etc/passwd 에서 현재 계정 줄을 찾아 홈 디렉터리와 기본 셸이 어디인지 읽어 보자.

## 정답 예시

1. groups 또는 id로 확인할 수 있으며 그룹은 권한 묶음 단위다.
2. sudo apt install -y tree 후 tree ~/linux_lab 를 실행하면 된다.
3. 시스템 전역 패키지 정보와 설정은 일반 사용자 권한으로 바꾸기 어려워서 sudo가 필요하다.
4. grep "^$USER:" /etc/passwd 결과에서 보통 /home/계정명 과 /bin/bash 또는 /bin/sh 같은 셸 정보를 볼 수 있다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
