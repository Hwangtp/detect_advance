<div align="center">

# 네트워크 기초와 다운로드

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> IP, 포트, localhost를 이해하고 curl과 wget을 사용한다.

> **오늘 배우는 내용**  
> 네트워크 기초 개념을 배우고 웹 요청 및 포트 확인 명령을 실습한다.

## 핵심 개념

- localhost는 현재 내 컴퓨터 자신을 의미한다.
- 포트는 하나의 컴퓨터 안에서 서비스를 구분하는 번호다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
hostname -I
ping -c 4 8.8.8.8
ping -c 2 google.com
curl https://example.com
curl -I https://example.com
wget -O sample.html https://example.com
head sample.html
ss -tulnp | head
python3 -m http.server 8000
curl http://localhost:8000
```

## 옵션 포인트

- `hostname -I` : -I 옵션은 네트워크 인터페이스의 IP 주소를 간단히 출력한다.
- `curl -I https://example.com` : -I 옵션은 본문 없이 헤더만 가져온다.
- `wget -O sample.html https://example.com` : wget은 파일 다운로드에 특화돼 있다. -O 옵션은 저장 파일명을 지정한다.

## 개인 실습 문제

1. python3 -m http.server 9000 을 띄운 뒤 curl http://localhost:9000 으로 확인해 보자.
2. curl -I 와 curl 본문의 차이를 직접 비교해 보자.
3. ss -tulnp 결과에서 LISTEN 상태의 의미를 설명해 보자.

## 정답 예시

1. 다른 터미널에서 서버를 띄우거나 실행 후 curl로 확인하면 된다.
2. -I 는 헤더만, 일반 curl 은 본문까지 가져온다.
3. LISTEN은 외부 연결을 기다리는 서버 포트 상태다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
