import datetime
import uuid

from django.contrib.auth.models import Group
from django.db import models
from django.utils import timezone


# Create your models here.

class Page(models.Model):
    status = {
        (0, 'Inactive'),
        (1, 'Active')
    }
    page_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    page_name = models.CharField(max_length=30)
    page_priority = models.IntegerField(default=50)
    page_status = models.SmallIntegerField(choices=status, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.page_name


class PageAdminGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    def __str__(self):
        return self.page.page_name
