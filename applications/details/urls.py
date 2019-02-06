from django.urls import path, re_path, include
from . import views

app_name = "details"

urlpatterns = [
    path('index/', views.ClientsView.as_view(), name = "index")
]