# Generated by Django 3.1.5 on 2021-05-24 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0020_auto_20210524_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=255, null=True),
        ),
    ]