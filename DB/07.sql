-- 07.sql: 종합 미션
-- 지금까지 배운 CREATE, INSERT, SELECT, JOIN, 서브쿼리, VIEW 개념을 종합적으로 연습합니다.

USE school_db;
-- 예상 결과: school_db 데이터베이스를 사용합니다.

-- 미션 1: 새로운 학생을 추가하고, Math와 English 과목의 성적을 입력하세요.
-- 학생: 이름 'Frank', 나이 23, 학년 'B'
-- Math 점수: 87.5, English 점수: 92.0
-- 예상 결과: students에 Frank 1행, grades에 2행이 추가됩니다.

-- 답:
-- INSERT INTO students (name, age, grade) VALUES ('Frank', 23, 'B');
-- INSERT INTO grades (student_id, subject_id, score) VALUES (4, 1, 87.5);
-- INSERT INTO grades (student_id, subject_id, score) VALUES (4, 2, 92.0);

-- 미션 2: 모든 학생의 이름과 평균 점수를 조회하세요. (조인과 그룹화 사용)
-- 예상 결과: 학생별 평균 점수 목록이 조회됩니다.

-- 답:
-- SELECT s.name, AVG(g.score) AS avg_score
-- FROM students s
-- LEFT JOIN grades g ON s.student_id = g.student_id
-- GROUP BY s.student_id, s.name;

-- 미션 3: 평균 점수가 90 이상인 학생의 이름을 서브쿼리로 조회하세요.
-- 예상 결과: 평균 점수가 90 이상인 학생 이름이 조회됩니다.

-- 답:
-- SELECT name FROM students WHERE student_id IN (
--     SELECT student_id FROM grades GROUP BY student_id HAVING AVG(score) >= 90
-- );

-- 미션 4: 학생 성적 뷰를 생성하고, 조회하세요.
-- 예상 결과: 학생 이름, 과목 이름, 점수를 보여 주는 뷰가 생성되고 조회됩니다.

-- 답:
-- CREATE VIEW full_student_grades AS
-- SELECT s.name, sub.subject_name, g.score
-- FROM students s
-- JOIN grades g ON s.student_id = g.student_id
-- JOIN subjects sub ON g.subject_id = sub.subject_id;
-- SELECT * FROM full_student_grades;

-- 미션 5: Science 과목의 평균 점수를 조회하세요. (서브쿼리 사용)
-- 예상 결과: Science 과목의 평균 점수 1개 값이 조회됩니다.

-- 답:
-- SELECT AVG(score) FROM grades WHERE subject_id = (SELECT subject_id FROM subjects WHERE subject_name = 'Science');

-- 모든 미션을 완료한 후, 데이터베이스를 정리하세요 (선택사항).
-- DROP DATABASE school_db;
