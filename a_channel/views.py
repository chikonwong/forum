from django.views.generic import ListView

from a_channel.models import Channel


class ChannelList(ListView):
    queryset = Channel.objects.all().order_by('-channel_priority')
    template_name = 'channel.html'
