# 05 Database

## 개요

이 문서는 Flask에서 SQLite 데이터베이스를 직접 연결하고 사용하는 방법을 설명합니다.

## SQLite 사용

SQLite는 별도의 서버 설치 없이 파일 하나로 사용할 수 있는 데이터베이스입니다.  
Flask 기초 학습에서 데이터 저장과 조회 흐름을 이해하기에 적합합니다.

## 데이터베이스 연결

```python
import sqlite3

conn = sqlite3.connect(DATABASE)
```

연결 객체를 만들고, SQL을 실행한 뒤, 필요한 경우 `commit()`과 `close()`를 호출합니다.

## row_factory

```python
conn.row_factory = sqlite3.Row
```

이 설정을 하면 조회 결과를 인덱스뿐 아니라 컬럼 이름으로도 접근할 수 있습니다.

## 테이블 생성

이 파일에서는 `user`와 `post` 테이블을 만듭니다.

- `user`: 사용자 정보 저장
- `post`: 게시글 정보 저장

`post.user_id`는 사용자와 게시글의 관계를 연결하는 외래키 역할을 합니다.

## 데이터 추가

`INSERT INTO`를 사용해 샘플 데이터를 넣을 수 있습니다.

파라미터는 `?`를 사용해 전달합니다.

```python
cursor.execute(
    "INSERT INTO user (username, email, password, age) VALUES (?, ?, ?, ?)",
    ('alice', 'alice@example.com', 'password123', 25)
)
```

이 방식은 문자열을 직접 이어 붙이는 것보다 안전합니다.

## 데이터 조회

`SELECT`로 전체 조회, 특정 조건 조회, 관계 기반 조회를 수행할 수 있습니다.

- 전체 사용자 조회
- 특정 사용자 조회
- 조건부 조회
- 특정 사용자의 게시글 조회

## 수정과 삭제

`UPDATE`와 `DELETE`를 통해 기존 데이터를 수정하거나 삭제할 수 있습니다.

## 고급 조회

이 파일은 개수 세기, 정렬, 역순 정렬, 제한(LIMIT) 같은 기본 SQL 활용도 함께 보여 줍니다.

## 핵심 정리

- Flask에서도 `sqlite3`를 직접 사용해 DB를 다룰 수 있습니다.
- 연결, 실행, 커밋, 종료 흐름이 중요합니다.
- `sqlite3.Row`를 사용하면 결과를 컬럼 이름으로 읽기 쉽습니다.
- `?` 파라미터 방식은 안전한 SQL 실행에 도움이 됩니다.
