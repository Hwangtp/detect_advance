-- 03.sql: 데이터 업데이트 및 삭제
-- UPDATE는 기존 데이터를 수정하고, DELETE는 기존 데이터를 삭제합니다.

USE school_db;
-- 예상 결과: school_db 데이터베이스를 사용합니다.

-- student_id가 1인 학생의 나이를 21로 수정
UPDATE students SET age = 21 WHERE student_id = 1;
-- 예상 결과: Alice의 age 값이 21로 변경됩니다.

-- 이름이 Bob인 학생의 나이와 학년 수정
UPDATE students SET age = 23, grade = 'A' WHERE name = 'Bob';
-- 예상 결과: Bob의 age는 23, grade는 A로 변경됩니다.

-- student_id가 3인 학생 삭제
DELETE FROM students WHERE student_id = 3;
-- 예상 결과: Charlie 데이터 1행이 삭제됩니다.

-- 점수가 85 미만인 성적 삭제
DELETE FROM grades WHERE score < 85;
-- 예상 결과: 현재 예제 데이터 기준으로는 삭제되는 행이 없습니다.

-- 변경 결과 확인
SELECT * FROM students;
-- 예상 결과: Alice, Bob 2행만 조회됩니다.

SELECT * FROM grades;
-- 예상 결과: 95.5, 88.0, 92.0 점수 3행이 그대로 조회됩니다.

-- 실습: subjects 테이블에 새로운 과목 'History'를 추가하고, 다시 조회하세요.
-- INSERT INTO subjects (subject_name) VALUES ('History');
-- SELECT * FROM subjects;

-- 미션: grades 테이블에서 student_id가 2인 데이터를 모두 삭제하세요.
-- 답:
-- DELETE FROM grades WHERE student_id = 2;
