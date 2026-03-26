# 04 JOIN 설명

## JOIN이란?

JOIN은 여러 테이블에 나누어 저장된 데이터를 서로 연결해서 한 번에 조회하는 방법입니다.

관계형 데이터베이스에서는 보통 데이터를 한 테이블에 모두 넣지 않습니다.  
중복을 줄이고 구조를 분명하게 만들기 위해 데이터를 여러 테이블로 나누어 저장합니다.

예를 들어 다음과 같이 나눌 수 있습니다.

- `students`: 학생 정보
- `subjects`: 과목 정보
- `grades`: 학생별 과목 점수

이때 학생 이름과 과목 이름과 점수를 한 번에 보고 싶다면 테이블을 연결해야 합니다.  
이 연결이 바로 JOIN입니다.

---

## 왜 JOIN이 필요한가

예를 들어 `grades` 테이블에는 이런 정보가 들어 있습니다.

| grade_id | student_id | subject_id | score |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 95.5 |
| 2 | 1 | 2 | 88.0 |
| 3 | 2 | 1 | 92.0 |

이 표만 보면 `student_id = 1`이 누구인지, `subject_id = 2`가 어떤 과목인지 바로 알 수 없습니다.

그래서 아래 테이블과 연결해야 합니다.

### students

| student_id | name  | age | grade |
|---:|---|---:|---|
| 1 | Alice | 20 | A |
| 2 | Bob | 22 | B |

### subjects

| subject_id | subject_name |
|---:|---|
| 1 | Math |
| 2 | English |
| 3 | Science |

이제 JOIN을 사용하면 다음과 같은 결과를 만들 수 있습니다.

| name | subject_name | score |
|---|---|---:|
| Alice | Math | 95.5 |
| Alice | English | 88.0 |
| Bob | Math | 92.0 |

즉, JOIN은 테이블에 나누어 저장된 데이터를 다시 연결해서 사람이 읽기 쉬운 결과로 만들어 줍니다.

---

## JOIN의 기본 문법

가장 기본적인 문법은 다음과 같습니다.

```sql
SELECT 컬럼목록
FROM 기준테이블
JOIN 연결할테이블
ON 연결조건;
```

예를 들면

```sql
SELECT s.name, g.score
FROM students s
JOIN grades g
ON s.student_id = g.student_id;
```

의미는 다음과 같습니다.

- `students`를 기준으로 가져오고
- `grades`를 연결하고
- `student_id`가 같은 행끼리 묶어서
- `name`과 `score`를 보여 준다

---

## ON은 무엇인가

`ON`은 어떤 기준으로 두 테이블을 연결할지 정하는 부분입니다.

```sql
ON s.student_id = g.student_id
```

이 뜻은

`students` 테이블의 `student_id`와  
`grades` 테이블의 `student_id`가 같은 행끼리 연결하라는 뜻입니다.

JOIN에서 가장 중요한 부분은 사실상 `ON`입니다.  
연결 조건을 잘못 쓰면 전혀 다른 결과가 나올 수 있습니다.

---

## 테이블 별칭(alias)

JOIN 예시에서 자주 보이는 `s`, `g`, `sub` 같은 글자는 테이블 별칭입니다.

```sql
FROM students s
JOIN grades g
```

이렇게 쓰면

- `students`를 `s`
- `grades`를 `g`

로 짧게 부를 수 있습니다.

그래서 아래처럼 간단하게 쓸 수 있습니다.

```sql
s.student_id
g.student_id
```

별칭은 필수는 아니지만 JOIN에서는 거의 항상 사용합니다.

---

## INNER JOIN

`INNER JOIN`은 두 테이블에서 연결 조건에 맞는 데이터만 보여 주는 방식입니다.

```sql
SELECT s.name, sub.subject_name, g.score
FROM students s
INNER JOIN grades g ON s.student_id = g.student_id
INNER JOIN subjects sub ON g.subject_id = sub.subject_id;
```

