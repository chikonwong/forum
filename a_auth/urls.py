from django.urls import path
from a_auth.views import signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='signin.html'), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(template_name='channel.html'), name='signout'),
]
