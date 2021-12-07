from django.db import models
from fanpage.upload_to import uuid_name_upload_to


class Post(models.Model):
    title = models.CharField(max_length= 200, verbose_name="제목:")
    fan_name = models.CharField(max_length=5, verbose_name="닉네임:")
    url = models.URLField(blank=True, verbose_name="출처:")
    content = models.TextField(verbose_name="내용:")
    photo = models.ImageField(blank=True, upload_to=uuid_name_upload_to, verbose_name="사진:")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)