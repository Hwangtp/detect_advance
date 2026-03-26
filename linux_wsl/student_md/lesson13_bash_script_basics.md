<div align="center">

# 배시 스크립트 기초

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> 셸 스크립트 구조와 변수, 입력, 조건문의 기본을 익힌다.

> **오늘 배우는 내용**  
> 처음으로 .sh 파일을 직접 만들고 실행하며 자동화 감각을 잡는다.

## 핵심 개념

- 반복 작업을 줄이기 위해 스크립트를 만든다.
- 스크립트는 명령어를 순서대로 묶은 자동화 문서다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
mkdir -p ~/linux_lab/day13
cd ~/linux_lab/day13
nano hello_script.sh
chmod +x hello_script.sh
./hello_script.sh
nano input_script.sh
chmod +x input_script.sh
./input_script.sh
```

### 실습 파일 예시: `hello_script.sh`

```bash
#!/bin/bash
echo "안녕하세요 리눅스 스크립트 수업입니다."
echo "현재 사용자는 $(whoami) 입니다."
echo "현재 위치는 $(pwd) 입니다."
```

### 실습 파일 예시: `input_script.sh`

```bash
#!/bin/bash
read -p "이름을 입력하세요: " USER_NAME
if [ -z "$USER_NAME" ]; then
  echo "이름이 비어 있습니다."
else
  echo "반갑습니다, $USER_NAME 님."
fi
```

## 개인 실습 문제

1. 오늘 날짜와 사용자 이름을 출력하는 스크립트를 직접 만들어 보자.
2. read -p 를 사용해 좋아하는 과일을 입력받고 출력해 보자.
3. 입력이 비어 있으면 경고 문장을 출력하는 if 문을 다시 작성해 보자.

## 정답 예시

1. date 와 whoami 명령을 echo와 함께 조합하면 된다.
2. read -p '좋아하는 과일: ' FRUIT 후 echo "$FRUIT" 를 사용하면 된다.
3. if [ -z "$VALUE" ]; then ... fi 형태를 그대로 응용하면 된다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
