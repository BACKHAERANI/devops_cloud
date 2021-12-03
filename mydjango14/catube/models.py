from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField()
    thumbnail = models.ImageField()
    thumbnail_file_thumb = ImageSpecField(
        source="thumbnail",
        processors=[ResizeToFill(800, 400)],
        format="JPEG",
        options={"quality": 60},
    )
    # TODO = 업로드되는 파일이 비디오파일인지 여부를 검사하는 게 있으면 좋아
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
