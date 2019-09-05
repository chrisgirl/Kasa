from django.urls import path
from . import views
from .views import IndexView, BlogView, AddBlogView, PostListView


app_name = 'blog'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', BlogView.as_view(), name='blog-detail'),
    path('list/', PostListView.as_view(), name='blog_entries'),
    path('contact/', views.contact_view, name='contact'),
    path('addblog/', AddBlogView.as_view(success_url='/'), name='add_blog')
]




