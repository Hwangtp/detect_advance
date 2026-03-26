-- 00_DB_Overview.sql: 데이터베이스 개요 및 용어 설명
-- MySQL 데이터베이스 기초 개념과 주요 용어를 정리합니다.
-- 이 파일은 설명용이며 실제 쿼리 실행은 포함하지 않습니다.

-- 데이터베이스(Database):
-- 데이터를 체계적으로 저장하고 관리하는 시스템입니다.
-- MySQL은 관계형 데이터베이스 관리 시스템(RDBMS)입니다.

-- 테이블(Table):
-- 데이터를 행과 열로 저장하는 2차원 구조입니다.

-- 행(Row):
-- 하나의 데이터 레코드를 의미합니다.

-- 열(Column):
-- 데이터의 속성이나 항목을 의미합니다.

-- 기본키(Primary Key, PK):
-- 테이블의 각 행을 유일하게 구분하는 컬럼입니다.
-- 예: student_id INT PRIMARY KEY AUTO_INCREMENT
-- 특징: NULL 불가, 중복 불가

-- 외래키(Foreign Key, FK):
-- 다른 테이블의 기본키를 참조하는 컬럼입니다.
-- 예: FOREIGN KEY (student_id) REFERENCES students(student_id)
-- 목적: 테이블 간 관계 표현, 데이터 무결성 유지

-- 스키마(Schema):
-- 데이터베이스 구조를 정의한 설계도입니다.

-- 인덱스(Index):
-- 검색 속도를 높이기 위한 데이터 구조입니다.

-- 뷰(View):
-- 실제 데이터를 저장하지 않고 SELECT 결과를 테이블처럼 보여 주는 가상 테이블입니다.

-- 관계형 데이터베이스의 특징
-- 1. 데이터 중복 최소화
-- 2. 데이터 무결성 유지
-- 3. 구조화된 데이터 관리
-- 4. SQL을 이용한 조회와 조작

-- SQL 언어 분류
-- DDL: CREATE, ALTER, DROP
-- DML: SELECT, INSERT, UPDATE, DELETE
-- DCL: GRANT, REVOKE
-- TCL: COMMIT, ROLLBACK

-- 예상 결과:
-- 이 파일은 설명용 주석만 포함하므로 실행 결과 테이블은 없습니다.
