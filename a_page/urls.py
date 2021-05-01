from django.urls import path
from a_page.views import index

urlpatterns = [
    path('', index),
]
