<div align="center">

# 압축 로그 디스크 사용량

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> tar, zip, du, df, tail을 이용해 로그와 파일 묶음을 다룬다.

> **오늘 배우는 내용**  
> 백업과 로그 관리의 핵심 명령어를 배우고 운영 습관을 만든다.

## 핵심 개념

- 배포와 운영에서는 압축과 로그 확인이 자주 등장한다.
- 디스크 사용량을 읽는 능력은 서버 관리의 기본이다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
mkdir -p ~/linux_lab/day12/project
cd ~/linux_lab/day12/project
printf 'log1\nlog2\nlog3\n' > app.log
printf 'config=true\nport=5000\n' > config.ini
cd ..
tar -cvf project.tar project
tar -tvf project.tar
mkdir -p extracted
tar -xvf project.tar -C extracted
du -sh project
df -h
tail -f project/app.log
```

## 옵션 포인트

- `tar -cvf project.tar project` : tar -cvf 는 create, verbose, file 옵션이다. 폴더를 tar 묶음으로 만든다.
- `tar -tvf project.tar` : -t 옵션은 압축 내부 목록을 본다.
- `tar -xvf project.tar -C extracted` : -x 는 extract, -C 는 특정 폴더에 푸는 옵션이다.
- `tail -f project/app.log` : -f 옵션은 파일 끝을 계속 따라가며 본다. 실시간 로그 확인용이다.

## 개인 실습 문제

1. practice 폴더를 만들고 tar로 묶었다가 다른 폴더에 풀어보자.
2. du -sh 와 df -h 의 차이를 설명해 보자.
3. tail -f 로 로그를 보는 이유를 말해 보자.

## 정답 예시

1. tar -cvf practice.tar practice 후 mkdir extracted && tar -xvf practice.tar -C extracted 로 실습할 수 있다.
2. du는 특정 폴더 사용량, df는 파일시스템 전체 용량을 본다.
3. 실시간으로 새로운 로그 줄을 확인하며 서버 상태를 보기 위해 쓴다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
