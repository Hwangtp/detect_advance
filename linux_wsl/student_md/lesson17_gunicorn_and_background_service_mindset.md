<div align="center">

# Gunicorn과 백그라운드 실행

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> 개발 서버와 운영 서버의 차이를 알고 Gunicorn으로 앱을 실행한다.

> **오늘 배우는 내용**  
> Flask 개발 서버와 Gunicorn의 차이, nohup, 백그라운드 실행, 로그 확인을 경험한다.

## 핵심 개념

- 개발 서버는 학습용, 운영 서버는 실제 서비스용에 가깝다.
- Gunicorn은 Python 웹 앱을 더 안정적으로 실행하는 WSGI 서버다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
cd ~/linux_lab/day16/flask_app
source .venv/bin/activate
pip install gunicorn
gunicorn --bind 0.0.0.0:8000 app:app
curl http://127.0.0.1:8000
nohup gunicorn --bind 0.0.0.0:8000 app:app > gunicorn.log 2>&1 &
jobs
ps -ef | grep gunicorn
tail -n 20 gunicorn.log
pkill -f gunicorn
```

## 개인 실습 문제

1. Flask 개발 서버와 Gunicorn의 차이를 말로 정리해 보자.
2. nohup으로 실행 후 로그 파일이 생기는지 확인해 보자.
3. 8000 대신 9000 포트로 Gunicorn을 띄우고 curl로 테스트해 보자.

## 정답 예시

1. Flask 개발 서버는 개발용, Gunicorn은 더 운영 환경에 가까운 WSGI 서버다.
2. nohup 명령 뒤에 > gunicorn.log 2>&1 & 를 붙이면 된다.
3. gunicorn --bind 0.0.0.0:9000 app:app 후 curl http://127.0.0.1:9000 로 확인한다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
