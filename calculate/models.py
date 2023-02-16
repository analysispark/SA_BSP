from django.db import models
from django.utils.translation import gettext as _
# sqlite3 db.sqlite3
# .mode csv
# .import TEST_UTF1.csv calculate_test

## DELETE FROM calculate_test



class TEST(models.Model):

    Match = models.CharField(_("match"), max_length=255, null=True)
    Game = models.CharField(_("game"), max_length=10, null=True)
    Team = models.CharField(_("team"), max_length=150, null=True)
    Name = models.CharField(_("name"),max_length=150, null=True)
    v_2p = models.FloatField(_("value1"))