from django.db import models
from django.utils.translation import gettext as _
# sqlite3 db.sqlite3
# .mode csv
# .import ./Backup/dump.csv calculate_student

## DELETE FROM calculate_test



class student(models.Model):
    match = models.CharField(_("match"), max_length=255, null=True)
    year = models.CharField(_("year"), max_length=50, null=True)
    game = models.CharField(_("game"), max_length=10, null=True)
    date = models.CharField(_("date"), max_length=50, null=True)
    team = models.CharField(_("team"), max_length=150, null=True)
    name = models.CharField(_("name"), max_length=150, null=True)
    score_total = models.CharField(_("score_total"), max_length=10, null=True, default='')
    game_time = models.CharField(_("game_time"),max_length=50,null=True)
    kpi_2p = models.FloatField(_("kpi_2p"), null=True)
    kpi_2pA = models.FloatField(_("kpi_2pA"), null=True)
    kpi_2pp = models.FloatField(_("kpi_2pp"), null=True)
    kpi_3p = models.FloatField(_("kpi_3p"), null=True)
    kpi_3pA = models.FloatField(_("kpi_3pA"), null=True)
    kpi_3pp = models.FloatField(_("kpi_3pp"), null=True)
    kpi_FGp = models.FloatField(_("kpi_FGp"), null=True)
    kpi_FT = models.FloatField(_("kpi_FT"), null=True)
    kpi_FTA = models.FloatField(_("kpi_FTA"), null=True)
    kpi_FTp = models.FloatField(_("kpi_FTp"), null=True)
    kpi_REB_OR = models.FloatField(_("kpi_REB_OR"), null=True)
    kpi_REB_DF = models.FloatField(_("kpi_REB_DF"), null=True)
    kpi_REB_TOT = models.FloatField(_("kpi_REB_TOT"), null=True)
    kpi_AS = models.FloatField(_("kpi_AS"), null=True)
    kpi_ST = models.FloatField(_("kpi_ST"), null=True)
    kpi_GD = models.FloatField(_("kpi_GD"), null=True)
    kpi_BS = models.FloatField(_("kpi_BS"), null=True)
    kpi_PF_w = models.FloatField(_("kpi_PF_W"), null=True)
    kpi_PF_wo = models.FloatField(_("kpi_PF_wo"), null=True)
    kpi_PF_TOT = models.FloatField(_("kpi_PF_TOT"), null=True)
    kpi_TO = models.FloatField(_("kpi_TO"), null=True)
    kpi_TF = models.FloatField(_("kpi_TF"), null=True)

class park_test(models.Model):
    match = models.CharField(max_length=10)
    game = models.CharField(max_length=10)
    team = models.CharField(max_length=20)
    value = models.FloatField()
