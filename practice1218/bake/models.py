from django.db import models


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(Timestamp):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Bake(Timestamp):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, db_index=True)
    content = models.TextField()
    photo = models.ImageField(blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]


class Comment(Timestamp):
    bake = models.ForeignKey(Bake, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        ordering = ["-id"]


class Tag(Timestamp):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]



