from django.db import models


class Stamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Star(Stamp):
    name = models.CharField(max_length=20, db_index=True)
    birth = models.CharField(max_length=10)
    ent = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(blank=True)
    content = models.TextField()
    tag_set = models.ManyToManyField("Tag", blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "멤버"
        verbose_name_plural = "멤버들"


class Comment(Stamp):
    star = models.ForeignKey(Star, on_delete= models.CASCADE)
    name = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글목록"


class Tag(Stamp):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그목록"