이 쿼리는 이렇게 이해하면 됩니다.

- 먼저 `students`와 `grades`를 학생 번호로 연결하고
- 그 다음 `grades`와 `subjects`를 과목 번호로 연결해서
- 최종적으로 학생 이름, 과목명, 점수를 보여 줍니다.

예를 들어 `students` 테이블이 아래와 같고

| student_id | name |
|---:|---|
| 1 | Alice |
| 2 | Bob |
| 3 | Charlie |

`subjects` 테이블이 아래와 같고

| subject_id | subject_name |
|---:|---|
| 1 | Math |
| 2 | English |
| 3 | Science |

`grades` 테이블이 아래와 같다면

| grade_id | student_id | subject_id | score |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 95.5 |
| 2 | 1 | 2 | 88.0 |
| 3 | 2 | 1 | 92.0 |

`INNER JOIN` 결과는 이렇게 됩니다.

| name | subject_name | score |
|---|---|---:|
| Alice | Math | 95.5 |
| Alice | English | 88.0 |
| Bob | Math | 92.0 |

여기서 `Charlie`는 `students`에는 있지만 `grades`에 연결된 점수가 없으므로 결과에 나오지 않습니다.  
`Science`도 `subjects`에는 있지만 연결된 점수가 없으므로 결과에 나오지 않습니다.

즉, `INNER JOIN`은 **양쪽에서 실제로 연결되는 데이터만 남기고, 연결되지 않는 것은 제외하는 방식**입니다.

한 문장으로 정리하면,

**INNER JOIN은 연결 조건에 맞아 서로 이어지는 데이터만 보여 주는 방식입니다.**

---

## LEFT JOIN

`LEFT JOIN`에서 말하는 "왼쪽"은 화면의 왼쪽이 아니라,  
`FROM` 뒤에 먼저 적은 테이블을 뜻합니다.

아래 구문에서는 `students`가 왼쪽 테이블이고, `grades`가 오른쪽 테이블입니다.

```sql
SELECT s.name, g.score
FROM students s
LEFT JOIN grades g ON s.student_id = g.student_id;
```

이 쿼리의 기준은 `students`입니다.  
즉, 학생 목록은 빠지지 않고 모두 먼저 가져오고,  
각 학생에 연결되는 점수 데이터가 있으면 옆에 붙이는 방식입니다.

그래서 결과를 이렇게 이해하면 됩니다.

- 학생이 있고 점수도 있으면: 이름과 점수가 함께 나옴
- 학생은 있는데 점수가 없으면: 이름은 나오고 점수는 `NULL`

예를 들어 `students` 테이블이 아래와 같다고 가정해 봅시다.

| student_id | name |
|---:|---|
| 1 | Alice |
| 2 | Bob |
| 3 | Charlie |

그리고 `grades` 테이블이 이렇게 있다면

| student_id | score |
|---:|---:|
| 1 | 95.5 |
| 2 | 92.0 |

`LEFT JOIN` 결과는 이렇게 됩니다.

| name | score |
|---|---:|
| Alice | 95.5 |
| Bob | 92.0 |
| Charlie | NULL |

즉, `Charlie`는 점수 데이터가 없어도 학생 테이블에 있으므로 결과에서 사라지지 않습니다.

한 문장으로 정리하면,

**LEFT JOIN은 `FROM` 뒤에 먼저 쓴 테이블을 기준으로 모두 보여 주고, 연결되는 데이터만 오른쪽에서 붙이는 방식입니다.**

---

## RIGHT JOIN

`RIGHT JOIN`에서 말하는 "오른쪽"은 화면 오른쪽이 아니라,  
`RIGHT JOIN` 뒤에 적은 테이블을 뜻합니다.

아래 구문에서는 `subjects`가 오른쪽 테이블이고, `grades`가 왼쪽 테이블입니다.

```sql
SELECT sub.subject_name, g.score
FROM grades g
RIGHT JOIN subjects sub ON g.subject_id = sub.subject_id;
```

