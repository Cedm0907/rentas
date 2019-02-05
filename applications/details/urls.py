from django.urls import path, re_path, include
from . import views

app_name = "details"

urlpatterns = [
    path('index/', views.Clientsview.as_view(), name = "index")
]