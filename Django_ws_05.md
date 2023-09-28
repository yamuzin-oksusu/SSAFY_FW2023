# Django ORM with view

2023.09.25 (Mon)
-----
## Read
### 전체 게시글 조회
```
# articles/views.py

from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
```

```
<!--articles/index.html-->

<h1>INDEX</h1>
{% for article in articles %}
    <p>글 번호 : {{ article.pk }}</p>
    <a href="{% url "articles:detail" article.pk %}">
        <p>글 제목 : {{ article.title }}</p>
    </a>
    <p>글 내용 : {{ article.content }}</p>
    <hr>
{% endfor %}
```


### 단일 게시글 조회
```
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    ...
    path('<int:pk>/', views.detail, name='detail'),
]
```
```
# articles/views.py

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```

```
<!--templates/articles/detail.html-->
<h2>DETAIL</h2>
<h3>{{ article.pk }} 번째 글</h3>
<hr>
<p>{{ article.title }}</p>
<p>{{ article.content }}</p>
<p>{{ article.created_at }}</p>
<p>{{ article.updated_at }}</p>
<hr>
<a href="{% url "articles:index" %}">[back]</a>
```

## Create
Create 로직을 구현하기 위해 필요한 view 함수의 개수는? **2개**
- new : 사용자 입력 데이터를 받을 페이지를 렌더링
- create : 사용자가 입력한 데이터를 받아 DB에 저장
### new  기능 구현

```
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    ...
    path('new/', views.new, name='new'),
]
```

```
# articles/views.py

def new(request):
    return render(request, 'articles/new.html')
```

```
<!--templates/articles/new.html-->

<h1>NEW</h1>
<form action="<!--create로 이동하는 url-->" method="GET">
{% csrf_token %}
<div>
    <label for="title">제목 : </label>
    <input type="text" id="title" name="title">
</div>
<div>
    <label for="content">내용 : </label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea>
</div>
<input type="submit">
</form>
```
- new 페이지로 이동할 수 있는 하이퍼링크 작성
    ```
    <!--templates/articles/index.html-->

    <a href="{% url "articles:new" %}">NEW</a>
    ```

### create 기능 구현
```
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    ...
    path('create/', views.create, name='create'),
]
```

```
<!--templates/articles/create.html-->
<h1>게시글이 작성 되었습니다.</h1>
```

```
# articles/views.py

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    article = Article(title=title, content=content)
    article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')
```

```
<!--templates/articles/new.html-->

<h1>NEW</h1>
<form action="{% url "articles:create" %}" method="POST">
```
## HTTP request methods
- HTTP
  - 네트워크 상에서 데이터를 주고 받기 위한 약속
- HTTP request methods
  - 데이터(리소스)에 어떤 요청(행동)을 원하는지를 나타내는 것
  - GET & POST
- 'GET' Method
  - 특정 리소스를 조회하는 요청(GET으로 데이터를 전달하면 Query String 형식으로 보내짐)
  - `http://127.0.0.1:8000/articles/create/?title=제목&content=내용`
- 'POST' Method
  - 특정 리소스에 변경(생성, 수정, 삭제)을 요구하는 요청
  - POST로 데이터를 전달하면 HTTP Body에 담겨 보내짐
  - POST method 적용
    ```
    <!--templates/articles/new.html-->

    <h1>NEW</h1>
    <form action="<!--create로 이동하는 url-->" method="POST">
    {% csrf_token %}
    <div>
        <label for="title">제목 : </label>
        <input type="text" id="title" name="title">
    </div>
    <div>
        <label for="content">내용 : </label>
        <textarea name="content" id="content" cols="30" rows="10"></textarea>
    </div>
    <input type="submit">
    </form>
    ```
    ```
    # articles/views.py

    def create(request):
        title = request.POST.get('title')
        content = request.POST.get('content')
    ```
  - POST 적용 결과 : 403 Forbidden
    ![403error](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-29.png)
    - 403 Forbidden : 서버에 요청이 전달되었지만 권한 때문에 거절되었다는 것을 의미
    - 거절 이유 : CSRF token이 누락되었다

