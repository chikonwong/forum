from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # channel
    path('', views.list_channel, name='home'),
    # path('createChannel/', views.create_channel),

    # post
    path('channel/<str:channel_name>/', views.list_post),
    path('post/create/<str:channel_id>/', views.create_post),
    # # post details
    path('post/<str:post_id>/', views.view_post),
    path('post/delete/<str:post_id>/<str:channel_id>/<str:channel_name>/', views.delete_post),
    # path('post/edit/<str:post_id>/', views.edit_post),
    # path('comment/create/', views.create_comment),

    # auth
    path('login/', auth_views.LoginView.as_view(template_name='index.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout')

]
