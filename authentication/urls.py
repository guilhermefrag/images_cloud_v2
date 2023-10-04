from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_redirect, name='login_redirect'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]