- HTTP response status code : 특정 HTTP 요청이 성공적으로 완료되었는지를 3자리 숫자로 표현하기로 약속한 것 <br>[참고자료](https://developer.mozilla.org/ko/docs/Web/HTTP/Status)

- CSRF (Cross-Site-Request-Forgery)
  - 사이트 간 요청 위조
  - 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹 페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법

- CSRF Token 적용
  - DTL의 csrf_token 태그를 사용해 사용자에게 토큰 값을 부여
  - 요청 시 토큰 값도 함께 서버로 전송될 수 있도록 함
      ```
      <!-- templates/articles/new.html -->

      <h1>NEW</h1>
      <form action = "{% url "articles:create" %}" method = "POST">
          {% csrf_token %}
      ```
      ![CSRF](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-30.png)

  - 요청 시 CSRF Token을 함께 보내야 하는 이유
    - Django 서버는 해당 요청이 DB에 데이터를 하나 생성하는(DB에 영향을 주는)요청에 대해 **Django가 직접 제공한 페이지에서 데이터를 작성하고 있는 것 인지**에 대한 확인 수단이 필요한 것
    - 겉모습이 똑같은 위조 사이트나 정상적이지 않은 요청에 대한 방어 수단
      - 기존 : 요청 데이터 -> 게시글 작성
      - 변경 : 요청 데이터 + 인증 토큰 -> 게시글 작성
  - 왜 POST일 때만 Token을 확인할까?
    - POST는 단순 조회를 위한 GET과 달리 특정 리소스에 변경(생성, 수정, 삭제)을 요구하는 의미와 기술적인 부분을 가지고 있기 때문
    - DB에 조작을 가하는 요청은 반드시 인증 수단이 필요
    - **DB에 대한 변경사항을 만드는 요청이기 때문에 토큰을 사용해 최소한의 신원 확인을 하는 것**

- 게시글 작성 결과
  - 게시글 생성 후 개발자 도구를 사용해 Form Data가 전송되는 것을 확인하면 더 이상 URL에 데이터가 표기되지 않음을 알 수 있다.

### redirect
**게시글 작성 후 완료를 알리는 페이지를 응답하는 것**<br>
게시글을 "조회해줘!"라는 요청이 아닌 "작성해줘!"라는 요청이기 때문에 게시글 저장 후 페이지를 응답하는 것은 POST 요청에 대한 적절한 응답이 아님<br>
> 데이터 저장 후 페이지를 주는 것이 아닌 다른 페이지로 사용자를 보내야 한다.<br> 사용자를 보낸다 == 사용자가 GET 요청을 한번 더 보내도록 해야한다

**redirect()** <br>
클라이언트가 인자에 작성된 주소로 다시 요청을 보내도록 하는 함수

- redirect() 함수 적용 
    - create view 함수 개선
    ```
    # articles/view.py

    from django.shortcuts import reㄴnder, redirect

    def create(request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()

        return redirect('articles:index')
        # return redirect('articles:detail',article.pk) # detail 페이지로 redirect
    ```
    - redirect 특징
        - 해당 redirect에서 클라이언트는 index(detail) url로 요청을 다시 보내게 됨
        - 결과적으로 index(detail) view 함수가 호출되어 index(detail) view 함수의 반환결과인 index(detail) 페이지를 응답받음
        - 결국 사용자는 게시글 작성 후 작성된 게시글의 index(detail) 페이지로 이동하는 것으로 느끼게 되는 것
- 게시글 작성 결과
    - 게시글 작성 후 생성된 게시글의 index 페이지로 redirect 되었는지 확인
    - create 요청 이후에 index로 다시 요청을 보냈다는 것을 알 수 있음
    ![redirect](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-31.png)


## Delete

### Delete 기능 구현

```
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    ...,
    path('<int:pk>/delete/', views.delete, name='delete'),
]
```

```
# articles/views.py

def delete(request, pk):
    # 몇 번 게시글을 삭제할 것인지 조회
    article = Article.objects.get(pk=pk)
    # 조회한 게시글을 삭제
    article.delete()
    return redirect('articles:index')
```

```
<!-- articles/detail.html -->

<form action="{% url "articles:delete" article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="삭제">
  </form>
  <a href="{% url "articles:index" %}">[back]</a>
```
## Update

Create 로직을 구현하기 위해 필요한 view 함수의 개수는? **2개**
- edit : 사용자 입력 데이터를 받을 페이지를 렌더링
- update : 사용자가 입력한 데이터를 받아 DB에 저장


### edit 기능 구현 (52p)
```
# articles/urls.py

urlpatterns = [
    ...,
    path('<int:pk>/edit/', views.edit, name='edit'),
]
```
```
# articles/views.py

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)
```

- 수정 시 이전 데이터가 출력될 수 있도록 작성
    ```
    <!-- articles/edit.html -->

    <h1>Edit</h1>
    <form action="{% url "articles:update" article.pk %}" method="POST">
    {% csrf_token %}
    <div>
        <label for="title">제목 : </label>
        <input type="text" id="title" name="title" value="{{ article.title }}">
    </div>
    <div>
        <label for="content">내용 : </label>
        <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea>
    </div>
    <input type="submit">
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">[back]</a>
    ```
    ![edit](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-31.png)

- edit 페이지로 이동하기 위한 하이퍼링크 작성
    ```
    <!-- articles/detail.html -->

    <a href="{% url "articles:edit" article.pk %}">EDIT</a>
    ```

### update 기능 구현
```
# articles/urls.py

urlpatterns = [
    ...,
    path('<int:pk>/update/', views.update, name='update'),
]
```
```
# articles/views.py

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)
```

## 참고

### HTTP request methods를 활용한 효율적인 URL 구성
**REST API**를 이용해 동일한 URL 이지만 method에 따라 서버에 요구하는 행동을 다르게 요구할 수 있음
<br>

|method|url|action|
|:---:|---|---|
|(GET)|articles/1/|1번 게시글 조회 요청|
|(POST)|articles/1/|1번 게시글 조작 요청|
