# Django Form

2023.09.26 (Mon)
-----

## 개요
### HTML 'form'
- 지금까지 사용자로부터 데이터를 받기위해 활용한 방법
- 그러나 비정상적 혹은 악의적인 요청을 필터링 할 수 없음 
  - **유효한 데이터인지에 대한 확인이 필요**

### 유효성 검사
- 수집한 데이터가 정확하고 유효한지 확인하는 과정
- 유효성 검사 구현 
  - 유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복, 범위, 보안 등 많은 것들을 고려해야 함
  - 이런 과정과 기능을 직접 개발하는 것이 아닌 Django가 제공하는 Form을 사용

## Django Form
> 사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구
> 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공
- Form class 정의
    ```
    # artices/forms.py

    from django import forms

    class ArticleForm(forms.Form):
        title = forms.CharField(max_length=10)
        content = forms.CharField()
    ```

- Form class를 적용한 new 로직
    ```
    # articles/views.py

    from .forms import ArticleForm

    def new(request):
        form = ArticleForm()
        context = {
            'form' : form,
        }
        return render(request, 'articles/new.html', context)
    ```
    ```
    <!-- articles/new.html-->

    <h1>NEW</h1>
    <form action="{% url "articles:create" %}" method="POST">
        {% csrf_token %}
        {{ form }}
        <input type="submit">
    </form>
    ```

