from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.urls import reverse


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
            login(request, user)
            messages.success(request, "Registration is successful")
            return redirect('blog:blog_entries')
        else:
            return render(request, 'users/register.html', context={"form": form})
    else:
        form = RegistrationForm()
        return render(request, 'users/register.html', context={"form": form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # import pdb;
        # pdb.set_trace()

        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user:
                login(request, user)
                messages.success(request, "Login successful!")
                return HttpResponseRedirect(reverse('blog:blog_entries'))
            else:
                messages.warning(request, 'Wrong Username and Password')
                return render(request, 'users/register.html', context={"form": form})
        else:
            messages.warning(request, 'Wrong Username and Password')
            return render(request, 'users/register.html', context={"form": form})

    else:
        form = LoginForm()
        return render(request, 'users/register.html', context={"form": form})


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Logout successful")
    return HttpResponseRedirect(reverse('blog:index'))

