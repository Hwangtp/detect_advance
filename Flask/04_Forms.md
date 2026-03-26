# 04 Forms

## 개요

이 문서는 Flask에서 HTML 폼을 통해 사용자 입력을 받고 처리하는 방법을 설명합니다.

## 폼이란?

폼(form)은 사용자가 데이터를 입력해서 서버로 보내는 화면 구성 요소입니다.

예:

- 회원가입
- 로그인
- 문의하기
- 검색
- 설문조사

## GET과 POST

폼 처리에서는 `GET`과 `POST`가 자주 함께 등장합니다.

- `GET`: 폼 화면 표시
- `POST`: 입력한 데이터 제출

```python
@app.route('/register', methods=['GET', 'POST'])
```

## request.form

제출된 폼 데이터는 `request.form`으로 읽을 수 있습니다.

```python
username = request.form.get('username')
email = request.form.get('email')
```

## 입력값 검증

폼 데이터를 사용할 때는 비어 있는 값이 있는지 먼저 검사하는 것이 중요합니다.

```python
if not username or not email:
    error = '모든 필드를 입력하세요.'
```

검증을 통해 잘못된 입력을 미리 처리할 수 있습니다.

## redirect와 url_for

폼 처리 후에는 다른 페이지로 이동시키는 경우가 많습니다.

```python
return redirect(url_for('contact_success'))
```

이 방식은 중복 제출을 줄이고 흐름을 자연스럽게 만듭니다.

## 여러 종류의 입력

폼에서는 다양한 입력 요소를 사용할 수 있습니다.

- `input`
- `textarea`
- `select`
- `checkbox`
- `radio`

여러 체크박스 값은 `request.form.getlist()`로 받을 수 있습니다.

```python
features = request.form.getlist('features')
```

## 검색 폼

폼은 데이터 입력뿐 아니라 검색 기능에도 자주 사용됩니다.  
사용자 목록이나 게시글 목록에서 특정 단어를 검색하는 형태로 응용할 수 있습니다.

## 핵심 정리

- Flask는 `GET`과 `POST`를 이용해 폼을 처리합니다.
- 제출된 데이터는 `request.form`으로 읽습니다.
- 입력값 검증은 필수입니다.
- 처리 후에는 `redirect()`로 다음 페이지로 이동할 수 있습니다.
- 체크박스처럼 여러 값이 오는 경우에는 `getlist()`를 사용합니다.
