from django.db import models
from django.contrib.auth.models import User


# Create your models here
class Blog(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_content = models.TextField(max_length=1000)
    blog_date = models.DateTimeField(auto_now_add=True)
    blog_author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.blog_title}'


class ContactUs(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)