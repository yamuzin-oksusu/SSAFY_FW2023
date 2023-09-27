# Django Static files

2023.09.27 (Wed)
-----

## static files 
### Static Files
서버 측에서 변경되지 않고 고정적으로 제공되는 파일(이미지, JS, CSS 파일 등)
- 웹 서버와 정적 파일
  - 웹 서버의 기본동작은 특정 위치(URL)에 있는 자원을 요청(HTTP request) 받아서 응답(HTTP response)을 처리하고 제공(serving)하는 것
  - 이는 '자원에 접근 가능한 주소가 있다.'라는 의미
  - 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공함
    - **정적 파일을 제공하기 위한 경로(URL)가 있어야 함**
### static files 제공하기
1. 기본 경로에서 제공하기
    1. Static files 기본 경로 : app폴더/static/
    2. 기본 경로 static file 제공하기 : {articles}/static/{articles}/ 경로에 이미지 파일 배치
    3. static tag를 이용해 이미지 파일에 대한 url 제공
        ```
        <!-- articles/index.html -->

        {% load static %}

        <img src="{% static "articles/sample-1.png" %}" alt="샘플 이미지">
        ```
    4. static url 확인

        ![static url](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-24.png)

        > **STATIC_URL?**<br>기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL<br>실제 파일이나 디렉토리가 아니며 URL로만 존재
    5. STATIC_URL
        ```
        #settings.py 에 이미 존재함

        STATIC_URL = 'static/'
        ```
        URL + ***STATIC URL*** + ***정적 파일 경로***

2. 추가 경로에서 제공하기
    - Static files 추가 경로: STATICFILES_DIRS에 문자열 값으로 추가 경로 설정
      - Staticfiles_dirs : 정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트  
    1. 임의의 추가 경로 설정
        ```
        # settings.py

        STATICFILES_DIRS = [
            BASE_DIR/'static',
        ]
        ```
    2. 추가 경로에 이미지 파일 배치
       - 위의 예시에선 BASE 디렉토리 안에 static file을 만들어 이미지 파일 배치
    3. static tag를 사용해 이미지 파일에 대한 url 제공
        ```
        <!-- articles/index.html -->

        <img src="{% static "sample-2.png" %}" alt="sample2">
        ```


**정적 파일을 제공하려면 요청에 응답하기 위한 URL이 필요함**

## Media files
사용자가 웹에서 업로드하는 정적 파일(user-uploaded)
### 이미지 업로드
- ImageField()
  - 이미지 업로드에 사용하는 모델 필드
  - 이미지 객체가 직접 저장되는 것이 아닌 **이미지 파일의 경로**가 문자열로 DB에 저장
- 미디어 파일을 제공하기 전 준비
  1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정
     - MEDIA_ROOT : 미디어 파일들이 위치하는 디렉토리의 절대 경로
        ```
        # settings.py

        MEDIA_ROOT = BASE_DIR / 'media'
        ```
     - MEDIA_URL : MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성(STATIC_URL과 동일한 역할)
        ```
        MEDIA_URL = 'media/' 
        ```
  2. 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 url 지정
     - 업로드 된 파일의 URL == settings.MEDIA_URL
     - 위 URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT
        ```
        #crud/urls.py

        from django.conf import settings
        from django.conf.urls.static import static

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('articles/', include('articles.urls')),
        ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
        ```
  3. 이미지 업로드
     - blank = True 속성을 작성해 빈 문자열이 저장될 수 있도록 제약 조건 설정 (이미지 첨부는 선택사항으로 만듦)
        ```
        # articles/models.py

        class Article(models.Model):
            ...
            image = models.ImageField(blank=True)
        ```
     - migration 진행 , 이전에 **Pillow 라이브러리 install** 필요
        ```
        pip install pillow

        python manage.py makemigrations
        python manage.py migrate

        pip freeze > requirements.txt
        ```
     - form 요소의 enctype 속성 추가 [참고문서](https://developer.mozilla.org/ko/docs/Web/HTML/Element/form)
        ```
        <!-- articles/create.html -->

        <h1>CREATE</h1>
        <form action="{% url "articles:create" %}" method="POST" enctype = 'multipart/form-data'>
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
        </form>
        ```
     - view 함수에서 업로드 파일에 대한 추가 코드 작성
        ```
        # articles/views.py

        def create(request):
            if request.method == 'POST':
                form = ArticleForm(request.POST , request.FILES)
        ```
     - 이미지 업로드 입력 양식 확인

        ![img upload](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-26.png)

     - 이미지 업로드 결과 확인 DB에는 파일 자체가 아닌 **파일 경로**가 저장

        ![img db](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-25.png)



### 업로드 이미지 제공
1. **url**속성을 통해 업로드 파일의 경로 값을 얻을 수 있음
     ```
     <!-- articles/detail.html -->

     <img src="{{article.image.url}}" alt="img">
     ```
 - article.image.url : 업로드 파일의 경로
 - article.image : 업로드 파일의 파일 이름

2. 업로드 이미지 출력 확인 및 MEDIA_URL 확인
     ![img uploaded](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-27.png)
3. 이미지를 업로드하지 않은 게시물은 detail 템플릿을 렌더링 할 수 없음 -> 이미지 데이터가 있는 경우만 이미지를 출력할 수 있도록 처리
     ```
     <!-- articles/detail.html -->

     {% if article.image %}
     <img src="{{article.image.url}}" alt="img">
     {% endif %}
     ```

### 업로드 이미지 수정
1. 수정 페이지 form 요소에 enctype 속성 추가
2. update view 함수에서 업로드 파일에 대한 추가 코드 작성


### 참고
- ImageField()의 upload_to 인자를 사용해 미디어 파일 추가 경로 설정
    ```
    # articles/models.py

    # 1. 이미지 파일의 경우 파일 명 앞에 images/를 붙임
    image = models.ImageField(blank=True, upload_to='images/')

    # 2 . 이미지 파일 업로드 시, 파일 명 앞에 날짜를 붙임
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')

    # 3. (user 생성 시) 파일 명 앞에 images/username/을 붙임
    def articles_image_path(instance, filename):
        return f'images/{instance.user.username}/{filename}'
    image = image = models.ImageField(blank=True, upload_to=articles_image_path)
    ```
- request.FILES가 두번째 위치 인자인 이유
  - ModelForm 상위 클래스 BaseModelForm의 생성자 함수 키워드 인자
    ![BaseModelForm](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-28.png)