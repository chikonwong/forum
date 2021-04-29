from django.db import models


# Create your models here.
class user(models.Model):
    uName = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.uName
