# Generated by Django 3.2.9 on 2021-12-06 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrdan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]