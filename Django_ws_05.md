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

    # return render(request, 'articles/create.html')
    return render(request, 'articles/create.html')
```

```
<!--templates/articles/new.html-->

<h1>NEW</h1>
<form action="{% url "articles:create" %}" method="POST">
```
## HTTP request methods
HTTP: 네트워크 상에서 데이터를 주고 받기 위한 약속

## Delete

## Update
