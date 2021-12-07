from django.db import models


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Shop(TimestampModel):
    author_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(upload_to="mall/shop/%Y/%m/%d")
    content = models.TextField()
    tag_set = models.ManyToManyField("Tag",blank=True)

    def __str__(self) -> str:
        return self.shop_name

    class Meta:
        verbose_name = "가게이름"
        verbose_name_plural = "가게목록"


class Comment(TimestampModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=15)
    message = models.TextField()

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글목록"


class Tag(TimestampModel):
    name = models.CharField(max_length=20, db_index=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그목록"






