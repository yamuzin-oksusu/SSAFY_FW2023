# Django Intro & Design Pattern

2023.09.12 (Tue)
-----

## Django and Framework
### Framework
> 웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구<br>
> (개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공)
### Django framework
> Python 기반의 대표적인 웹 프레임워크<br>
> 2022 기준 가장 인기있는 백엔드 프레임워크
### 클라이언트와 서버
웹의 동작 방식 : **클라이언트와 서버**
![clientandserver](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-10.png)
- Client
  - 서비스를 요청하는 주체
  - 웹 사용자의 인터넷이 연결된 장치, 웹 브라우저
- Server
  - 클라이언트의 요청에 응답하는 주체
  - 웹페이지, 앱을 저장하는 컴퓨터  
- 우리가 웹 페이지를 보게되는 과정
  1. 웹 브라우저(Client)에서 'google.com'을 입력
  2. 브라우저는 인터넷에 연결된 전세계 어딘가에 있는 구글 컴퓨터(Server)에게 'Google 홈페이지.html'파일을 달라고 request
  3. Request를 받은 구글 컴퓨터는 데이터베이스에서 'Google 홈페이지.html'파일을 찾아 Response
  4. 전달받은 Google 홈페이지.html파일을 웹 브라우저가 사람이 볼 수 있도록 해석해주면서 사용자는 구글의 메인페이지를 보게 됨

**What we do ?**
> Django를 사용해서 서버를 구현할 것

### Django 프로젝트 및 가상환경

**가상환경**<br>
> Python 애플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 **독립적인** 실행 환경

**Django project 생성 전 루틴**
```
# 1. 가상환경 venv 생성
$ python -m venv {venv.name}

# 2. 가상환경 활성화
$ source venv/Scripts/activate

# 3. Django 설치
$ pip install Django

# 4. 의존성 파일 생성
$ pip freeze > requirements.txt



# ---- 참고 ---- #

# 공유받은 의존성 파일 내 패키지 설치
$ pip install -r requirements.txt

# 비활성화
$ deactivate

# 환경에 설치된 패키지 목록 확인
$ pip list

```
**Django Project 실행**
```
# Django pjt 생성
$ django-admin startproject {pjt.name} . 

# django 서버 실행
$ python manage.py runserver

```
참고) 서버 종료 시에는 Ctrl + C 사용함

- Django 프로젝트 생성 전 루틴 정리 + git
  1. 가상환경 생성
  2. 가상환경 활성화
  3. Django 설치
  4. 의존성 파일 생성(패키지 설치시마다 진행)
  5. .gitignore 파일 생성 (첫 add 전)
  6. git 저장소 생성
  7. Django 프로젝트 생성

- LTS(Long-Term Support)
  - 프레임워크나 라이브러리 등의 소프트웨어에서 장기간 지원되는 안정적인 버전을 의미할 때 사용
  - 기업이나 대규모 프로젝트에서는 소프트웨어 업그레이드에 많은 비용과 시간이 필요하기 때문에 안정적이고 장기간 지원되는 버전이 필요


## Django Design Pattern

### Django 프로젝트와 앱

- Django project
  - 애플리케이션의 집합 (DB설정, URL 연결, 전체 앱 설정 등을 처리)
- Django application
  - 독립적으로 작동하는 기능 단위 모듈 (각자 특정한 기능을 담당하며 다른 앱들과 함께 하나의 프로젝트를 구성)

- 앱 사용과정
  1. 앱 생성 
     - 앱의 이름은 '복수형'으로 지정하는 것을 권장
        ```
        # articles == 생성할 app name
        $ python manage.py startapp articles
        ```
  2. 앱 등록
     - 반드시 앱을 생성한 후에 등록해야 함
     - 등록 후 생성은 불가능
        ```
        # settings.py
        INSTALLED_APPS = [
            'articles',
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        ]
        ```

### Django 디자인 패턴
- 디자인 패턴 
  - 소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책 (공통적인 문제를 해결하는데 쓰이는 형식화 된 관행)
- MVC 디자인 패턴 (Model, View, Controller)
  - 애플리케이션을 구조화하는 대표적인 패턴(데이터, 사용자 인터페이스, 비즈니스 로직을 분리)
  - why? 시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이, 독립적이고 쉽게 유지 보수할 수 있는 애플리케이션을 만들기 위해
- MTV 디자인 패턴 (Model, Template, View)
  - Django에서 애플리케이션을 구조화하는 패턴 (기존 MVC 패턴과 동일하나 명칭을 다르게 정의한 것)

- 프로젝트 구조
  - **`settings.py`**
    - 프로젝트의 모든 설정을 관리
  - **`urls.py`**
    - URL과 이에 해당하는 적절한 views를 연결
  - `__init__.py`<sup>1)</sup>
    - 해당 폴더를 패키지로 인식하도록 설정
  - `asgi.py`<sup>1)</sup>
    - 비동기식 웹 서버와의 연결 관련 설정
  - `wsgi.py`<sup>1)</sup>
    - 웹 서버와의 연결 관련 설정
  - `manage.py`<sup>1)</sup>
    - Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티

- 앱 구조
  - **`admin.py`**
    - 관리자용 페이지 설정
  - **`models.py`**
    - DB와 관련된 Model을 정의
    - MTV 패턴의 M
  - **`views.py`**
    - MVC 패턴에서는 Controller 역할이며, 우리가 가장 작성을 많이 할 코드
    - HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환 (url, mode, template과 연계)
  - `apps.py`<sup>1)</sup>
    - 앱의 정보가 작성된 곳
  - `tests.py`<sup>1)</sup>
    - 프로젝트 테스트 코드를 작성하는 곳

1) 수업 과정에서 수정할 일 없음

### 요청과 응답
![Request response](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-11.png)

- URLs 
- http://127.0.0.1:8000/articles/ 로 요청이 왔을 때 view 모듈의 index 뷰 함수를 호출
