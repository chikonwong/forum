from django.shortcuts import redirect, render
from a_auth.forms import CustomUserCreationForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})
