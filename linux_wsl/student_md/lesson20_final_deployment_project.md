<div align="center">

# 최종 배포 프로젝트

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> WSL Ubuntu에서 Flask 앱을 Docker Compose로 실행하고 배포 흐름을 정리한다.

> **오늘 배우는 내용**  
> 리눅스 명령어, 네트워크, Python, Flask, Docker를 하나로 묶어 실제 배포형 예제를 완성한다.

## 핵심 개념

- 배포는 앱을 다른 사람도 접속 가능한 상태로 만드는 과정이다.
- 개발과 운영 사이의 핵심 차이는 실행 방식, 로그, 포트, 재현 가능성이다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
mkdir -p ~/linux_lab/day20/final_project
cd ~/linux_lab/day20/final_project
cp -r ~/linux_lab/day19/flask_docker/* .
nano docker-compose.yml
docker compose up -d
docker compose ps
curl http://127.0.0.1:5050
docker compose logs
docker compose down
```

### 실습 파일 예시: `docker-compose.yml`

```bash
services:
  web:
    build: .
    container_name: linux_final_web
    ports:
      - "5050:5000"
```

## 개인 실습 문제

1. 서비스 이름을 webapp으로 바꾸고 compose up이 어떻게 반영되는지 확인해 보자.
2. docker compose logs 로 앱 로그를 읽고 어떤 서버가 실행 중인지 말해 보자.
3. 최종적으로 리눅스와 Docker가 왜 배포에 연결되는지 설명해 보자.

## 정답 예시

1. docker-compose.yml 의 service 키 이름을 webapp으로 바꾸고 다시 up 하면 된다.
2. Gunicorn 또는 Flask 앱 로그가 보이며 포트 바인딩 정보도 확인할 수 있다.
3. 리눅스는 실행 환경, Docker는 동일한 환경을 재현해 배포를 쉽게 만드는 도구이기 때문이다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
