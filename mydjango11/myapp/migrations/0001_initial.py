# Generated by Django 3.2.9 on 2021-11-29 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='이름')),
                ('address', models.CharField(max_length=100, verbose_name='주소')),
                ('mobile', models.CharField(max_length=11, verbose_name='연락처')),
                ('menu', models.TextField(verbose_name='주문 메뉴들')),
            ],
        ),
    ]
