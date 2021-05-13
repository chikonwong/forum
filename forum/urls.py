from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # channel
    path('', views.list_channel, name='home'),
    # path('createChannel/', views.create_channel),

    # post
    path('channel/<str:channel_name>/', views.list_post),
    path('post/create/<str:channel_id>/', views.create_post),
    path('post/<str:post_id>/', views.view_post, name='view_post'),
    path('post/edit/<str:post_id>/', views.edit_post),
    path('post/delete/<str:post_id>/', views.delete_post),
    path('post/like/<str:post_id>/', views.like_post),

    # comment
    path('comment/create/', views.create_comment),

    # # auth
    # path('login/', auth_views.LoginView.as_view(template_name='index.html'), name='login'),
    # path('signup/', views.signup, name='signup'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),

    # auth
    path('login/', auth_views.LoginView.as_view(template_name='index.html'), name='login'),
    path('home/', auth_views.LoginView.as_view(template_name='index.html'), name='home'),
    path('home/live/', auth_views.LoginView.as_view(template_name='live.html'), name='live'),
    path('home/academic/', auth_views.LoginView.as_view(template_name='academic.html'), name='academic'),
    path('home/creation/', auth_views.LoginView.as_view(template_name='creation.html'), name='creation'),
    path('home/chat/', auth_views.LoginView.as_view(template_name='chat.html'), name='chat'),
    path('home/news/', auth_views.LoginView.as_view(template_name='news.html'), name='news'),
    path('home/others/', auth_views.LoginView.as_view(template_name='others.html'), name='others'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout')
]
