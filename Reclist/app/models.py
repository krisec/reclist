"""
Definition of models.
"""

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 25, unique=True)

    password = models.CharField(max_length=255)


class Actor(models.Model):
    first_name = models.CharField(max_length = 70)
    last_name = models.CharField(max_length = 70)
    imdb_index = models.CharField(max_length = 24)

class Series(models.Model):
    title = models.CharField(max_length = 70)
    episode_count = models.IntegerField()
    season_count = models.IntegerField()
    imdb_index = models.CharField(max_length = 24)
    img_source = models.CharField(max_length = 128, default="http://epaper.gujaratimidday.com/images/no_image_thumb.gif")

class Season(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    series_number = models.IntegerField()
    imdb_index = models.CharField(max_length = 24)

class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    name = models.CharField(max_length = 70)
    imdb_index = models.CharField(max_length = 24)



class EpisodeActor(models.Model):
    actor = models.ForeignKey(Actor, on_delete = models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete = models.CASCADE)

class Band(models.Model):
    name = models.CharField(max_length = 50)

class Album(models.Model):
    title = models.CharField(max_length = 50)
    artist = models.ForeignKey(Band, on_delete = models.CASCADE)

class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ListSeries(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    score = models.IntegerField()