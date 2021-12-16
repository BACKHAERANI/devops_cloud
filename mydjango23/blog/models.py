import tablib
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Category(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Post(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to="blog/post/%Y/%m/%d")
    tag_set = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(max_length=1, choices=[('D', '초안'), ('P', '공개')], db_index=True, default='D')

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("blog:post_detail", args=[self.pk])

    @classmethod
    def get_tabular_data(cls, queryset, format="xlsx") -> bytes:
        dataset = tablib.Dataset()
        dataset.headers = ["id", "title", "created_at", "updated_at"]

        for post in queryset:
            dataset.append([post.id,
                            post.title,
                            post.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                            post.updated_at.strftime("%Y-%m-%d %H:%M:%S"),])
        return dataset.export(format)






class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        ordering = ["id"]


class Tag(TimeStampedModel):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Subscriber(TimeStampedModel):
    phone = models.CharField(max_length=15, validators=[RegexValidator(r"^\d{3,4}-?\d{3,4}-?\d{4}$")])


