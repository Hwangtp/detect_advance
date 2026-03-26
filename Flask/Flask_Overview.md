# Flask Overview

## Flask란?

Flask는 Python으로 웹 애플리케이션을 만들기 위한 가벼운 웹 프레임워크입니다.

## Flask의 특징

- 구조가 단순합니다.
- 필요한 기능부터 작게 시작할 수 있습니다.
- Python 기초를 바탕으로 웹 개발 흐름을 익히기 좋습니다.
- 확장성이 높아 데이터베이스, 인증, 파일 업로드 같은 기능을 점진적으로 추가할 수 있습니다.

## 이 폴더의 학습 흐름

이 폴더는 Flask의 기초부터 게시판 형태의 응용 예제까지 순서대로 구성되어 있습니다.

- `00_Hello_Flask.py`: 첫 Flask 앱과 기본 라우팅
- `01_Routing.py`: 라우팅 확장 기능
- `02_Static_Files.py`: CSS, JavaScript, 이미지 같은 정적 파일
- `03_Templates.py`: Jinja 템플릿
- `04_Forms.py`: 폼 처리
- `05_Database.py`: SQLite 데이터베이스 연결
- `06_CRUD.py`: 생성, 조회, 수정, 삭제
- `07_Authentication.py`: 로그인과 세션
- `08_File_Upload.py`: 파일 업로드
- `09_Board.py`: 게시판 형태의 종합 예제

## 필요한 라이브러리

```bash
pip install flask
```

## 기본 실행 방법

각 파일은 독립적으로 실행할 수 있습니다.

```bash
python 00_Hello_Flask.py
```

그 뒤 브라우저에서 안내된 주소로 접속해 결과를 확인합니다.

## 함께 알아두면 좋은 폴더

Flask 프로젝트에서는 보통 다음 구조가 함께 등장합니다.

- `templates/`: HTML 템플릿
- `static/`: CSS, JavaScript, 이미지
- `uploads/`: 업로드 파일
- `*.db`: SQLite 데이터베이스 파일

## 핵심 정리

Flask는 웹 개발의 핵심 개념인 라우팅, 템플릿, 폼, 데이터베이스, 인증, 파일 처리 흐름을 작고 이해하기 쉬운 형태로 배울 수 있게 해 주는 프레임워크입니다.
