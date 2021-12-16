from django.db import models


class TimeStampeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampeModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Shop(TimeStampeModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200)
    photo = models.ImageField()
    description = models.TextField()
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Review(TimeStampeModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    message = models.TextField()

    def __str__(self):
        return self.name


class Tag(TimeStampeModel):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]