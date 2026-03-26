# 03 Templates

## 개요

이 문서는 Flask에서 Jinja 템플릿을 사용해 동적인 HTML 페이지를 만드는 방법을 설명합니다.

## 템플릿이 필요한 이유

단순 문자열로 HTML을 직접 반환할 수도 있지만,  
페이지가 많아지거나 데이터가 바뀌는 경우에는 템플릿 파일을 사용하는 편이 훨씬 편리합니다.

템플릿을 사용하면

- HTML 구조를 파일로 분리할 수 있고
- Python 데이터를 페이지에 넣을 수 있으며
- 반복과 조건 처리를 템플릿 안에서 할 수 있습니다

## render_template

Flask에서 템플릿을 렌더링할 때는 `render_template()`를 사용합니다.

```python
from flask import render_template

return render_template('index.html', title='홈')
```

이 코드는 `templates/index.html` 파일을 읽고, `title` 값을 함께 전달합니다.

## 템플릿에 데이터 전달

Flask에서는 문자열, 리스트, 딕셔너리 등을 템플릿으로 넘길 수 있습니다.

```python
return render_template(
    'products.html',
    products=products_list,
    total_products=len(products_list)
)
```

템플릿에서는 전달된 값을 그대로 사용할 수 있습니다.

## 템플릿의 장점

- HTML을 Python 코드와 분리할 수 있습니다.
- 같은 레이아웃을 여러 페이지에서 재사용할 수 있습니다.
- 목록 출력, 조건 분기 같은 화면 로직을 표현할 수 있습니다.

## 사용자 정보와 목록 출력

템플릿은 사용자 정보 한 건이나 여러 상품 목록 같은 구조를 표시할 때 특히 유용합니다.

- 사용자 상세 페이지
- 상품 목록 페이지
- 공통 레이아웃 페이지

## Jinja 템플릿

Flask는 기본적으로 Jinja 템플릿 엔진을 사용합니다.

대표적인 문법:

- `{{ 변수 }}`: 값 출력
- `{% if %}`: 조건문
- `{% for %}`: 반복문

## 템플릿 파일 위치

기본적으로 `templates/` 폴더 안에 HTML 파일을 둡니다.

예:

```text
templates/
├── index.html
├── user.html
├── products.html
└── base.html
```

## 핵심 정리

- 템플릿은 동적인 HTML 페이지를 만들기 위한 기능입니다.
- `render_template()`로 템플릿 파일을 렌더링합니다.
- Python 데이터를 템플릿으로 전달할 수 있습니다.
- Jinja 문법을 이용해 화면에 반복과 조건을 적용할 수 있습니다.
