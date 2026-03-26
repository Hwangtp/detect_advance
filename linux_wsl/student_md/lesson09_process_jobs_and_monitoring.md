<div align="center">

# 프로세스 작업 제어 모니터링

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> 실행 중인 프로그램을 확인하고 종료하거나 백그라운드로 보낸다.

> **오늘 배우는 내용**  
> ps, top, kill, jobs를 사용해 프로세스 관리 감각을 익힌다.

## 핵심 개념

- 프로세스는 실행 중인 프로그램이다.
- 서버 운영에서는 실행 상태 확인과 종료가 매우 중요하다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
ps
ps -ef | head
top
sleep 300 &
jobs
ps -ef | grep sleep
kill %1
sleep 300 &
jobs -l
kill -9 $(jobs -p)
free -h
df -h
```

## 옵션 포인트

- `jobs -l` : jobs -l 의 -l 옵션은 PID까지 함께 보여준다.
- `free -h` : free는 메모리 사용량을 보여준다. -h 옵션은 human readable 형식이다.
- `df -h` : df는 디스크 사용량을 파일시스템별로 본다. -h 옵션은 보기 쉬운 단위다.

## 개인 실습 문제

1. sleep 120 백그라운드 작업을 2개 띄우고 jobs로 확인해 보자.
2. ps -ef | grep sleep 으로 PID를 찾은 뒤 kill로 종료해 보자.
3. top, free -h, df -h 세 명령의 역할 차이를 설명해 보자.

## 정답 예시

1. sleep 120 & 를 두 번 실행하면 된다.
2. grep으로 PID를 확인한 뒤 kill PID 형식으로 종료하면 된다.
3. top은 실시간 프로세스, free는 메모리, df는 디스크 사용량을 확인한다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
