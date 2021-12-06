from django.db import models


class Post(models.Model):    # id = PK (INT)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    tag_set = models.ManyToManyField('Tag', blank=True)    # Tag를 문자열로 쓰거나 Tag를 class Post가 시행되기 전에 넣어주거나
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 인스턴스에 대한 문자열 표현을 기대
    # post.title
    # print(post) -- 내부적으로 post __str__을  찾아서 호출해서 반환값을 출력
    # print(post.__str__()) post obj
    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    # 외래키는 N에게 심는다.
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # 포스트가 삭제되면 COMMENT도 삭제하겠다.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name



