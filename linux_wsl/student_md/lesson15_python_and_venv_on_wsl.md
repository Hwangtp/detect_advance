<div align="center">

# WSL에서 파이썬과 가상환경

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> python3, pip, venv를 이용해 개발 환경을 분리한다.

> **오늘 배우는 내용**  
> WSL Ubuntu에서 파이썬 개발 준비를 하고 가상환경을 사용해 본다.

## 핵심 개념

- 가상환경은 프로젝트별 패키지 충돌을 막아 준다.
- 배포 전 개발 환경을 분리하는 습관이 중요하다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
python3 --version
pip3 --version
mkdir -p ~/linux_lab/day15/flask_project
cd ~/linux_lab/day15/flask_project
python3 -m venv .venv
source .venv/bin/activate
which python
python --version
pip install flask
pip freeze
pip freeze > requirements.txt
deactivate
```

## 개인 실습 문제

1. 새 가상환경을 만들고 requests 패키지를 설치한 뒤 pip freeze 결과를 확인해 보자.
2. 가상환경 활성화 전후 which python 결과가 왜 다른지 설명해 보자.
3. requirements.txt를 만드는 이유를 말해 보자.

## 정답 예시

1. python3 -m venv .venv 후 source .venv/bin/activate, pip install requests 순서로 진행하면 된다.
2. 활성화 후에는 셸이 .venv/bin/python 을 우선 사용하기 때문이다.
3. 다른 환경에서도 동일한 패키지 버전을 다시 설치하기 위해서다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
