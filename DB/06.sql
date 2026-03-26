-- 06.sql: 인덱스와 뷰 (Index and View)
-- 인덱스는 조회 성능을 높이고, 뷰는 복잡한 SELECT 결과를 재사용하기 쉽게 만듭니다.

USE school_db;
-- 예상 결과: school_db 데이터베이스를 사용합니다.

-- 학생 이름 인덱스 생성
CREATE INDEX idx_student_name ON students (name);
-- 예상 결과: students.name 컬럼에 인덱스가 생성됩니다.

-- grades 테이블 복합 인덱스 생성
CREATE INDEX idx_grade_student_subject ON grades (student_id, subject_id);
-- 예상 결과: grades(student_id, subject_id) 복합 인덱스가 생성됩니다.

-- 인덱스 확인
SHOW INDEX FROM students;
-- 예상 결과: PRIMARY 인덱스와 idx_student_name 인덱스 정보가 조회됩니다.

-- 학생 성적 뷰 생성
CREATE VIEW student_grades_view AS
SELECT s.name, sub.subject_name, g.score
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sub ON g.subject_id = sub.subject_id;
-- 예상 결과: student_grades_view가 생성됩니다.

-- 뷰 조회
SELECT * FROM student_grades_view;
-- 예상 결과: Alice-Math-95.5, Alice-English-88.0, Bob-Math-92.0 총 3행이 조회됩니다.

-- 뷰 수정
ALTER VIEW student_grades_view AS
SELECT s.name, AVG(g.score) AS avg_score
FROM students s
LEFT JOIN grades g ON s.student_id = g.student_id
GROUP BY s.student_id, s.name;
-- 예상 결과: student_grades_view가 학생별 평균 점수 뷰로 변경됩니다.

-- 뷰 삭제 예시
-- DROP VIEW student_grades_view;
-- 예상 결과: 주석을 해제하면 student_grades_view가 삭제됩니다.

-- 실습: subjects 테이블의 subject_name에 인덱스를 생성하세요.
-- CREATE INDEX idx_subject_name ON subjects (subject_name);

-- 미션: grades 테이블의 score에 인덱스를 생성하고, 평균 점수를 보여주는 뷰를 만드세요.
-- 답:
-- CREATE INDEX idx_score ON grades (score);
-- CREATE VIEW avg_grades_view AS SELECT student_id, AVG(score) AS avg_score FROM grades GROUP BY student_id;
