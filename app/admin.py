from django.contrib import admin

# Register your models here.
from app import models

admin.site.register(models.Channel)
admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.PostLike)
