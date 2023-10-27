# Django REST framework 2

2023.10.19 (Thu)
-----
## DRF with N:1 Relation
### 사전 준비
- Comment 모델 정의
  - Comment 클래스 정의 및 DB 초기화
```
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
  - Migration 및 fixtures 데이터 로드
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py loaddata articles.json comments.json
```
- URL 및 HTTP request method 구성

|URL|GET|POST|PUT|DELETE|
|:---:|---|---|---|---|
|`comments/`|댓글 목록 조회||||
|`comments/1/`|단일 댓글 조회||단일 댓글 수정|단일 댓글 삭제|
|`articles/1/comments/`||댓글 생성|||


### GET
- GET-List
  - 댓글 목록 조회를 위한 CommentSerializer 정의
```
# articles/serializers.py

from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
```
  - url 작성

```
```
  - view 함수 작성
```
```
  - GET  
### POST
### DELETE & PUT
### 응답 데이터 재구성
## 역참조 데이터 구성

## API 문서화