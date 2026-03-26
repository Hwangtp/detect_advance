-- 03.sql: 데이터 업데이트 및 삭제
-- UPDATE와 DELETE 명령어 설명
-- UPDATE: 기존 데이터를 수정합니다.
-- DELETE: 데이터를 삭제합니다.

USE school_db;

-- 데이터 업데이트: 학생 나이 변경
UPDATE students SET age = 21 WHERE student_id = 1;
-- student_id가 1인 학생의 나이를 21로 업데이트합니다.

-- 데이터 업데이트: 여러 컬럼 변경
UPDATE students SET age = 23, grade = 'A' WHERE name = 'Bob';

-- 데이터 삭제: 특정 학생 삭제
DELETE FROM students WHERE student_id = 3;
-- student_id가 3인 학생을 삭제합니다. (주의: 외래키 제약으로 인해 grades 테이블의 관련 데이터도 삭제될 수 있음)

-- 데이터 삭제: 조건 삭제
DELETE FROM grades WHERE score < 85;
-- 점수가 85 미만인 성적 데이터를 삭제합니다.

-- 조회하여 변경 확인
SELECT * FROM students;
SELECT * FROM grades;

-- 실습: subjects 테이블에 새로운 과목 'History'를 추가하고, 다시 조회하세요.
-- INSERT INTO subjects (subject_name) VALUES ('History');
-- SELECT * FROM subjects;

-- 미션: grades 테이블에서 student_id가 2인 데이터를 모두 삭제하세요.
-- 답:
-- DELETE FROM grades WHERE student_id = 2;