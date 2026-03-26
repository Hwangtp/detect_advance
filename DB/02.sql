-- 02.sql: 데이터 삽입 및 기본 조회 (DML)
-- MySQL DML (Data Manipulation Language) 소개
-- DML은 데이터를 조작하는 명령어입니다.
-- INSERT, SELECT, UPDATE, DELETE 등이 포함됩니다.

USE school_db;  -- 데이터베이스 선택

-- 데이터 삽입: 학생 데이터
INSERT INTO students (name, age, grade) VALUES ('Alice', 20, 'A');
INSERT INTO students (name, age, grade) VALUES ('Bob', 22, 'B');
INSERT INTO students (name, age, grade) VALUES ('Charlie', 19, 'A');
-- students 테이블에 데이터를 삽입합니다.

-- 데이터 삽입: 과목 데이터
INSERT INTO subjects (subject_name) VALUES ('Math');
INSERT INTO subjects (subject_name) VALUES ('English');
INSERT INTO subjects (subject_name) VALUES ('Science');

-- 데이터 삽입: 성적 데이터
INSERT INTO grades (student_id, subject_id, score) VALUES (1, 1, 95.5);
INSERT INTO grades (student_id, subject_id, score) VALUES (1, 2, 88.0);
INSERT INTO grades (student_id, subject_id, score) VALUES (2, 1, 92.0);

-- 기본 조회: 모든 학생 조회
SELECT * FROM students;
-- students 테이블의 모든 데이터를 조회합니다.

-- 조건 조회: 나이가 20 이상인 학생
SELECT * FROM students WHERE age >= 20;
-- WHERE 절로 조건을 지정하여 조회합니다.

-- 특정 컬럼 조회: 이름과 학년만
SELECT name, grade FROM students;

-- 실습: subjects 테이블의 모든 데이터를 조회하세요.
-- SELECT * FROM subjects;

-- 미션: grades 테이블에서 점수가 90 이상인 데이터를 조회하세요.
-- 답:
-- SELECT * FROM grades WHERE score >= 90;