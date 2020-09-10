from django.db import models


class Player(models.Model):
    games = models.ManyToManyField(to='Game', related_name='players', through='PlayerGameInfo')


class Game(models.Model):
    number = models.IntegerField()
    owner = models.ForeignKey(to='Player', on_delete=models.CASCADE, related_name='owned_games', null=True)
    solved = models.BooleanField(default=False)


class PlayerGameInfo(models.Model):
    game = models.ForeignKey(to='Game', on_delete=models.CASCADE)
    player = models.ForeignKey(to='Player', on_delete=models.CASCADE)

    attempts = models.PositiveSmallIntegerField(default=0)
