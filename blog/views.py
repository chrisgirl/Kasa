from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SignIn, SignUp, ContactUs, Blog, PostList
<<<<<<< HEAD
from .forms import SignInForm, SignUpForm, ContactUsForm, AddForm
=======
from .forms import SignInForm, SignUpForm, ContactUsForm, BlogForm
>>>>>>> 559c24331dabd26464f5cd9315187683fa128e6d

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def register_view(request):
    register_form = None
    # login_form = SignInForm()
    if request.method == 'POST':
        register_form = SignUpForm(request.POST)
        if register_form.is_valid():
            new_signup = SignUp(name=register_form.cleaned_data['name'],
                                email=register_form.cleaned_data['email'],
                                password=register_form.cleaned_data['password'])
            new_signup.save()
            messages.success(request, "SignUp Successful!")
    else:
        login_form = SignInForm()
        if request.method == 'POST':
            login_form = SignInForm(request.POST)
            if register_form.is_valid():
                new_login = SignIn(email=login_form.cleaned_data['email'],
                                   password=login_form.cleaned_data['password'])
                new_login.save()
                messages.success(request, "Login Successful!")
    context_object = {"register_form": SignUpForm, "login_form": SignInForm}
    return render(request, 'register.html', context=context_object)
# postlist


def contact_view(request):
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            new_message = ContactUs(name=contact_form.cleaned_data['name'],
                                    email=contact_form.cleaned_data['email'],
                                    message=contact_form.cleaned_data['message'])
            new_message.save()
            messages.success(request, "Message sent!")
            return redirect('blog:index')

        messages.warning(request, "Message not sent!")
    new_message = ContactUs()
    template = 'contact.html'
    return render(request, template_name=template, context={"contactForm": ContactUsForm})


def post_list(request):
    template = 'postlist.html'
    context = {'all_posts': Blog.objects.all()}
    return render(request, template_name=template, context=context)


def delete_post(request, post_id):
    post = PostList.objects.get(pk=post_id)
    post.delete()
    messages.success(request, "Deleted successfully")
    return redirect('blog:post_list')


def post_view(request, post_id):
    posts = PostList.objects.get(pk=post_id)
    template = 'post.html'
    return render(request, template_name=template, context={"post_view": posts})


def add_view(request):
    if request.method == 'POST':
        post_form = BlogForm(request.POST)

        if post_form.is_valid():
            new_post = Blog(title=post_form.cleaned_data['title'],
<<<<<<< HEAD
                            subtext=post_form.cleaned_data['subtext'],
                            content=post_form.cleaned_data['content'])
=======
                           subtext=post_form.cleaned_data['subtext'],
                           content=post_form.cleaned_data['content'])
>>>>>>> 559c24331dabd26464f5cd9315187683fa128e6d
            new_post.save()
            messages.success(request, "Post Submitted!")
            return redirect('blog:post_list')

        messages.warning(request, "Error")
    new_post = BlogForm()
    template = 'addpost.html'
    return render(request, template_name=template, context={"post": new_post})
