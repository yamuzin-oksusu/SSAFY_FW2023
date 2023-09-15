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

    urlpatterns = [
        path('throw/', views.throw),
    ]
    ```
    ```
    # views.py

    def throw(request):
        return render (request, 'articles/throw.html')
    ```
    ```
    <!--articles/throw.html -->
    
    {% extends "articles/base.html" %}

    {% block content %}
      <h1>throw</h1>
      <form action ="/articles/catch/", method = 'GET'>
          <label for= 'message'>메세지: </label>
          <input type='text' name = "message" id = 'message'>
          <input type='submit'>
      </form>
    {% endblock content %}
    ```
  2. catch 로직 작성
    ```
    # urls.py

    urlpatterns = [
        path('catch/', views.catch),
    ]
    ```
    ```
    # views.py

    def catch(request):
        message = request.GET.get('message')
        context = {
            'message' : message,
        }
        # 사용자로부터 요청을 받아서
        # 요청에서 사용자 입력 데이터를 찾아
        # context에 저장 후 catch 템플릿에 출력
        return render(request, 'articles/catch.html',context)
    ```
    - (참고) HTTP request 객체
      - form으로 전송한 데이터 뿐만 아니라 모든 요청 관련 데이터가 담겨 있음
      - view 함수의 첫번째 인자
      - request 객체 살펴보기
        ```
        print(request) # >> <WSGIRequest: GET '/articles/catch/?message=d'>
        print(type(request)) # >> <class 'django.core.handlers.wsgi.WSGIRequest'>
        print(request.GET) # >> <QueryDict: {'message': ['hi']}>
        print(request.GET.get('message')) # 딕셔너리 get 메서드를 사용해 key 값 조회
        # >> hi 
        ```
    ```
    <!--articles/throw.html -->
    
    {% extends "articles/base.html" %}

    {% block content %}
        <h1>{{message}} 받기 완료 </h1>
    {% endblock content %}
    ```

### 참고
- 추가 템플릿 경로 지정
  - 템플릿 기본 경로 외 커스텀 경로 추가하기
    ```
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR/'templates',],
            ...,
        }
    ]
    ```
  - 새로운 템플릿 경로 생성 
    - 원하는 경로에 템플릿 지정해서 생성함 (보통은 app 폴더 안에 templates 혹은 pjt와 같은 경로에 templates 생성)
  - extends 경로 수정

    ```
    # 예시

    # 전
    {% extends "articles/base.html" %}

    # 후
    {% extends "base.html" %}
    ```
- BASE_DIR
  - settings에서 경로지정을 편하게 하기 위해 최상단 지점을 지정 해놓은 변수
  ```
  # Build paths inside the project like this: BASE_DIR / 'subdir'.
  BASE_DIR = Path(__file__).resolve().parent.parent
  ```
- DTL 주의사항
  - Python처럼 일부 프로그래밍 구조(it, for 등)를 사용할 수 있지만 명칭을 그렇게 설계 했을 뿐이지 Python 코드로 실행되는 것이 아니며 Python과는 관련 없음
  - 프로그래밍적 로직이 아니라 프레젠테이션을 위한 것 임을 명심할 것
  - 프로그래밍적 로직은 되도록 view 함수에서 작성 및 처리
  - [공식문서](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/)를 참고해 다양한 태그와 필터 사용해보기

## Django URLs

### Django URLs
요청과 응답에서 Django URLs의 역할
![DjangoUrls](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-18.png)
**URL dispatcher**<br>
> URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결(매핑)
### 변수와 URL
- 현재 URL 관리의 문제점
  - 템플릿의 많은 부분이 중복되고, URL의 일부만 병경되는 상황이라면 계속해서 비슷한 URL과 템플릿을 작성해나가야 할까?
- Variable Routing 
  - URL 일부에 변수를 포함시키는 것
  - 변수는 view 함수의 인자로 전달할 수 있음
  - Variable routing 작성법 : **`<path_converter:variable_name>`**
  ```
  path('articles/<int:num>/', views.detail)
  path('hello/<strLname>', views.greeting)
  ```
  - Path converters : URL 변수의 타입을 지정 (str, int 등 5가지 타입 지원)
    ```
    # urls.py

    urlpatterns = [
      path('articles/<int:num>/', views.detail),
    ]
    ```
    ```
    # views.py

    def detail(request, num):
      context = {
        'num' : num,
      }
      return render(request,'articles/detail.html', context)
    ```
    ```
    <!-- articles/detail.html -->

    {% extends "articles/base.html" %}

    {% block content %}
        <p>{{num}}번째 게시글 입니다.</p>
    {% endblock content %}
    ```
### App과 URL
**App URL mapping**
> 각 앱에 URL을 정의하는 것<br>프로젝트와 각 앱이 URL을 나누어 관리를 편하게 하기 위함
- 2번째 앱 pages 생성 후 발생할 수 있는 문제
  - view 함수 이름이 같거나 같은 패턴의 url 주소를 사용하게 되는 경우, **URL을 각자 app에서 관리**함으로써 충돌 문제 방지
![Appurl](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-19.png)
- URL 구조 변화
![url 구조변화](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-19.png)

- include()
  - 프로젝트 내부 앱들의 URL을 참조할 수 있도록 매핑하는 함수
  - URL의 일치하는 부분까지 잘라내고, 남은 문자열 부분은 후속처리를 위해 include 된 URL로 전달
```
#firstpjt/urls.py

