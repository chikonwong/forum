from django.contrib import admin
from a_channel.models import Channel, Post, Comment

# Register your models here.

admin.site.register(Channel)
admin.site.register(Post)
admin.site.register(Comment)
