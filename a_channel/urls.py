from django.urls import path
from a_channel.views import ListChannel, CreateChannel, UpdateChannel, DeleteChannel, ListPost, ViewPost

urlpatterns = [
    # Channel
    path('list/', ListChannel.as_view(), name='ListChannel'),
    path('create/', CreateChannel.as_view(), name='CreateChannel'),
    path('update/<id>/', UpdateChannel.as_view(), name='UpdateChannel'),
    path('delete/<id>/', DeleteChannel.as_view(), name='DeleteChannel'),
    # Post
    path('posts/<str:channel_id>/', ListPost.as_view(), name='ListPost'),
    path('post/<str:post_id>/', ViewPost.as_view(), name='ListPost'),
]
