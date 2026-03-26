-- 00_DB_Overview.sql: 데이터베이스 개요 및 용어 설명
-- MySQL 데이터베이스 기초 개념과 용어 설명
-- 이 파일은 DB 수업의 기초를 다룹니다. SQL 쿼리 실행 없이 설명만 포함.

-- 데이터베이스 (Database): 데이터를 체계적으로 저장하고 관리하는 시스템입니다.
-- MySQL은 관계형 데이터베이스 관리 시스템(RDBMS)입니다.

-- 테이블 (Table): 데이터를 행과 열로 구성된 2차원 구조로 저장합니다.
-- 행 (Row): 테이블의 가로줄, 하나의 레코드(데이터 항목)를 나타냅니다.
-- 열 (Column): 테이블의 세로줄, 데이터의 속성(필드)을 나타냅니다.

-- 기본키 (Primary Key, PK): 테이블에서 각 행을 유일하게 식별하는 컬럼입니다.
-- 예: student_id INT PRIMARY KEY AUTO_INCREMENT
-- 기본키는 NULL일 수 없고, 중복될 수 없습니다.

-- 외래키 (Foreign Key, FK): 다른 테이블의 기본키를 참조하는 컬럼입니다.
-- 예: student_id INT, FOREIGN KEY (student_id) REFERENCES students(student_id)
-- 테이블 간 관계를 맺어 데이터 무결성을 유지합니다.

-- 참조키 (Reference Key): 외래키와 같은 의미로 사용됩니다. 다른 테이블을 참조하는 키입니다.

-- 기타 용어:
-- 스키마 (Schema): 데이터베이스의 구조를 정의하는 청사진입니다.
-- 인덱스 (Index): 쿼리 성능을 향상시키기 위한 데이터 구조입니다.
-- 뷰 (View): 가상의 테이블로, 복잡한 쿼리를 단순화합니다.

-- 관계형 데이터베이스 특징:
-- 1. 데이터 중복 최소화
-- 2. 데이터 무결성 보장
-- 3. 효율적인 데이터 검색

-- SQL 언어 분류:
-- DDL (Data Definition Language): CREATE, ALTER, DROP
-- DML (Data Manipulation Language): SELECT, INSERT, UPDATE, DELETE
-- DCL (Data Control Language): GRANT, REVOKE
-- TCL (Transaction Control Language): COMMIT, ROLLBACK

-- 실습: 이 파일은 설명용입니다. 다음 파일 01.sql부터 실제 쿼리를 실행하세요.

-- 미션: 위 용어 중 3개를 선택하여 간단히 설명하세요.
-- 답: (학생 스스로 작성)