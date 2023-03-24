from django.db import models
from django.utils.translation import gettext as _

# sqlite3 db.sqlite3
# .mode csv
# .import result.csv result_result

class result(models.Model):
    match = models.CharField(_("match"), max_length=255, null=True)
    year = models.CharField(_("year"), max_length=50, null=True)
    team = models.CharField(_("team"), max_length=150, null=True)
    name = models.CharField(_("name"), max_length=150, null=True)
    Center_At = models.FloatField(_("Center_At"), null=True)
    Center_Df = models.FloatField(_("Center_Df"), null=True)
    Center_Pr = models.FloatField(_("Center_Pr"), null=True)
    Forward_At = models.FloatField(_("Forward_At"), null=True)
    Forward_Df = models.FloatField(_("Forward_Df"), null=True)
    Forward_Pr = models.FloatField(_("Forward_Pr"), null=True)
    Guard_At= models.FloatField(_("Guard_At"), null=True)
    Guard_Df= models.FloatField(_("Guard_Df"), null=True)
    Guard_Pr= models.FloatField(_("Guard_Pr"), null=True)
