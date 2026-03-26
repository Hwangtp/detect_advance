<div align="center">

# 도커 입문과 기본 명령어

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> Docker가 무엇인지 이해하고 이미지와 컨테이너를 직접 실행한다.

> **오늘 배우는 내용**  
> 리눅스 위에서 Docker가 어떤 역할을 하는지 배우고 hello-world와 nginx 컨테이너를 실습한다.

## 핵심 개념

- 이미지는 실행 준비가 끝난 프로그램 묶음이고 컨테이너는 실제 실행 중인 인스턴스다.
- Docker는 환경 차이를 줄여 배포를 쉽게 만드는 도구다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
docker --version
docker pull hello-world
docker images
docker run hello-world
docker pull nginx
docker run -d -p 8080:80 --name mynginx nginx
docker ps
curl http://127.0.0.1:8080
docker logs mynginx
docker stop mynginx
docker rm mynginx
```

## 개인 실습 문제

1. hello-world와 nginx 이미지의 차이를 설명해 보자.
2. 8081:80 포트 매핑으로 nginx를 다시 실행해 보자.
3. docker ps 와 docker images 의 차이를 설명해 보자.

## 정답 예시

1. hello-world는 테스트용, nginx는 실제 웹서버 예시 이미지다.
2. docker run -d -p 8081:80 --name mynginx2 nginx 로 실습할 수 있다.
3. ps는 실행 중인 컨테이너, images는 저장된 이미지 목록을 보여준다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
