-- 04.sql: 조인 (JOIN)
-- 조인은 여러 테이블을 연결하여 데이터를 조회하는 방법입니다.
-- INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN, SELF JOIN, CROSS JOIN 등이 있습니다.

USE school_db;

-- INNER JOIN: 두 테이블의 공통 데이터만 조회
SELECT s.name, sub.subject_name, g.score
FROM students s
INNER JOIN grades g ON s.student_id = g.student_id
INNER JOIN subjects sub ON g.subject_id = sub.subject_id;
-- 학생 이름, 과목 이름, 점수를 INNER JOIN으로 조회합니다.

-- LEFT JOIN: 왼쪽 테이블의 모든 데이터와 오른쪽 테이블의 매칭 데이터
SELECT s.name, g.score
FROM students s
LEFT JOIN grades g ON s.student_id = g.student_id;
-- 학생 이름과 점수를 LEFT JOIN으로 조회합니다. 점수가 없는 학생도 포함됩니다.

-- RIGHT JOIN: 오른쪽 테이블의 모든 데이터와 왼쪽 테이블의 매칭 데이터
SELECT sub.subject_name, g.score
FROM grades g
RIGHT JOIN subjects sub ON g.subject_id = sub.subject_id;
-- 과목 이름과 점수를 RIGHT JOIN으로 조회합니다. 점수가 없는 과목도 포함됩니다.

-- FULL OUTER JOIN: MySQL에서는 UNION으로 시뮬레이션
SELECT s.name, g.score
FROM students s
LEFT JOIN grades g ON s.student_id = g.student_id
UNION
SELECT s.name, g.score
FROM students s
RIGHT JOIN grades g ON s.student_id = g.student_id;
-- 모든 학생과 점수를 FULL OUTER JOIN으로 조회합니다.

-- SELF JOIN: 같은 테이블 내에서 조인 (예: 친구 관계 테이블이 있다고 가정)
-- 예를 위해 임시 테이블 생성 (실제로는 별도 테이블)
CREATE TEMPORARY TABLE friendships (
    friend1_id INT,
    friend2_id INT
);
INSERT INTO friendships VALUES (1, 2), (2, 3);
SELECT f1.name AS friend1, f2.name AS friend2
FROM friendships fr
JOIN students f1 ON fr.friend1_id = f1.student_id
JOIN students f2 ON fr.friend2_id = f2.student_id;
-- SELF JOIN 예시: 친구 관계 조회.

-- CROSS JOIN: 모든 조합 생성 (카테시안 곱)
SELECT s.name, sub.subject_name
FROM students s
CROSS JOIN subjects sub;
-- 학생과 과목의 모든 조합을 CROSS JOIN으로 조회합니다.

-- NATURAL JOIN: 같은 이름의 컬럼으로 자동 조인 (주의: 컬럼 이름이 같아야 함)
-- 예: 컬럼 이름이 같다면 NATURAL JOIN 사용 가능하지만, 여기서는 생략.

-- 조인 조건 예시: ON vs USING
-- ON: 명시적 조건
SELECT s.name, g.score FROM students s JOIN grades g ON s.student_id = g.student_id;
-- USING: 같은 이름 컬럼
-- SELECT name, score FROM students JOIN grades USING (student_id);  -- 컬럼 이름이 student_id로 같아야 함

-- 실습 1: 학생과 과목을 INNER JOIN하여 이름과 과목명을 조회하세요.
-- SELECT s.name, sub.subject_name FROM students s INNER JOIN grades g ON s.student_id = g.student_id INNER JOIN subjects sub ON g.subject_id = sub.subject_id;

-- 실습 2: LEFT JOIN을 사용하여 점수가 없는 학생을 조회하세요.
-- SELECT s.name FROM students s LEFT JOIN grades g ON s.student_id = g.student_id WHERE g.score IS NULL;

-- 실습 3: CROSS JOIN으로 학생 수와 과목 수의 곱을 확인하세요.
-- SELECT COUNT(*) FROM students CROSS JOIN subjects;

-- 미션 1: RIGHT JOIN을 사용하여 점수가 없는 과목을 조회하세요.
-- 답:
-- SELECT sub.subject_name FROM grades g RIGHT JOIN subjects sub ON g.subject_id = sub.subject_id WHERE g.score IS NULL;

-- 미션 2: SELF JOIN 예시를 확장하여 친구의 친구를 조회하세요. (임시 테이블 사용)
-- 답:
-- SELECT f1.name AS person, f3.name AS friend_of_friend
-- FROM friendships fr1
-- JOIN friendships fr2 ON fr1.friend2_id = fr2.friend1_id
-- JOIN students f1 ON fr1.friend1_id = f1.student_id
-- JOIN students f3 ON fr2.friend2_id = f3.student_id;