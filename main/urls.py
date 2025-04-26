from django.urls import path
from django.contrib.auth import login
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),

]