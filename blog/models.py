from django.db import models


# Create your models here.
class SignUp(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)


class SignIn(models.Model):
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)


class Add(models.Model):
    title = models.CharField(max_length=200)
    subtext = models.CharField(max_length=250)
    category = models.CharField(max_length=250, default='Select')
    content = models.TextField(max_length=1000)


class ContactUs(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)


class PostList(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)


