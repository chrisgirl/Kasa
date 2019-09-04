from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Blog, ContactUs
from django.contrib import messages
from .forms import ContactUsForm
# Create your views here.


class IndexView(ListView):
    model = Blog
    template_name = "blog/index.html"
    context_object_name = "blog_entries"


class BlogView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"


def post_list(request):
    template = 'blog/blog_list.html'
    context = {"blog_entries": Blog.objects.all()}
    return render(request, template_name=template, context=context)


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
    template = 'blog/contact.html'
    return render(request, template_name=template, context={"contactForm": ContactUsForm})
