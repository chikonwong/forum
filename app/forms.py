from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ChannelForm(forms.Form):
    channel_name = forms.CharField(max_length=30)
    created_by = forms.CharField(max_length=30)


class PostForm(forms.Form):
    post_title = forms.CharField(max_length=100)
    post_content = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'rows': 20, 'cols': 40}))


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))


class UserForm(forms.Form):
    username = forms.CharField(label='Enter username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    first_name = forms.CharField(label='Enter First name', min_length=1, max_length=150)
    last_name = forms.CharField(label='Enter Last name', min_length=1, max_length=150)
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].lower()
        r = User.objects.filter(first_name=first_name)
        if r.count():
            raise ValidationError("First name already exists")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].lower()
        r = User.objects.filter(last_name=last_name)
        if r.count():
            raise ValidationError("Last name already exists")
        return last_name

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passowrd dont match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        return user
