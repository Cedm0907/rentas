from django.contrib import admin
from django.urls import path, re_path, include
from . import views

app_name = "details"

urlpatterns = [
    path('index/', views.IndexView.as_view(), name = "index")
]