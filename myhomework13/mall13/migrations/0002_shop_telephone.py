# Generated by Django 3.2.9 on 2021-12-01 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall13', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='telephone',
            field=models.CharField(default='', max_length=13),
            preserve_default=False,
        ),
    ]
