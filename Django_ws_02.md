# Django Template & URLs

2023.09.13 (Wed)
-----
## Django Template
### Template System

- Django Template system
  - 데이터 표현을 제어하면서, 표현과 관련된 부분을 담당
- Django Template Language(DTL)
  - Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템
- DTL Syntax
  1. Variable
     - render함수의 세번째 인자로 딕셔너리 데이터를 사용
     - 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
     - dot(.)을 사용하여 변수 속성에 접근할 수 있음
        ```
        {{variable}}
        ```
  2. Filters
     - 표시할 변수를 수정할 때 사용
     - chained가 가능하며 일부 필터는 인자를 받기도 함
     - 약 60개의 built-in template filters를 제공
        ```
        {{variable|filter}}
        {{name|truncatewords: 30}}
        ```
  3. Tags
     - 반복 또는 논리를 수행하여 제어 흐름을 만듦
     - 일부 태그는 시작과 종료 태그가 필요
     - 약 24개의 built-in template tags를 제공
        ```
        {% tag %}
        {% if  %}{% endif %}
        ```
  4. Comments
     - DTL에서의 주석
        ```
        {% comment %} 이것이 주석 역할을 합니다 {% endcomment %}
        ```


### 템플릿 상속(Template inheritance)
> 페이지의 공통요소를 포함하고, 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 "skeleton" template을 작성하여 상속 구조를 구축

- **extends** tag
  - 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림
  - **반드시 템플릿 최상단에 작성되어야 함 (2개 이상 사용 불가)**
    ```
    {% extends "articles/base.html" %}
    ```

- **block** tag
  - 하위 템플릿에서 재정의 할 수 있는 블록을 정의 (하위 템플릿이 작성할 수 있는 공간을 지정)
    ```
    {% block content %} {% endblock content %}
    ```
### HTML form (요청과 응답)
- 데이터를 보내고 가져오기 (Sending and Retrieving form data)
  - HTML form element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기
- **form** element
  - 사용자로부터 할당된 데이터를 서버로 전송
  - 웹에서 사용자 정보를 입력하는 여러 방식(text, password, checkbox 등)을 제공
- **action** & **method** ; 데이터를 어디(action)로 어떤 방식(method)으로 요청할지
  - action
    - 입력 데이터가 전송될 URL을 지정(목적지)
    - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
  - method 
    - 데이터를 어떤 방식으로 보낼 것인지 정의
    - 데이터의 HTTP request methods (GET, POST)를 지정
- **input** element
  - 사용자의 데이터를 입력 받을 수 있는 요소
  - type 속성 값에 따라 다양한 유형의 입력 데이터를 받음
- **name** attribute
  - 입력한 데이터에 붙이는 이름(key)
  - 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근할 수 있음 
- Query String Parameters 
  - 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버로 보내는 방법
  - 문자열은 앰퍼샌드(&)로 연결된 key=value 쌍으로 구성되며, 기본 URL과 물음표(?)로 구분됨
    ```
    # 예시
    http://host:port/path?key=value&key=value
    ```
- [form 활용 1] fake Naver 실습
  1. url.py > path 지정하기
        ```
        urlpatterns = [
        path('admin/', admin.site.urls),
        path('search/',views.search),
        ]
        ```
  2. views.py에 search 함수 생성하기
        ```
        def search(request):
            return render(request, 'articles/search.html')
        ```
  3. articles 앱에 search page 생성하기
        ```
        {% extends "articles/base.html" %}
        {% block content %}
            <h1>fake naver</h1>
            <form action ="https://search.naver.com/search.naver/", method = 'GET'>
                <label for= 'message'>검색어 : </label>
                <input type='text' name = "query" id= 'message'>
                <input type='submit'>
            </form>
        {% endblock content %}
        ```
     1. action : https://search.naver.com/search.naver/
     2. method : GET
     3. input: text 와 submit
     4. name : message id를 가지는 text input값의 key는 'query'이다. (why? naver에서 query = 검색어 형식으로 검색함) 
- [form 활용 2] 사용자 입력 데이터를 받아 그대로 출력하는 서버 만들기
  - 두 개의 view함수가 필요함
  1. throw 로직 작성 (43p)
```
# urls.py
```
```
# views.py
```
```
<!--ar>
```
  2. catch 로직 작성
## Django URLs
### Django URLs
### 변수와 URL
### App과 URL
### URL 이름 지정
### URL 이름 공간