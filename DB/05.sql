-- 05.sql: 서브쿼리 (Subquery)
-- 서브쿼리는 쿼리 안에 또 다른 쿼리를 포함하는 것입니다.
-- SELECT, INSERT, UPDATE, DELETE에서 사용할 수 있습니다.

USE school_db;

-- 서브쿼리 in SELECT: 평균 점수보다 높은 학생 조회
SELECT name FROM students WHERE student_id IN (
    SELECT student_id FROM grades WHERE score > (SELECT AVG(score) FROM grades)
);
-- 평균 점수보다 높은 점수를 가진 학생의 이름을 조회합니다.

-- 서브쿼리 in FROM: 임시 테이블로 사용
SELECT avg_scores.student_id, avg_scores.avg_score
FROM (
    SELECT student_id, AVG(score) AS avg_score FROM grades GROUP BY student_id
) AS avg_scores
WHERE avg_scores.avg_score > 90;
-- 각 학생의 평균 점수를 계산한 임시 테이블에서 90점 이상인 학생을 조회합니다.

-- 서브쿼리 in WHERE: 특정 조건
SELECT * FROM students WHERE age > (SELECT AVG(age) FROM students);
-- 평균 나이보다 많은 나이의 학생을 조회합니다.

-- EXISTS 서브쿼리: 존재 여부 확인
SELECT name FROM students s WHERE EXISTS (
    SELECT 1 FROM grades g WHERE g.student_id = s.student_id AND g.score > 95
);
-- 95점 이상의 점수가 있는 학생의 이름을 조회합니다.

-- 실습: Math 과목의 평균 점수보다 높은 점수를 가진 학생을 조회하세요.
-- SELECT name FROM students WHERE student_id IN (SELECT student_id FROM grades WHERE subject_id = (SELECT subject_id FROM subjects WHERE subject_name = 'Math') AND score > (SELECT AVG(score) FROM grades WHERE subject_id = (SELECT subject_id FROM subjects WHERE subject_name = 'Math')));

-- 미션: 서브쿼리를 사용하여 가장 높은 점수를 가진 학생의 이름을 조회하세요.
-- 답:
-- SELECT name FROM students WHERE student_id = (SELECT student_id FROM grades WHERE score = (SELECT MAX(score) FROM grades));