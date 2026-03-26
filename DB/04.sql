-- 04.sql: 조인 (JOIN)
-- 조인은 여러 테이블을 연결하여 관련 데이터를 함께 조회하는 방법입니다.

USE school_db;
-- 예상 결과: school_db 데이터베이스를 사용합니다.

-- INNER JOIN: 공통으로 연결되는 데이터만 조회
SELECT s.name, sub.subject_name, g.score
FROM students s
INNER JOIN grades g ON s.student_id = g.student_id
INNER JOIN subjects sub ON g.subject_id = sub.subject_id;
-- 예상 결과: Alice-Math-95.5, Alice-English-88.0, Bob-Math-92.0 총 3행이 조회됩니다.

-- LEFT JOIN: 왼쪽 테이블 기준으로 모두 조회
SELECT s.name, g.score
FROM students s
LEFT JOIN grades g ON s.student_id = g.student_id;
-- 예상 결과: 현재 예제 데이터 기준으로 Alice 2행, Bob 1행 총 3행이 조회됩니다.

-- RIGHT JOIN: 오른쪽 테이블 기준으로 모두 조회
SELECT sub.subject_name, g.score
FROM grades g
RIGHT JOIN subjects sub ON g.subject_id = sub.subject_id;
-- 예상 결과: Math 2행, English 1행, Science NULL 1행으로 총 4행이 조회됩니다.

-- FULL OUTER JOIN 시뮬레이션: UNION 사용
SELECT s.name, g.score
FROM students s
LEFT JOIN grades g ON s.student_id = g.student_id
UNION
SELECT s.name, g.score
FROM students s
RIGHT JOIN grades g ON s.student_id = g.student_id;
-- 예상 결과: 현재 예제 데이터 기준으로 Alice 2행, Bob 1행 총 3행이 조회됩니다.

-- SELF JOIN 설명용 임시 테이블 생성
CREATE TEMPORARY TABLE friendships (
    friend1_id INT,
    friend2_id INT
);
-- 예상 결과: friendships 임시 테이블이 생성됩니다.

INSERT INTO friendships VALUES (1, 2), (2, 3);
-- 예상 결과: friendships에 2행이 추가됩니다.

SELECT f1.name AS friend1, f2.name AS friend2
FROM friendships fr
JOIN students f1 ON fr.friend1_id = f1.student_id
JOIN students f2 ON fr.friend2_id = f2.student_id;
-- 예상 결과: 현재 예제 데이터 기준으로 Alice-Bob 1행이 조회됩니다.

-- CROSS JOIN: 모든 조합 생성
SELECT s.name, sub.subject_name
FROM students s
CROSS JOIN subjects sub;
-- 예상 결과: 학생 2명 x 과목 3개 = 총 6행이 조회됩니다.

-- ON을 사용한 조인 조건 명시
SELECT s.name, g.score
FROM students s
JOIN grades g ON s.student_id = g.student_id;
-- 예상 결과: Alice 2행, Bob 1행 총 3행이 조회됩니다.

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
