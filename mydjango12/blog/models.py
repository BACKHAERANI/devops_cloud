from django.db import models
from blog.upload_to import uuid_name_upload_to


class Post(models.Model):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length= 200)
    content = models.TextField()
    #upload_to
    # - 문자열 : 파일이 저장되는 폴더의 경로

    photo = models.ImageField(blank=True,upload_to= uuid_name_upload_to)
                              #(upload_to='blog/post/%Y/%m/%d/%H')    #Y = Year  m = month d = day H = hour
    created_at = models.DateTimeField(auto_now_add=True)  # 현재 시간 장고가 자동으로 받아모
    updated_at = models.DateTimeField(auto_now=True)


