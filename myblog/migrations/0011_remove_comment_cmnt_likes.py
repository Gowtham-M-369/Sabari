# Generated by Django 3.1.5 on 2021-04-14 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0010_comment_cmnt_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='cmnt_likes',
        ),
    ]
