# Django Template & URLs

2023.09.15 (Fri)
-----
## ORM(Object-Relational-Mapping)
> 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술

## QuerySet API
> ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는데 사용하는 도구
> <br> API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리

- QuerySet API 구문
  - {Model class}.{Manager}.{Queryset API}의 형태
  - ex. Article.objects.all()

- Query 
  - 데이터베이스에 특정한 데이터를 보여 달라는 요청
  - '쿼리문을 작성한다' => 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다
  - 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달
- QuerySet 
  - 데이터베이스에게서 전달 받은 객체 목록(데이터 모음)
    - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
  - Django ORM을 통해 만들어진 자료형
  - 단, 데이터베이스가 단일한 객체를 반환할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨

**즉, Python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장, 조회, 수정, 삭제하는 것**

## QuerySet API 실습

### 1. Create
- QuerySet API 실습 사전 준비 : 외부 라이브러리 설치 및 설정
    ```
    # terminal
    pip install ipython
    pip install django-extensions
    ```
    ```
    # settings.py
    INSTALLED_APPS = [
        'articles',
        'django_extensions',
    ...,
    ]
    ```
    ```
    # terminal

    pip freeze > requirements.txt
    ```
- Django shell
  - Django 환경 안에서 실행되는 python shell
  - 입력하는 QuerySet API 구문이 Django 프로젝트에 영향을 미침

- Django shell 실행
    ```
    # terminal

    python manage.py shell_plus 

    # exit 으로 나올 수 있음
    ```
- 데이터 객체를 만드는(생성하는) 3가지 방법
  - 첫번째 방법
    ```
    # 특정 테이블에 새로운 행을 추가하여 데이터 추가
    article = Article() # Article(class)로부터 article(instance)생성

    article.title = 'first'
    article.content = 'django!'

    article.save() # save하지 않으면 저장되지 않음

    Article.objects.all() # QuerySet 형태로 저장
    # >> <QuerySet [<Article: Article object (2)>, <Article: Article object (3)>, <Article: Article object (5)>]>

    # article 인스턴스를 활용하여 변수를 활용 할 수 있음
    article.title # >> 'first'
    article.content # >> 'django'
    ```
  - 두번째 방법
    - 테이블에 한 줄(행, 레코드)이 쓰여진 것
    - **save메서드를 호출해야 DB에 데이터가 저장됨**
    ```
    article = Article(title = 'second' , content = 'django')
    article.save()
    ```
  - 세번째 방법
    - QuerySey API 중 create() 메서드 활용
    ```
    Article.objects.create(title='third', content = 'django!')
    ```

**save() 메서드를 꼭 기억하기**
### 2. Read
- all() : 전체 데이터 조회
  ```
  Article.objects.all()
  ```
- get() : 단일 데이터 조회
  - 객체를 찾을 수 없으면 DoesNotExist예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴
  - 위와 같은 특징을 가지고 있기 때문에 **primary key와 같이 고유성을 보장하는 조회**에서 사용해야함
    ```
    Article.objects.get(pk=2) # >> <Article: Article object (2)>
    ```
- filter() : 특정 조건 데이터 조회(QuerySet 형태로 출력)
    ```
    Article.objects.filter(content='django!') 
    # >> <QuerySet [<Article: Article object (3)>, <Article: Article object (4)>]>
    ```
### 3. Update
- 데이터 수정 : 인스턴스 변수를 변경 후 save 메서드 호출
    ```
    # 수정할 인스턴스 조회
    article = Article.objects.get(pk=1)

    # 인스턴스 변수를 변경
    article.title = 'byebye'

    # 저장
    article.save()

    # 정상적으로 변경된 것을 확인
    article.title # >> 'byebye'
    ```
### 4. Delete
- 데이터 삭제 : 삭제하려는 데이터 조회 후 delete 메서드 호출
    ```
    # 삭제할 인스턴스 조회
    article = Article.objects.get(pk=1)

    # delete 메서드 호출
    article.delete()

    #삭제한 데이터는 더이상 조회할 수 없음
    Article.objects.get(pk=1) # >> DoesNotExist

    ```

### 참고
- Field lookups
  - 특정 레코드에 대한 조건을 설정하는 방법
  - QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인자로 지정됨
  - [참고](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups)
    ```
    # content 에 dja가 포함된 모든 데이터 조회
    Article.objects.filter(content__contains = 'dja)
    ```
- ORM , QuerySey API를 사용하는 이유
  - DB쿼리를 추상화하여 Django 개발자가 DB와 직접 상호작용하지 않아도 되도록 함
  - DB와의 결합도를 낮추고 개발자가 더욱 직관적이고 생산적으로 개발할 수 있도록 도움


[공식문서](https://docs.djangoproject.com/en/4.2/ref/models/querysets/)