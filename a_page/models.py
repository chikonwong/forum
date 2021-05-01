import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Page(models.Model):
    page_name = models.CharField(max_length=30)
    page_priority = models.IntegerField(default=50)

    # pub_date = models.DateTimeField('date publish')

    def __str__(self):
        return self.page_name

    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
