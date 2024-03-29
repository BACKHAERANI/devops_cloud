from django.db import models
from django.core.validators import RegexValidator


class Shop(models.Model):
    name = models.CharField(max_length=100, db_index=True)   #디비에서 이름은 샵엔엠이다
    description = models.TextField(blank=True)
    address = models.CharField(max_length=100)
    # TODO: GEODJANGO의 POINTFIELD를 사용
    latitude = models.FloatField(verbose_name="위도")
    longitude = models.FloatField(verbose_name="경도")
    #TODO: 전화번호 값인지 여부를 체킹
    telephone = models.CharField(max_length=15,
                                 validators=[
                                     RegexValidator(r"\d{3,4}-?/d{4}$",
                                                    message="전화번호를 입력해주세요.")
                                 ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
