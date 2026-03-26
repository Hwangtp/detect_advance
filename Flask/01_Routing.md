# 01 Routing

## 개요

이 문서는 Flask 라우팅의 확장된 기능을 설명합니다.  
정수형 URL 매개변수, 여러 경로 변수, 쿼리 문자열, 리다이렉트, `url_for`, HTTP 메서드 분리 등을 다룹니다.

## 라우팅의 의미

라우팅은 브라우저의 URL 요청을 Flask의 특정 함수와 연결하는 기능입니다.

```python
@app.route('/products')
def products_list():
    return '상품 목록'
```

## 정수형 매개변수

URL 변수의 자료형을 제한할 수 있습니다.

```python
@app.route('/product/<int:product_id>')
```

이 경우 `product_id`는 정수만 허용됩니다.  
문자열이 들어오면 Flask가 자동으로 404를 반환합니다.

## 여러 경로 매개변수

URL 안에서 여러 값을 동시에 받을 수도 있습니다.

```python
@app.route('/user/<username>/posts/<int:post_id>')
```

이 방식은 사용자별 게시글, 날짜별 문서, 카테고리별 페이지 등을 만들 때 자주 사용됩니다.

## 쿼리 문자열

쿼리 문자열은 URL 뒤에 `?`로 붙는 값입니다.

예:

```text
/search?keyword=python&page=2
```

Flask에서는 `request.args`로 읽습니다.

```python
keyword = request.args.get('keyword')
page = request.args.get('page', 1, type=int)
```

## 여러 경로를 하나의 함수에 연결

하나의 함수에 여러 URL을 연결할 수 있습니다.

```python
@app.route('/main')
@app.route('/index')
@app.route('/home')
def home():
    return '홈'
```

## redirect와 url_for

### redirect

다른 페이지로 자동 이동시킬 때 사용합니다.

```python
return redirect(url_for('index'))
```

### url_for

함수 이름을 기준으로 URL을 생성합니다.

```python
url_for('product_detail', product_id=1)
```

이 방식은 경로를 직접 문자열로 쓰는 것보다 유지보수가 쉽습니다.

## HTTP 메서드 분리

하나의 경로에서 요청 방식에 따라 다른 동작을 만들 수 있습니다.

```python
@app.route('/api/comments', methods=['GET', 'POST'])
```

- `GET`: 목록 조회
- `POST`: 새 데이터 생성

## path 변환기

슬래시(`/`)를 포함한 경로 전체를 받을 때는 `path` 변환기를 사용합니다.

```python
@app.route('/files/<path:filename>')
```

예를 들어 `/files/css/style.css` 같은 경로를 하나의 값으로 받을 수 있습니다.

## 핵심 정리

- 라우팅은 URL과 함수를 연결합니다.
- `<int:id>`처럼 자료형을 지정할 수 있습니다.
- 쿼리 문자열은 `request.args`로 읽습니다.
- `redirect()`는 이동, `url_for()`는 URL 생성에 사용합니다.
- 하나의 라우트에서 여러 HTTP 메서드를 처리할 수 있습니다.
