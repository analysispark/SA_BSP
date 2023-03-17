from django.db import models

# sqlite3 db.sqlite3
# .mode csv
# .import TEST_UTF1.csv calculate_test

## DELETE FROM calculate_test



class student(models.Model):
    match = models.CharField(max_length=255, null=True)
    game = models.CharField(max_length=10, null=True)
    team = models.CharField(max_length=150, null=True)
    ame = models.CharField(max_length=150, null=True)
    score_total = models.CharField(max_length=10, null=True, default='')
    game_time = models.DateTimeField(null=True)
    kpi_2p = models.FloatField(null=True)
    kpi_2pA = models.FloatField(null=True)
    kpi_2pp = models.FloatField(null=True)
    kpi_3p = models.FloatField(null=True)
    kpi_3pA = models.FloatField(null=True)
    kpi_3pp = models.FloatField(null=True)
    kpi_FGp = models.FloatField(null=True)
    kpi_FT = models.FloatField(null=True)
    kpi_FTA = models.FloatField(null=True)
    kpi_FTp = models.FloatField(null=True)
    kpi_REB_OR = models.FloatField(null=True)
    kpi_REB_DF = models.FloatField(null=True)
    kpi_REB_TOT = models.FloatField(null=True)
    kpi_AS = models.FloatField(null=True)
    kpi_ST = models.FloatField(null=True)
    kpi_GD = models.FloatField(null=True)
    kpi_BS = models.FloatField(null=True)
    kpi_PF_w = models.FloatField(null=True)
    kpi_PF_wo = models.FloatField(null=True)
    kpi_PF_TOT = models.FloatField(null=True)
    kpi_TO = models.FloatField(null=True)
    kpi_TF = models.FloatField(null=True)

class park_test(models.Model):
    match = models.CharField(max_length=10)
    game = models.CharField(max_length=10)
    team = models.CharField(max_length=20)
    value = models.FloatField()
