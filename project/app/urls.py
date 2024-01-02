from django.urls import path
from . import views


urlpatterns = [
     path('', views.home, name='home'),
     path('login', views.login, name='login'),
     path('signup', views.signup, name='signup'),
     path('create_post', views.create_post, name='create_post'),
]