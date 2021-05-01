from django.db import models


# Create your models here.

class Page(models.Model):
    page_name = models.CharField(max_length=30)
