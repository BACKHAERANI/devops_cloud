from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField()
    thumbnail = models.ImageField()
    # TODO = 업로드되는 파일이 비디오파일인지 여부를 검사하는 게 있으면 좋아
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
