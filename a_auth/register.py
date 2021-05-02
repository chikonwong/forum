from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from register_forms import CustomUserCreationForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return request('index')

    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})
