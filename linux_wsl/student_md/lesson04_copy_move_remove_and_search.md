<div align="center">

# 복사 이동 삭제와 파일 찾기

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> cp, mv, rm, find를 이해하고 안전하게 파일을 관리한다.

> **오늘 배우는 내용**  
> 복사와 이동, 이름 변경, 삭제, 검색 작업을 실습 폴더 안에서 반복적으로 수행한다.

## 핵심 개념

- cp는 복사, mv는 이동 또는 이름 변경, rm은 삭제다.
- 삭제는 되돌리기 어렵기 때문에 항상 대상 경로를 먼저 확인해야 한다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
mkdir -p ~/linux_lab/day04/source ~/linux_lab/day04/target
cd ~/linux_lab/day04
echo 'report v1' > source/report.txt
cp source/report.txt target/report_copy.txt
cp -r source target/source_backup
mv target/report_copy.txt target/report_final.txt
mv source/report.txt source/report_old.txt
find . -name '*.txt'
find . -type d
rm target/report_final.txt
rm -r target/source_backup
ls -R
```

## 옵션 포인트

- `cp -r source target/source_backup` : cp -r 의 -r 옵션은 디렉터리를 재귀적으로 복사한다.
- `find . -name '*.txt'` : -name 옵션은 파일 이름 패턴으로 검색한다. 작은따옴표로 패턴을 감싼다.
- `rm -r target/source_backup` : rm -r 의 -r 옵션은 디렉터리와 그 안 내용을 재귀적으로 삭제한다.

## 개인 실습 문제

1. source 안에 notes.txt와 todo.txt를 만들고 target으로 각각 다른 이름으로 복사해 보자.
2. find 명령으로 report가 포함된 파일만 찾아보자.
3. 삭제 전에 ls와 pwd를 먼저 실행하는 습관을 직접 실습해 보자.

## 정답 예시

1. cp source/notes.txt target/notes_copy.txt 와 cp source/todo.txt target/todo_copy.txt 를 사용할 수 있다.
2. find . -name '*report*' 로 찾을 수 있다.
3. pwd 로 현재 위치를 확인하고 ls 로 대상을 다시 본 뒤 rm 을 실행하는 흐름이 안전하다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
