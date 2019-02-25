from django.urls import path, re_path, include
from . import views

app_name = "details"

urlpatterns = [
    path('', views.IndexView.as_view(), name = "home"),
    #path('index/<pk>/', views.ClientsView.as_view(), name = "index")
]