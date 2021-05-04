from django.contrib import admin
from django.urls import path, include

from a_channel.views import ListChannel

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Home
    path('', ListChannel.as_view(), name='home'),
    # Urls
    path('', include('a_auth.urls')),
    path('channel/', include('a_channel.urls'))
]
