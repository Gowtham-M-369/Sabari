# Generated by Django 3.2.3 on 2021-06-24 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notifications', '0003_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.IntegerField(choices=[(1, 'like'), (2, 'comment'), (3, 'follow'), (4, 'add post'), (5, 'update post'), (0, 'fav cat')]),
        ),
    ]