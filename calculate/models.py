from django.db import models

# sqlite3 db.sqlite3
# .mode csv
# .import TEST_UTF1.csv calculate_test

## DELETE FROM calculate_test



class TEST (models.Model):

    Match = models.CharField(max_length=255, null=True)
    Game = models.CharField(max_length=10, null=True)
    Team = models.CharField(max_length=150, null=True)
    Name = models.CharField(max_length=150, null=True)
    v_2p = models.CharField(max_length=10, null=True, default='')