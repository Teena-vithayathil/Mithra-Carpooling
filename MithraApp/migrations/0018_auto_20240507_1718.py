# Generated by Django 3.2 on 2024-05-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MithraApp', '0017_auto_20240504_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_proof',
            field=models.FileField(null=True, upload_to='./frontend/images/idproofs/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]