이 쿼리의 기준은 `subjects`입니다.  
즉, 과목 목록은 빠지지 않고 모두 먼저 가져오고,  
각 과목에 연결되는 점수 데이터가 있으면 옆에 붙이는 방식입니다.

그래서 결과를 이렇게 이해하면 됩니다.

- 과목이 있고 점수도 있으면: 과목명과 점수가 함께 나옴
- 과목은 있는데 점수가 없으면: 과목명은 나오고 점수는 `NULL`

예를 들어 `subjects` 테이블이 아래와 같다고 가정해 봅시다.

| subject_id | subject_name |
|---:|---|
| 1 | Math |
| 2 | English |
| 3 | Science |

그리고 `grades` 테이블이 이렇게 있다면

| subject_id | score |
|---:|---:|
| 1 | 95.5 |
| 1 | 92.0 |
| 2 | 88.0 |

`RIGHT JOIN` 결과는 이렇게 됩니다.

| subject_name | score |
|---|---:|
| Math | 95.5 |
| Math | 92.0 |
| English | 88.0 |
| Science | NULL |

즉, `Science`는 점수 데이터가 없어도 과목 테이블에 있으므로 결과에서 사라지지 않습니다.

한 문장으로 정리하면,

**RIGHT JOIN은 `RIGHT JOIN` 뒤에 쓴 테이블을 기준으로 모두 보여 주고, 연결되는 데이터만 왼쪽에서 붙이는 방식입니다.**

---

## CROSS JOIN

`CROSS JOIN`은 두 테이블을 조건으로 연결하는 것이 아니라,  
한쪽 테이블의 각 행을 다른 쪽 테이블의 모든 행과 한 번씩 짝짓는 방식입니다.

```sql
SELECT s.name, sub.subject_name
FROM students s
CROSS JOIN subjects sub;
```

이 쿼리는 다음처럼 이해하면 쉽습니다.

- 학생 1명마다 모든 과목을 붙인다
- 다시 다음 학생에게도 모든 과목을 붙인다

즉, 가능한 모든 조합을 만드는 것입니다.

예를 들어 `students`가 아래와 같고

| student_id | name |
|---:|---|
| 1 | Alice |
| 2 | Bob |

`subjects`가 아래와 같다면

| subject_id | subject_name |
|---:|---|
| 1 | Math |
| 2 | English |
| 3 | Science |

`CROSS JOIN` 결과는 이렇게 됩니다.

| name | subject_name |
|---|---|
| Alice | Math |
| Alice | English |
| Alice | Science |
| Bob | Math |
| Bob | English |
| Bob | Science |

학생이 2명이고 과목이 3개라면 결과는 `2 x 3 = 6행`이 됩니다.

즉, `CROSS JOIN`은 "연결 조건"보다 "가능한 모든 경우의 수"를 만드는 데 가깝습니다.

한 문장으로 정리하면,

**CROSS JOIN은 두 테이블의 모든 행을 서로 한 번씩 짝지어 모든 조합을 만드는 방식입니다.**

---

## SELF JOIN

`SELF JOIN`은 같은 테이블을 자기 자신과 다시 연결하는 방식입니다.

같은 테이블을 두 번 사용하는 것이므로,  
서로 다른 테이블처럼 보이도록 별칭(alias)을 붙여서 구분하는 것이 중요합니다.

예를 들어 친구 관계를 저장한 `friendships` 테이블이 있고,  
학생 이름은 모두 `students` 테이블에 들어 있다고 가정해 봅시다.

```sql
SELECT f1.name AS friend1, f2.name AS friend2
FROM friendships fr
JOIN students f1 ON fr.friend1_id = f1.student_id
JOIN students f2 ON fr.friend2_id = f2.student_id;
```

위 쿼리는 `students` 테이블을 두 번 사용합니다.

- `f1`은 첫 번째 학생
- `f2`는 두 번째 학생

으로 생각하면 됩니다.

예를 들어 `students` 테이블이 아래와 같고

