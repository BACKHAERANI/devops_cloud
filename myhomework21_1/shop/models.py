from django.core.validators import RegexValidator
from django.db import models


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimestampModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Shop(TimestampModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    telephone = models.CharField(max_length=14, validators=[RegexValidator(r"^\d{3}-?\d{4}-?\d{4}$",
                                                                           message="전화번호를 입력하시오.")], help_text="입력예) 042-1234-1234")
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering =["id"]


class Review(TimestampModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name


class Tag(TimestampModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]