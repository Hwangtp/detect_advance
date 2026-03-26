-- 01.sql: 데이터베이스 및 테이블 생성 (DDL)
-- DDL(Data Definition Language)은 데이터베이스 구조를 정의하는 명령어입니다.
-- CREATE, ALTER, DROP 등이 대표적입니다.

-- 데이터베이스 생성
CREATE DATABASE IF NOT EXISTS school_db;
-- 예상 결과: school_db 데이터베이스가 생성됩니다.

-- 데이터베이스 선택
USE school_db;
-- 예상 결과: 이후 쿼리가 school_db에서 실행됩니다.

-- 학생 테이블 생성
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    grade VARCHAR(10)
);
-- 예상 결과: students 테이블이 생성됩니다.

-- 과목 테이블 생성
CREATE TABLE subjects (
    subject_id INT PRIMARY KEY AUTO_INCREMENT,
    subject_name VARCHAR(100) NOT NULL
);
-- 예상 결과: subjects 테이블이 생성됩니다.

-- 성적 테이블 생성
CREATE TABLE grades (
    grade_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    subject_id INT,
    score DECIMAL(5,2),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);
-- 예상 결과: grades 테이블이 생성됩니다.

-- 실습: 위 쿼리들을 실행하여 테이블을 생성하세요.

-- 미션: 새로운 테이블 'teachers'를 생성하세요. 컬럼: teacher_id (INT, PK, AUTO_INCREMENT), name (VARCHAR(100), NOT NULL), subject (VARCHAR(100)).
-- 답:
-- CREATE TABLE teachers (
--     teacher_id INT PRIMARY KEY AUTO_INCREMENT,
--     name VARCHAR(100) NOT NULL,
--     subject VARCHAR(100)
-- );
