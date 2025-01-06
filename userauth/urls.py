from django.contrib import admin
from django.urls import include, path

from userauth import views

urlpatterns = [
    path('',views.register.as_view(),name='register'),
]