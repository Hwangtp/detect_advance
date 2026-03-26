<div align="center">

# 리다이렉션과 파이프

**WSL Ubuntu 리눅스 실습 자료**

</div>

---

> **오늘의 목표**  
> 출력 방향을 바꾸고 여러 명령어를 연결하는 법을 익힌다.

> **오늘 배우는 내용**  
> >, >>, | 를 중심으로 텍스트를 가공하고 결과를 파일로 저장하는 패턴을 연습한다.

## 핵심 개념

- 리눅스의 강점은 작은 명령어를 파이프로 연결해 큰 작업을 만드는 데 있다.
- 리다이렉션은 출력을 화면이 아니라 파일로 보내는 기술이다.

## 복붙 실습 코드

> **실습 환경 안내**  
> 아래 명령은 모두 **WSL Ubuntu 터미널** 기준입니다.

```bash
mkdir -p ~/linux_lab/day06
cd ~/linux_lab/day06
printf 'apple\nbanana\napple\norange\nbanana\nbanana\n' > fruits.txt
cat fruits.txt
sort fruits.txt
sort fruits.txt > fruits_sorted.txt
sort fruits.txt | uniq
sort fruits.txt | uniq -c
sort fruits.txt | uniq -c > count.txt
echo 'grape' >> fruits.txt
cat fruits.txt | wc -l
grep 'banana' fruits.txt | wc -l
```

## 옵션 포인트

- `sort fruits.txt | uniq -c` : uniq -c 의 -c 옵션은 중복 횟수를 함께 보여준다.
- `cat fruits.txt | wc -l` : wc -l 의 -l 옵션은 줄 수를 센다.

## 개인 실습 문제

1. student 목록 파일을 만들어 정렬 후 count.txt 같은 결과 파일을 직접 만들어 보자.
2. 중복된 과일 파일에서 가장 많이 나온 단어를 눈으로 찾아보자.
3. 원본 파일을 덮어쓸 때와 이어 쓸 때의 차이를 > 와 >> 로 실험해 보자.

## 정답 예시

1. sort students.txt | uniq -c > students_count.txt 패턴을 그대로 응용하면 된다.
2. sort 후 uniq -c 결과를 보면 banana가 가장 많다는 것을 확인할 수 있다.
3. > 는 덮어쓰기, >> 는 이어쓰기다.

---

<table>
  <tr><td><strong>수업 체크포인트</strong></td><td>명령어 결과를 읽고 설명할 수 있으면 성공입니다.</td></tr>
  <tr><td><strong>권장 복습</strong></td><td>코드를 다시 직접 입력하고 출력이 왜 나왔는지 말로 정리해 보세요.</td></tr>
</table>
