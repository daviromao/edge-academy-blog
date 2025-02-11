from django.urls import path
from . import views

app_name = 'myauth'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]