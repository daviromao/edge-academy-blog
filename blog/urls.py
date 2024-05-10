from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.blog_index, name='index'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]