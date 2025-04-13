from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('', views.show_customer, name='show_customer'),
    path('add_new_customer', views.add_new_customer, name='add_new_customer'),
    path('remove_customer/<int:id>', views.remove_cutomer, name='remove_customer'),
]
