# Generated by Django 3.2 on 2024-04-29 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MithraApp', '0011_user_rating_user_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='r1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='r2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='r3',
            field=models.IntegerField(default=0),
        ),
    ]
