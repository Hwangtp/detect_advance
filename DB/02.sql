-- 02.sql: 데이터 삽입 및 기본 조회 (DML)
-- DML(Data Manipulation Language)은 데이터를 조작하는 명령어입니다.
-- INSERT, SELECT, UPDATE, DELETE 등이 대표적입니다.

USE school_db;
-- 예상 결과: school_db 데이터베이스를 사용합니다.

-- 학생 데이터 삽입
INSERT INTO students (name, age, grade) VALUES ('Alice', 20, 'A');
INSERT INTO students (name, age, grade) VALUES ('Bob', 22, 'B');
INSERT INTO students (name, age, grade) VALUES ('Charlie', 19, 'A');
-- 예상 결과: students 테이블에 3행이 추가됩니다.

-- 과목 데이터 삽입
INSERT INTO subjects (subject_name) VALUES ('Math');
INSERT INTO subjects (subject_name) VALUES ('English');
INSERT INTO subjects (subject_name) VALUES ('Science');
-- 예상 결과: subjects 테이블에 3행이 추가됩니다.

-- 성적 데이터 삽입
INSERT INTO grades (student_id, subject_id, score) VALUES (1, 1, 95.5);
INSERT INTO grades (student_id, subject_id, score) VALUES (1, 2, 88.0);
INSERT INTO grades (student_id, subject_id, score) VALUES (2, 1, 92.0);
-- 예상 결과: grades 테이블에 3행이 추가됩니다.

-- 모든 학생 조회
SELECT * FROM students;
-- 예상 결과: Alice, Bob, Charlie 3명의 데이터가 조회됩니다.

-- 나이가 20 이상인 학생 조회
SELECT * FROM students WHERE age >= 20;
-- 예상 결과: Alice와 Bob 2행이 조회됩니다.

-- 이름과 학년만 조회
SELECT name, grade FROM students;
-- 예상 결과: name, grade 컬럼만 3행 조회됩니다.

-- 실습: subjects 테이블의 모든 데이터를 조회하세요.
-- SELECT * FROM subjects;

-- 미션: grades 테이블에서 점수가 90 이상인 데이터를 조회하세요.
-- 답:
-- SELECT * FROM grades WHERE score >= 90;
