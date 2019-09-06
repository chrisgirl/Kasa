from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegistrationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            confirm_password = form.cleaned_data.get('password2')

            user = User()
            user.username = username
            user.email = email
            user.set_password(raw_password)
            user.save()
            #new_user = authenticate(username=username, email=email, password1=raw_password, password2=confirm_password)
            #if new_user is not None:
            login(request, user)
            return redirect('blog:blog_entries')
        else:
            return render(request, 'users/register.html', context={"form": form})
    else:
        form = RegistrationForm()
        return render(request, 'users/register.html', context={"form": form})


def user_login(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = User()
            user.email = email
            user.set_password(raw_password)
            new_user = authenticate(email=email, password1=raw_password)
            if new_user is not None:
                login(request, user)
        return redirect('blog:blog_entries')
    else:
        form = RegistrationForm()
        return render(request, 'users/register.html', context={"form": form})