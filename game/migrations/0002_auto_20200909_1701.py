# Generated by Django 3.1 on 2020-09-09 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='games',
            field=models.ManyToManyField(related_name='players', through='game.PlayerGameInfo', to='game.Game'),
        ),
        migrations.RemoveField(
            model_name='game',
            name='owner',
        ),
        migrations.AddField(
            model_name='game',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_games', to='game.player'),
        ),
    ]
