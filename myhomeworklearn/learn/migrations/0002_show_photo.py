# Generated by Django 3.2.9 on 2021-12-06 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
