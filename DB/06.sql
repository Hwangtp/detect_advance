-- 06.sql: 인덱스와 뷰 (Index and View)
-- 인덱스: 쿼리 성능을 향상시키기 위한 데이터 구조입니다.
-- 뷰: 가상의 테이블로, 복잡한 쿼리를 단순화합니다.

USE school_db;

-- 인덱스 생성: 학생 이름에 인덱스
CREATE INDEX idx_student_name ON students (name);
-- students 테이블의 name 컬럼에 인덱스를 생성합니다. 이름으로 검색할 때 성능 향상.

-- 인덱스 생성: 복합 인덱스
CREATE INDEX idx_grade_student_subject ON grades (student_id, subject_id);
-- grades 테이블에 student_id와 subject_id의 복합 인덱스를 생성합니다.

-- 인덱스 확인
SHOW INDEX FROM students;

-- 뷰 생성: 학생 성적 요약 뷰
CREATE VIEW student_grades_view AS
SELECT s.name, sub.subject_name, g.score
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sub ON g.subject_id = sub.subject_id;
-- student_grades_view 뷰를 생성합니다. 학생 이름, 과목, 점수를 포함.

-- 뷰 조회
SELECT * FROM student_grades_view;

-- 뷰 수정 (ALTER VIEW)
ALTER VIEW student_grades_view AS
SELECT s.name, AVG(g.score) AS avg_score
FROM students s
LEFT JOIN grades g ON s.student_id = g.student_id
GROUP BY s.student_id, s.name;

-- 뷰 삭제
-- DROP VIEW student_grades_view;

-- 실습: subjects 테이블의 subject_name에 인덱스를 생성하세요.
-- CREATE INDEX idx_subject_name ON subjects (subject_name);

-- 미션: grades 테이블의 score에 인덱스를 생성하고, 평균 점수를 보여주는 뷰를 만드세요.
-- 답:
-- CREATE INDEX idx_score ON grades (score);
-- CREATE VIEW avg_grades_view AS SELECT student_id, AVG(score) AS avg_score FROM grades GROUP BY student_id;