# Many to one relationships 1

2023.10.11 (Wed)
-----
## 개요
### Many to one relationships 
- N:1 or 1:N
- 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계
- Comment(N) - Article(1):0개 이상의 댓글은 1개의 게시글에 작성될 수 있다
### ForeignKey()
- N:1 관계 설정 모델 필드
## 댓글 모델 구현

### 댓글 모델 정의
```
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
- ForeignKey()클래스의 인스턴스 이름은 참조하는 **모델 클래스 이름의 단수형**으로 작성하는 것을 권장
- ForeignKey 클래스를 작성하는 위치와 관계없이 외래 키는 테이블 필드 마지막에 생성됨

**ForeignKey(to,on_delete)**
- to : 참조하는 모델 class 이름
- on_delete : 외래 키가 참조하는 객체(1)가 사라졌을 때, 외래 키를 가진 객체(N)을 어떻게 처리할 지를 정의하는 설정(데이터 무결성)
  - 'CASCADE' : 부모 객체(참조된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제  [기타 설정값 참고](https://docs.djangoproject.com/en/4.2/ref/models/fields/#arguments)

Migration
- 댓글 테이블의 article_id 필드 확인
- 참조하는 클래스 이름의 소문자(단수형)로 작성하는 것이 권장 되었던 이유
  - django에서 '참조대상 클래스 이름'에 **'_' 와 '클래스 이름'** 을 더하여 필드를 만듦 <br>
![comment_id](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-43.png)

### 댓글 생성 연습
- shell_plus 실행 및 게시글 작성
    ```
    $ python manage.py shell_plus

    # 게시글 생성
    Article.objects.create(title='third', content='django!')
    ```
- 댓글 생성
    ```
    # Comment 클래스의 인스턴스 comment 생성
    comment = Comment()

    # 인스턴스 변수 저장
    comment.content = 'first comment'

    # DB에 댓글 저장
    comment.save()

    # 에러 발생
    IntegrityError: NOT NULL constraint failed: articles_comment.article_id
    ```
    - articles_comment 테이블의 ForeignKeyField, article_id 값이 저장 시 누락되었기 때문
- shell_plus 실행 및 게시글 작성
    ```
    #게시글 조회
    article = Article.objects.get(pk=1)

    # 외래 키 데이터 입력
    comment.article = article
    # comment.article.id = article.pk 처럼 pk 값을 직접 외래 키 칼럼에 넣어줄 수 있지만 권장하지 않음

    # 댓글 저장 및 확인
    comment.save()
    ```
- comment 인스턴스를 통한 article 값 참조하기
    ```
    In [9]: comment.pk
    Out[9]: 1

    In [10]: comment.content
    Out[10]: 'first comment'

    # 클래스 변수명인 article로 조회 시 해당 참조하는 게시물 객체를 조회할 수 있음
    In [11]: comment.article
    Out[11]: <Article: Article object (1)>

    # article_pk는 존재하지 않는 필드이기 때문에 사용 불가
    In [12]: comment.article_id
    Out[12]: 1
    ```
- 게시물의 pk와 content 조회
    ```
    In [14]: comment.article.pk
    Out[14]: 1

    In [15]: comment.article.content
    Out[15]: 'django!'
    ```
- 두번째 댓글 생성
    ```
    comment = Comment(content = 'second comment', article = article)

    comment.save()

    In [18]: comment.pk
    Out[18]: 2

    In [19]: comment
    Out[19]: <Comment: Comment object (2)>

    In [20]: comment.article.pk
    Out[20]: 1
    ```
- 작성된 댓글 데이터 확인<br>
  ![comment_data](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-44.png)
## 관계 모델 참조
### 역참조
> N:1 관계에서 1에서 N을 참조하거나 조회하는 것 (1 -> N)
- N은 외래 키를 가지고 있어 물리적으로 참조가 가능하지만 1은 N에 대한 참조 방법이 존재하지 않아 별도의 역참조 이름이 필요
- 역참조 사용 예시
  - article.comment_set.all()
  - {모델 인스턴스}.{related manager(역참조 이름)}.{QuerySetAPI}
### related manager
> N:1 혹은 M:N 관계에서 역참조 시에 사용하는 매니저
- 'objects'매니저를 통해 queryset api를 사용했던 것처럼 related manager를 통해 queryset api를 사용할 수 있게 됨
- related manager 이름 규칙
  - N:1 관계에서 생성되는 Related manager의 이름은 참조하는 '모델명_set'이름 규칙으로 만들어짐
  - 해당 댓글의 게시글(Comment -> Article)
    - comment.article
  - 게시글의 댓글 목록 (Article -> Comment)
    - article.comment_set.all()
- Related manager 연습
  - shell_plus 실행 및 1번 게시글 조회
    ```
    $ python manage.py shell_plus

    article = Article.objects.get(pk=1)
    ```
  - 1번 게시글에 작성된 모든 댓글 조회하기(역참조)
    ```
    In [21]: article.comment_set.all()
    Out[21]: <QuerySet [<Comment: Comment object (1)>, <Comment: Comment object (2)>]>
    ```
  - 1번 게시글에 작성된 모든 댓글 내용 출력
    ```
    In [22]: comments = article.comment_set.all()

    In [23]: for comment in comments :
        ...:     print(comment.content)
        ...: 
    first comment
    second comment
    ```
## 댓글 구현
### 댓글 CREATE
- 사용자로부터 댓글 데이터를 입력 받기 위한 CommentForm 정의
```
# article/forms.py

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
```
- detail view 함수에서 CommentForm을 사용하여 detail 페이지에 렌더링
    ```
    # articles/views.py

    from .forms import ArticleForm , CommentForm

    def detail(request, pk):
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm()
        comments = article.comment_set.all()
        context = {
            'article': article,
            'comment_form' : comment_form,
        }
        return render(request, 'articles/detail.html', context)
    ```

    ```
    <!-- articles/detail.html -->

    <form action="#" method = "POST">
    {% csrf_token %}
    {{comment_form}}
    <input type="submit">
    </form>
    ```
  - 결과 : 외래 키 필드 article 또한 데이터 입력이 필요한 필드이기 때문에 출력됨<br>
    ![article foreignkey](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-45.png)
  - 외래 키 필드는 **사용자 입력 값으로 받는 것이 아닌 view 함수 내에서 다른 방법으로 전달받아 저장**되어야 함 
- CommentForm 의 출력 필드 조정
    ```
    # article/forms.py

    class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            fields = ('content',)
    ```
    - 출력에서 제외된 외래 키 데이터는 어디서 받아와야 할까?
    - detail 페이지의 url `path('<int:pk>/', views.detail, name='detail')`에서 해당 게시글의 pk값이 사용되고 있음
    - 댓글의 외래 키 데이터에 필요한 정보가 바로 게시글의 pk값
- url 작성 및 action 값 설정
    ```
    # articles/urls.py

    urlpatterns = [
        ...
        path('<int:pk>/comments/', views.comments_create, name= 'comments_create'),
    ]
    ```
    ```
    <!-- articles/detail.html -->

    <form action="{% url "articles:comments_create" article.pk %}" method = "POST">
    {% csrf_token %}
    {{comment_form}}
    <input type="submit">
    </form>
    ```
- comments_create view 함수 정의
    ```
    # articles/views.py

    def comments_create(request,pk):
        article = Article.objects.get(pk = pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            
            ## save의 commit 인자를 활용해 외래 키 데이터 추가 입력 
            comment = comment_form.save(commit=False)
            comment.article = article
            
            ## 댓글 data redirect
            comment.save()
            return redirect('articles:detail',article.pk)
        context = {
            'article' : article ,
            'comment_form' : comment_form,
        }
        return render(request, 'articles/detail.html' ,context)
    ```
    - save(commit=False) : DB에 저장하지 않고 인스턴스만 반환
- 댓글 작성 후 테이블 확인<br>
![comment table](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-46.png)

### 댓글 READ
- detail view 함수에서 전체 댓글 데이터를 조회
    ```
    # articles/views.py

    from .models import Article , Comment

    def detail(request, pk):
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm()
        comments = article.comment_set.all()
        context = {
            'article': article,
            'comment_form' : comment_form,
            'comments' : comments,
        }
        return render(request, 'articles/detail.html', context)
    ```
- 전체 댓글 출력
    ```
    <!-- articles/detail.html -->

    <h4>댓글 목록</h4>
    {% for comment in comments %}
        <li> {{comment.content}}</li>
    {% endfor %}
    ```
### 댓글 DELETE
- 댓글 삭제 url 작성
    ```
    # articles/urls.py

    app_name = 'articles'
    urlpatterns = [
        ...,
        path('<int:article_pk>/comments/<int:comment_pk>/delete/',
            views.comments_delete,
            name = 'comments_delete'),
    ]
    ```
- 댓글 삭제 view 함수 정의
    ```
    # articles/views.py

    from .models import Article , Comment

    def comments_delete(request,article_pk,comment_pk):
        comment = Comment.objects.get(pk = comment_pk)
        comment.delete()
        return redirect('articles:detail',article_pk)
    ```
- 댓글 삭제 버튼 작성
    ```
    <!-- articles/detail.html -->

    <h4>댓글 목록</h4>
    {% for comment in comments %}
        <li> {{comment.content}}
        <form action="{% url "articles:comments_delete" article.pk comment.pk %}" method = "POST">
            {% csrf_token %}
            <input type="submit" value = "DELETE">
        </form>
        </li>
    {% endfor %}
    ```
- 댓글 리스트 및 삭제 버튼 확인<br>
    ![comment delete](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-47.png)