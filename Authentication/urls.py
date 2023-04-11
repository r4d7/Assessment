from django.urls import path
from Authentication import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('login', views.login, name="login")
]