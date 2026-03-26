<div align="center">

# 배시 스크립트 실전 자동화

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> 반복문과 파일 작업을 활용해 작은 자동화 도구를 만든다.

> **오늘 배우는 내용**  
> 백업 스크립트, 반복 출력, 조건 검사, 로그 남기기 예제를 통해 실전 감각을 익힌다.

## 핵심 개념

- 스크립트는 여러 리눅스 명령어를 묶어 자동화하는 도구다.
- 운영자는 반복적인 작업을 스크립트로 줄여 시간을 절약한다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
mkdir -p ~/linux_lab/day14/source
cd ~/linux_lab/day14
printf 'alpha\nbeta\n' > source/list.txt
nano backup_script.sh
chmod +x backup_script.sh
./backup_script.sh
ls -R
cat backup.log
```

### 실습 파일 예시: `backup_script.sh`

```bash
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="backup_$DATE"
mkdir -p "$BACKUP_DIR"
cp -r source "$BACKUP_DIR"
echo "[$DATE] backup completed" >> backup.log
echo "백업이 완료되었습니다: $BACKUP_DIR"
```

## 개인 실습 문제

1. for 문을 사용해 student1, student2, student3 폴더를 자동 생성해 보자.
2. 백업 스크립트에 백업 후 tree 출력 줄을 추가해 보자.
3. if 문을 사용해 source 폴더가 없으면 경고 후 종료하는 기능을 넣어 보자.

## 정답 예시

1. for i in 1 2 3; do mkdir -p student$i; done 형태를 사용할 수 있다.
2. tree "$BACKUP_DIR" 또는 find "$BACKUP_DIR" 를 추가하면 된다.
3. if [ ! -d source ]; then echo 'source 폴더 없음'; exit 1; fi 를 넣으면 된다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
