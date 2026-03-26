# 00 Hello Flask

## 개요

이 문서는 Flask 애플리케이션을 처음 만드는 과정을 다룹니다.  
Flask 앱 생성, 기본 라우팅, URL 매개변수, 요청 방식 구분, 오류 처리의 기초를 함께 보여 줍니다.

## Flask란?

Flask는 Python으로 웹 애플리케이션을 만드는 가벼운 웹 프레임워크입니다.

- 필요한 기능부터 작게 시작할 수 있습니다.
- Python 문법과 비슷한 흐름으로 이해하기 쉽습니다.
- 웹 개발의 핵심 구조를 배우기에 적합합니다.

## Flask 앱 생성

```python
from flask import Flask

app = Flask(__name__)
```

`Flask(__name__)`는 애플리케이션 객체를 만드는 코드입니다.  
이 객체를 기준으로 URL과 함수를 연결하게 됩니다.

## 라우팅

라우팅은 URL과 Python 함수를 연결하는 기능입니다.

```python
@app.route('/')
def hello():
    return '<h1>Hello Flask</h1>'
```

브라우저에서 `/` 경로로 접속하면 `hello()` 함수가 실행됩니다.

## URL 매개변수

Flask는 URL의 일부를 변수처럼 받아올 수 있습니다.

```python
@app.route('/user/<name>')
def user_profile(name):
    return f'{name}님의 프로필'
```

예를 들어 `/user/Alice`로 접속하면 `name`에는 `Alice`가 들어갑니다.

## GET과 POST

하나의 라우트에서 여러 HTTP 메서드를 처리할 수도 있습니다.

```python
@app.route('/contact', methods=['GET', 'POST'])
```

- `GET`: 페이지나 폼을 보여 줄 때
- `POST`: 사용자가 입력한 데이터를 보낼 때

## request 객체

폼 데이터나 요청 정보를 읽으려면 `request`를 사용합니다.

```python
from flask import request

request.method
request.form.get('name')
```

## 오류 처리

존재하지 않는 페이지에 접근했을 때 별도의 응답을 만들 수 있습니다.

```python
@app.errorhandler(404)
def page_not_found(error):
    return '페이지를 찾을 수 없습니다.', 404
```

## 실행

```python
if __name__ == '__main__':
    app.run(debug=True)
```

`debug=True`를 사용하면 코드 수정 후 자동으로 서버가 다시 시작되고, 오류 확인도 쉬워집니다.

## 핵심 정리

- Flask 앱은 `Flask(__name__)`로 시작합니다.
- `@app.route()`로 URL과 함수를 연결합니다.
- URL 매개변수로 동적인 경로를 만들 수 있습니다.
- `GET`, `POST`를 구분해 요청을 처리할 수 있습니다.
- 오류 처리 함수도 직접 만들 수 있습니다.
