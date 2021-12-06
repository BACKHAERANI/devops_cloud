from django.db import models


class Post(models.Model):    #id = PK (INT)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # M:N에서 외래키는 N에게 심는다.
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # 포스트가 삭제되면 COMMENT도 삭제하겠다.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


