# Django Template & URLs

2023.09.14 (Thu)
-----
## Django Model

### Model
Model을 통한 DB관리
![Model](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-14.png)

- Django Model
  - DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공
  - 테이블 구조를 설계하는 청사진(blueprint)
- Model 클래스
    ```
    # articles/models.py

    class Article(models.Model):
        title = models.CharField(max_length=10):
        content = models.TextField()
    ```
  - 모델 클래스는 최종적으로 DB에 테이블 구조를 만듦
  - django.db.models 모듈의 Model이라는 부모 클래스를 상속받음
  - Model은 model에 관련된 모든 코드가 이미 작성되어있는 클래스 [참고](https://github.com/django/django/blob/main/django/db/models/base.py)
  - 개발자는 가장 중요한 테이블 구조를 어떻게 설계할지에 대한 코드만 작성하도록 하기 위한 것 (프레임워크의 이점)
  - 클래스 변수명 (title, content)
    - 테이블의 각 **필드(Col) 이름**
  - model Field 클래스 (CharField, TextField)
    - 테이블 필드의 **데이터 타입**
    - [참고](https://docs.djangoproject.com/en/4.2/ref/models/fields/)
  - model Field 클래스의 키워드 인자; Field option (max_length=10)
    - 테이블 필드의 **제약조건** 관련 설정 
    - 제약조건? 
      - 데이터가 올바르게 저장되고 관리되도록 하기 위한 규칙
      - ex. 숫자만 저장되도록, 문자가 100까지만 저장되도록 하는 등

### Migrations
> model 클래스의 변경사항(필드 생성, 수정 삭제 등)을 DB에 최종 반영하는 방법
- Migrations 과정
    ![datas](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-17.png)
1. Migrations 핵심 명령어 2가지
```
python manage.py makemigrations
```
  - model class를 기반으로 최종 설계도(migration) 작성
```
python manage.py migrate
```
  - 최종 설계도를 DB에 전달하여 반영
2. migrate 후 DB 내에 생성된 테이블 확인
3. 추가 Migrations
    1. 추가 Model Field 작성<sup>1)</sup>
        ```
        # articles/models.py

        class Article(models.Model):
            title = models.CharField(max_length=10):
            content = models.TextField()

            # 추가
            created_at = models.DateTimeField(auto_now_add=True)
            updated_at = models.DateTimeField(auto_now=True)
        ```
    2. makemigrations<sup>2)</sup>
        ```
        python manage.py makemigrations
        ```
        - 이미 기존 테이블이 존재하기 때문에 필드를 추가할 때 필드의 기본 값 설정이 필요
          - 1번. 현재 대화를 유지하면서 직접기본값 입력
          - 2번. 현재 대화에서 나간 후 models.py에 기본 값 관련 설정을 하는 방법
        - 이후, 추가하는 필드의 기본값을 입력한다 (enter 누르면 Django가 제안하는 기본값으로 설정)
    3. migrate<sup>3)</sup>
        ```
        python manage.py migrate
        ```
        - migrate 후 테이블 필드 변화 확인


>model class에 변경사항<sup>1)</sup>이 생겼다면, 반드시 새로운 설계도를 생성<sup>2)</sup>하고, 이를 DB에 반영<sup>3)</sup>해야 한다

- Model Field : DB 테이블의 필드(열)을 정의하며, 해당 필드에 저장되는 데이터 타입과 제약조건을 정의
  - CharField()
    - 길이의 제한이 있는 문자열을 넣을 때 사용
    - 필드의 최대 길이를 결정하는 max_length는 필수 인자
  - TextField()
    - 글자의 수가 많을 때 사용
  - DateTimeField()
    - 날짜와 시간을 넣을 때 사용
    - auto_now : 데이터가 **저장될 때마다** 자동으로 현재 날짜시간을 저장 (수정일)
    - auto_now_add : 데이터가 **처음 생성될 때만** 자동으로 현재 날짜시간을 저장 (생성일)

### Admin site
Automatic admin interface
> Django는 추가 설치 및 설정 없이 자동으로 관리자 interface를 제공<br>
> 데이터 확인 및 테스트 등을 진행하는데 매우 유용

- admin 계정 생성
    ```
    python manage.py createsuperuser
    ```
  - email은 선택사항이기 때문에 입력하지 않고 진행 가능
  - 비밀번호 입력 시 보안상 터미널에 출력되지 않으니 무시하고 입력 이어가기
- DB에 생성된 admin 계정 확인
    ![admin](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-15.png)
- admin.py에 작성한 모델 클래스를 등록해야만 admin site에서 확인 가능
    ```
    # articles/admin.py

    from django.contrib import admin

    # 1. 명시적 상대경로 지정
    from .models import Article

    # 2. Article 모델 class를 admin site에 등록
    admin.site.register(Article)
    ```
- admin site 로그인 후 등록된 모델 클래스 확인 > 데이터 생성, 수정, 삭제 테스트
  ![datas](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-16.png)
- SQLite 에서 테이블 확인


## 참고
- 데이터베이스 초기화
  1. migration 파일 삭제
  2. db.sqlite 파일 삭제

  - **아래 파일과 폴더를 지우지 않도록 주의!**
    - `__init__.py`
    - migrations 폴더
- Migrations 기타 명령어
```
python manage.py showmigrations
```
  - migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 명령어
  - [X]표시가 있으면 migrate가 완료되었음을 의미
```
python manage.py sqlmigrate articles 0001
```
  - 해당 migrations 파일이 SQL언어로 어떻게 번역되어 DB에 전달되는지 확인하는 명령어

- 첫 migrate 시 출력 내용이 많은 이유는?
  - Django 프로젝트가 동작하기 위해 미리 작성되어있는 기본 내장 app들에 대한 migration 파일들이 함께 migrate 되기 때문
- CRUD
  - 소프트웨어가 가지는 기본적인 데이터 처리 기능
  - Create(저장), Read(조회), Update(갱신), Delete (삭제)