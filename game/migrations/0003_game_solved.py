# Generated by Django 3.1 on 2020-09-10 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20200909_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='solved',
            field=models.BooleanField(default=False),
        ),
    ]
