# Generated by Django 3.2.9 on 2021-12-05 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hwangridangil', '0002_shop_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]