- Form rendering options
label, input 쌍을 특정 HTML 태그로 감싸는 옵션
[참고자료](https://docs.djangoproject.com/en/4.2/topics/forms/#form-rendering-options)

    ```
    <!-- articles/new.html-->

    <h1>NEW</h1>
    <form action="{% url "articles:create" %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>

    ```
  - as_p : `<p>`태그로 감싼다

### Widgets
HTML 'input' element의 표현을 담당
- Widget은 단순히 input 요소의 속성 및 출력되는 부분을 변경하는 것 [참고자료](https://docs.djangoproject.com/en/4.2/ref/forms/widgets/#built-in-widgets)
    ```
    # artices/forms.py

    from django import forms

    class ArticleForm(forms.Form):
        title = forms.CharField(max_length=10)
        content = forms.CharField(widget=forms.Textarea)
    ```
## Django ModelForm
**Form** : 사용자가 입력 데이터를 DB에 저장하지 않을 때 (ex. 로그인)<br>
**ModelForm** : 사용자 입력 데이터를 DB에 저장해야 할 때 (ex. 게시글, 회원가입)
### ModelForm
Model과 연결된 Form을 자동으로 생성해주는 기능을 제공 
- ModelForm class 정의
    ```
    # articles/forms.py

    from django import forms
    from .models import Article

    class ArticleForm(forms.ModelForm):
        # model 등록
        class Meta:
            model = Article
            fields = '__all__'
    ```
### Meta class
ModelForm의 정보를 작성하는 곳

- 'fields' 및 'exclude' 속성
  - exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수도 있음
    ```
    # articles/forms.py

    from django import forms
    from .models import Article

    class ArticleForm(forms.ModelForm):
        # model 등록
        class Meta:
            model = Article
            fields = '__all__'
            # fields = ('title',)
            # exclude = ('title',)
    ```
- ModelForm을 적용한 create 로직
    ```
    # artices/views.py

    from .forms import ArticleForm

    def create(request):
        form = ArticleForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail',article.pk)
        
        context = {
            'form':form,
        }
        return render(request, 'articles/new.html', context)
    ```
  - is_valid()
    - 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를  Boolean으로 반환
  - 공백 데이터가 유효하지 않은 이유
    - 모델 필드에는 기본적으로 빈 값은 허용하지 않는 제약조건이 설정되어있음
  - 에러메시지가 출력되는 과정
    - 빈 값은 is_valid()에 의해 False로 평가되고 form 객체에는 그에 맞는 에러 메시지가 포함되어 다음 코드로 진행됨

- ModelForm을 적용한 edit 로직
    ```
    # artices/views.py

    def edit(request, pk):
        article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article)
        context = {
            'article': article,
            'form':form,
        }
        return render(request, 'articles/edit.html', context)
    ```
    ```
    <!-- articles/edit.html-->

    <h1>EDIT</h1>
    <form action="{% url "articles:update" article.pk %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
    ```
- ModelForm을 적용한 update 로직
    ```
    def update(request, pk):
        article = Article.objects.get(pk=pk)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            form.save()
            return redirect('articles:detail', article.pk)
        context = {
            'article': article,
            'form': form, 
        }
        return render(request, 'articles/edit.html', context)
    ```

- save()
  - 데이터베이스 객체를 만들고 저장
  - save() 메서드가 생성과 수정을 구분하는 법
    - 키워드 인자 instance 여부를 통해 생성할 지, 수정할 지를 결정
    ```
    # CREATE
    form = ArticleForm(request.POST)
    form.save()

    # UPDATE
    form = ArticleForm(request.POST, instance=article)
    form.save()
    ```

- Django Form 정리
  - 사용자로부터 데이터를 수집하고 처리하기 위한 강력하고 유연한 도구
  - HTML form의 생성, 데이터 유효성 검사 및 처리를 쉽게 할 수 있도록 도움

### 참고
- ModelForm 키워드 인자 data와 instance 살펴보기[here](https://github.com/django/django/blob/main/django/forms/models.py#L341)
- Widget 응용
    ```
    # articles/forms.py

    class ArticleForm(forms.ModelForm):
        title = forms.CharField(
            label  = '제목',
            widget= forms.TextInput(
                attrs={
                    'class' : 'my-title',
                    'placeholder': 'Enter the title',
                    'maxlength' : 10,
                }
            ),
        )
        content = forms.CharField(
            label = '내용',
            widget = forms.Textarea(
                attrs={
                    'class' : 'my-content' ,
                    'placeholder' : 'Enter the content',
                    'rows' : 5,
                    'cols' : 50,

                }
            ),
            error_messages={'required' : '내용을 입력해주세요.'},
        )
        # model 등록
        class Meta:
            model = Article
            fields = '__all__'
    ```
    - 실행 결과
        ![Widget](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-23.png)


## Handling HTTP requests
**new & create view 함수간 공통점과 차이점**
- 공통점 : 데이터 생성을 구현하기 위함
- 차이점 :  new는 GET method 요청만, create는 POST method 요청만 처리

### HTTP request method 차이점을 활용한 view 함수 구조 변경
- new & create 함수 결합
    1. 새로운 create view 함수
        ```
        def create(request):
            # 요청의 메서드가 POST라면(create)
            if request.method == 'POST':
                form = ArticleForm(request.POST)
                # 유효성 검사
                if form.is_valid():
                    article = form.save()
                    return redirect('articles:detail',article.pk)
                
            else : # 요청의 메서드가 POST가 아니라면 (new)
                form = ArticleForm()
            context = {
                'form' : form,
            }
            return render(request, 'articles/create.html', context)
        ```
    2. 기존 new 관련 코드 수정 (사용하지 않는 new url 제거)
        ```
        app_name = 'articles'
        urlpatterns = [
            path('', views.index, name='index'),
            path('<int:pk>/', views.detail, name='detail'),
            # path('new/', views.new, name='new'),
        ```
    3. new url을 create url로 변경
        ```
        <!-- articles/index.html-->

        <h1>INDEX</h1>
        <a href="{% url 'articles:create' %}">NEW</a>
        ```
        ```
        <!-- articles/create.html-->

        <h1>create</h1>
        <form action="{% url "articles:create" %}" method="POST">
        ```
    > **request method에 따른 요청의 변화**<br>
    > (GET) articles/create/ : 게시글 생성 문서를 줘!
    > (POST) articles/create/ : 게시글을 생성해줘!

- 새로운 update view 함수
1. 기존 edit과 update view 함수 결합
    ```
    def update(request, pk):
        article = Article.objects.get(pk=pk)
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid:
                form.save()
                return redirect('articles:detail', article.pk)
        else :
            form = ArticleForm(instance=article)

        context = {
            'article' : article,
            'form': form, 
        }
        return render(request, 'articles/update.html', context)
    ```
2. 사용하지 않는 edit url 제거
    ```
    app_name = 'articles'
    urlpatterns = [
        ...,
        # path('<int:pk>/edit/', views.edit, name='edit'),
    ```
3. edit 템플릿을 update 템플릿으로 변경
    ```
    <!-- articles/detail.html-->

        <h2>DETAIL</h2>
        <h3>{{ article.pk }} 번째 글</h3>
        <hr>
        ...
        <a href="{% url "articles:update" article.pk %}">UPDATE</a>
    ```
    ```
    <!-- articles/update.html-->

    <h1>Update</h1>
    <form action="{% url "articles:update" article.pk %}" method="POST">
    ```