from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from a_auth.views import signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='pages.html'), name='home'),
    path('signup/', signup, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='signin.html'), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(template_name='pages.html'), name='signout'),
]
