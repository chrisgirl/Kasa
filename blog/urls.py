from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('join/', views.register_view, name='register_view'),
    path('contact/', views.contact_view, name='contact_view'),
    path('list/', views.post_list, name='post_list'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('add/', views.add_view, name='add_view'),
    path('post/<int:post_id>/', views.post_view, name='post_view')
]

