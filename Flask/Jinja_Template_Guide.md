# Jinja Template Guide

## Jinja란?

Jinja는 Flask에서 사용하는 템플릿 엔진입니다.  
HTML 안에 변수, 반복문, 조건문을 넣어 동적인 페이지를 만들 수 있습니다.

## 기본 문법

### 변수 출력

```jinja2
{{ title }}
```

전달받은 값을 화면에 출력합니다.

### 코드 블록

```jinja2
{% if user %}
{% endif %}
```

조건문이나 반복문 같은 템플릿 로직을 작성합니다.

### 주석

```jinja2
{# 주석 내용 #}
```

HTML 결과에는 보이지 않는 주석입니다.

## 필터

필터는 값을 변형해서 출력할 때 사용합니다.

예:

- `upper`
- `lower`
- `capitalize`
- `length`
- `replace`
- `join`

```jinja2
{{ name|upper }}
{{ items|length }}
```

## 조건문

```jinja2
{% if age >= 18 %}
    <p>성인입니다.</p>
{% else %}
    <p>미성년자입니다.</p>
{% endif %}
```

조건에 따라 다른 HTML을 보여 줄 수 있습니다.

## 반복문

```jinja2
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
```

리스트나 딕셔너리 데이터를 화면에 나열할 때 사용합니다.

## loop 변수

반복문 안에서는 `loop` 객체를 사용할 수 있습니다.

- `loop.index`
- `loop.first`
- `loop.last`
- `loop.length`

## 딕셔너리와 리스트

템플릿에서는 딕셔너리나 리스트 데이터도 쉽게 읽을 수 있습니다.

```jinja2
{{ user.name }}
{{ items[0] }}
```

## 템플릿 상속

Jinja에서는 공통 레이아웃을 재사용할 수 있습니다.

### 부모 템플릿

```jinja2
{% block content %}{% endblock %}
```

### 자식 템플릿

```jinja2
{% extends "base.html" %}
{% block content %}
    <h1>내용</h1>
{% endblock %}
```

이 방식은 공통 헤더, 메뉴, 푸터를 여러 페이지에서 재사용할 때 유용합니다.

## include

다른 템플릿 조각을 불러와 사용할 수 있습니다.

```jinja2
{% include 'header.html' %}
```

## set

템플릿 안에서 임시 변수를 만들 수 있습니다.

```jinja2
{% set username = 'John' %}
```

## 핵심 정리

- Jinja는 Flask의 기본 템플릿 엔진입니다.
- `{{ }}`는 값 출력, `{% %}`는 로직 처리에 사용합니다.
- 필터, 조건문, 반복문을 통해 동적인 HTML을 만들 수 있습니다.
- 템플릿 상속과 include를 사용하면 HTML 구조를 재사용하기 쉬워집니다.