| student_id | name |
|---:|---|
| 1 | Alice |
| 2 | Bob |
| 3 | Charlie |

`friendships` 테이블이 아래와 같다면

| friend1_id | friend2_id |
|---:|---:|
| 1 | 2 |
| 2 | 3 |

쿼리 결과는 이렇게 됩니다.

| friend1 | friend2 |
|---|---|
| Alice | Bob |
| Bob | Charlie |

즉, 같은 `students` 테이블을 두 번 불러와서  
한 번은 친구 1, 한 번은 친구 2 역할로 사용한 것입니다.

한 문장으로 정리하면,

**SELF JOIN은 하나의 테이블을 두 번 이상 불러와 서로 다른 역할로 연결하는 방식입니다.**

---

## JOIN을 읽는 순서

JOIN 쿼리는 아래 순서로 읽으면 이해가 쉬워집니다.

1. `FROM`에서 기준 테이블 확인
2. 어떤 테이블을 `JOIN`하는지 확인
3. `ON`에서 어떤 컬럼끼리 연결하는지 확인
4. `SELECT`에서 최종적으로 어떤 컬럼을 보여 주는지 확인

예를 들어

```sql
SELECT s.name, g.score
FROM students s
JOIN grades g
ON s.student_id = g.student_id;
```

는 이렇게 읽을 수 있습니다.

- `students`를 기준으로 시작하고
- `grades`를 붙이고
- `student_id`가 같은 것끼리 연결해서
- 학생 이름과 점수를 출력한다

---

## JOIN에서 자주 헷갈리는 점

### 1. JOIN은 테이블을 그냥 옆에 붙이는 것이 아니다

조건 없이 붙이는 것이 아니라, `ON` 조건에 맞는 행끼리 연결합니다.

### 2. 외래키가 JOIN의 힌트가 된다

예를 들어 `grades.student_id`는 `students.student_id`를 참조하므로  
두 테이블은 이 컬럼으로 연결하는 경우가 많습니다.

### 3. 컬럼 이름이 겹칠 수 있다

예를 들어 여러 테이블에 `student_id`가 있으면,  
반드시 `s.student_id`, `g.student_id`처럼 테이블 이름이나 별칭을 붙여 주는 것이 좋습니다.

---

## 참고 예시 1: 학생 이름과 점수 조회

```sql
SELECT s.name, g.score
FROM students s
JOIN grades g ON s.student_id = g.student_id;
```

의미:

- 학생 테이블과 성적 테이블 연결
- 같은 학생 번호끼리 묶음
- 학생 이름과 점수 출력

---

## 참고 예시 2: 학생 이름, 과목명, 점수 조회

```sql
SELECT s.name, sub.subject_name, g.score
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sub ON g.subject_id = sub.subject_id;
```

의미:

- 학생과 성적 연결
- 성적과 과목 연결
- 최종적으로 이름, 과목, 점수 출력

---

## 참고 예시 3: 점수가 없는 학생 찾기

```sql
SELECT s.name
FROM students s
LEFT JOIN grades g ON s.student_id = g.student_id
WHERE g.score IS NULL;
```

의미:

- 모든 학생을 기준으로 조회
- 점수가 연결되지 않은 학생만 찾기

---

## JOIN 핵심 정리

- JOIN은 여러 테이블을 연결해서 조회하는 방법입니다.
- 관계형 데이터베이스에서는 매우 자주 사용됩니다.
- 가장 중요한 것은 `ON`의 연결 조건입니다.
- `INNER JOIN`은 공통 데이터만, `LEFT JOIN`은 왼쪽 기준 전체, `RIGHT JOIN`은 오른쪽 기준 전체를 보여 줍니다.
- `grades` 같은 테이블은 다른 테이블을 연결하는 중간 역할을 할 수 있습니다.

## 한 문장 정리

JOIN은 나누어 저장된 데이터를 다시 연결해서 의미 있는 결과표로 보여 주는 SQL 기능입니다.
