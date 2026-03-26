-- 05.sql: 서브쿼리 (Subquery)
-- 서브쿼리는 쿼리 안에 또 다른 쿼리를 포함하는 방식입니다.

USE school_db;
-- 예상 결과: school_db 데이터베이스를 사용합니다.

-- 평균 점수보다 높은 점수를 받은 학생 이름 조회
SELECT name FROM students WHERE student_id IN (
    SELECT student_id FROM grades WHERE score > (SELECT AVG(score) FROM grades)
);
-- 예상 결과: Alice, Bob 2행이 조회됩니다.

-- FROM 절의 서브쿼리: 학생별 평균 점수 계산 후 90점 이상만 조회
SELECT avg_scores.student_id, avg_scores.avg_score
FROM (
    SELECT student_id, AVG(score) AS avg_score FROM grades GROUP BY student_id
) AS avg_scores
WHERE avg_scores.avg_score > 90;
-- 예상 결과: student_id 1, 2의 평균 점수 2행이 조회됩니다.

-- 평균 나이보다 나이가 많은 학생 조회
SELECT * FROM students WHERE age > (SELECT AVG(age) FROM students);
-- 예상 결과: Bob 1행이 조회됩니다.

-- EXISTS 사용: 95점 초과 점수가 있는 학생 조회
SELECT name FROM students s WHERE EXISTS (
    SELECT 1 FROM grades g WHERE g.student_id = s.student_id AND g.score > 95
);
-- 예상 결과: Alice 1행이 조회됩니다.

-- 실습: Math 과목의 평균 점수보다 높은 점수를 가진 학생을 조회하세요.
-- SELECT name FROM students WHERE student_id IN (SELECT student_id FROM grades WHERE subject_id = (SELECT subject_id FROM subjects WHERE subject_name = 'Math') AND score > (SELECT AVG(score) FROM grades WHERE subject_id = (SELECT subject_id FROM subjects WHERE subject_name = 'Math')));

-- 미션: 서브쿼리를 사용하여 가장 높은 점수를 가진 학생의 이름을 조회하세요.
-- 답:
-- SELECT name FROM students WHERE student_id = (SELECT student_id FROM grades WHERE score = (SELECT MAX(score) FROM grades));
