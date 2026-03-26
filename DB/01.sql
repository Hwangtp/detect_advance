-- 01.sql: 데이터베이스 및 테이블 생성 (DDL)
-- MySQL DDL (Data Definition Language) 소개
-- DDL은 데이터베이스 구조를 정의하는 명령어입니다.
-- CREATE, ALTER, DROP 등이 포함됩니다.

-- 데이터베이스 생성
CREATE DATABASE IF NOT EXISTS school_db;
-- school_db 데이터베이스를 생성합니다. IF NOT EXISTS는 이미 존재하면 생성하지 않습니다.

-- 데이터베이스 사용
USE school_db;
-- school_db 데이터베이스를 선택하여 이후 쿼리를 실행합니다.

-- 테이블 생성: 학생 테이블
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,  -- 학생 ID, 기본키, 자동 증가
    name VARCHAR(100) NOT NULL,  -- 이름, 필수 입력
    age INT,  -- 나이
    grade VARCHAR(10)  -- 학년
);
-- students 테이블을 생성합니다. 컬럼: student_id (자동 증가), name (필수), age, grade.

-- 테이블 생성: 과목 테이블
CREATE TABLE subjects (
    subject_id INT PRIMARY KEY AUTO_INCREMENT,  -- 과목 ID
    subject_name VARCHAR(100) NOT NULL  -- 과목 이름
);

-- 테이블 생성: 성적 테이블
CREATE TABLE grades (
    grade_id INT PRIMARY KEY AUTO_INCREMENT,  -- 성적 ID
    student_id INT,  -- 학생 ID (외래키)
    subject_id INT,  -- 과목 ID (외래키)
    score DECIMAL(5,2),  -- 점수 (소수점 2자리)
    FOREIGN KEY (student_id) REFERENCES students(student_id),  -- 외래키 제약
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

-- 실습: 위 쿼리들을 실행하여 테이블을 생성하세요.

-- 미션: 새로운 테이블 'teachers'를 생성하세요. 컬럼: teacher_id (INT, PK, AUTO_INCREMENT), name (VARCHAR(100), NOT NULL), subject (VARCHAR(100)).
-- 답:
-- CREATE TABLE teachers (
--     teacher_id INT PRIMARY KEY AUTO_INCREMENT,
--     name VARCHAR(100) NOT NULL,
--     subject VARCHAR(100)
-- );