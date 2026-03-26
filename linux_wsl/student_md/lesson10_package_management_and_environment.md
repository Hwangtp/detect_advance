<div align="center">

# 패키지 관리와 환경 정보

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> apt로 프로그램을 설치하고 환경 관련 명령을 이해한다.

> **오늘 배우는 내용**  
> 업데이트, 설치, 제거, 환경변수, which, whereis를 통해 개발 환경을 준비한다.

## 핵심 개념

- 패키지 관리자는 리눅스에서 프로그램을 설치하는 표준 방법이다.
- 어떤 명령이 어디에 설치됐는지 아는 습관이 중요하다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
sudo apt update
sudo apt upgrade -y
which python3
whereis python3
python3 --version
echo $PATH
sudo apt install -y curl
curl --version
sudo apt remove -y tree
sudo apt install -y tree
tree -L 2 ~/linux_lab
```

## 옵션 포인트

- `python3 --version` : --version 옵션은 설치된 버전을 확인할 때 자주 사용한다.

## 개인 실습 문제

1. which, whereis, --version 세 가지로 python3 정보를 각각 확인해 보자.
2. curl과 tree를 설치하거나 재설치해 보고 버전을 확인해 보자.
3. $PATH를 보고 왜 명령어를 폴더명 없이 실행할 수 있는지 설명해 보자.

## 정답 예시

1. which python3, whereis python3, python3 --version 을 순서대로 실행하면 된다.
2. sudo apt install -y curl tree 후 curl --version, tree --version 또는 tree 실행으로 확인한다.
3. PATH에 등록된 폴더를 셸이 탐색해 실행 파일을 찾기 때문이다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
