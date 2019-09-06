from django.urls import path
from .import views
from django.contrib.auth.views import LoginView


app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login')
]
