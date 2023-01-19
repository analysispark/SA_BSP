from django.db import models

# Create your models here.

class TEST (models.Model):

    Match = models.CharField(max_length=255, null=True)
    Game = models.IntegerField(null=True)
    Team = models.CharField(max_length=150, null=True)
    Name = models.CharField(max_length=150, null=True)
    v_2p = models.IntegerField(null=True)