from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
```
### URL 이름 지정
- Url 구조 변경에 따른 문제점
  - 기존 'articles/'주소가 'articles/index/'로 변경될 때, 해당 주소를 사용하는 모든 위치를 찾아가 변경하는 대신 **URL에 이름을 지어준 후 이름만 기억함**
- Naming URL patterns
  - URL에 이름을 지정하는 것
  - path 함수의 name 인자를 정의해서 사용
  ```
  # articles/urls.py

  from django.urls import path
  from . import views
  urlpatterns = [
      path('index/',views.index, name='index'), 
      path('dinner/',views.dinner, name='dinner'),
      path('search/',views.search, name='search'),
      path('throw/', views.throw, name= 'throw'),
      path('catch/',views.catch, name='catch'),
      path('hello/<str:name>/', views.greeting, name = "greeting"),
  ]
  ```
  ```
  # pages/urls.py

  from django.urls import path
  from . import views

  urlpatterns = [
      path('index/',views.index, name='index'), 
  ]
  ```
- URL 표기 변화
  - href 속성 값 뿐만 아니라 form의 action 속성처럼 url을 작성하는 모든 위치에서 변경
  ```
  {% extends "articles/base.html" %}

  {% block content %}
  안녕하세요 {{name}}

  # 지정 전

  <a href= "/articles/dinner/"> dinner</a>
  <a href= "/articles/throw/"> throw</a>

  # 지정 후

  <a href= {% url "articles:dinner" %}> 이런 dinner도</a>
  <a href= {% url "articles:throw" %}> 작동합니다</a>
  {% endblock content %}
  ```

-  url tag
   -  주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 반환
    ```
    # 구조

    {% url 'url-name' arg1 arg2 %}
    ```
    ```
    #example

    {% extends "articles/base.html" %}

    {% block content %}
    <a href= {% url "articles:greeting" 'jihoon' %}>얘라면?</a>
    {% endblock content %}
    ```
-   

### URL 이름 공간
- URL 이름 지정 후 남은 문제
  - articles앱의 url이름과 pages 앱의 url이름이 같은 상황에서, **이름에 key를 붙여** 완벽하게 분리함
  1. 'app_name' 속성 지정 
  2. URL tag가 사용하는 모든 곳의 표기 변경
```
# articles/urls.py

from django.urls import path
from . import views

# app_name 지정
app_name = 'articles'

urlpatterns = [
    # index name에 key 표기
    path('index/',views.index, name='pages:index'), 
    path('dinner/',views.dinner, name='dinner'),
    path('search/',views.search, name='search'),
    path('throw/', views.throw, name= 'throw'),
    path('catch/',views.catch, name='catch'),
    path('hello/<str:name>/', views.greeting, name = "greeting"),
]
```
```
from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('index/',views.index, name='articles:index'), # 서로 왔다갔다 하게 article 의 인덱스로 감
]
```

### 참고
- Trailing Slashes
  - Django는 URL 끝에 '/'가 없다면 자동으로 붙임 (Django의 url 설계 철학)
  - '기술적 측면에서 naver.com/bar 와 naver.com/bar/는 서로 다른 url
    - 검색 엔진 로봇이나 웹 트래픽 분석 도구에서는 이 두 주소를 서로 다른 페이지로 봄
  - 그래서 Django는 검색 엔진이 혼동하지 않게 하기 위해 붙이는 것을 선택함
  - 그러나 모든 프레임워크가 이렇게 동작하지 않으므로 주의