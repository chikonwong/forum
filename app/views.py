from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView
from django.http import HttpResponseRedirect
# Create your views here.
from app.models import Channel, Post, Comment
from app import forms


# channel
def list_channel(request):
    if request.method == 'GET':
        # channel_list = Channel.objects.all().order_by('-channel_priority')
        return render(request, 'index.html', locals())


# def create_channel(request):
#     if request.method == "POST":
#         print('create channel result', request.POST)
#         channel_form = forms.ChannelForm(request.POST)
#         if channel_form.is_valid():
#             name = channel_form.cleaned_data['channel_name']
#             author = channel_form.cleaned_data['created_by']
#             user = User.objects.get(username=author)
#             channel = Channel.objects.create(channel_name=name, created_by=user)
#             textmassage = 'saved'
#             return redirect('/')
#         else:
#             textmassage = 'saved'
#
#     if request.method == "GET":
#         channel_form = forms.ChannelForm()
#         return render(request, "create_channel_form.html", locals())


# post
def list_post(request, channel_name):
    if request.method == 'GET':
        channel = Channel.objects.get(channel_name=channel_name)
        post_list = Post.objects.filter(channel=channel).order_by('-post_priority')
        return render(request, 'post_list.html', locals())


def view_post(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(post_id=post_id)
        comment_list = Comment.objects.filter(post=post).order_by('-created_at')
        comment_form = forms.CommentForm()
        if request.user == post.created_by:
            visible = 1
        else:
            visible = 0
        return render(request, 'post_view.html', locals())


def delete_post(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(post_id=post_id)
        comment_list = Comment.objects.filter(post=post)
        comment_list.delete()
        post.delete()
        return redirect('/channel/' + post.channel.channel_name + '/')


def edit_post(request, post_id):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            title = post_form.cleaned_data['post_title']
            content = post_form.cleaned_data['post_content']
            post = Post.objects.get(pk=post_id)
            post.post_title = title
            post.post_content = content
            post.save()
            return redirect('view_post', post_id=post_id)
    else:
        post = Post.objects.get(post_id=post_id)
        post_form = forms.PostForm(initial={'post_title': post.post_title, 'post_content': post.post_content})
        return render(request, "edit_post_form.html", locals())


def create_post(request, channel_id):
    if request.method == 'POST':
        channel_id = request.POST['channel_id']
        post_form = forms.PostForm(request.POST)

        if post_form.is_valid():
            title = post_form.cleaned_data['post_title']
            content = post_form.cleaned_data['post_content']
            channel = Channel.objects.get(channel_id=channel_id)
            post = Post.objects.create(post_title=title,
                                       created_by=request.user,
                                       post_content=content,
                                       channel=channel)

            textmassage = 'saved'
            return redirect('/channel/' + post.channel.channel_name + '/')
        else:
            textmassage = 'can not saved'

    if request.method == 'GET':
        channel_id = channel_id
        post_form = forms.PostForm()
        return render(request, "create_post_form.html", locals())


def create_comment(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        comment_form = forms.CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.cleaned_data['comment']
            post = Post.objects.get(pk=post_id)
            Comment.objects.create(created_by=request.user,
                                   post=post,
                                   comment=comment)
            textmessage = 'saved'
            return redirect('/post/' + post_id + '/')
        else:
            textmessage = 'can not saved'


#
def signup(request):
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = forms.UserForm()
    return render(request, 'signup.html', {'form': form})
