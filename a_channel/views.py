from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from a_channel.models import Channel, Post, Comment


class ListChannel(ListView):
    queryset = Channel.objects.all().order_by('-channel_priority')
    template_name = 'channel.html'


class CreateChannel(CreateView):
    pass


class UpdateChannel(UpdateView):
    pass


class DeleteChannel(DeleteView):
    pass


class ListPost(ListView):
    context_object_name = 'post_list'
    template_name = 'posts.html'

    def get_queryset(self):
        channel = Channel.objects.get(pk=self.kwargs['channel_id'])
        return Post.objects.filter(channel=channel).order_by('-post_priority')


class ViewPost(ListPost):
    template_name = 'post.html'
    context_object_name = 'comment_list'

    def get_queryset(self):
        post = Post.objects.get(pk=self.kwargs['post_id'])
        return Comment.objects.filter(post=post)
