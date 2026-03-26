# 02 Static Files

## 개요

이 문서는 Flask에서 CSS, JavaScript, 이미지 같은 정적 파일을 사용하는 방법을 설명합니다.

## 정적 파일이란?

정적 파일은 서버에서 가공하지 않고 그대로 브라우저에 전달하는 파일입니다.

- CSS
- JavaScript
- 이미지
- 글꼴 파일

## static 폴더

Flask는 기본적으로 `static` 폴더를 정적 파일 위치로 사용합니다.

예시 구조:

```text
project/
├── app.py
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── templates/
```

## 정적 파일 연결

HTML 안에서 정적 파일을 불러올 수 있습니다.

```html
<link rel="stylesheet" href="/static/css/style.css">
<script src="/static/js/script.js"></script>
<img src="/static/images/logo.png">
```

## url_for와 static

정적 파일 경로도 `url_for()`로 만들 수 있습니다.

```python
url_for('static', filename='css/style.css')
```

이 방식은 경로가 바뀌더라도 코드를 수정하기 쉽습니다.

## CSS와 JavaScript의 역할

- CSS: 화면 스타일 지정
- JavaScript: 버튼 클릭, 입력 처리, 화면 변화 같은 동작 처리

정적 파일을 사용하면 HTML, 스타일, 동작을 분리해서 관리할 수 있습니다.

## 이미지 사용

이미지 파일도 `static/images/` 같은 구조로 보관한 뒤 HTML에서 불러올 수 있습니다.

```html
<img src="/static/images/logo.png" alt="로고">
```

## 핵심 정리

- Flask의 기본 정적 파일 폴더는 `static`입니다.
- CSS, JavaScript, 이미지를 이 폴더 아래에서 관리합니다.
- `url_for('static', filename=...)` 방식이 안전하고 편리합니다.
- 정적 파일을 분리하면 화면 구조와 스타일, 동작을 깔끔하게 관리할 수 있습니다.
