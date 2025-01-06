from django.contrib import admin
from django.urls import include, path

from userauth import views

urlpatterns = [
    path('',views.register.as_view(),name='register'),
    path('login',views.login.as_view(),name='login'),
    path('logout',views.logout.as_view(),name='logout'),
]