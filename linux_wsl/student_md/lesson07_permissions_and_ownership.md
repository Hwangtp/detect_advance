<div align="center">

# 권한과 소유자

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> ls -l 결과를 읽고 chmod로 권한을 바꿀 수 있다.

> **오늘 배우는 내용**  
> 권한 표기, 읽기 쓰기 실행 권한, chmod 숫자 표기와 문자 표기를 함께 익힌다.

## 핵심 개념

- 리눅스에서는 파일마다 권한과 소유자가 존재한다.
- 권한 문제를 이해해야 서버 실행 오류를 해결할 수 있다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
mkdir -p ~/linux_lab/day07
cd ~/linux_lab/day07
echo '#!/bin/bash
echo hello linux' > hello.sh
ls -l hello.sh
chmod u+x hello.sh
ls -l hello.sh
./hello.sh
chmod 644 hello.sh
ls -l hello.sh
chmod 755 hello.sh
ls -l hello.sh
id
```

## 옵션 포인트

- `./hello.sh` : ./ 는 현재 폴더를 의미한다. 실행 권한이 있는 스크립트를 직접 실행한다.
- `chmod 644 hello.sh` : 숫자 권한 표기 예시다. 6은 rw, 4는 r, 4는 r 을 의미한다.
- `chmod 755 hello.sh` : 755는 소유자 rwx, 그룹 r-x, 기타 r-x 를 의미한다.

## 개인 실습 문제

1. readme.txt 파일을 만들고 600, 644, 666 권한으로 각각 바꿔보자.
2. hello.sh의 실행 권한을 뺀 뒤 다시 주는 과정을 반복해 보자.
3. 숫자 권한 700, 744, 755의 차이를 말로 설명해 보자.

## 정답 예시

1. chmod 600 readme.txt, chmod 644 readme.txt, chmod 666 readme.txt 순으로 실습할 수 있다.
2. chmod u-x hello.sh 로 제거하고 chmod u+x hello.sh 로 다시 추가할 수 있다.
3. 700은 소유자만 모두 가능, 744는 소유자만 쓰기 가능, 755는 소유자 전체와 타인 읽기 실행 가능이다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
