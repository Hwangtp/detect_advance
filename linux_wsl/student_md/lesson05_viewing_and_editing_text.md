<div align="center">

# 텍스트 읽기와 편집

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> cat, less, head, tail, nano로 텍스트 파일을 읽고 수정한다.

> **오늘 배우는 내용**  
> 긴 로그 파일과 설정 파일을 읽는 기본 패턴을 익히고 nano 편집을 처음 경험한다.

## 핵심 개념

- 서버 운영에서 텍스트 파일을 읽는 능력은 매우 중요하다.
- 설정 파일, 로그 파일, 코드 파일을 모두 텍스트로 다룬다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
mkdir -p ~/linux_lab/day05
cd ~/linux_lab/day05
printf 'line1\nline2\nline3\nline4\nline5\nline6\n' > log.txt
cat log.txt
head log.txt
head -n 3 log.txt
tail log.txt
tail -n 2 log.txt
less log.txt
nano notes.txt
cat notes.txt
nl log.txt
```

## 옵션 포인트

- `head -n 3 log.txt` : head -n 3 의 -n 옵션은 줄 수를 지정한다.

## 개인 실습 문제

1. 10줄 이상의 practice.txt 파일을 만든 뒤 head와 tail로 앞뒤를 각각 확인해 보자.
2. nano로 자기소개 파일을 만들고 두 줄 이상 입력해 보자.
3. less에서 /line4 검색을 해 보고 q로 종료해 보자.

## 정답 예시

1. printf를 활용해 여러 줄을 쉽게 만들 수 있고 head -n, tail -n 으로 앞뒤를 잘라 볼 수 있다.
2. nano intro.txt 로 열고 저장 후 cat intro.txt 로 확인하면 된다.
3. less 안에서 /line4 입력 후 Enter 로 검색하고 q 로 종료한다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
