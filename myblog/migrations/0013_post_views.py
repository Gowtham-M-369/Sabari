# Generated by Django 3.1.5 on 2021-04-15 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0012_remove_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
