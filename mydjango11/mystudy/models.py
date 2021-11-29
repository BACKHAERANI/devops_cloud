from django.db import models

class study(models.Model):
    title = models.CharField(max_length=100, verbose_name="제목")
    subject = models.CharField(max_length=100, verbose_name="주제")
    Reference = models.URLField(blank=True, verbose_name="참조")
    date = models.DateField(verbose_name="날짜")
    content = models.TextField(verbose_name="내용")

    def __str__(self):
        return self.subject