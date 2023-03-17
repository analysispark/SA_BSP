from django.db import models

# Create your models here.
class Document(models.Model):
    upload_file = models.FileField(upload_to='upload_file/%Y/m%d/')